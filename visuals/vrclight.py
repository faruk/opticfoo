from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
from panda3d.core import DirectionalLight, Vec3, Vec4, PointLight, AmbientLight
from visual import visual

class VRCLight(visual):
    def setup(self):
        self.ambient = AmbientLight('aligh')
        self.ambient.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.light = PointLight('skatepark light')
        self.light.setColor(Vec4(1,1,1,1))
        self.lightpath = self.path.attachNewNode(self.light)
        self.lightpath.setPos(0,0,0)
        self.ambientpath = self.render.attachNewNode(self.ambient)
        #self.render.setLight(self.light)

        #self.slight = self.render.attachNewNode(SpotLight('spot'))
        #self.slight.node().setScene(self.render)
        #self.slight.node().setShadowCaster(True)
        self.ambientLightLevels = {
            'none' : Vec4(0,0,0,1),
            'light' : Vec4(0.1,0.1,0.1,1),
            'mid' : Vec4(0.5,0.5,0.5,1),
            'strong': Vec4(1,1,1,0.5),
        }
        self.ambientLevels = self.ambientLightLevels.values()
        self.ambientLevels = [
            self.ambientLightLevels['none'],
            self.ambientLightLevels['light'],
            self.ambientLightLevels['mid'],
            self.ambientLightLevels['strong'],
        ]

    def effect1up(self):
        x = self.ambientLevels.pop(0)
        self.ambient.setColor(x)
        self.ambientLevels.append(x)

    def effect5(self):
        self.light.setAttenuation(Vec3(0,0,0.01))

    def effect6(self):
        self.light.setAttenuation(Vec3(0,0,0.001))
    
    def effect7(self):
        self.light.setAttenuation(Vec3(0,0,0.0001))

    def effect7(self):
        self.light.setAttenuation(Vec3(0,0,0.00001))

    def effect0(self):
        self.render.clearLight(self.lightpath)
        self.render.clearLight(self.ambientpath)

    def effect9(self):
        self.render.setLight(self.lightpath)
        self.render.setLight(self.ambientpath)
