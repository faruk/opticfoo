from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
from helper.colors import Colors
import random
from visual import visual

class MidiVideo(visual):

    def setup(self):
        self.walktex = MovieTexture("textures/charcoal_walk.mpg")
        assert self.walktex.read("textures/charcoal_walk.mpg")
        self.groundtex = MovieTexture("textures/charcoal_ground_darker.mpg")
        assert self.groundtex.read("textures/charcoal_ground_darker.mpg")
        self.peopletex = MovieTexture("textures/charcoal_people.mpg")
        assert self.peopletex.read("textures/charcoal_people.mpg")
        self.wavetex = MovieTexture("texture/wave.mpg")
        assert self.wavetex.read("textures/wave.mpg")
        self.lichtboingtex = MovieTexture("textures/licht_boing.mpg")
        assert self.lichtboingtex.read("textures/licht_boing.mpg")
        self.lichtmotiontex = MovieTexture("textures/licht_motion.mpg")
        assert self.lichtmotiontex.read("textures/licht_motion.mpg")
        self.card = CardMaker("plane")
        self.card.setFrame(-10,10,-10,10)

        self.plane = self.path.attachNewNode(self.card.generate())
        self.videotex = self.walktex
        self.plane.setTexture(self.videotex, 1)
        self.videotex.play()

        self.midi_control_functions[74] = self.set_video_speed
        
    def set_video_speed(self):
        val = (self.midi_value/127.0) * 4
        self.videotex.setPlayRate(val)

    def effect1up(self):
        self.videotex.stop()
        self.videotex = self.walktex
        self.videotex.play()

    def effect2up(self):
        self.videotex.stop()
        self.videotex = self.groundtex
        self.videotex.play()

    def effect3up(self):
        self.videotex.stop()
        self.videotex = self.peopletex
        self.videotex.play()

    def effect4up(self):
        self.videotex.stop()
        self.videotex = self.wavetex
        self.videotex.play()

    def effect5up(self):
        self.videotex.stop()
        self.videotex = self.lichtboingtex
        self.videotex.play()

    def effect6up(self):
        self.videotex.stop()
        self.videotex = self.lichtmotiontex
        self.videotex.play()
