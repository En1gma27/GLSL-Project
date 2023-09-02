

from manim import *

class KochCurve(Scene):
    def construct(self):
        def KochCurve(
            n, length=12, stroke_width=8, color=("#ed1303", "#03ed36", "#033aed")
        ):
            #Tính chiều dài cạnh cắt nhỏ trong đường cong Koch. Chiều dài ban đầu length sẽ được chia cho 3^n.
            l = length / (3 ** n)
            # Tạo một đoạn thẳng  với chiều dài l. Đoạn thẳng này sẽ được sử dụng để tạo ra đường cong Koch và nhóm lại với nhau bằng  LineGroup.
            LineGroup = Line().set_length(l)
            
            def NextLevel(LineGroup):
                return VGroup(
                    *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]#copy lại LineGroup và xoay LineGroup theo các góc: 0 độ, PI/3 (60 độ), -PI/3 (-60 độ)
                                                                                 # để tạo ra cạnh mới tạo thành đường cong Koch
                ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

            for _ in range(n):
                LineGroup = NextLevel(LineGroup)
            #set các điểm trên đt=color=("#ed1303", "#03ed36", "#033aed")
            KC = (
                VMobject(stroke_width=stroke_width)
                .set_points(LineGroup.get_all_points())
                .set_color(color)
            )
            return KC

        level = Variable(0, Tex("level"), var_type=Integer).set_color("#ffffff")
        txt = (
            VGroup(Text("Đường cong Koch",font="AlegreyaSans", font_size=60), level)
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL)
        )
        kc = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5)

        self.add(txt, kc)
        self.wait()
        #Lặp qua các cấp từ 1 đến 5
        for i in range(1, 6):
            self.play(
                level.tracker.animate.set_value(i),#dùng để để cập nhật giá trị của biến level và đổi đường cong Koch 
                kc.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)# play animation đường cong Koch với cấp level tương ứng. Đường cong mới sẽ có độ dày nét vẽ thay đổi theo công thức 12 - (2 * i).
                ),
            )
            self.wait()
        korch_curver_length = MathTex(
            r"\text{chieu dai duong cung koch:}",
            r"(\frac{4}{3})^n \times l",
           font_size=24
        )
        korch_curver_length.move_to(3.5* UP + 5 * RIGHT)
        self.play(Write(korch_curver_length))
        
        segment = MathTex(
            r"\text{so canh tao thanh: }",
            r"4^n",
           font_size=24
        )
        segment.move_to(3.20* UP + 5 * RIGHT)
        self.play(Write(segment))

        segment_length = MathTex(
            r"\text{chieu dai moi canh: }",
            r"(\frac{1}{3})^n \times l",
             font_size=24
        )
        segment_length.move_to(2.8* UP + 5 * RIGHT)
        self.play(Write(segment_length))

        for i in range(4, -1, -1):
            self.play(
                level.tracker.animate.set_value(i),
                kc.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
                ),
            )
            self.wait()
