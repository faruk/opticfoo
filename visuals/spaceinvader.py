from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib, Shader
from direct.interval.LerpInterval import LerpColorInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc
from visual import visual
import random

class SpaceInvader(visual):
    def setup(self):
        #self.box = self.loader.loadModel("box.egg")
        #self.box.setScale(10)
        #self.box.setPos(-5,-5,-5)

        self.s1 = self.loader.loadModel("spaceinvader1.egg")
        self.s1.reparentTo(self.path)
        self.s1.setScale(0.4)
        self.s1.setP(90)
        self.s1.setZ(-15)

        self.s2 = self.loader.loadModel("spaceinvader2.egg")
        self.s2.reparentTo(self.path)
        self.s2.setScale(0.4)
        self.s2.setP(90)
        self.s2.setZ(-15)

        self.s3 = self.loader.loadModel("spaceinvader3.egg")
        self.s3.reparentTo(self.path)
        self.s3.setScale(0.4)
        self.s3.setP(90)
        self.s3.setZ(-15)
        
        self.s2.detachNode()
        self.s3.detachNode()

        self.videotex = MovieTexture("textures/astronaut_big.avi")
        assert self.videotex .read("textures/astronaut_big.avi")
        self.videotex.play()
        self.s1.setTexture(self.videotex, 1)
        self.s2.setTexture(self.videotex, 1)
        self.s3.setTexture(self.videotex, 1)
        
        myShader = Shader.load(Shader.SL_GLSL, "shader/myvertexshader.glsl", "shader/myfragmentshader.glsl")
        self.s1.set_shader(myShader)




        self.m = 0
        self.func = {}

    def performBeat(self):
        self.m = self.sndX +self.sndY + self.sndZ
        map(lambda x: x(), self.func.values())

    def bzz(self):
        if self.m > 40: self.m = 40.0
        self.m/2
        self.path.setSz(self.scale+self.m/20.0)
    
    def byy(self):
        if self.m > 40: self.m = 40.0
        self.m/2
        self.path.setSy(self.scale+self.m/20.0)

    def bxx(self):
        if self.m > 40: self.m = 40.0
        self.m/2
        self.path.setSx(self.scale+self.m/20.0)

    def ccc(self):
        if self.sndX > self.snd.xThreshold or self.sndY > self.snd.yThreshold:
            self.path.setColor(random.randint(0,100)/100.0,
                random.randint(0,100)/100.0,
                random.randint(0,100)/100.0,
                self.transparency)

    def rrr(self):
        if self.sndX > self.snd.xThreshold or self.sndY > self.snd.yThreshold:
            x = random.randint(1,3)
            if x == 1:
                self.effect1()
            elif x == 2:
                self.effect2()
            elif x == 3:
                self.effect3()

    def effect1(self):
        self.s1.reparentTo(self.path)
        self.s2.detachNode()
        self.s3.detachNode()

    def effect2(self):
        self.s2.reparentTo(self.path)
        self.s1.detachNode()
        self.s3.detachNode()

    def effect3(self):
        self.s3.reparentTo(self.path)
        self.s1.detachNode()
        self.s2.detachNode()

    def effect4(self):
        if 'bzz' in self.func:
            self.func.pop("bzz")
            self.path.setSz(self.scale)
        else: self.func['bzz'] = self.bzz

    def effect5(self):
        if 'byy' in self.func:
            self.func.pop("byy")
            self.path.setSy(self.scale)
        else: self.func['byy'] = self.byy

    def effect6(self):
        if 'bxx' in self.func:
            self.func.pop("bxx")
            self.path.setSx(self.scale)
        else: self.func['bxx'] = self.bxx

    def effect7(self):
        if 'ccc' in self.func:
            self.func.pop('ccc')
            self.path.setColor(0,0,0,1)
        else: self.func['ccc'] = self.ccc
        
    def effect8(self):
        if 'rrr' in self.func:
            self.func.pop('rrr')
        else: self.func['rrr'] = self.rrr
