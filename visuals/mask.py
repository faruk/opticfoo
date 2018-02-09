from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import DirectionalLight, Vec3, Vec4
from panda3d.core import PandaNode
#from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpPosInterval
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import math, sys, colorsys
from visual import visual
import random

class Mask(visual):

    def setup(self):
        self.mask= self.loader.loadModel('mask')
        self.mask.setP(90)
        self.mask.setH(180)
        #self.mask.setX(3)
        #self.mask.setZ(-2)
        self.mask.reparentTo(self.path)
        self.path.setTwoSided(1)

        self.tex = self.loader.loadTexture("mask.jpg")
        self.mask.setTexture(self.tex)

        self.colorLerp0 = LerpColorInterval(self.mask, 0.15, Vec4(0,0,0,1), Vec4(1,1,1,1))
        self.colorLerp1 = LerpColorInterval(self.mask, 0.85, Vec4(1,1,1,1), Vec4(0,0,0,1))
        self.scaleLerp0 = LerpScaleInterval(self.mask, 0.15, self.scale + self.scale/5, self.scale)
        self.scaleLerp1 = LerpScaleInterval(self.mask, 0.85, self.scale, self.scale + self.scale/5 )

        self.yFunc = self.nothing

        self.mask1= self.loader.loadModel('mask')
        self.mask1.setP(90)
        self.mask1.setH(180)
        self.mask1.setX(-10)
        self.mask1.setTexture(self.tex)
        self.mask1.reparentTo(self.path)

        self.mask2= self.loader.loadModel('mask')
        self.mask2.setP(90)
        self.mask2.setH(180)
        self.mask2.setX(10)
        self.mask2.setTexture(self.tex)
        self.mask2.reparentTo(self.path)
        
        ''' 
        self.mask3= self.loader.loadModel('mask')
        self.mask3.setP(90)
        self.mask3.setH(180)
        self.mask3.setZ(10)
        self.mask3.setTexture(self.tex)
        self.mask3.reparentTo(self.path)

        self.mask4= self.loader.loadModel('mask')
        self.mask4.setP(90)
        self.mask4.setH(180)
        self.mask4.setZ(-10)
        self.mask4.setTexture(self.tex)
        self.mask4.reparentTo(self.path)

        self.mask5= self.loader.loadModel('mask')
        self.mask5.setP(90)
        self.mask5.setH(180)
        self.mask5.setX(10)
        self.mask5.setZ(10)
        self.mask5.setTexture(self.tex)
        self.mask5.reparentTo(self.path)

        self.mask6= self.loader.loadModel('mask')
        self.mask6.setP(90)
        self.mask6.setH(180)
        self.mask6.setX(10)
        self.mask6.setZ(-10)
        self.mask6.setTexture(self.tex)
        self.mask6.reparentTo(self.path)

        self.mask7= self.loader.loadModel('mask')
        self.mask7.setP(90)
        self.mask7.setH(180)
        self.mask7.setX(-10)
        self.mask7.setZ(10)
        self.mask7.setTexture(self.tex)
        self.mask7.reparentTo(self.path)

        self.mask8= self.loader.loadModel('mask')
        self.mask8.setP(90)
        self.mask8.setH(180)
        self.mask8.setX(-10)
        self.mask8.setZ(-10)
        self.mask8.setTexture(self.tex)
        self.mask8.reparentTo(self.path)
        '''
        self.func = {}

    def performBeat(self):
        map(lambda x: x(), self.func.values())

    def scaleFunc(self):
        if self.sndX > self.snd.xThreshold:
            Sequence(self.scaleLerp0, self.scaleLerp1).start()

    def effect1up(self):
        self.path.setRenderModeFilled()

    def effect2up(self):
        self.path.setRenderModeWireframe()

    def effect3up(self):
        if 'wobwob' in self.func:
            self.func.pop('wobwob')
        else:
            self.func['wobwob'] = self.scaleFunc

    def effect4up(self):
        if 'flash' in self.func:
            self.func.pop('flash')
            self.mask1.setAlphaScale(0)
            self.mask2.setAlphaScale(0)
            self.mask.setAlphaScale(1)
        else:
            self.func['flash'] = self.flashMasks

    def effect5up(self):
        if 'color' in self.func:
            self.func.pop('color')
            self.mask1.setColor(1,1,1,1)
            self.mask2.setColor(1,1,1,1)
            self.mask.setColor(1,1,1,1)
        else:
            self.func['color'] = self.colorMasks

    def nothing(self):
        pass

    def flashMasks(self):
        if self.sndX > self.snd.xThreshold:
            x = random.randint(1,3)
            if x == 1:
                self.mask.setAlphaScale(0)
                self.mask1.setAlphaScale(1)
                self.mask2.setAlphaScale(0)
            if x == 2:
                self.mask.setAlphaScale(0)
                self.mask2.setAlphaScale(1)
                self.mask1.setAlphaScale(0)
            if x == 3:
                self.mask.setAlphaScale(1)
                self.mask2.setAlphaScale(0)
                self.mask1.setAlphaScale(0)

    def colorMasks(self):
        if self.sndX > self.snd.xThreshold:
            self.mask.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
            self.mask1.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
            self.mask2.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
        
