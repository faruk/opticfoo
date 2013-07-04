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
from visual import visual
from firsttry import FirstTry
from backgroundbeats import BackgroundBeat
from cardquad import CardQuad
from enterprise import Enterprise
from texturecard import TextureCard
from skaterampone import SkateRampOne
from vrclight import VRCLight
from skull import Skull
from p90 import P90
from stars import Stars

class VisualFactory:
    def __init__(self, loader, render, snd, windows):
        self.loader = loader
        self.render = render
        self.snd = snd
        self.windows = windows  # not necessary for now
        self.visuals = {} # dict to hold visuals as "name":visual-reference
        self.spawnVisuals()

    def spawnVisuals(self):
        #self.visuals['firsttry'] = FirstTry(self.loader, self.render, self.snd)
        self.visuals['placeholder'] = visual(self.loader, self.render, self.snd)
        self.visuals['backgroundbeat'] = BackgroundBeat(self.loader, self.render, self.snd)
        self.visuals['backgroundbeat1'] = BackgroundBeat(self.loader, self.render, self.snd)
        self.visuals['cardquad'] = CardQuad(self.loader, self.render, self.snd)
        self.visuals['enterprise'] = Enterprise(self.loader, self.render, self.snd)
        self.visuals['enterprise'] = Enterprise(self.loader, self.render, self.snd)
        #self.visuals['texturecard'] = TextureCard(self.loader, self.render, self.snd)
        #self.visuals['skatesculp1'] = SkateRampOne(self.loader, self.render, self.snd)
        self.visuals['vrclight'] = VRCLight(self.loader, self.render, self.snd) # experimental use of light and shadows
        self.visuals['skull'] = Skull(self.loader, self.render, self.snd)
        self.visuals['P90'] = P90(self.loader, self.render, self.snd)
        self.visuals['stars'] = Stars(self.loader, self.render, self.snd)
