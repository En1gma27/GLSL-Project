#define MAX_STEPS 100
#define MAX_DIST 100.0
#define SURF_DIST 0.01


// Hàm tính toán ma trận quay theo trục X
mat3 getRotationMatrixX(float angle) {
    float c = cos(angle);
    float s = sin(angle);
    return mat3(
        1.0, 0.0, 0.0,
        0.0, c,   s,
        0.0, -s,  c
    );
}

// Hàm tính toán ma trận quay theo trục Y
mat3 getRotationMatrixY(float angle) {
    float c = cos(angle);
    float s = sin(angle);
    return mat3(
        c,   0.0, -s,
        0.0, 1.0, 0.0,
        s,   0.0, c
    );
}


//Hàm GetDist tính toán khoảng cách từ điểm p đến các hình ảnh trong không gian 3D:
float GetDist(vec3 p)
{
 vec4 s = vec4(0, 1, 6, 1);
    
    float sphereDist = length(p-s.xyz) - s.w;
    float planeDist = p.y;
    
    float d = min(sphereDist, planeDist);
   
    return d;
}

//Hàm RayMarch thực hiện thuật toán ray marching:
//Hàm này sử dụng vòng lặp để di chuyển ray (ro) từ điểm bắt đầu đến điểm giao điểm với các hình ảnh. 
//Nếu khoảng cách tới điểm giao điểm (dO) vượt quá giới hạn hoặc khoảng cách đến bề mặt tiếp xúc nhỏ hơn giới hạn (SURF_DIST),
// quá trình ray marching kết thúc.
float RayMarch(vec3 ro, vec3 rd)
{
 float dO = 0.0;
    
    for(int i=0; i<MAX_STEPS; i++)
    {
     vec3 p = ro + rd*dO;
        float dS = GetDist(p);
        dO += dS;
        
        if(dO>MAX_DIST || dS < SURF_DIST) break;
    }
    
    return dO;
}
//Hàm GetNormal tính toán vectơ pháp tuyến tại điểm p:
vec3 GetNormal(vec3 p)
{
 float d = GetDist(p);
    vec2 e = vec2(0.01, 0);
    
    vec3 n = d - vec3(
     GetDist(p-e.xyy),
        GetDist(p-e.yxy),
        GetDist(p-e.yyx));
    
    return normalize(n);
}


float GetLight(vec3 p)
{
 vec3 lightPos = vec3(0, 5, 6);
    
    //move the light
    float moveSpeed = 2.0;
    lightPos.xz += vec2(sin(iTime), cos(iTime)) * moveSpeed;
    vec3 l = normalize(lightPos-p);
    vec3 n = GetNormal(p);
    
    float dif = clamp(dot(n, l), 0.0, 1.0);
    
    //producing shadow
    float d = RayMarch(p+n*SURF_DIST *2.0 , l);
    if (d < length(lightPos - p)) {
    // Nếu trong bóng, gán màu đỏ nhạt cho quả bóng
    return vec3(1.0, 0.0, 0.0); // Màu đỏ (1.0, 0.0, 0.0)
    }
}



void mainImage(out vec4 fragColor, in vec2 fragCoord)
{
    vec2 uv = (fragCoord - 0.5 * iResolution.xy) / iResolution.y;

    vec3 col = vec3(0.0);

    vec3 ro = vec3(0.2745, 0.0902, 0.0902);

    // Tính toán góc quay dựa trên tọa độ chuột (iMouse)
    float rotationX = (iMouse.y - iResolution.y * 0.5) * 0.1;
    float rotationY = (iMouse.x - iResolution.x * 0.5) * 0.1;
    
    // Lấy ma trận quay
    mat3 rotx = getRotationMatrixX(radians(rotationX));
    mat3 roty = getRotationMatrixY(radians(rotationY));

    // Tính toán hướng ray sau khi quay
    vec3 rd = normalize(roty * rotx * vec3(uv.x, uv.y, 1.0));

    float d = RayMarch(ro, rd);

    vec3 p = ro + rd * d;

    float dif = GetLight(p);
    col = vec3(dif);

    // Output to screen
    fragColor = vec4(col, 1.0);
}