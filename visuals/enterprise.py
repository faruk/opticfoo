from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
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

        self.faserbank = NodePath("faserbank")
        self.faserbank.reparentTo(self.path)
        self.faserbank.setTransparency(TransparencyAttrib.MAlpha)
        self.fasershots = 1
        self.faserLines()
        self.faserbank.clearLight()

        self.noise = self.loader.loadTexture('stripes.png')

        self.colorLerp0 = LerpColorInterval(self.enterprise, 0.05, Vec4(1,0,0,1),Vec4(1,1,1,1))
        self.colorLerp1 = LerpColorInterval(self.enterprise, 0.25, Vec4(1,1,1,1),Vec4(1,0,0,1))
        self.scaleLerp0 = LerpScaleInterval(self.enterprise, 0.2, self.scale + self.scale/10, self.scale)
        self.scaleLerp1 = LerpScaleInterval(self.enterprise, 1, self.scale, self.scale + self.scale/10)
        self.faserLerp = LerpFunc(self.faserTransparency, fromData = 1, toData = 0, duration = 2, name = "faser")

        self.midFunc = self.funcRedWhite
        #self.loMidFunc = self.funcScaleRedWhite
        self.loFunc = self.funcScale
        self.midFunctions = {}
        self.hiFunctions = {}

    def performBeat(self):
        if self.sndY > self.snd.yThreshold:
            self.midFunc()
            map(lambda x: x(), self.midFunctions.values())

        #if self.sndY > self.snd.yThreshold and self.sndX > self.snd.xThreshold:
        #    self.loMidFunc()
        if self.sndX > self.snd.xThreshold:
            self.loFunc()

        if self.sndZ > self.snd.zThreshold:
            map(lambda x: x(), self.hiFunctions.values())

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

    def effect6up(self):
        if 'warp' in self.hiFunctions:
            self.hiFunctions.pop("warp")
            self.enterprise.clearTexture()
        else:
            self.enterprise.setTexture(self.noise)
            self.hiFunctions['warp'] = self.warp

    def warp(self):
        print self.sndZ
        self.path.setSy(self.scale+self.sndZ*1000000)

    def effect8up(self):
        if self.fasershots > 1:
            self.fasershots = self.fasershots - 1
            self.faserShots(self.fasershots)

    def effect9up(self):
        if self.fasershots < 9:
            self.fasershots = self.fasershots + 1
            self.faserShots(self.fasershots)

    def effect0up(self):
        if 'faser' in self.midFunctions:
            self.midFunctions.pop('faser')
            fasers = self.faserbank.getChildren()
            for f in fasers:
                f.removeNode()
        else:
            self.faserLines()
            self.midFunctions['faser'] = self.faser

    def f(self, x):
        print x
        return x

    def nothing(self):
        pass

    def startFasers(self):
        self.faserbank.show()
        
    def stopFasers(self):
        self.faserbank.hide()

    def faser(self):
        print "yay"
        self.faserShots(self.fasershots)
        Sequence(self.faserLerp).start()

    def faserTransparency(self, i):
        self.faserbank.setAlphaScale(i)

    def faserShots(self, number):
        fasershots = self.faserbank.getChildren()
        fasershots.hide()
        shots = random.sample(fasershots.getPaths(), number)
        for shot in shots:
            shot.show()

    def faserLine(self, point):
        seg = LineSegs()
        seg.setThickness(10.0)
        seg.setColor(Vec4(0,0,1,1))
        seg.moveTo(self.faserbank.getPos())
        seg.drawTo(point)
        return seg.create()

    def faserLines(self):
        for x in self.faserPoints():
            shot = self.faserLine(x)
            self.faserbank.attachNewNode(shot)

    def faserPoints(self):
        points = []
        for x in range(0,10):
            points.append(Point3(
                float(random.randint(-400,400)),
                float(random.randint(0,400)),
                float(random.randint(-400,0))
            ))
        return points
