from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from direct.interval.LerpInterval import LerpColorInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc
from visual import visual

class TextureCard(visual):

    def setup(self):
        self.path.removeNode()
        self.path = self.render.attachNewNode("texturequad")
        self.path.setTransparency(TransparencyAttrib.MAlpha, 1)

        self.tex1 = self.loader.loadTexture("mandala1_transparent.png")
        self.tex2 = self.loader.loadTexture("dark1_transparent.png")
        self.tex3 = self.loader.loadTexture("dark2_transparent.png")
        self.tex4 = self.loader.loadTexture("truchet_transparent.png")

        self.plane = CardMaker("plane")

        self.card = self.path.attachNewNode(self.plane.generate())
        self.cardNode = self.path.attachNewNode("texturecards")
        self.cards1 = []
        for i in range(0, 100):
            self.cards1.append(self.cardNode.attachNewNode(self.plane.generate()))

        coords = range(-50,50)
        i = 0
        for card in self.cards1:
            card.setPos(coords[i], 0, 0)
            i = i + 1


        self.cardNode.detachNode()

        self.path.setTexture(self.tex1)
        self.path.setTwoSided(1)

    def effect1(self):
        self.path.setTexture(self.tex1)

    def effect2(self):
        self.path.setTexture(self.tex2)

    def effect3(self):
        self.path.setTexture(self.tex3)

    def effect4(self):
        self.path.setTexture(self.tex4)

    def effect5(self):
        self.cardNode.reparentTo(self.path)
