from panda3d.core import Vec3, Vec4
from direct.interval.LerpInterval import LerpColorInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel

class Colors:
    def __init__(self):
        self.colors = {
            'yellow sunset colors': [
                self.hex2vec4("f27300"),
                self.hex2vec4("fa9800"),
                self.hex2vec4("fd9234"),
                self.hex2vec4("ffc931"),
                self.hex2vec4("ffc442"),
                self.hex2vec4("ffc235"),
            ],
            'sunset cloud colors': [
                self.hex2vec4("ef2001"),
                self.hex2vec4("dd2200"),
                self.hex2vec4("bc5510"),
                self.hex2vec4("b22a00"),
                self.hex2vec4("a3440e"),
                self.hex2vec4("9c3009"),
                self.hex2vec4("783814"),
                self.hex2vec4("66231b"),
                self.hex2vec4("5f1e18"),
                self.hex2vec4("59282c"),
            ]
        }


    def hex2vec4(self, s):
        if len(s) == 6:
            r = s[0] + s[1]
            g = s[2] + s[3]
            b = s[4] + s[5]

            return Vec4(
                int(r, 16)/255.0,
                int(g, 16)/255.0,
                int(b, 16)/255.0,
                1)
        else:
            print "wrong color hex color format"
            return False

    def makeColorLerpSequence(self, path, color1, color2, time):
        interval = LerpColorInterval(path, time, color1, color2)
        return Sequence(interval)
