from panda3d.core import Shader
from visual import visual

def ShaderTest(visual):


    def setup(self):

        fragmentshader = """
        // vertex to fragment shader io
        varying vec3 n;
        varying vec3 i;
        varying vec4 cs;

        // globals
        //uniform float edgefalloff;
        //uniform float intensity;
        //uniform float ambient;

        // entry point
        void main()
        {
            float opac = dot(normalize(-n), normalize(-i));
            opac = abs(opac);
            opac = 0.0 + 0.2*(1.0-pow(opac, 0.3));
            //opac = 1.0 - opac;
                                
            gl_fragcolor =  opac * cs;
            gl_fragcolor.a = opac;
        }
        """

        vertexshader = """
        // application to vertex shader
        varying vec3 n;
        varying vec3 i;
        varying vec4 cs;

        void main()
        {
            vec4 p = gl_modelviewmatrix * gl_vertex;
            i  = p.xyz - vec3 (0);
            n  = gl_normalmatrix * gl_normal;
            cs = gl_color;
            gl_position = gl_modelviewprojectionmatrix * gl_vertex;
        } 
        """

        self.path.removeNode()
        self.path = self.loader.load("box")

        self.shader = Shader.load(Shader.SL_GLSL, self.vertexShader, self.fragmentShader)
        self.path.setShader(self.shader)


