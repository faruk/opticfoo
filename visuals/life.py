from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class Life(visual):
    
    def setup(self):
        card = CardMaker("plane")

        card.setFrame(-10,10,-10,10)

        self.textures = {
            '1': loader.loadTexture('davinci_human.png'),
            '2': loader.loadTexture('embryo_0.png'),
            '3': loader.loadTexture('embryo_2.png'),
            '4': loader.loadTexture('lsd.png'),
            '5': loader.loadTexture('amoeba_proteus.png'),
        }

        self.texlist = [
            self.textures['1'], 
            self.textures['2'], 
            self.textures['3'], 
            self.textures['4'], 
            self.textures['5'], 
        ]

        self.path.setTwoSided(1)
        self.card = self.path.attachNewNode("card")
        self.card.attachNewNode(card.generate())

    def effect1(self):
        self.card.setTexture(self.textures['1'])

    def effect2(self):
        self.card.setTexture(self.textures['2'])

    def effect3(self):
        self.card.setTexture(self.textures['3'])

    def effect4(self):
        self.card.setTexture(self.textures['4'])

    def effect5(self):
        self.card.setTexture(self.textures['5'])
    
    def effect6(self):
        i = random.randint(0,4)
        self.card.setTexture(self.texlist[i])

    def effect7up(self):
        i = random.randint(0,4)
        self.card.setTexture(self.texlist[i])
