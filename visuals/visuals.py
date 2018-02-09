'''
Author: Jan Swoboda
Date: April - July 2013

Copyright 2013

LEGAL INFO:

This file is part of opticfoo (virtual room VJ concept - VRC in short).

Opticfoo is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Opticfoo is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''

# import created visuals
from helper.videotextures import VideoTextures
from helper.textures import Textures
from visual import visual
#from firsttry import FirstTry
#from backgroundbeats import BackgroundBeat
#from cardquad import CardQuad
from enterprise import Enterprise
from texturecard import TextureCard
#from skaterampone import SkateRampOne
from vrclight import VRCLight
#from skull import Skull
#from p90 import P90
from technics import Technics
from skybox import Skybox
from skycube import SkyCube
from rotatingcards import RotatingCards
from spaceinvader import SpaceInvader
from mask import Mask
from feelingfeels import FeelingFeels
#from technix import Technix
from intro import Intro
#from megabox import MegaBox
#from videodeck import VideoDeck
from cards import Cards
from sky import Sky
from sphere import Sphere
from rotatingcubes import RotatingCubes
from rastafari import Rastafari
from pixelplanes import PixelPlanes
from boxbox import BoxBox
from spaceships import SpaceShips
#from stars import Stars
from hackers import Hackers
from life import Life
from mrt import MRT
from midi import MidiVideo
from strobo import Strobo
#from trotzdem import Trotzdem
#from shadertest import ShaderTest

class VisualFactory:
    def __init__(self, loader, render, snd, windows):
        self.loader = loader
        self.render = render
        self.snd = snd
        self.windows = windows  # not necessary for now
        self.visuals = {} # dict to hold visuals as "name":visual-reference
        #self.videos = VideoTextures()
        self.textures= Textures(loader)
        self.spawnVisuals()

    def spawnVisuals(self):
        #self.visuals['firsttry'] = FirstTry(self.loader, self.render, self.snd)
        self.visuals['placeholder'] = visual(self.loader, self.render, self.snd)
        #self.visuals['cardquad'] = CardQuad(self.loader, self.render, self.snd)
        self.visuals['enterprise'] = Enterprise(self.loader, self.render, self.snd)
        #self.visuals['enterprise'] = Enterprise(self.loader, self.render, self.snd)
        #self.visuals['texturecard'] = TextureCard(self.loader, self.render, self.snd)
        #self.visuals['skatesculp1'] = SkateRampOne(self.loader, self.render, self.snd)
        self.visuals['vrclight'] = VRCLight(self.loader, self.render, self.snd) # experimental use of light and shadows
        #self.visuals['skull'] = Skull(self.loader, self.render, self.snd)
        #self.visuals['P90'] = P90(self.loader, self.render, self.snd)
        #self.visuals['stars'] = Stars(self.loader, self.render, self.snd)
        #self.visuals['technics'] = Technics(self.loader, self.render, self.snd)
        self.visuals['skybox'] = Skybox(self.loader, self.render, self.snd)
        self.visuals['skycube'] = SkyCube(self.loader, self.render, self.snd)
        self.visuals['skycube'].setTextures(self.textures)
        #self.visuals['Flashy Cubes'] = RotatingCards(self.loader, self.render, self.snd)
        #self.visuals['Space Invader'] = SpaceInvader(self.loader, self.render, self.snd)
        #self.visuals['mask'] = Mask(self.loader, self.render, self.snd)
        #self.visuals['feelingfeels'] = FeelingFeels(self.loader, self.render, self.snd)
        #self.visuals['technix'] = Technix(self.loader, self.render, self.snd)
        #self.visuals['Intro'] = Intro(self.loader, self.render, self.snd)
        #self.visuals['MegaBox'] = MegaBox(self.loader, self.render, self.snd)
        #self.visuals['VideoDeck'] = VideoDeck(self.loader, self.render, self.snd)
        #self.visuals['VideoDeck'].setVideoTextures(self.videos)
        self.visuals['Cards'] = Cards(self.loader, self.render, self.snd)
        self.visuals['Planets'] = Sky(self.loader, self.render, self.snd)
        #self.visuals['Sphere'] = Sphere(self.loader, self.render, self.snd)
        #self.visuals['Rotating Cubes'] = RotatingCubes(self.loader, self.render, self.snd)
        #self.visuals['Rastafari'] = Rastafari(self.loader, self.render, self.snd)
        self.visuals['Midi Video Text'] = MidiVideo(self.loader, self.render, self.snd)
        self.visuals['Strobo'] = Strobo(self.loader, self.render, self.snd)
        self.visuals['Pixel Planes'] = PixelPlanes(self.loader, self.render, self.snd)
        self.visuals['Pixel Planes'].setTextures(self.textures)
        #self.visuals['Box Box'] = BoxBox(self.loader, self.render, self.snd)
        #self.visuals['Space Ship'] = SpaceShips(self.loader, self.render, self.snd)
        #self.visuals['Hackers'] = Hackers(self.loader, self.render, self.snd)
        #self.visuals['Hackers'].setTextures(self.textures)
        self.visuals['Life'] = Life(self.loader, self.render, self.snd)
        self.visuals['MRT'] = MRT(self.loader, self.render, self.snd)
        #self.visuals['trotzdem'] = Trotzdem(self.loader, self.render, self.snd)
        #self.visuals['shadertest'] = ShaderTest(self.loader, self.render, self.snd)

