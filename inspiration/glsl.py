from pandac.PandaModules import PythonCallbackObject
from pandac.PandaModules import CallbackNode, VBase3
from direct.directbase import DirectStart

from OpenGL.GL import *
import sys

VSHADER = """
void main() {
  gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
"""
FSHADER = """
uniform sampler2D tex;
void main() {
  gl_FragColor.rgb = 1.0 - texture2D(tex,gl_TexCoord[0].st).rgb;
}
"""

def init(cbdata):
  """We'll be compiling & assigning the shader here.
  This method will only be called once."""
  v = glCreateShader(GL_VERTEX_SHADER)
  f = glCreateShader(GL_FRAGMENT_SHADER)
  glShaderSource(v, VSHADER)
  glShaderSource(f, FSHADER)
  glCompileShader(v)
  glCompileShader(f)
  program = glCreateProgram()
  glAttachShader(program,v)
  glAttachShader(program,f)
  glLinkProgram(program)
  glUseProgram(program)
  glDeleteShader(v)
  glDeleteShader(f)
  # We don't need to set the shader again. Clear the callback.
  cbnode.clearDrawCallback()

# Make sure we're using da OpenGL.
if base.pipe.getInterfaceName() != "OpenGL":
  print "This program requires OpenGL."
  sys.exit(1)

# Set up the callback object
cbnode = CallbackNode("cbnode")
cbnode.setDrawCallback(PythonCallbackObject(init))
cbnp = render.attachNewNode(cbnode)

# Load the panda and reparent it to the callback object.
panda = loader.loadModel("panda")
panda.reparentTo(cbnp)

# Let it rotate to show that transforms work well too.
panda.hprInterval(2.0, VBase3(360, 0, 0)).loop()

# Put the camera where it will be able to actually see something.
base.trackball.node().setPos(0, 30, -7)

run()
