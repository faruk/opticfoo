from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
from visual import visual

class Enterprise(visual):
    def setup(self):
        self.path.removeNode()

        self.path = self.render.attachNewNode("Enterprise")

        self.enterprise = self.loader.loadModel("ent")
        self.enterprise.reparentTo(self.path)
#        self.path.setRenderModeWireframe()

        self.enterprise.setPos((-25,0,0))
        self.enterprise.setH(180)
        self.enterprise.setP(90)

        self.colorLerp0 = LerpColorInterval(self.enterprise, 0.05, Vec4(1,0,0,1),Vec4(1,1,1,1))
        self.colorLerp1 = LerpColorInterval(self.enterprise, 0.25, Vec4(1,1,1,1),Vec4(1,0,0,1))
        self.scaleLerp0 = LerpScaleInterval(self.enterprise, 0.2, self.scale + self.scale/10, self.scale)
        self.scaleLerp1 = LerpScaleInterval(self.enterprise, 1, self.scale, self.scale + self.scale/10)

        self.midFunc = self.funcRedWhite
        #self.loMidFunc = self.funcScaleRedWhite
        self.loFunc = self.funcScale

    def performBeat(self):
        if self.sndY > self.snd.yThreshold:
            self.midFunc()
        #if self.sndY > self.snd.yThreshold and self.sndX > self.snd.xThreshold:
        #    self.loMidFunc()
        if self.sndX > self.snd.xThreshold:
            self.loFunc()

    def funcRedWhite(self):
        Sequence(self.colorLerp0, self.colorLerp1).start()

    #def funcScaleRedWhite(self):
    #    Parallel(self.colorLerp, self.scaleLerp).start()

    def funcScale(self):
        Sequence(self.scaleLerp0, self.scaleLerp1).start()

    def effect1(self):
        self.path.setRenderModeFilled()

    def effect2(self):
        self.path.setRenderModeWireframe()

    def effect3(self):
        self.loFunc = self.nothing

    def effect4(self):
        self.loFunc = self.funcScale

    def effect5(self):
        self.midFunc = self.funcRedWhite

    def nothing(self):
        pass
