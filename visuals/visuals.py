from visual import visual
from firsttry import FirstTry
from backgroundbeats import BackgroundBeat

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
        self.visuals['backgroundbeat'] = BackgroundBeat(self.loader, self.render, self.snd, self.windows)


