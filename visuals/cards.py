from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Cards(visual):
    
    def setup(self):
        card = CardMaker("plane")

        card.setFrame(-10,10,-10,10)

        self.cards = []
        self.cardspath = self.path.attachNewNode("cards")
        for x in range(0,10):
            self.cards.append(self.cardspath.attachNewNode(card.generate()))
        

        self.scaleSeqs = self.scaleWob(self.cards, 0.2, 1.5, 1, 2)
        self.rotateLerps = self.randomRotateParralel(self.cards, 1, 10)
        self.path.setTwoSided(1)

        self.textures = {
            'noise': MovieTexture("textures/noise.avi"),
            'apollo': MovieTexture("textures/apollo_big.avi"),
            #'quad1px': self.loader.loadTexture("quad1px.png"),
            #'quad2px': self.loader.loadTexture("quad2px.png"),
            'quad5px': self.loader.loadTexture("quad5px.png"),
            #'circle1px': self.loader.loadTexture("circle1px.png"),
            #'circle2px': self.loader.loadTexture("circle2px.png"),
            'circle5px': self.loader.loadTexture("circle5px.png"),
        }
        assert self.textures['noise'].read("textures/noise.avi")
        assert self.textures['apollo'].read("textures/apollo_big.avi")
        self.texList = self.textures.values()

        self.soundFuncDict = {
            'first': self.soundFunction1,
            'second': self.soundFunction2,
            'third': self.soundFunction3,
            'none': self.nothing
        }
        self.soundFuncList = self.soundFuncDict.values()
        self.soundFunc = self.nothing

    def performBeat(self):
        self.soundFunc()
    
    def nothing(self):
        pass

    def soundFunction1(self):
        if self.sndX > self.snd.xThreshold:
            self.effect0up()
        if self.sndY > self.snd.yThreshold:
            self.effect8()

    def soundFunction2(self):
        if self.sndX > self.snd.xThreshold:
            self.effect0up()
        if self.sndY > self.snd.yThreshold:
            self.effect8()
            self.effect8()
            self.effect8()
    
    def soundFunction3(self):
        if self.sndX > self.snd.xThreshold:
            self.effect0up()
            self.effect4()
        if self.sndY > self.snd.yThreshold:
            self.effect8()
            self.effect8()
            self.effect8()
    
    def scaleWob(self, paths, v1, v2, s1, s2):
        newpaths = []
        i = 0
        for p in paths:
            newpaths.append(Sequence(
                LerpScaleInterval(p, v1, s2, s1),
                LerpScaleInterval(p, v2, s1, s2))
            )
        return newpaths

    def randomRotateParralel(self, paths, t_min, t_max):
        newpaths = Parallel()
        i = 0
        for c in paths:
            t = random.randint(int(t_min), int(t_max)-1) * random.random()
            h = c.getH()
            p = c.getP()
            r = c.getR()
            newpaths.append(
                LerpHprInterval(c, t, Vec3(-h, -p, -r), Vec3(h, p, r)) 
            )
        return newpaths
    
    def randomRotateCards(self):
        for c in self.cards:
            h = random.randint(-180,180)
            p = random.randint(-180,180)
            r = random.randint(-180,180)

            c.setHpr(h, p, r)

    def randomCardsPos(self):
        x = random.randint(-11, 10) + random.random()
        y = random.randint(-11, 10) + random.random()
        z = random.randint(-11, 10) + random.random()
        self.cardspath.setPos(x,y,z)

    def moveCardUp(self, c, d):
        c.setY(c.path, d) 

    def moveCards(self, paths, t, d):
        newpaths = Parallel()
        i = 0
        tmp = self.cardspath.attachNewNode("dummyCard")
        for c in paths:
            tmp.setHpr(c.getHpr())
            tmp.setPos(c.getPos())
            tmp.setZ(tmp, d)
            newpaths.append(
                LerpPosInterval(c, t, tmp.getPos(), c.getPos() ) 
            )
        tmp.removeNode()
        return newpaths
        
    def centerCards(self, paths, t):
        newpaths = Parallel()
        i = 0
        for c in paths:
            newpaths.append(
                LerpPosInterval(c, t, Vec3(0,0,0), c.getPos() ) 
            )
        return newpaths
    
    def effect6(self):
        if self.sndX > self.snd.xThreshold:
            self.cardspath.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)

    def effect7up(self):
        self.cardspath.clearTexture()
        self.cardspath.setColor(1,1,1,1)

    def effect8(self):
        i = random.randint(0,len(self.cards)-1)
        self.scaleSeqs[i].start()
    
    def effect9up(self):
        self.rotateLerps = self.randomRotateParralel(self.cards, 1, 10)
        self.rotateLerps.start()

    def effect0up(self):
        self.randomRotateCards()

    def effect1up(self):
        x = self.texList.pop(0)
        self.cardspath.setTexture(x,1)
        self.texList.append(x)

    def effect2up(self):
        self.moveLerps = self.moveCards(self.cards, 5, 20)
        self.moveLerps.start()

    def effect3up(self):
        self.moveLerps = self.centerCards(self.cards, 3)
        self.moveLerps.start()

    def effect4up(self):
        self.cardspath.setPos(0,0,0)

    def effect4(self):
        self.randomCardsPos()

    def effect5up(self):
        x = self.soundFuncList.pop(0)
        self.soundFunc = x
        self.soundFuncList.append(x)

