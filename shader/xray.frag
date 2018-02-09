
// vertex to fragment shader io
varying vec3 N;
varying vec3 I;
varying vec4 Cs;

// globals
uniform float edgefalloff;
uniform float intensity;
uniform float ambient;

// entry point
void main()
{
    float opac = dot(normalize(-N), normalize(-I));
    opac = abs(opac);
    opac = ambient + intensity*(1.0-pow(opac, edgefalloff));
    //opac = 1.0 - opac;
    
    gl_FragColor =  opac * Cs;
    gl_FragColor.a = opac;
}

