from panda3d.core import CardMaker, MovieTexture, NodePath, TextureStage, TransparencyAttrib
from panda3d.core import AmbientLight, Vec3, Vec4, Point3, LineSegs
from direct.interval.LerpInterval import LerpColorInterval, LerpScaleInterval, LerpHprInterval, LerpPosInterval
from direct.interval.IntervalGlobal import Sequence, LerpFunc, Parallel
from helper.colors import Colors
import random
from visual import visual

class Strobo(visual):
    
    def setup(self):
        self.animation_speed = 1.0
        self.animation_fuzz = 10.0

        self.horizontal_stripes = [
            self.loader.loadTexture("stripes_100_50.png"),
            self.loader.loadTexture("stripes_200_100.png"),
            self.loader.loadTexture("stripes_300_150.png"),
        ]

        self.vertical_stripes = [
            self.loader.loadTexture("vstripes_100_50.png"),
            self.loader.loadTexture("vstripes_200_100.png"),
            self.loader.loadTexture("vstripes_300_150.png"),
        ]

        self.odd_stripes = [
            self.loader.loadTexture("vstripes_100_50_45.png"),
            self.loader.loadTexture("vstripes_200_100_45.png"),
            self.loader.loadTexture("vstripes_300_150_45.png"),
        ]

        self.odder_stripes = [
            self.loader.loadTexture("vstripes_100_50_-45.png"),
            self.loader.loadTexture("vstripes_200_100_-45.png"),
            self.loader.loadTexture("vstripes_300_150_-45.png"),
        ]            

        self.card = CardMaker("plane")
        self.card.setFrame(-10,10,-10, 10)

        self.top = self.path.attachNewNode(self.card.generate())
        self.bottom = self.path.attachNewNode(self.card.generate())
        self.left = self.path.attachNewNode(self.card.generate())
        self.right = self.path.attachNewNode(self.card.generate())

        self.cards = [
            self.top,
            self.bottom,
            self.left,
            self.right,
        ]
        self.card_indices = [0, 1, 2, 3]

        self.left.setY(-0.2)
        self.right.setY(-0.1)
        self.top.setY(0.0)
        self.bottom.setY(0.1)

        self.left_to_left_interval = LerpPosInterval(
            self.left, 
            self.animation_speed, 
            Vec3(self.left.getX() - self.animation_fuzz, 0, 0),
            Vec3(self.left.getX(), 0, 0)
        )
        self.left_to_right_interval = LerpPosInterval(
            self.left, 
            self.animation_speed, 
            Vec3(self.left.getX() + self.animation_fuzz, 0, 0),
            Vec3(self.left.getX(), 0, 0)
        )
        self.right_to_right_interval = LerpPosInterval(
            self.right, 
            self.animation_speed, 
            Vec3(self.right.getX() + self.animation_fuzz, 0, 0),
            Vec3(self.right.getX(), 0, 0)
        )
        self.right_to_left_interval = LerpPosInterval(
            self.right, 
            self.animation_speed, 
            Vec3(self.right.getX() - self.animation_fuzz, 0, 0),
            Vec3(self.right.getX(), 0, 0)
        )
        self.top_to_top_interval = LerpPosInterval(
            self.top,
            self.animation_speed,
            Vec3(0, 0, self.top.getZ() + self.animation_fuzz),
            Vec3(0, 0, self.top.getZ())
        )
        self.top_to_bottom_interval = LerpPosInterval(
            self.top,
            self.animation_speed,
            Vec3(0, 0, self.top.getZ() - self.animation_fuzz),
            Vec3(0, 0, self.top.getZ())
        )
        self.bottom_to_bottom_interval = LerpPosInterval(
            self.bottom,
            self.animation_speed,
            Vec3(0, 0, self.bottom.getZ() - self.animation_fuzz),
            Vec3(0, 0, self.bottom.getZ())
        )
        self.bottom_to_top_interval = LerpPosInterval(
            self.bottom,
            self.animation_speed,
            Vec3(0, 0, self.bottom.getZ() + self.animation_fuzz),
            Vec3(0, 0, self.bottom.getZ())
        )
        self.left_to_center_interval = LerpPosInterval(
            self.left,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(self.left.getX() - self.animation_fuzz, 0, 0)
        )
        self.right_to_center_interval = LerpPosInterval(
            self.right,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(self.right.getX() + self.animation_fuzz, 0, 0)
        )
        self.top_to_center_interval = LerpPosInterval(
            self.top,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(0, 0, self.top.getZ() + self.animation_fuzz)
        )
        self.bottom_to_center_interval = LerpPosInterval(
            self.bottom,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(0, 0, self.bottom.getZ() - self.animation_fuzz)
        )
        
        self.center_intervals = [
            self.left_to_center_interval,
            self.right_to_center_interval,
            self.top_to_center_interval,
            self.bottom_to_center_interval,
        ]

        self.midi_note_on_functions[108] = self.left_to_left
        self.midi_note_off_functions[108] = self.left_to_center
        self.midi_note_on_functions[110] = self.right_to_right
        self.midi_note_off_functions[110] = self.right_to_center
        self.midi_note_on_functions[112] = self.top_to_top
        self.midi_note_off_functions[112] = self.top_to_center
        self.midi_note_on_functions[113] = self.bottom_to_bottom
        self.midi_note_off_functions[113] = self.bottom_to_center

        self.midi_note_on_functions[96] = self.left_to_center
        self.midi_note_off_functions[96] = self.left_to_left
        self.midi_note_on_functions[98] = self.right_to_center
        self.midi_note_off_functions[98] = self.right_to_right
        self.midi_note_on_functions[100] = self.top_to_center
        self.midi_note_off_functions[100] = self.top_to_top
        self.midi_note_on_functions[101] = self.bottom_to_center
        self.midi_note_off_functions[101] = self.bottom_to_bottom

        self.midi_control_functions[71] = self.update_animation_speed
        self.midi_control_functions[74] = self.update_animation_fuzz

        # sound functions here
        self.func = {}
       
    def left_to_left(self):
        print "left_to_left: "+str(self.animation_fuzz)
        self.left_to_left_interval.start()

    def left_to_right(self):
        print "left_to_right: "+str(self.animation_fuzz)
        self.left_to_right_interval.start()
        
    def right_to_left(self):
        print "right_to_left: "+str(self.animation_fuzz)
        self.right_to_left_interval.start()

    def right_to_right(self):
        print "right_to_right: "+str(self.animation_fuzz)
        self.right_to_right_interval.start()

    def top_to_top(self):
        print "top_to_top: "+str(self.animation_fuzz)
        self.top_to_top_interval.start()

    def top_to_bottom(self):
        print "top_to_bottom: "+str(self.animation_fuzz)
        self.top_to_bottom_interval.start()
        
    def bottom_to_bottom(self):
        print "bottom_to_bottom: "+str(self.animation_fuzz)
        self.bottom_to_bottom_interval.start()

    def bottom_to_top(self):
        print "bottom_to_top: "+str(self.animation_fuzz)
        self.bottom_to_top_interval.start()

    def left_to_center(self):
        print "left_to_center: "+str(self.animation_fuzz)
        self.left_to_center_interval.start()

    def right_to_center(self):
        print "right_to_center: "+str(self.animation_fuzz)
        self.right_to_center_interval.start()
        
    def top_to_center(self):
        print "top_to_center: "+str(self.animation_fuzz)
        self.top_to_center_interval.start()

    def bottom_to_center(self):
        print "bottom_to_center: "+str(self.animation_fuzz)
        self.bottom_to_center_interval.start()

    def update_animation_speed(self):
        self.animation_speed = (self.midi_value/127.0)*4
        self.update_animations()

    def update_animation_fuzz(self):
        self.animation_fuzz = (self.midi_value/12.7)*2
        self.update_animations()

    def performBeat(self):
        map(lambda x: x(), self.func.values())

    def effect1up(self):
        self.left.setTexture(self.odd_stripes[random.randint(0,2)], 1)
        self.right.setTexture(self.odd_stripes[random.randint(0,2)], 1)
        self.top.setTexture(self.odder_stripes[random.randint(0,2)], 1)
        self.bottom.setTexture(self.odder_stripes[random.randint(0,2)], 1)

    def effect2up(self):
        self.left.setTexture(self.horizontal_stripes[random.randint(0,2)], 1)
        self.right.setTexture(self.horizontal_stripes[random.randint(0,2)], 1)
        self.top.setTexture(self.vertical_stripes[random.randint(0,2)], 1)
        self.bottom.setTexture(self.vertical_stripes[random.randint(0,2)], 1)

    def effect3up(self):
        self.left.setTexture(self.vertical_stripes[random.randint(0,2)], 1)
        self.right.setTexture(self.vertical_stripes[random.randint(0,2)], 1)
        self.top.setTexture(self.horizontal_stripes[random.randint(0,2)], 1)
        self.bottom.setTexture(self.horizontal_stripes[random.randint(0,2)], 1)

    def effect4up(self):
        self.top.setTexture(self.odd_stripes[random.randint(0,2)], 1)
        self.bottom.setTexture(self.odder_stripes[random.randint(0,2)], 1)
        self.left.setTexture(self.horizontal_stripes[random.randint(0,2)], 1)
        self.right.setTexture(self.horizontal_stripes[random.randint(0,2)], 1)

    def effect5up(self):
        if 'beat_strobo' in self.func:
            self.func.pop('beat_strobo')
            self.left.setAlphaScale(1.0)
            self.right.setAlphaScale(1.0)
            self.top.setAlphaScale(1.0)
            self.bottom.setAlphaScale(1.0)
        else:
            self.func['beat_strobo'] = self.beat_strobo

    def effect6up(self):
        if 'beat_to_center' in self.func:
            self.func.pop('beat_to_center')
        else:
            self.func['beat_to_center'] = self.beat_start_center_animation

    def effect7up(self):
        if 'random_colors' in self.func:
            self.func.pop('random_colors')
        else:
            self.func['random_colors'] = self.random_colors


    def effect0up(self):
        self.left.clearTexture()
        self.right.clearTexture()
        self.top.clearTexture()
        self.bottom.clearTexture()
        self.left.setColor(1,1,1,1)
        self.right.setColor(1,1,1,1)
        self.right.setColor(1,1,1,1)
        self.right.setColor(1,1,1,1)

    def beat_strobo(self):
        if self.sndY > self.snd.yThreshold:
            for card in self.cards:
                card.setAlphaScale(0.0)
            x = random.sample(self.cards, random.randint(1,3))
            for card in x:
                card.setAlphaScale(1.0)

    def beat_start_center_animation(self):
        if self.sndX > self.snd.xThreshold:
            x = random.sample(self.center_intervals, 1)
            x[0].start()

    def random_colors(self):
        if self.sndX > self.snd.xThreshold:
            x = random.sample(self.cards, 1)
            x[0].setColor(self.generate_random_color())
        
    def update_animations(self):
        self.left_to_left_interval = LerpPosInterval(
            self.left, 
            self.animation_speed, 
            Vec3(self.left.getX() - self.animation_fuzz, 0, 0),
            Vec3(self.left.getX(), 0, 0)
        )
        self.left_to_right_interval = LerpPosInterval(
            self.left, 
            self.animation_speed, 
            Vec3(self.left.getX() + self.animation_fuzz, 0, 0),
            Vec3(self.left.getX(), 0, 0)
        )
        self.right_to_right_interval = LerpPosInterval(
            self.right, 
            self.animation_speed, 
            Vec3(self.right.getX() + self.animation_fuzz, 0, 0),
            Vec3(self.right.getX(), 0, 0)
        )
        self.right_to_left_interval = LerpPosInterval(
            self.right, 
            self.animation_speed, 
            Vec3(self.right.getX() - self.animation_fuzz, 0, 0),
            Vec3(self.right.getX(), 0, 0)
        )
        self.top_to_top_interval = LerpPosInterval(
            self.top,
            self.animation_speed,
            Vec3(0, 0, self.top.getZ() + self.animation_fuzz),
            Vec3(0, 0, self.top.getZ())
        )
        self.top_to_bottom_interval = LerpPosInterval(
            self.top,
            self.animation_speed,
            Vec3(0, 0, self.top.getZ() - self.animation_fuzz),
            Vec3(0, 0, self.top.getZ())
        )
        self.bottom_to_bottom_interval = LerpPosInterval(
            self.bottom,
            self.animation_speed,
            Vec3(0, 0, self.bottom.getZ() - self.animation_fuzz),
            Vec3(0, 0, self.bottom.getZ())
        )
        self.bottom_to_top_interval = LerpPosInterval(
            self.bottom,
            self.animation_speed,
            Vec3(0, 0, self.bottom.getZ() + self.animation_fuzz),
            Vec3(0, 0, self.bottom.getZ())
        )
        self.left_to_center_interval = LerpPosInterval(
            self.left,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(self.left.getX() - self.animation_fuzz, 0, 0)
        )
        self.right_to_center_interval = LerpPosInterval(
            self.right,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(self.right.getX() + self.animation_fuzz, 0, 0)
        )
        self.top_to_center_interval = LerpPosInterval(
            self.top,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(0, 0, self.top.getZ() + self.animation_fuzz)
        )
        self.bottom_to_center_interval = LerpPosInterval(
            self.bottom,
            self.animation_speed,
            Vec3(0,0,0),
            Vec3(0, 0, self.bottom.getZ() - self.animation_fuzz)
        )

    def generate_random_color(self):
        x = self.path.getColorScale()
        r, g, b, a = x
        r = (r + random.randint(0,255)/255.0) / 2.0
        g = (g + random.randint(0,255)/255.0) / 2.0
        b = (b + random.randint(0,255)/255.0) / 2.0
        return Vec4(r,g,b, 1.0)

