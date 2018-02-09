from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class VideoDeck(visual):
    
    def setVideoTextures(self, v):
        self.videos = v.videos

    def setup(self):
        self.card = CardMaker("plane")

        self.card.setFrame(-10, 10, -1.1, 1.1)
        
        # video deck
        self.deckpath = self.path.attachNewNode("videodeck")
        self.deck = {} 
        self.deck['front'] = self.deckpath.attachNewNode(self.card.generate())
        self.deck['left'] = self.deckpath.attachNewNode(self.card.generate())
        self.deck['right'] = self.deckpath.attachNewNode(self.card.generate())
        self.deck['back'] = self.deckpath.attachNewNode(self.card.generate())

        self.card.setFrame(-10,10,-10,10)

        self.deck['top'] = self.path.attachNewNode(self.card.generate())
        self.deck['bottom'] = self.path.attachNewNode(self.card.generate())

        # arrange video deck sides

        self.deck['left'].setX(-10)
        self.deck['left'].setH(270)
        self.deck['left'].setColor(0.3,0.3,0.3,1)

        self.deck['right'].setX(10)
        self.deck['right'].setH(90)
        self.deck['right'].setColor(0.3,0.3,0.3,1)
        
        self.deck['back'].setY(-10)
        self.deck['back'].setColor(0.3,0.3,0.3,1)

        self.deck['front'].setY(10)
        self.deck['front'].setH(180)

        self.deck['top'].setZ(1.1)
        self.deck['top'].setP(270)
        self.deck['top'].setColor(0.3,0.3,0.3,1)

        self.deck['bottom'].setZ(-1.1)
        self.deck['bottom'].setP(90)
        self.deck['bottom'].setColor(0.3,0.3,0.3,1)

        # set textures and colors
        self.frontTex = self.loader.loadTexture("videodeckfront.jpg")
        self.deck['front'].setTexture(self.frontTex)

        self.deckpath.setColor(0.3,0.3,0.3,1,1)

        # dvd

        self.card.setFrame(-3.58, 3.58, -3.58, 3.58)
        self.dvdpath = self.path.attachNewNode("dvd")
        self.dvd = {}
        self.dvd['top'] = self.dvdpath.attachNewNode(self.card.generate())
        self.dvd['bottom'] = self.dvdpath.attachNewNode(self.card.generate())
        self.dvd['bottom'].setZ(-0.05)
        self.dvd['top'].setP(270)
        self.dvd['bottom'].setP(90)
        self.dvd['top'].setTexture(self.loader.loadTexture("dvdtop.png"))
        self.dvd['bottom'].setTexture(self.loader.loadTexture("dvdbottom.png"))
        self.dvdpath.setTwoSided(1)
        self.dvdpath.setY(15)
        #self.dvdpath.setP(180)

        self.spindvd = LerpHprInterval(self.dvdpath, 100, Vec3(0,0,0), Vec3(360, 0, 0))
        self.dvdseq = Sequence(self.spindvd).loop()
        self.rolldvd = LerpHprInterval(self.dvdpath, 50, Vec3(0,0,0), Vec3(0,0,360))
        dvdup = LerpPosInterval(self.dvdpath,     0.5, Vec3(0,15,0.9), Vec3(0,15,0))
        dvdright = LerpPosInterval(self.dvdpath,  0.1, Vec3(-6,15,0), Vec3(0,15,0.9))
        dvdinsert = LerpPosInterval(self.dvdpath,   1.5, Vec3(-6,0,0.9), Vec3(-6,15,0.9))
        self.insertdvd = Sequence(dvdup, dvdright, dvdinsert)

        # screens

        self.card.setFrame(-15,15,-15,15)
        self.screenpath = self.path.attachNewNode("screen")
        left = self.screenpath.attachNewNode(self.card.generate())
        right = self.screenpath.attachNewNode(self.card.generate())
        up = self.screenpath.attachNewNode(self.card.generate())
        down = self.screenpath.attachNewNode(self.card.generate())
        front = self.screenpath.attachNewNode(self.card.generate())
        back = self.screenpath.attachNewNode(self.card.generate())

        left.setX(-20)
        left.setH(90)
        right.setX(20)
        right.setH(270)
        up.setZ(20)
        up.setP(90)
        down.setZ(-20)
        down.setP(270)
        front.setY(-20)
        front.setH(180)
        back.setY(20)

        # videotextures
        self.noise = MovieTexture("textures/noise.avi")
        assert self.noise.read("textures/noise.avi")
        #self.screenpath.setTexture(noise)

    def effect1up(self):
        Parallel(self.rolldvd).start()

    def effect2up(self):
        self.insertdvd.start()

    def effect3up(self):
        self.screenpath.setTexture(self.noise)
        self.noise.play()
    
    def effect4up(self):
        self.screenpath.setTexture(self.videos['noise'])
        self.videos['noise'].play()
