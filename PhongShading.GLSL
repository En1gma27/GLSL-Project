precision lowp float;
// varying là loại biến dùng để truyền dữ liệu từ vertex shader
//  tới fragment shader. Biến v_normal sẽ chứa vector pháp tuyến của bề mặt mà fragment shader đang xử lý.
varying vec4 v_normal;

void main() {
//   Ánh Sáng Môi Trường (Ambient Light)
//     Định nghĩa: Ánh sáng môi trường là ánh sáng tỏa ra một cách đồng đều trong không gian, không có nguồn sáng cụ thể. Nó mô phỏng ánh sáng phản chiếu từ các bề mặt xung quanh, giúp làm sáng các khu vực không có ánh sáng trực tiếp.
//     Tính chất:
//     Không có hướng: Ánh sáng môi trường không tạo ra bóng đổ hay hiệu ứng ánh sáng đặc biệt.
//     Màu sắc đều: Màu sắc của ánh sáng môi trường thường là một màu duy nhất và ảnh hưởng đến tất cả các bề mặt.
  vec3 ambient = vec3(0.502, 0.502, 0.502); // color - grey

// Ánh Sáng Khuếch Tán (Diffuse Light)
    // Định nghĩa: Ánh sáng khuếch tán là ánh sáng từ nguồn cụ thể (như mặt trời) chiếu lên bề mặt và phân tán đều.
    // Tính chất: Ánh sáng khuếch tán có hướng, phụ thuộc vào góc giữa vector ánh sáng và vector pháp tuyến của bề mặt.
    // Công thức: idiffuse = kd * Ilight * max(0, dot(L, N))
    //  - kd: hệ số khuếch tán
    //  - Ilight: cường độ ánh sáng
    //  - L: vector ánh sáng (từ nguồn sáng tới điểm bề mặt)
    //  - N: vector pháp tuyến tại điểm bề mặt
 vec3 normal = normalize(v_normal.xyz);  // Chuẩn hóa pháp tuyến
    vec3 lightColor = vec3(1.0, 0.0, 0.0);  // Màu của ánh sáng (đỏ)
    vec3 lightSource = vec3(1.0, 1.0, 1.0); // Vị trí nguồn sáng
    float diffuseStrength = max(0.0, dot(lightSource, normal)); // Tính cường độ khuếch tán
    vec3 diffuse = diffuseStrength * lightColor; // Kết quả ánh sáng khuếch tán

  // Ánh Sáng Phản Chiếu (Specular Light)
    // Định nghĩa: Ánh sáng phản chiếu là ánh sáng bị phản xạ từ bề mặt bóng loáng, tạo các điểm sáng (highlight).
    // Tính chất: Phụ thuộc vào góc giữa camera và nguồn sáng. Đặc biệt rõ trên các bề mặt bóng.
    // Công thức: Ispecular = ks * Ilight * max(0, dot(R, V))^alpha
    //  - ks: hệ số phản chiếu
    //  - Ilight: cường độ ánh sáng
    //  - R: vector phản xạ (phản chiếu của L qua N)
    //  - V: vector từ bề mặt tới camera
    //  - alpha: độ bóng của bề mặt (mũ số lớn làm điểm sáng tập trung hơn)
 vec3 cameraSource = vec3(0.0, 0.0, 1.0); // Vị trí camera
    vec3 viewSource = normalize(cameraSource); // Chuẩn hóa vector từ bề mặt đến camera
    vec3 reflectSource = normalize(reflect(-lightSource, normal)); // Tính toán vector phản chiếu
    float specularStrength = max(0.0, dot(viewSource, reflectSource)); // Cường độ ánh sáng phản chiếu
    specularStrength = pow(specularStrength, 256.0); // Làm nổi bật điểm sáng với mũ 256
    vec3 specular = specularStrength * lightColor; // Kết quả ánh sáng phản chiếu

  // lighting = ambient + diffuse + specular
  vec3 lighting = vec3(0.0, 0.0, 0.0); // color - black
  lighting = ambient * 0.0 + diffuse * 0.5 + specular * 0.5;

  // Màu của model khi được chiếu sáng ánh sáng là color = modelColor * lighting
  vec3 modelColor = vec3(1.0, 1.0, 1.0);
  vec3 color = modelColor * lighting;

  gl_FragColor = vec4(color, 1.0);
}
