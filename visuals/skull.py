from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import DirectionalLight, Vec3, Vec4
from panda3d.core import PandaNode
#from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpPosInterval
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import math, sys, colorsys
from visual import visual

class Skull(visual):

    def setup(self):
        self.skull = self.loader.loadModel('skull')
        self.skull.setP(90)
        self.skull.setX(3)
        self.skull.setZ(-2)
        self.skull.reparentTo(self.path)
        self.skull.setRenderModeWireframe()

        self.colorLerp0 = LerpColorInterval(self.skull, 0.15, Vec4(0,0,0,1), Vec4(1,1,1,1))
        self.colorLerp1 = LerpColorInterval(self.skull, 0.85, Vec4(1,1,1,1), Vec4(0,0,0,1))
        self.scaleLerp0 = LerpScaleInterval(self.skull, 0.15, self.scale + self.scale/5, self.scale)
        self.scaleLerp1 = LerpScaleInterval(self.skull, 0.85, self.scale, self.scale + self.scale/5 )

        self.yFunc = self.nothing

    def performBeat(self):
        if self.sndX > self.snd.xThreshold:
            Sequence(self.colorLerp0, self.colorLerp1).start()
        if self.sndY > self.snd.yThreshold:
            self.yFunc()

    def scaleFunc(self):
        Sequence(self.scaleLerp0, self.scaleLerp1).start()

    def effect1(self):
        self.skull.setRenderModeFilled()

    def effect2(self):
        self.skull.setRenderModeWireframe()

    def effect3(self):
        self.yFunc = self.nothing

    def effect4(self):
        self.yFunc = self.scaleFunc

    def nothing(self):
        pass
