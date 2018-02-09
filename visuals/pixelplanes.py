from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import random
from visual import visual

class PixelPlanes(visual):

    def setTextures(self, t):
        self.textures = t.textures
        self.shapes = self.textures['shapes']

    def setup(self):
        card = CardMaker("plane")
        card.setFrame(-5,5,-5,5)

        self.cards = []
        self.cardspath = self.path.attachNewNode("cards")
        self.cardspath.setTwoSided(1)
        self.fadelerps = []
        self.fadecount = 5

        for x in range(0,5):
            l = []
            for y in range(0,5):
                c = self.cardspath.attachNewNode(card.generate())
                l.append(c)
                self.fadelerps.append(
                    LerpColorInterval(c, 5, Vec4(1,0,0,0), Vec4(1,0,0,1))
                )
            self.cards.append(l)

        i = 0
        for y in range(-2,3):
            j = 0
            for x in range(-2,3):
                self.cards[i][j].setPos(10*x, 0, 10*y)
                self.cards[i][j].detachNode()
                j = j + 1
            i = i + 1 

        self.reverse = False

        self.cardmatrix = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.define_patterns()
        self.pixelplane_function = self.nothing
        self.texture_function = self.nothing
        self.acab = False

    def nothing(self):
        pass
    
    def update_from_matrix(self):
        i = 0
        for y in self.cardmatrix:
            j = 0
            for x in y:
                if x is 1:
                    self.cards[i][j].reparentTo(self.cardspath)
                else:
                    self.cards[i][j].detachNode()
                j = j + 1
            i = i + 1

    def from_inner_to_outter_horizontal(self):
        if self.cardmatrix[2] == [0,0,1,0,0]: 
            self.cardmatrix[2] = [0,1,0,1,0]
            return
        if self.cardmatrix[2] == [0,1,0,1,0]:
            self.cardmatrix[2] = [1,0,0,0,1]
            return
        if self.cardmatrix[2] == [1,0,0,0,1]:
            self.cardmatrix[2] = [0,0,1,0,0]
            return

    def horizontal(self):
        self.cardmatrix = self.patterns['horizontal'][self.horizontal_index]
        if self.horizontal_index < len(self.patterns['horizontal'])-1:
            self.horizontal_index = self.horizontal_index + self.operant
        else:
            self.horizontal_index = 0
        print self.horizontal_index
        self.update_from_matrix()

    def cross(self):
        self.cardmatrix = self.patterns['cross'][self.cross_index]
        if self.cross_index < len(self.patterns['cross'])-1:
            self.cross_index = self.cross_index + self.operant
        else:
            self.cross_index = 0
        self.update_from_matrix()

    def square(self):
        self.cardmatrix = self.patterns['square'][self.square_index]
        if self.square_index < len(self.patterns['square'])-1:
            self.square_index = self.square_index + self.operant
        else:
            self.square_index = 0
        self.update_from_matrix()
    
    def set_shapes(self):
        shapes = self.shapes.values()
        shapes = random.sample(shapes, random.randint(1, len(shapes)))
        for cardlist in self.cards:
            for card in cardlist:
                card.setTexture(random.sample(shapes, 1)[0], 1)
                card.setR(random.randint(0, 360))
                if self.acab:
                    card.setColor(random.randint(0,100)/100.0,random.randint(0,100)/100.0,random.randint(0,100)/100.0, 1)

    def fade_cards(self):
        lerps = random.sample(self.fadelerps, self.fadecount)
        map(lambda x: x.start(), lerps)

    def performBeat(self):
        if self.sndX > self.snd.xThreshold:
            self.pixelplane_function()
        if self.sndY > self.snd.yThreshold:
            self.texture_function()

    def effect1up(self):
        self.pixelplane_function = self.horizontal

    def effect2up(self):
        self.pixelplane_function = self.cross

    def effect3up(self):
        self.pixelplane_function = self.square
    """
    def effect4up(self):
        self.operant = self.operant* -1
    """

    def effect5up(self):
        if self.texture_function != self.set_shapes:
            self.texture_function = self.set_shapes
        else:
            self.texture_function = self.nothing
            for cardlist in self.cards:
                for card in cardlist:
                    card.clearTexture()
                    card.setR(0)

    def effect6up(self):
        self.acab = not self.acab

    def effect7up(self):
        self.pixelplane_function = self.nothing
        self.texture_function = self.nothing
        self.cardmatrix = self.patterns['all'][0]
        self.update_from_matrix()
        for cardlist in self.cards:
            for card in cardlist:
                card.setColor(1,0,0)

    def effect8up(self):
        self.pixelplane_function = self.fade_cards

    def effect9up(self):
        if self.fadecount > 1:
            self.fadecount = self.fadecount - 1

    def effect0up(self):
        if self.fadecount < 25:
            self.fadecount = self.fadecount + 1


    def define_patterns(self):
        self.horizontal_index = 0
        self.cross_index = 0
        self.square_index = 0
        self.operant = 1
        self.patterns = {
            'horizontal': [
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [1,0,0,0,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                ],
            ],
            'cross': [
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                ],
                [
                    [1,0,0,0,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                ],
            ],
            'square': [
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [0,1,0,1,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0],
                ],
                [
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                ],
                [
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                ],
            ],
            'all': [
                [
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                ]
            ],
        }
