from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import DirectionalLight, Vec3, Vec4
from panda3d.core import PandaNode
#from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpPosInterval
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import math, sys, colorsys
from visual import visual
import random

class MegaBox(visual):

    def setup(self):
        box = self.loader.loadModel("box.egg")
        box.setScale(20)
        box.setPos(-10, -10, -10)
        box.reparentTo(self.path)
        self.boxes = []
        self.boxes.append(box)
        for x in range(0, 999):
            self.boxes.append(box.copyTo(self.path))
        
        x = [-4, -2, 0, 2, 4 ]
        y = [-4, -2, 0, 2, 4 ]
        z = [-4, -2, 0, 2, 4 ]
        
        n = 0
        for i in x:
            for j in y:
                for k in z:
                    self.boxes[n].setPos(self.boxes[n], i, j, k)
                    n = n + 1

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
        
        self.func = {}

    def performBeat(self):
        map(lambda x: x(), self.func.values())

    def effect1up(self):
        if 'emos' in self.func:
            self.func.pop('emos')
        else:
            self.func['emos'] = self.emoticons

    def effect2(self):
        if 'colors' in self.func:
            self.func.pop('colors')
            self.path.setColor(1,1,1,1)
        else:
            self.func['colors'] = self.colorCard

    def emoticons(self):
        if self.sndX > self.snd.xThreshold:
            x = random.randint(0, len(self.emoticonList)-1)
            self.path.clearTexture()
            self.path.setTexture(self.emoticonList[x], 1)

    def colorCard(self):
        if self.sndY > self.snd.yThreshold:
            self.path[0].setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
