from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
import random

class VideoTextures:
    def __init__(self):
        #self.loader = loader

        self.videos = {
            'day of the fight': {
                'clap': "textures/dayofthefight-clap1024.mpeg",
                'dancing': "textures/dayofthefight-dancing1024.mpeg",
                'driving1': "textures/dayofthefight-driving11024.mpeg",
                'driving2': "textures/dayofthefight-driving21024.mpeg",
                'hand': "textures/dayofthefight-hand1024.mpeg",
                'jumpin': "textures/dayofthefight-jumpin1024.mpeg",
                'streetview': "textures/dayofthefight-streetview1024.mpeg",
            },
            'space': {
                'astronaut': "textures/astronaut_big.avi",
                'apollo': "textures/apollo_big.avi",
            },
            'noise': "textures/noise.avi",
            'mrt': "textures/mrt.avi",
        }
        self.init_videos(self.videos)
        
    def init_videos(self, v):
        res = {}
        for x in v:
            if type(v[x]) is dict:
                v[x] = self.init_videos(v[x])
            if type(v[x]) is str:
                v[x] = self.init_video(v[x])
                #v[x] = MovieTexture(v[x])
            res[x] = v[x]
        return res


    def init_video(self, v):
        x = MovieTexture(v)
        assert x.read(v)
        return x
