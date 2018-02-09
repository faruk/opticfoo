from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class FeelingFeels(visual):
    def setup(self):
        self.path.setTwoSided(1)
        self.plane = CardMaker("plane")
        self.plane.setFrame(-10,10,-10,10)
        self.card = self.path.attachNewNode(self.plane.generate())

        self.feelingfeels = self.loader.loadTexture("feelingfeels.png")
        self.feelsfeeling = self.loader.loadTexture("feelsfeeling.png")
        self.emoticon1 = self.loader.loadTexture("emoticon1.png")
        self.emoticon2 = self.loader.loadTexture("emoticon2.png")
        self.emoticon3 = self.loader.loadTexture("emoticon3.png")
        self.emoticon4 = self.loader.loadTexture("emoticon4.png")
        self.emoticon5 = self.loader.loadTexture("emoticon5.png")
        self.emoticon6 = self.loader.loadTexture("emoticon6.png")
        self.emoticon7 = self.loader.loadTexture("emoticon7.png")
        self.emoticon8 = self.loader.loadTexture("emoticon8.png")
        self.emoticon9 = self.loader.loadTexture("emoticon9.png")
        self.emoticon10 = self.loader.loadTexture("emoticon10.png")
        self.emoticon11 = self.loader.loadTexture("emoticon11.png")
        self.emoticon12 = self.loader.loadTexture("emoticon12.png")
        self.emoticon13 = self.loader.loadTexture("emoticon13.png")
        self.lol = self.loader.loadTexture("lol.png")
        self.ha = self.loader.loadTexture("ha.png")

        self.emoticonList = [
            self.emoticon1,
            self.emoticon2,
            self.emoticon3,
            self.emoticon4,
            self.emoticon5,
            self.emoticon6,
            self.emoticon7,
            self.emoticon8,
            self.emoticon9,
            self.emoticon10,
            self.emoticon11,
            self.emoticon12,
            self.emoticon13,
        ]
        
        self.transLerp = LerpFunc(self.cardTransparency, fromData= 1,toData= 0, duration = 1, name = "trans")
       
        self.func = {}

    def performBeat(self):
        map(lambda x: x(), self.func.values())

    def effect1(self):
        self.card.clearTexture()
        self.card.setTexture(self.feelingfeels, 1)

    def effect2(self):
        self.card.clearTexture()
        self.card.setTexture(self.feelsfeeling, 1)

    def effect3(self):
        self.card.clearTexture()
        self.card.setTexture(self.lol, 1)

    def effect4up(self):
        if 'emos' in self.func:
            self.func.pop('emos')
        else:
            self.func['emos'] = self.emoticons

    def effect5up(self):
        if 'colors' in self.func:
            self.func.pop('colors')
            self.card.setColor(1,1,1,1)
        else:
            self.func['colors'] = self.colorCard

    def effect6up(self):
        if 'trans' in self.func:
            self.func.pop('trans')
            self.card.setAlphaScale(1)
        else:
            self.func['trans'] = self.flashTransparency

    def effect7up(self):
        if 'ha' in self.func:
            self.func.pop('ha')
            self.card.clearTexture()
            self.card.setAlphaScale(1)
        else:
            self.card.setTexture(self.ha, 1)
            self.func['ha'] = self.haha

    def effect0(self):
        self.card.setAlphaScale(1)
        self.card.setColor(1,1,1,1)

    def emoticons(self):
        if self.sndX > self.snd.xThreshold:
            x = random.randint(0, len(self.emoticonList)-1)
            self.card.clearTexture()
            self.card.setTexture(self.emoticonList[x], 1)

    def cardTransparency(self, i):
        self.card.setAlphaScale(i)

    def colorCard(self):
        if self.sndY > self.snd.yThreshold:
            self.card.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)

    def flashTransparency(self):
        if self.sndX > self.snd.xThreshold:
            Sequence(self.transLerp).start()

    def haha(self):
        if self.sndX > self.snd.xThreshold:
            a = self.card.getSa()
            if a < 0.5:
                self.card.setAlphaScale(1)
            if a > 0.5:
                self.card.setAlphaScale(0)
