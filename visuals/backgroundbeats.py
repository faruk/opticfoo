from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from direct.interval.LerpInterval import LerpColorInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc
from visual import visual

class BackgroundBeat(visual):

    def setup(self):
        self.lastBeat = 0
        self.maxMag = 0
        self.path.removeNode()
        self.path = self.render.attachNewNode("bgb")
        self.path.setTransparency(TransparencyAttrib.MAlpha)
        self.cards = []
        self.cardPaths = []
        for i in range(0, 10*10):
            self.cards.append(CardMaker("background beat card"+str(i)))
            self.cardPaths.append(NodePath(self.cards[i].generate()))
            self.cardPaths[i].reparentTo(self.path)
        coords = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
        index = 0
        for i in range(0,10):
            for k in range(0,10):
                self.cardPaths[index].setPos(coords[i], 0, coords[k])
                index = index + 1
        self.colorLerp = LerpColorInterval(self.path, 0.5, (1,1,1,1), (1,0,0,1))
        self.transparencyLerp = LerpFunc(self.flashWhite,
            fromData = 1, toData = 0, duration = 0.5, name = "transFlash")

    def performBeat(self):
        self.lastBeat = self.sndX
        self.maxMag = max(self.lastBeat, self.maxMag)
        if self.sndY > self.snd.xThreshold:
            print "whaaaaaaaaat", self.sndY
            Sequence(self.transparencyLerp).start()
        if self.sndX > self.snd.yThreshold:
            Sequence(self.colorLerp).start()
            print "whuuuuuz", self.sndX

    def flashWhite(self, i):
        self.path.setAlphaScale(i)
