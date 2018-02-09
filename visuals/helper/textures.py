from panda3d.core import Texture, Vec4

class Textures:
    def __init__(self, loader):
        self.textures = {
            'shapes': {
                'circle': loader.loadTexture("circle.png"),
                'triangle': loader.loadTexture("triangle0.png"),
                'negative triangle': loader.loadTexture("triangle1.png"),
                'halfcircle': loader.loadTexture("halfcircle.png"),
                'halfsquaretriangle': loader.loadTexture("halfsquaretriangle.png"),
                'circlesquare': loader.loadTexture("circlesquare.png"),
            },
            'emoticons': {
                '0': loader.loadTexture("emoticon1.png"),
                '1': loader.loadTexture("emoticon2.png"),
                '2': loader.loadTexture("emoticon3.png"),
                '3': loader.loadTexture("emoticon4.png"),
                '4': loader.loadTexture("emoticon5.png"),
                '5': loader.loadTexture("emoticon6.png"),
                '6': loader.loadTexture("emoticon7.png"),
                '7': loader.loadTexture("emoticon8.png"),
                '8': loader.loadTexture("emoticon9.png"),
                '9': loader.loadTexture("emoticon10.png"),
                '10': loader.loadTexture("emoticon11.png"),
                '11': loader.loadTexture("emoticon12.png"),
                '12': loader.loadTexture("emoticon13.png"),
            },
            'stripes': loader.loadTexture("stripes.png"),
            'grid': loader.loadTexture("grid2.png"),
            'circle1px': loader.loadTexture("circle1px.png"),
            'circle2px': loader.loadTexture("circle2px.png"), 
            'circle5px': loader.loadTexture("circle5px.png"), 
            'quad1px': loader.loadTexture("quad1px.png"), 
            'quad2px': loader.loadTexture("quad2px.png"), 
            'quad5px': loader.loadTexture("quad5px.png"), 
            'white': loader.loadTexture("white.png"),
            'technics': {
                'amplifier': loader.loadTexture("1210amplifier.png"),
                'drivecoil': loader.loadTexture("1210drivecoil.png"),
                'drivecontrol': loader.loadTexture("1210drivecontrol_pcb.png"),
                'output': loader.loadTexture("1210output_pcb.png"),
                'parts1': loader.loadTexture("1210parts1.png"),
                'parts2': loader.loadTexture("1210parts2.png"),
                'pickup': loader.loadTexture("1210pickup.png"),
                'pitchled': loader.loadTexture("1210pitchled.png"),
                'scheme': loader.loadTexture("1210scheme.png"),
                'setup': loader.loadTexture("1210setup.png"),
                'strobeilluminator': loader.loadTexture("1210strobeilluminator_pcb.png"),
                'stylus': loader.loadTexture("1210stylus.png"),
                'top': loader.loadTexture("1210top.png"),
                'tonearmbalance': loader.loadTexture("1210tonearmbalance.png"),
            },
            'spherical': {
                'planets': {
                    'planet1': loader.loadTexture("planet1.jpg"),
                    'planet2': loader.loadTexture("planet2.jpg"),
                    'planet3': loader.loadTexture("planet3.jpg"),
                    'planet4': loader.loadTexture("planet4.jpg"),
                },
                'checkersphere': loader.loadTexture("checkersphere.png"),
            },
            'ring': loader.loadTexture("ring.png"),
            'pinkpixels': {
                '0': loader.loadTexture("pinkpixels1.png"),
                '1': loader.loadTexture("pinkpixels2.png"),
                '2': loader.loadTexture("pinkpixels3.png"),
                '3': loader.loadTexture("pinkpixels4.png"),
                '4': loader.loadTexture("pinkpixels5.png"),
                '5': loader.loadTexture("pinkpixels6.png"),
                '6': loader.loadTexture("pinkpixels7.png"),
                '7': loader.loadTexture("pinkpixels8.png"),
                '8': loader.loadTexture("pinkpixels9.png"),
                '9': loader.loadTexture("pinkpixels10.png"),
                '10': loader.loadTexture("pinkpixels11.png"),
                '11': loader.loadTexture("pinkpixels12.png"),
                '12': loader.loadTexture("pinkpixels13.png"),
                '13': loader.loadTexture("pinkpixels14.png"),
                '14': loader.loadTexture("pinkpixels15.png"),
                '15': loader.loadTexture("pinkpixels16.png"),
            },
            'spaceschematics': {
                '0': loader.loadTexture("sts1.png"),
                '1': loader.loadTexture("sts2.png"),
            },
            'vrc': {
                '0': loader.loadTexture("code1.png"),
                '1': loader.loadTexture("code2.png"),
                '2': loader.loadTexture("code3.png"),
                '3': loader.loadTexture("code4.png"),
                '4': loader.loadTexture("code5.png"),
                '5': loader.loadTexture("code6.png"),
                '6': loader.loadTexture("code7.png"),
                '7': loader.loadTexture("code8.png"),
                '8': loader.loadTexture("code9.png"),
                '9': loader.loadTexture("code10.png"),
            },
            'life': {
                '1': loader.loadTexture('davinci_human.png'),
                '2': loader.loadTexture('embryo_0.png'),
                '3': loader.loadTexture('embryo_2.png'),
                '4': loader.loadTexture('lsd.png'),
                '5': loader.loadTexture('amoeba_proteus.png'),
            },
        }
        self.textures['vrc']['0'].setWrapU(Texture.WMBorderColor)
        self.textures['vrc']['0'].setWrapV(Texture.WMBorderColor)
        self.textures['vrc']['0'].setBorderColor(Vec4(0,0,0,0))
        
        for x in self.textures['vrc'].values():
            x.setWrapU(Texture.WMBorderColor)
            x.setWrapV(Texture.WMBorderColor)
            x.setBorderColor(Vec4(0,0,0,0))

