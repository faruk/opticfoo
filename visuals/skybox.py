from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Skybox(visual):
    def setup(self):
        self.tex = [
            self.loader.loadTexture('spherical_panorama1.jpg'),
            self.loader.loadTexture('spherical_texture2.jpg'),
            self.loader.loadTexture('spherical_stars_hi.png'),
            self.loader.loadTexture('spherical_clouds.jpg'),
        ]
        self.plasmasphere = self.loader.loadModel("smiley.egg")
        self.plasmatex = self.loader.loadTexture("spherical_stars_hi.png")
        self.plasmasphere.setTexture(self.plasmatex,1)
        self.plasmasphere.reparentTo(self.path)
        self.plasmasphere.setTwoSided(1)

        self.cubicsphere = self.loader.loadModel("smiley.egg")
        self.cubictex = self.loader.loadTexture("cubic_transparent.png")
        self.cubicsphere.setTexture(self.cubictex, 1)
        self.cubicsphere.reparentTo(self.path)
        self.cubicsphere.setTwoSided(1)

        self.colorsphere = self.loader.loadModel("smiley.egg")


        self.plasmasphere.setScale(200)
        self.cubicsphere.setScale(180)
        
        self.plasmaHpr = LerpHprInterval(self.plasmasphere, 20, Vec3(0,0,0), Vec3(360,360,360))
        self.cubicHpr = LerpHprInterval(self.cubicsphere, 30, Vec3(-360,-360,0), Vec3(0,0,360))
        #self.plasmaSequence = Sequence(self.plasmaHpr).loop()
        self.cubicSequence = Sequence(self.cubicHpr).loop()

        self.alphaplasma = 1
        self.alphacubic = 1
        
        self.showlerp = LerpFunc(self.alpha, fromData = 0, toData = 1, duration = 0.5, name = "trans1")
        self.fadelerp = LerpFunc(self.alpha, fromData = 1, toData = 0, duration = 2.5, name = "fade1")

        self.flash = Sequence(self.showlerp, self.fadelerp)
        self.hifunc = {}

        self.cubicSequenceToggle = True

    def performBeat(self):
        if self.sndY > self.snd.zThreshold:
            map(lambda x: x(), self.hifunc.values())

    def effect1(self):
        if self.alphaplasma > 0:
            self.alphaplasma = self.alphaplasma - 0.01
            self.plasmasphere.setAlphaScale(self.alphaplasma)

    def effect2(self):
        if self.alphaplasma < 1:
            self.alphaplasma = self.alphaplasma + 0.01
            self.plasmasphere.setAlphaScale(self.alphaplasma)

    def effect3(self):
        if self.alphacubic > 0:
            self.alphacubic = self.alphacubic - 0.01
            self.cubicsphere.setAlphaScale(self.alphacubic)

    def effect4(self):
        if self.alphacubic < 1:
            self.alphacubic = self.alphacubic + 0.01
            self.cubicsphere.setAlphaScale(self.alphacubic)

    def effect5(self):
        Sequence(self.showlerp, self.fadelerp).start()

    def effect6up(self):
        x = self.tex.pop(0)
        self.plasmasphere.setTexture(x,1)
        self.tex.append(x)

    def effect7up(self):
        self.plasmasphere.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)

    def effect8(self):
        self.plasmasphere.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)

#    def effect9up(self):
        #self.plasmaSequence = Sequence(self.plasmaHpr).loop()
#        if self.cubicSequenceToggle is True:
#            self.cubicSequence.pause()
#        else:
#            self.cubicSequence.resume()

    def effect0up(self):
        self.plasmasphere.setColor(1.0, 1.0, 1.0, 1)


    """
    def effect0up(self):
        if self.plasmaSequence.isPlaying():
            self.plasmaSequence.finish()
            self.cubicSequence.finish()
        else:
            self.plasmaSequence.loop()
            self.cubicSequence.loop()
    """

    def alpha(self, i):
        self.path.setAlphaScale(i)
