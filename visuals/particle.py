from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import DirectionalLight, Vec3, Vec4
from panda3d.core import PandaNode
#from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpPosInterval
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
import math, sys, colorsys
from visual import visual
from direct.particles.ParticleEffect import ParticleEffect

class Particle(visual):

    def setup(self):
        
