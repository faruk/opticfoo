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

class VisualFactory:
    def __init__(self, loader, render, snd, windows):
        self.loader = loader
        self.render = render
        self.snd = snd
        self.windows = windows
        self.visuals = {}
        self.spawnVisuals()

    def spawnVisuals(self):
        self.visuals['firsttry'] = FirstTry(self.loader, self.render, self.snd)
        self.visuals['placeholder'] = visual(self.loader, self.render, self.snd)
        self.visuals['backgroundbeat'] = BackgroundBeat(self.loader, self.render, self.snd)
        self.visuals['cardquad'] = CardQuad(self.loader, self.render, self.snd)
        self.visuals['enterprise'] = Enterprise(self.loader, self.render, self.snd)
        self.visuals['texturecard'] = TextureCard(self.loader, self.render, self.snd)
        self.visuals['skatesculp1'] = SkateRampOne(self.loader, self.render, self.snd)
        self.visuals['vrclight'] = VRCLight(self.loader, self.render, self.snd)
        self.visuals['skull'] = Skull(self.loader, self.render, self.snd)
        self.visuals['P90'] = P90(self.loader, self.render, self.snd)
