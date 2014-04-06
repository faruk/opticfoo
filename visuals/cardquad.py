from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from visual import visual

class CardQuad(visual):
    def setup(self):
        self.path.removeNode()
        self.path = self.render.attachNewNode("Card Quad")

        self.plane = CardMaker("plane")

        self.plane.setFrame(-10,10,-10,10)
        self.left = self.path.attachNewNode(self.plane.generate())
        self.right = self.path.attachNewNode(self.plane.generate())
        self.up = self.path.attachNewNode(self.plane.generate())
        self.down = self.path.attachNewNode(self.plane.generate())
        self.front = self.path.attachNewNode(self.plane.generate())
        self.back = self.path.attachNewNode(self.plane.generate())
        self.left.setX(-10)
        self.right.setX(10)
        self.up.setZ(10)
        self.down.setZ(-10)
        self.left.setH(270)
        self.right.setH(90)
        self.up.setP(270)
        self.down.setP(90)
        self.front.setY(-10)
        self.back.setY(10)
        self.back.setH(180)

        self.tex = self.loader.loadTexture("indian_ornament_texture.png")

        self.path.setTexture(self.tex)
        self.path.setTransparency(TransparencyAttrib.MAlpha, 1)
        self.path.setTwoSided(1)

    def performBeat(self):
        x, y, z = self.snd.getBeat()
        self.path.setSx(self.scale*(1+x*0.01))
        self.path.setSy(self.scale*(1+y*0.1))
        self.path.setSz(self.scale*(1+z*3))
