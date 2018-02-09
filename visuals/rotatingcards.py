from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from direct.interval.LerpInterval import LerpColorInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc
from visual import visual
import random

class RotatingCards(visual):
    def setup(self):
        self.box = self.loader.loadModel("box.egg")
        self.box.setScale(20)
        self.box.setPos(-10, -10, -10)
        self.box1 = self.path.attachNewNode("box")
        self.box.reparentTo(self.box1)
        #self.plane = CardMaker("plane")
        #self.plane.setFrame(-10,10,-10,10)
        #self.box1 = self.path.attachNewNode("box")
        
        #self.left = self.box1.attachNewNode(self.plane.generate())
        #self.right = self.box1.attachNewNode(self.plane.generate())
        #self.up = self.box1.attachNewNode(self.plane.generate())
        #self.down = self.box1.attachNewNode(self.plane.generate())
        #self.front = self.box1.attachNewNode(self.plane.generate())
        #self.back = self.box1.attachNewNode(self.plane.generate())
        #self.left.setX(-10)
        #self.right.setX(10)
        #self.up.setZ(10)
        #self.down.setZ(-10)
        #self.left.setH(270)
        #self.right.setH(90)
        #self.up.setP(270)
        #self.down.setP(90)
        #self.front.setY(-10)
        #self.back.setY(10)
        #self.back.setH(180)
        self.path.setTwoSided(1)
       
        self.box2 = self.box1.copyTo(self.path)
        self.box3 = self.box1.copyTo(self.path)
        self.box4 = self.box1.copyTo(self.path)
        self.box5 = self.box1.copyTo(self.path)
        self.box6 = self.box1.copyTo(self.path)
        self.box7 = self.box1.copyTo(self.path)
        self.box8 = self.box1.copyTo(self.path)

        self.box1.setPos(self.box1, 10, 10, 10)
        self.box2.setPos(self.box2, -10, 10, 10)
        self.box3.setPos(self.box3, 10, -10, 10)
        self.box4.setPos(self.box4, -10, -10, 10)
        self.box5.setPos(self.box5, 10, 10, -10)
        self.box6.setPos(self.box6, -10, 10, -10)
        self.box7.setPos(self.box7, 10, -10, -10)
        self.box8.setPos(self.box8, -10, -10, -10)

        self.func = {}
        self.m = 0.0
        self.facetex = MovieTexture("textures/astronaut_big.avi")
        self.apollotex = MovieTexture("textures/apollo_big.avi")
        self.whitetex = self.loader.loadTexture("white.png")
        self.applyTexture(self.whitetex)
        assert self.apollotex.read("textures/apollo_big.avi")
        assert self.facetex.read("textures/astronaut_big.avi")

    
    def performBeat(self):
        self.m = self.sndX + self.sndY + self.sndZ
        if self.m >30: self.m = 30;
        map(lambda x: x(), self.func.values())

    def bzz(self):
        self.box1.setPos(10,10,10+self.m)
        self.box2.setPos(-10, 10+self.m, 10)
        self.box3.setPos(10, -10-self.m, 10)
        self.box4.setPos(-10-self.m, -10, 10)
        self.box5.setPos(10, 10, -10-self.m)
        self.box6.setPos(-10, 10+self.m, -10)
        self.box7.setPos(10, -10, -10-self.m)
        self.box8.setPos(-10, -10-self.m, -10)

    def krr(self):
        if self.sndX > self.snd.xThreshold:
            self.box1.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box2.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box3.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box4.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box5.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box6.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box7.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)
            self.box8.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, random.randint(0,100)/100.0)

    def effect1up(self):
        if 'bzz' in self.func:
            self.func.pop('bzz')
        else: self.func['bzz'] = self.bzz

    def effect2up(self):
        if "krr" in self.func:
            self.func.pop("krr")
        else: self.func['krr'] = self.krr

    def effect3up(self):
        self.clearTexture()
        self.applyTexture(self.facetex)
        self.facetex.play()

    def effect4up(self):
        self.clearTexture()
        self.box1.setTexture(self.apollotex, 1)
        self.box2.setTexture(self.apollotex, 1)
        self.box3.setTexture(self.apollotex, 1)
        self.box4.setTexture(self.apollotex, 1)
        self.box5.setTexture(self.apollotex, 1)
        self.box6.setTexture(self.apollotex, 1)
        self.box7.setTexture(self.apollotex, 1)
        self.box8.setTexture(self.apollotex, 1)
        self.apollotex.play()

    def effect0up(self):
        self.apollotex.stop()
        self.facetex.stop()
        self.box1.setColor(1,1,1,1)
        self.box2.setColor(1,1,1,1)
        self.box3.setColor(1,1,1,1)
        self.box4.setColor(1,1,1,1)
        self.box5.setColor(1,1,1,1)
        self.box6.setColor(1,1,1,1)
        self.box7.setColor(1,1,1,1)
        self.box8.setColor(1,1,1,1)
        self.clearTexture()
        self.clearTexture()
        self.applyTexture(self.whitetex)
        

    def clearTexture(self):
        self.box1.clearTexture()
        self.box2.clearTexture()
        self.box3.clearTexture()
        self.box4.clearTexture()
        self.box5.clearTexture()
        self.box6.clearTexture()
        self.box7.clearTexture()
        self.box8.clearTexture()

    def applyTexture(self, tex):
        self.box1.setTexture(tex, 1)
        self.box2.setTexture(tex, 1)
        self.box3.setTexture(tex, 1)
        self.box4.setTexture(tex, 1)
        self.box5.setTexture(tex, 1)
        self.box6.setTexture(tex, 1)
        self.box7.setTexture(tex, 1)
        self.box8.setTexture(tex, 1)
