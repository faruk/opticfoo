from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage
from visual import visual

class FirstTry(visual):
    def setup(self):
        self.tex1 = MovieTexture('videos/saturn5_apollo_launch.mp4')
        assert self.tex1.read('videos/saturn5_apollo_launch.mp4')
        self.tex2 = MovieTexture('videos/boards_eye_view.mp4')
        assert self.tex2.read('videos/boards_eye_view.mp4')

        self.cm1 = CardMaker('saturn')
        self.cm1.setFrameFullscreenQuad()
        self.cm1.setUvRange(self.tex1)
        self.card1 = NodePath(self.cm1.generate())
        self.card1.reparentTo(self.path)
        self.card1.setPos(0,0,10)
        self.card1.setP(50)

        self.cm2 = CardMaker('board')
        self.cm2.setFrameFullscreenQuad()
        self.cm2.setUvRange(self.tex2)
        self.card2 = NodePath(self.cm2.generate())
        self.card2.reparentTo(self.path)
        self.card2.setPos(0,0,-10)
        self.card2.setP(-50)

        self.card1.setTexture(self.tex1)
        self.card1.setTexScale(TextureStage.getDefault(), self.tex1.getTexScale())
        self.card2.setTexture(self.tex2)
        self.card2.setTexScale(TextureStage.getDefault(), self.tex2.getTexScale())

        self.card1.setScale(10)
        self.card2.setScale(10)

    def getBeat(self):
        pass
