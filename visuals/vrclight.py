from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
from panda3d.core import DirectionalLight, Vec3, Vec4
from visual import visual

class VRCLight(visual):
    def setup(self):
        self.light = self.render.attachNewNode(DirectionalLight('skatepark light'))
        self.light.node().setDirection( Vec3( 1, 1, 1 ) )
        self.light.node().setShadowCaster(True)
        self.light.node().setScene(self.render)
        self.light.setPos(6,6,6)
        dlens = self.light.node().getLens()
        dlens.setFilmSize(41, 21)
        dlens.setNearFar(50, 75)
        self.render.setLight(self.light)

        #self.slight = self.render.attachNewNode(SpotLight('spot'))
        #self.slight.node().setScene(self.render)
        #self.slight.node().setShadowCaster(True)

    def effect1(self):
        self.light.setX(10)

    def effect2(self):
        self.light.setX(-10)

    def effect0(self):
        self.render.clearLight(self.light)

    def effect9(self):
        self.render.setLight(self.light)
