from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import DirectionalLight, Vec3, Vec4
from panda3d.core import PandaNode
#from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpPosInterval
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import math, sys, colorsys
from visual import visual

class SkateRampOne(visual):
    def setup(self):
        #self.path.removeNode()
        #self.path = self.render.attachNewNode("skatesculp2")

        self.ramp = self.loader.loadModel('skatesculp2')
        self.ramp.setScale(0.5)
        #self.ramp.setRenderModeWireframe()

        #self.card = CardMaker("plane")
        #self.card.setFrame(-10, 10, -5, 5)
        #self.card.setHasNormals(True)
        #self.plane = self.path.attachNewNode(self.card.generate())
        self.plane = self.loader.loadModel('plane')
        self.plane.setP(270)
        self.plane.setScale(60)
        self.plane.setPos(-30, -30, 0)
        #self.plane.setTwoSided(1)
        #self.plane.setColor(Vec4(1,1,1,1))
        #self.plane.setRenderModeWireframe()

        self.light = self.path.attachNewNode(DirectionalLight('skatepark light'))
        self.light.node().setDirection( Vec3( 1, 1, -2 ) )
        self.light.setZ(6)
        dlens = self.light.node().getLens()
        dlens.setFilmSize(41, 21)
        dlens.setNearFar(50, 75)

        self.ramp.reparentTo(self.path)
        self.plane.reparentTo(self.path)
        #self.path.setRenderModeWireframe()

        #self.path.setLight(self.light)

        self.rampColorLerpRedWhite = LerpColorInterval(self.ramp, 0.15, Vec4(1,0,0,1),Vec4(1,1,1,1))
        self.rampColorLerpWhiteRed = LerpColorInterval(self.ramp, 0.15, Vec4(1,1,1,1),Vec4(1,0,0,1))
        self.rampColorLerpBlueWhite = LerpColorInterval(self.ramp, 0.15, Vec4(0,0,1,1),Vec4(1,1,1,1))
        self.rampColorLerpWhiteBlue = LerpColorInterval(self.ramp, 0.15, Vec4(1,1,1,1),Vec4(0,0,1,1))
        self.rampLeftRotationLerp = LerpHprInterval(self.ramp, 0.3, Vec3(360,0,0), Vec3(0,0,0), blendType = 'easeInOut')


        self.planeColorLerpWhiteYellow = LerpColorInterval(self.plane, 0.3, Vec4(1,1,1,1), Vec4(1,1,0,1))
        self.planeScaleLerp = LerpScaleInterval(self.plane, 0.3, 60, 70)
        self.planePositionLerpUp = LerpPosInterval(self.plane, 1, Vec3(-30,-30,60), Vec3(-30,-30,0))
        self.planePositionLerpDown = LerpPosInterval(self.plane, 2, Vec3(-30,-30,0), Vec3(-30,-30,60))

        #self.lightColorLerpBlackWhite = LerpColorInterval(self.light, 0.15, Vec4(1,1,1,1), Vec4(0,0,0,1))
        #self.lightColorLerpWhiteBlack = LerpColorInterval(self.light, 1.35, Vec4(0,0,0,1), Vec4(1,1,1,1))
        self.lightColorLerpBlackWhite = LerpFunc( self.flashLight, fromData = 0, toData = 1, duration = 0.15, name = "flashLight0")
        self.lightColorLerpWhiteBlack = LerpFunc( self.flashLight, fromData = 1, toData = 0, duration = 1.35, name = "flashLight1")
        

        self.beatBassFunc = self.flashRampLeftRotation
        self.beatMidFunc = self.flashPlaneScaleColor
        self.beatHiFunc = self.flashNothing

        self.planeUpDownLoop = Sequence(self.planePositionLerpUp, self.planePositionLerpDown)

    def flashRampWhiteRedWhite(self):
        Sequence(self.rampColorLerpRedWhite).start()

    def flashRampLeftRotation(self):
        Sequence(self.rampLeftRotationLerp).start()

    def flashPlaneScaleColor(self):
        #Parallel(self.planeScaleLerp, self.planeColorLerpWhiteYellow).start()
        Sequence(self.planeColorLerpWhiteYellow).start()

    def flashLightBlackWhiteBlack(self):
        Sequence(self.lightColorLerpBlackWhite, self.lightColorLerpWhiteBlack).start()

    def flashNothing(self):
        pass

    def flashLight(self, i):
        self.light.node().setColor(Vec4(i,i,i,1))

    def performBeat(self):
        if self.sndX > self.snd.xThreshold:
            self.beatBassFunc()
        if self.sndY > self.snd.yThreshold:
            self.beatMidFunc()
        if self.sndZ > self.snd.zThreshold:
            self.beatHiFunc()

    def effect1(self):
        self.light.node().setColor(Vec4(1,0,0,1))

    def effect2(self):
        self.light.node().setColor(Vec4(0,1,0,1))

    def effect3(self):
        self.planeUpDownLoop.loop()

    def effect4(self):
        self.planeUpDownLoop.pause()

    def effect5(self):
        self.beatBassFunc = self.flashLightBlackWhiteBlack

    def effect0(self):
        #self.path.clearLight(self.light)
        #self.path.setRenderModeWireframe()
        #self.path.setColor(Vec4(1,1,1,1))
        pass

    def effect9(self):
        self.ramp.setRenderModeFilled()
        self.path.setLight(self.light)
