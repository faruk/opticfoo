opticfoo
========

This is a program about VJing in 3d inside a game engine.

About
-----

This is the project repository for my bachelor thesis. Its about a 
VJing concept with heavy use of keyboard for performance. You'll also 
need mouse to use the GUI. Basically it is a virtual 3d room where you 
can place visuals and watch them.


Installation
------------

In order to run this code you will need 

    * panda3d (v1.8) (see manual on http://panda3d.org for installation
      instruction)
    * several python libs like alsaaudio, audioop, fftw3, numpy, ttk

For the models and videos and textures you'll need to setup the model's
path in the 'Config.prc' file.
If you installed panda3d on linux you should find your 'Config.prc'
file in /etc.

Add the following lines to Configure.prc and adapt to your installation
path. The specified directories are the directories where you should
hold all visual material for visuals if you are going to code your own.

    model-path    /path/to/opticfoo/models
    model-path    /path/to/opticfoo/textures


Panda3d has an apt-repository and offers a debian .deb-package for
smooth installation with debian based operating systems (see details
on Panda3d download page
http://www.panda3d.org/download.php?runtime&platform=ubuntu )

Run VRC
-------

execute main.py file with python from command line:

    user@computer:/path/opticfoo$ python main.py

you can also create a shortcut with an executable script that does
this for you.

Usage
-----

In order to perform a VJ show you need to animate your visuals and
camera, adjust transparency, speeds and and.
You should defenetely hold some general movement keys pressed and
switch to escaped mode to see how you can store operations until
the key-up event occurs. This allows you to animate things and let
them be animated.
You can also access the last visual again with the stored keyboard
input and activate toggles for transparency, scale and speed.
The speed value can also be negative which allows you to invert
animation.

Best thing is to load some visuals, make sure mic is activated and
calibrated and try and error.

Keyboard layout for Performing, general keys:

    * "wasd"        - move forward/backward/left/right
    * "shift/space" - move up/down
    * "hl"          - head left/right
    * "jk"          - pitch down/up
    * "ui"          - rotate counter clockwise/clockwise
    * "esc"         - switch to escaped mode
    * "c"           - switch to camera mode
    * "v"           - switch to visual mode

Keyboard layout for special keys, camera mode:

    * "mouse wheel" - camera speed
    * "f"           - synchronize position of cams depeding on 'sync-to'
                      variable in camera operation map
    * "g"           - toggle camera fixation on visual on/off
    * "t"           - toggle 'sync-to' variable to synchronize
                      cam/othercam or vice versa
    * "left mouse + mouse movement" - rotate cam heading/pitch with mouse
                      when not fixed on visual (see "g")

Keyboard layout for special keys, visual mode:

    * "f"           - enable scale value access for mouse wheel on 
                      active visual, disable any other wheel access
    * "g"           - enable speed value access for mouse wheel on
                      active visual, disable any other access
    * "t"           - enable transparency value access for mouse wheel on
                      active visual, disable any other access
    * "1234567890"  - programmable effect keys to call effect1..0 function
                      on active visual
    * "tab"         - switch to next visual in active visual list
    * "r"           - reset visual operation to stop visual movement and
                      sets visual speed to 1

Write Visuals
-------------

If you are a programmer and you want to write some visuals, see the code in
the ./visuals directory for some inspiration of possibilities.
Basically you just put your stuff into the visual class with panda3d-functions
(http://panda3d.org/manual/). see panda3d's common state changes for visual
positioning and stuff 
(http://www.panda3d.org/manual/index.php/Common_State_Changes).

To load your material into a visual you need to call the visuals loader object
and specify the name of the resource to load. Watch out with multiple identical
file names across your model paths.

    class Testvisual(visual): #derive from visual class all needed initialisation
        def setup(self):
            self.something1 = self.loader.loadModel("3dmodelname")
            ...

        def performToBeat(self):
            ...

        def effect1(self): # for effect called by key "1"
            ...

        ...

After you have saved your custom visual class you need to import it in the
visual-factory class and initialize it there. See already added example
visuals in ./visuals/visuals.py .
