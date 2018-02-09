from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Intro(visual):
    def setup(self):
        self.path.removeNode()
        self.path = self.render.attachNewNode("trolol")

        self.plane = CardMaker("plane")

        self.plane.setFrame(-10,10,-10,10)
        
        self.card = self.path.attachNewNode(self.plane.generate())

        self.tex1 = self.loader.loadTexture("explanation.png")
        self.card.setTexture(self.tex1)

        self.path.setTransparency(TransparencyAttrib.MAlpha, 1)
        self.path.setTwoSided(1)
        
        self.fuck = self.loader.loadTexture('fuck.png')
        self.it = self.loader.loadTexture('it.png')
        self.fuckit = self.loader.loadTexture('fuckit.png')
        
        self.texlist = [ self.fuck, self.it, self.fuckit ]

        self.func = {}
        self.scaleLerp0 = LerpScaleInterval(self.path, 0.15, self.scale + self.scale/5, self.scale)
        self.scaleLerp1 = LerpScaleInterval(self.path, 0.85, self.scale, self.scale + self.scale/5 )

    def performBeat(self):
        map(lambda x: x(), self.func.values())

    def effect1(self):
        self.card.setColor(1,1,1,1)
        self.card.clearTexture()
        self.card.setTexture(self.tex1)

    def effect2(self):
        self.card.setColor(1,1,1,1)
        self.card.clearTexture()
        self.card.setTexture(self.fuck)

    def effect3(self):
        self.card.setColor(1,1,1,1)
        self.card.clearTexture()
        self.card.setTexture(self.it)

    def effect4up(self):
        if 'fuck' in self.func:
            self.func.pop('fuck')
            self.card.setColor(1,1,1,1)
        else:
            self.func['fuck'] = self.fuckitFunc

    def effect5up(self):
        if 'colors' in self.func:
            self.func.pop('colors')
            self.card.setColor(1,1,1,1)
        else:
            self.func['colors'] = self.colorCard

    def effect6up(self):
        if 'wob' in self.func:
            self.func.pop('wob')
        else:
            self.func['wob'] = self.scaleFunc
        

    def fuckitFunc(self):
        if self.sndX > self.snd.xThreshold:
            x = random.randint(0, len(self.texlist)-1)
            self.card.clearTexture()
            self.card.setTexture(self.texlist[x], 1)

    def cardTransparency(self, i):
        self.card.setAlphaScale(i)

    def colorCard(self):
        if self.sndY > self.snd.yThreshold:
            self.card.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)

    def scaleFunc(self):
        if self.sndX > self.snd.xThreshold:
            Sequence(self.scaleLerp0, self.scaleLerp1).start()
