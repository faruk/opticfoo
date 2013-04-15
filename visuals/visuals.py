from visual import visual
from firsttry import FirstTry

class VisualFactory:
    def __init__(self, loader, render, snd):
        self.visuals = {}
        self.spawnVisuals(loader, render, snd)

    def spawnVisuals(self, loader, render, snd):
        self.visuals['firsttry'] = FirstTry(loader, render, snd)
        self.visuals['placeholder'] = visual(loader, render, snd)


