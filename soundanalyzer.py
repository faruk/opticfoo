import threading
import alsaaudio, time, audioop
import fftw3
import numpy
import math

class SoundAnalyzer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.nfreq = 1024/2+1
        self.low_cut_f = 100
        self.high_cut_f = 1000
        self.amp_thres = 10.0
        self.rate = 44100
        print alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK
        #self.inp = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK,alsaaudio.PCM_NORMAL)
        self.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
        self.inp.setchannels(1)
        self.inp.setrate(44100)
        self.inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self.inp.setperiodsize(1024)
        self.freq = numpy.zeros((1024), dtype='complex')
        self.sample = numpy.zeros((1024), dtype='double')
        self.wave = numpy.zeros((1024), dtype = 'double')
        self.spect = numpy.zeros((self.nfreq), dtype = 'float')
        self.spect_old = numpy.zeros((self.nfreq), dtype = 'float')
        self.spect_flux = numpy.zeros((self.nfreq), dtype = 'float')
        self.bands = numpy.zeros((3), dtype = 'float')
        self.bands_s = numpy.zeros((3), dtype = 'float')
        self.bands_avg = numpy.zeros((3), dtype = 'float')
        self.indizes = range(1024)
        self.plan = fftw3.Plan(self.wave, self.freq, direction='forward')
        self.nframe = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.xThreshold = 30
        self.yThreshold = 1
        self.zThreshold = 1
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def analyze(self):
        l,data = self.inp.read()
        #print l
        if l:
            i = 0
            for x in self.indizes:
                try:
                    self.wave[i] = audioop.getsample(data,2,i)/32767.0
                    self.sample[i] = audioop.getsample(data,2,i)
                except audioop.error:
                    break
                i = i+1

            self.freq[self.indizes] = 0
            self.bands[[0,1,2]] = 0
            fftw3.execute(self.plan)
            ilc = self.nfreq * (self.low_cut_f/ (self.rate*0.5)) - 1
            ihc = self.nfreq * (self.high_cut_f/ (self.rate*0.5)) - 1
            ilc = max(ilc, 1)
            nlow = int(ilc)
            nmid = int(ihc - ilc)
            nhigh = int(self.nfreq - nmid)

            #print nlow, nmid, nhigh

            for i in range(self.nfreq):
                self.spect[i] = math.sqrt(self.freq[i].real*self.freq[i].real + self.freq[i].imag*self.freq[i].imag) * math.log1p(i+2)
                self.spect_flux[i] = self.spect[i] - self.spect_old[i]
                self.spect_old[i] = self.spect[i]
                self.spect_flux[i] = max(self.spect_flux[i], 0.0)
                if((i < ilc) and (i < ihc)):
                    self.bands[0] += self.spect_flux[i]/nlow
                elif((i<ihc) and (i < self.nfreq)):
                    self.bands[1] += self.spect_flux[i]/nmid
                else:
                    self.bands[2] += self.spect_flux[i]/nhigh

            for i in [0,1,2]:
                temp = max(self.bands[i], 0,0)
                old_temp = self.bands_avg[i]
                self.bands[i] = max((temp - old_temp - self.amp_thres), 0,0)
                if(self.nframe > 1):
                    if(self.bands[i] == 0): self.bands_avg[i] = temp*0.15 + self.bands_avg[i]*0.85
                    if(self.bands[i] > self.bands_s[i]):
                        self.bands_s[i] = self.bands[i]
                    else:
                        self.bands_s[i] = self.bands_s[i] * 0.15 + self.bands[i]*0.85
                else:
                    self.bands_avg[i] = temp
                    self.bands_s[i] = self.bands[i]

            self.nframe = self.nframe + 1
            #return self.bands_s[0], self.bands_s[1], self.bands_s[2]

    def run(self):
        while True:
            if self.stopped():
                self.exit()
            self.analyze()

    def getBeat(self):
        return self.bands_s[0], self.bands_s[1], self.bands_s[2]

    def getThresholds(self):
        return self.xThreshold, self.yThreshold, self.zThreshold

    def setXThreshold(self, value):
        self.xThreshold = value

    def setYThreshold(self, value):
        self.yThreshold = value

    def setZThreshold(self, value):
        self.zThreshold = value
