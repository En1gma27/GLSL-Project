float polarStar( in vec2 p )
{
    const float pi=3.1415926535;
    const float pi5 = 0.628318530718; // pi/5
    const float ph2 = 3.2360679775; // 2 * phi
    
    float m2 = mod(atan(p.y, p.x)/pi5 + 1.0, 2.0);
    
    return ph2 * length(p) * cos(pi5 * (m2 - 4.0 * step(1.0, m2) + 1.0)) - 1.0;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // coords
    float px = 2.0/iResolution.y;
	vec2 q = (2.0 * fragCoord - iResolution.xy)/iResolution.y;

    // rotate
    float t = 0.2 * iTime;
    q = mat2(cos(t), -sin(t),sin(t) ,cos(t)) * q;

	// star shape    
	float d = polarStar( q );       

    // colorize
    vec3 col = mix(vec3(1.000,0.833,0.224), vec3(1.0,0.0,0.0), smoothstep(-2.0 * px, 2.0 * px, d));
	col *= smoothstep(0.02, 0.02 + 2.0 * px, abs(d));
    
	fragColor = vec4( col, 1.0 );
}
