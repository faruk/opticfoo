from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class RotatingCubes(visual):
    
    def setup(self):

        #self.sphere = self.loader.loadModel("smiley.egg")
        #self.sphere.reparentTo(self.path)

        self.boxes = []
        for x in range(0,8):
            self.boxes.append(self.path.attachNewNode("box"+str(x)))

        for x in range(0,8):
            box = self.loader.loadModel("box.egg")
            box.setScale(20)
            box.setPos(-10, -10, -10)
            box.reparentTo(self.boxes[x])
        
        self.boxes[0].setPos( 14, 14, 14)
        self.boxes[1].setPos(-14, 14, 14)
        self.boxes[2].setPos( 14,-14, 14)
        self.boxes[3].setPos(-14,-14, 14)
        self.boxes[4].setPos( 14, 14,-14)
        self.boxes[5].setPos(-14, 14,-14)
        self.boxes[6].setPos( 14,-14,-14)
        self.boxes[7].setPos(-14,-14,-14)
        self.setPitchRotations()

        self.pinkpixels = [
            self.loader.loadTexture("pinkpixels1.png"),
            self.loader.loadTexture("pinkpixels2.png"),
            self.loader.loadTexture("pinkpixels3.png"),
            self.loader.loadTexture("pinkpixels4.png"),
            self.loader.loadTexture("pinkpixels5.png"),
            self.loader.loadTexture("pinkpixels6.png"),
            self.loader.loadTexture("pinkpixels7.png"),
            self.loader.loadTexture("pinkpixels8.png"),
            self.loader.loadTexture("pinkpixels9.png"),
            self.loader.loadTexture("pinkpixels10.png"),
            self.loader.loadTexture("pinkpixels11.png"),
            self.loader.loadTexture("pinkpixels12.png"),
            self.loader.loadTexture("pinkpixels13.png"),
            self.loader.loadTexture("pinkpixels14.png"),
            self.loader.loadTexture("pinkpixels15.png"),
            self.loader.loadTexture("pinkpixels16.png"),
        ]

        self.technics = [
            self.loader.loadTexture("1210amplifier.png"),
            self.loader.loadTexture("1210drivecoil.png"),
            self.loader.loadTexture("1210drivecontrol_pcb.png"),
            self.loader.loadTexture("1210output_pcb.png"),
            self.loader.loadTexture("1210parts1.png"),
            self.loader.loadTexture("1210parts2.png"),
            self.loader.loadTexture("1210pickup.png"),
            self.loader.loadTexture("1210pitchled.png"),
            self.loader.loadTexture("1210scheme.png"),
            self.loader.loadTexture("1210setup.png"),
            self.loader.loadTexture("1210strobeilluminator_pcb.png"),
            self.loader.loadTexture("1210stylus.png"),
            self.loader.loadTexture("1210top.png"),
            self.loader.loadTexture("1210tonearmbalance.png"),
        ]
            

        self.intervalSpeeds = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        self.speedIndex = len(self.intervalSpeeds)-1

        self.wobs = []
        for x in self.boxes:
            self.wobs.append(self.scaleWob(x, 0.2, 1.5, 1, 2))

        self.soundfunctions = {
            'nothing': self.nothing
        }

    def performBeat(self):
        map(lambda x: x(), self.soundfunctions.values())

    def setPitchRotations(self):
        self.rotations = [
            self.rotateInterval(self.boxes[0], 5, 'p'),
            self.rotateInterval(self.boxes[1], 5, 'p'),
            self.rotateInterval(self.boxes[2], 5, 'p', False),
            self.rotateInterval(self.boxes[3], 5, 'p', False),
            self.rotateInterval(self.boxes[4], 5, 'p', False),
            self.rotateInterval(self.boxes[5], 5, 'p', False),
            self.rotateInterval(self.boxes[6], 5, 'p'),
            self.rotateInterval(self.boxes[7], 5, 'p'),
        ]

    def setRandomRotation(self):
        o = ['h', 'p', 'r']
        x = random.randint(0, len(self.boxes)-1) 
        self.rotations.pop(x)
        r = self.rotateInterval(self.boxes[x], random.randint(1,10), o[random.randint(0,2)], bool(random.randint(0,1)))
        self.rotations.insert(x, r)

    def rotateInterval(self, path, t, hpr, positive = True):
        degree = 360
        if not positive: degree = -360
        if hpr == "h":
            return LerpHprInterval(path, t, Vec3(0,0,0), Vec3(degree, 0, 0))
        if hpr == "p":
            return LerpHprInterval(path, t, Vec3(0,0,0), Vec3(0, degree, 0))
        if hpr == "r":
            return LerpHprInterval(path, t, Vec3(0,0,0), Vec3(0, 0, degree))

    def scaleWob(self, path, v1, v2, s1, s2):
        return Sequence(
            LerpScaleInterval(path, v1, s2, s1),
            LerpScaleInterval(path, v2, s1, s2)
        )

    def effect1up(self):
        if self.rotations[0].isPlaying():
            map(lambda x: x.finish(), self.rotations)
        else:
            map(lambda x: x.loop(), self.rotations)

    def effect2up(self):
        map(lambda x: x.finish(), self.rotations)
        self.setRandomRotation()
        map(lambda x: x.loop(), self.rotations)

    def effect3up(self):
        if self.speedIndex > 0:
            self.speedIndex = self.speedIndex - 1
            map(lambda x: x.setPlayRate(self.intervalSpeeds[self.speedIndex]), self.rotations)

    def effect4up(self):
        if self.speedIndex < len(self.intervalSpeeds)-1:
            self.speedIndex = self.speedIndex + 1
            print self.speedIndex, len(self.intervalSpeeds)
            map(lambda x: x.setPlayRate(self.intervalSpeeds[self.speedIndex]), self.rotations)

    def wob(self):
        if self.sndX > self.snd.xThreshold:
            wobs = random.sample(self.wobs, random.randint(1, len(self.boxes)-1))
            map(lambda x: x.start(), wobs)

    def effect5up(self):
        if 'wob' in self.soundfunctions:
            self.soundfunctions.pop('wob')
        else:
            self.soundfunctions['wob'] = self.wob

    def technix(self):
        if self.sndX > self.snd.xThreshold:
            t = random.sample(self.technics, 8)
            for x in range(0,8):
                self.boxes[x].setTexture(t[x], 1)

    def effect6up(self):
        if 'technics' in self.soundfunctions:
            self.soundfunctions.pop('technics')
        else:
            self.soundfunctions['technics']= self.technix

    def effect7(self):
        x = random.randint(0,7)
        map(lambda x: x.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1), self.boxes)

    def effect9(self):
        x = random.randint(0,len(self.pinkpixels)-1)
        #i = random.randint(0,len(self.boxes)-1)
        #self.boxes[i].setTexture(self.pinkpixels[x], 1)
        map(lambda x: x.setTexture(self.pinkpixels[random.randint(0, len(self.pinkpixels)-1)],1), self.boxes)

    def effect0up(self):
        map(lambda x: x.setColor(1,1,1,1), self.boxes)
        map(lambda x: x.finish(), self.rotations)
        self.setPitchRotations()

    def nothing(self):
        pass
