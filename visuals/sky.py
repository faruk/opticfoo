from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual
from helper.colors import Colors

class Sky(visual):
    
    def setup(self):
        self.Colors = Colors()

        card = CardMaker("plane")
        card.setFrame(-100,100,-100,100)

        self.moons = [ 
            self.path.attachNewNode('moon1'),
            self.path.attachNewNode('moon2'),
        ]

        self.ringpath = self.path.attachNewNode("ring")
        self.ring = self.ringpath.attachNewNode(card.generate())
        self.ring2 = self.ringpath.attachNewNode(card.generate())
        self.ring2.setP(180)
        self.ring2.setY(0.01)
        #self.ring.setPos(-50,0,-50)
        #self.ringpath.setScale(150)
        self.ringpath.setP(90)
        self.ringpath.setTwoSided(1)
        self.ringtex = self.loader.loadTexture("ring.png")
        self.ringpath.setTexture(self.ringtex, 1)

        self.moons[0].reparentTo(self.path)
        self.moons[1].reparentTo(self.path)
        
        self.spheres = [
            self.sphere((0,0,0),70),
            self.sphere((0,0,0),20),
            self.sphere((0,0,0),10),
        ]
        self.spheres[0].reparentTo(self.path)
        self.spheres[1].reparentTo(self.moons[0])
        self.spheres[2].reparentTo(self.moons[1])

        self.moons[0].setPos(0,0,0)
        self.moons[1].setPos(0,0,0)
        self.spheres[1].setPos(-150,0,0)
        self.spheres[2].setPos(-200,0,0)

        self.textures = {
            'checkersphere': self.loader.loadTexture("checkersphere.png"),
            'planet1': self.loader.loadTexture("planet1.jpg"),
            'planet2': self.loader.loadTexture("planet2.jpg"),
            'planet3': self.loader.loadTexture("planet3.jpg"),
            'planet4': self.loader.loadTexture("planet4.jpg"),
        }
        self.moons[0].setTexture(self.textures['checkersphere'])
        self.moons[1].setTexture(self.textures['checkersphere'])
        self.spheres[0].setTexture(self.textures['checkersphere'])
        self.spheres[1].setTexture(self.textures['checkersphere'])
        self.spheres[2].setTexture(self.textures['checkersphere'])

        self.texlist = []
        for k in self.textures:
            self.texlist.append(self.textures[k])

        self.soundFuncDict = {
            'one' : self.soundFunction1,
            'two' : self.soundFunction2,
            'three': self.soundFunction3,
            'none' : self.nothing
        }
        self.soundFunc = self.nothing
        self.ringOn = True
        self.ringScale = LerpScaleInterval(self.ringpath, 3, 3, 1, blendType = 'easeOut')
        self.ringFade = LerpFunc(self.fadeRing, fromData = 1 , toData = 0, duration = 3, name = "ring fade")
        self.ringAnimation = Parallel(self.ringScale, self.ringFade)

    def perfomBeat(self):
        self.soundFunc()

    def sphere(self, pos, size):
        path = self.loader.loadModel("smiley.egg")
        path.clearTexture()
        path.setColor(1,1,1,1)
        x, y, z = pos
        s = size
        path.setPos(x,y,z)
        path.setScale(s)
        return path

    def soundFunction1(self):
        if self.sndX > self.snd.xThreshold:
            self.detachAttachSpheres()

    def soundFunction2(self):
        #self.ringpath.setScale(self.sndX)
        pass

    def soundFunction3(self):
        pass

    def nothing(self):
        pass


    def detachAttachSpheres(self):
        x = random.randint(0, len(self.spheres) - 1)
        self.spheres[x].detach()
        x = random.randint(0, len(self.spheres) - 1)
        self.spheres[x].attach()
        x = random.randint(0, len(self.spheres) - 1)
        self.spheres[x].attach()
        
    
    def effect1up(self):
        x = self.texlist.pop(0)
        s = self.spheres[0]
        s.setTexture(x, 1)
        self.texlist.append(x)
    
    def effect2up(self):
        x = self.texlist.pop(0)
        s = self.spheres[1]
        s.setTexture(x, 1)
        self.texlist.append(x)
        
    def effect3up(self):
        x = self.texlist.pop(0)
        s = self.spheres[2]
        s.setTexture(x, 1)
        self.texlist.append(x)

    def effect4(self):
        self.moons[0].setH(self.moons[0], +self.visualMovementSpeed/2)

    def effect5(self):
        self.moons[1].setH(self.moons[1], +self.visualMovementSpeed*2)

    def effect6(self):
        self.spheres[0].setH(self.spheres[0], +self.visualMovementSpeed)

    def effect7(self):
        if self.sndX > self.snd.xThreshold:
            self.moons[0].setHpr(random.randint(0,360), random.randint(0,360), random.randint(0,360))
            self.moons[1].setHpr(random.randint(0,360), random.randint(0,360), random.randint(0,360))
        if self.sndY > self.snd.yThreshold:
        #    self.ringpath.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
            v = random.sample( self.Colors.colors['sunset cloud colors'], 1 )[0]
            r, g, b, a = v
            self.ringpath.setColor(r, g, b, a)
        if self.sndZ > self.snd.zThreshold:
            v = random.sample( self.Colors.colors['yellow sunset colors'], 1 )[0]
            r,g,b,a = v
            self.spheres[0].setColor(r,g,b,a)
            v = random.sample( self.Colors.colors['yellow sunset colors'], 1 )[0]
            r,g,b,a = v
            self.spheres[1].setColor(r,g,b,a)
            v = random.sample( self.Colors.colors['yellow sunset colors'], 1 )[0]
            r,g,b,a = v
            self.spheres[2].setColor(r,g,b,a)


    def effect7up(self):
        self.moons[0].setP(0)
        self.moons[0].setR(0)
        self.moons[1].setP(0)
        self.moons[1].setR(0)

    def effect8(self):
        if self.sndX > self.snd.xThreshold:
            if self.ringOn:
                self.ringpath.detachNode()
                self.ringOn = False
            else:
                self.ringpath.reparentTo(self.path)
                self.ringAnimation.start()
    
    def effect8up(self):
        self.ringpath.setScale(1)
        self.ringpath.setAlphaScale(1)
        self.ringpath.reparentTo(self.path)

    def effect8up(self):
        self.soundFunc = self.soundFunction2
    def effect9(self):
        self.ringpath.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)
        
    def effect0up(self):
        self.soundFunc = self.nothing

    def fadeRing(self, i):
        self.ringpath.setAlphaScale(i)
