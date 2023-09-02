from manim import *
# Tạo hàm để hiển thị text trong frame box hình chữ nhật để play animation giới thiệu các đặc tính của dictinonary
def create_text_with_rectangle(self, text):
    # Hiển thị text
    text.scale(0.5)
    text_height = text.height
    text_width = text.width
    # Hiển thị hình chữ nhật chứa text
    rec = Rectangle(
        height=text_height + 0.5,
        width=text_width + 0.5,
        color=RED_A,
        stroke_width=6,
        stroke_color=ORANGE
    )
    self.play(Write(text),Write(rec))
    self.wait(2)
    # Xóa text và hình chữ nhật
    self.play(Unwrite(text, reverse=False), Uncreate(rec, reverse=True, remover=True))
    self.wait(2)
    #hàm tạo animation hcn chứ thông tin chú thích
def create_rectangle_infor(self, text):
        text.scale(0.5)
        text_height = text.height
        text_width = text.width
        rec = Rectangle(
            height=text_height + 1,
            width=text_width + 1,
            fill_color=BLACK,
            fill_opacity=1.0,
            color=RED_A,
            stroke_width=6,
            stroke_color= YELLOW,
        )
        self.play( Write(rec))
        self.wait(2)
        self.play(Write(text),run_time=3)
        self.wait(4)
        self.play(FadeOut(rec),FadeOut(text))

class Dictinonary_Introduction(Scene):
    def construct(self):
        #phần intro
        text = Text("Giới thiệu về kiểu dữ liệu dictinonary trong python",font="AlegreyaSans",font_size=24)
        self.play(Write(text))
        self.play(FadeOut(text))
        self.wait(1)
        dict_one = Text("dictinonary trong python",font="AlegreyaSans",font_size=24)
        dict_one.move_to(3.5 * UP + ORIGIN)
        self.play(Write(dict_one))
        self.wait(1)
        text0= Text("Tạo dictinonary trong python",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self,text0)
        self.wait(1)      

        # tạo hình chũ nhật phía trên
        def create_rectangle1(x, y, z):
            EXPLAIN_WIDTH = x
            EXPLAIN_HEIGHT = y
            explain_filled_rect = Rectangle(
                width=EXPLAIN_WIDTH,
                height=EXPLAIN_HEIGHT,
                stroke_width=1,
                fill_color=DARK_GRAY
            )
            explain_filled_rect.shift(z)
            explain_filled_rect.set_fill(DARK_GRAY, 0.5)
            self.play(GrowFromCenter(explain_filled_rect, run_time=1))

            explain_line_left, explain_line_bottom = [
                Line(
                    explain_filled_rect.get_corner(start),
                    explain_filled_rect.get_corner(end),
                    color=RED_A
                )
                for start, end in [(DL, UL), (DL, DR)]
            ]

            self.play(
                GrowFromEdge(explain_line_left, DOWN),
                GrowFromEdge(explain_line_bottom, LEFT)
            )

        create_rectangle1(14, 1.25, 2.25* UP + ORIGIN)
        dict_code = MarkupText(
            "<span color=\"white\">First_dict</span> = {'<span color=\"green\">brand</span>': '<span color=\"green\">ford</span>', "
            "'<span color=\"red\">year</span>': <span color=\"white\">2131</span>, '<span color=\"green\">model</span>': '<span color=\"green\">xmustang</span>'}"
        )
        dict_code.scale(0.5)
        dict_code.move_to(2 * UP + ORIGIN)
        self.play(Write(dict_code))

        #tao frame variable/object
        First_dict_surrounding=SurroundingRectangle(dict_code[0:9], color=YELLOW, buff=0.1)
        self.play(Create(First_dict_surrounding))
        variable_object_text = Text("Biến/đối tượng",font="AlegreyaSans",font_size=24)
        variable_object_text.move_to(First_dict_surrounding,4*DOWN,1.5*RIGHT)
        variable_object_surrounding = SurroundingRectangle(variable_object_text, color=YELLOW, buff=0.1)
        self.play(Write(variable_object_text))
        self.play(Create(variable_object_surrounding))

        #frame box key
        brand_surrounding = SurroundingRectangle(dict_code[13:18], color=YELLOW, buff=0.1)#đóng khung chữ brand trong biến dict_code với vị trí 13->18 
        self.play(Create(brand_surrounding))#play animation đóng khung chữ brand
        key_text = Text("khóa",font="AlegreyaSans",font_size=24)# khoi tao biến keytext
        key_text.move_to(brand_surrounding, 4 * DOWN, 0.75*RIGHT)#key text di chuyển xuống dưới brand_surrounding
        key_surrounding = SurroundingRectangle(key_text, color=YELLOW, buff=0.1)#tạo biến đóng khung key text
        self.play(Write(key_text))
        self.play(Create(key_surrounding))

        #frame box value
        ford_surrounding = SurroundingRectangle(dict_code[21:25], color=YELLOW, buff=0.1)
        self.play(Create(ford_surrounding))
        value_text = Text("giá trị",font="AlegreyaSans",font_size=24)
        value_text.move_to(ford_surrounding, 4 * DOWN,0.25*LEFT)
        value_surrounding = SurroundingRectangle(value_text, color=YELLOW, buff=0.1)
        self.play(Write(value_text))
        self.play(Create(value_surrounding))

        # noi mui ten frame box key va value
        arrow0 = Arrow( First_dict_surrounding.get_bottom(),variable_object_surrounding .get_top(), color=YELLOW)
        arrow1 = Arrow(brand_surrounding.get_bottom(), key_surrounding.get_top(), color=YELLOW)
        arrow2 = Arrow(ford_surrounding.get_bottom(), value_surrounding.get_top(), color=YELLOW)
        self.play(Create(arrow0),Create(arrow1),Create(arrow2))

        #framebox key_value_pair
        key_value_pair_surrounding=SurroundingRectangle(dict_code[13:25],color=YELLOW,buff=0.1)
        self.play(Create(key_value_pair_surrounding))
        key_value_pair_text = Text("cặp khóa-giá trị",font="AlegreyaSans",font_size=24)
        key_value_pair_text.move_to( key_value_pair_surrounding, 4*DOWN,3*LEFT)
        value_pair_surrounding = SurroundingRectangle(key_value_pair_text , color=YELLOW, buff=0.1)
        self.play(Write(key_value_pair_text))
        self.play(Create(value_pair_surrounding))
        arrow3 = Arrow(key_value_pair_surrounding.get_bottom(), value_pair_surrounding.get_top(), color=YELLOW)
        self.play(Create(arrow3))
        year_surrounding = SurroundingRectangle(dict_code[28:37], color=YELLOW, buff=0.1)
        model_surrounding = SurroundingRectangle(dict_code[40:56], color=YELLOW, buff=0.1)
        self.play(Create(year_surrounding))
        self.play(Create(model_surrounding))
        arrow4 = Arrow(year_surrounding.get_bottom(), key_value_pair_text.get_top(), color=YELLOW)
        arrow5 = Arrow(model_surrounding .get_bottom(), key_value_pair_text.get_top(), color=YELLOW)
        self.play(Create(arrow4),Create(arrow5))
        self.wait(2)
        #xoa cac doi tuong tren
        self.play(FadeOut(dict_code,key_text,value_text,key_value_pair_text,key_value_pair_surrounding,brand_surrounding,ford_surrounding,year_surrounding,model_surrounding,variable_object_surrounding,
                          key_surrounding,variable_object_surrounding,value_pair_surrounding,variable_object_text,First_dict_surrounding,value_surrounding,
                          arrow1,arrow0,arrow2,arrow3,arrow4,arrow5))
        # phan animation tao dicttinonary iterable
        text1 = Text("Tạo dictionary bằng cách sử dụng iterable", color="#FFFF00", font="AlegreyaSans", font_size=24)
        create_text_with_rectangle(self, text1)
        second_dict=MarkupText('<span fgcolor="white">second_dict</span> =''<span fgcolor="yellow">dict</span>('
            '<span fgcolor="white">[</span>'
            '<span fgcolor="white">(</span>'
            '<span fgcolor="green">\'gpu name\', </span>'
            '<span fgcolor="green">\'Nvidia GTX 1650\'</span>'
            '<span fgcolor="white">), </span>'
            '<span fgcolor="white">(</span>'
            '<span fgcolor="green">\'model\', </span>'
            '<span fgcolor="green">\'GTX\'</span>'
            '<span fgcolor="white">), </span>'
            '<span fgcolor="white">(</span>'
            '<span fgcolor="green">\'Price\', </span>'
            '<span fgcolor="green">\'170$\'</span>'
            '<span fgcolor="white">)</span>'
            '<span fgcolor="white">]</span>'
            ')',
            font_size=24
        )
            
        second_dict.move_to(2 * UP + ORIGIN)
        self.play(Write(second_dict))
        self.wait(2)
        self.play(FadeOut(second_dict))
         # phan animation Tạo dictionary từ đối số chính
        text2 = Text("Tạo dictionary từ đối số chính",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text2)
        third_dict = MarkupText('<span color="white">third_dict</span> = <span color="blue">dict</span>('
                                '<span color="green">name</span>=<span color="white">\'Huy\'</span>, '
                                '<span color="green">age</span>=<span color="white">\'21\'</span>, '
                                '<span color="green">IQ</span>=<span color="white">\'300\'</span>)',font_size=24)
        third_dict.move_to(2 * UP + ORIGIN)
        self.play(Write(third_dict))
        self.wait(2)
        self.play(FadeOut(third_dict))
        #phan animation Tạo directory bằng hàm zip
        text3=Text("Tạo directory bằng hàm zip ",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text3)
        self.wait(2)
        fourth_dict = MarkupText('<span color="white">fourth_dict</span> = <span color="yellow">dict</span>(<span color="red">zip</span>([<span color="red">2</span>,<span color="red">3</span>,<span color="red">4</span>], [<span color="green">\'fry\'</span>,<span color="green">\'ant\'</span>,<span color="green">\'snake\'</span>]))',font_size=24)
        fourth_dict.move_to(2 * UP + ORIGIN)
        self.play(Write(fourth_dict))
        self.wait(2)
        self.play(FadeOut(fourth_dict))
        #hàm tạo hcn2 phía dưới hcn 1
        def create_rectangle2(x, y, z):
            EXPLAIN_WIDTH = x
            EXPLAIN_HEIGHT = y
            explain_filled_rect = Rectangle(
                                        width=EXPLAIN_WIDTH,
                                        height=EXPLAIN_HEIGHT,
                                        stroke_width=1,
                                        fill_color=DARK_GRAY
                                    )
            explain_filled_rect.to_edge(z,buff=0)
            explain_filled_rect.set_fill(DARK_GRAY,0.5)
            explain_line_left, explain_line_bottom = [
                Line(
                        explain_filled_rect.get_corner(start),
                        explain_filled_rect.get_corner(end),
                        color=RED_A
                    )
                for start,end in [(DL,UL),(DL,DR)] 
            ]

            self.play(FadeIn(explain_filled_rect))
            self.play(
                    GrowFromEdge(explain_line_left, DOWN),
                    GrowFromEdge(explain_line_bottom, LEFT)
            ) 
        create_rectangle2(14, 3, 0.5*ORIGIN + ORIGIN)#goi ham tao hcn ben duoi rectange1
        #phan animation Sự quan trọng của khóa
        text4=Text("Sự quan trọng của khóa",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text4)
        unique_dict = MarkupText('<span color="white">unique_dict</span> = <span color="green">{</span>'
                                      '<span color="green">\'A\'</span>:<span color="green">\'Apple\'</span>, '
                                      '<span color="green">\'C\'</span>:<span color="green">\'Code\'</span>, '
                                      '<span color="green">\'C\'</span>:<span color="green">\'Cat\'</span>'
                                      '<span color="green">}</span>',font_size=24)
        unique_dict.move_to(2 * UP + ORIGIN) 
        self.play(Write( unique_dict))  
        c_surrounding = SurroundingRectangle(unique_dict[26:27], color=YELLOW, buff=0.1)
        code_surrounding = SurroundingRectangle(unique_dict[30:35], color=YELLOW, buff=0.1)
        self.wait(2)
        self.play(Create(c_surrounding), Create(code_surrounding))
        #animation ghi đè bằng bởi giá trị
        text5=Text("Giá trị code của key C đã được ghi đè bằng bởi giá trị cat",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text5)
        text6=MarkupText('<span color="yellow">print</span> (unique_dict) <span color="white"></span>',font_size=14)
        text7=Text("output={'A': 'Apple', 'C': 'Cat'}",font_size=14)
        text6.move_to(1.25 * UP +5 * LEFT)  # Di chuyển đến bên góc trái dưới
        text7.move_to(1 * UP+ 4.5 * LEFT)  # Di chuyển đến bên dưới text6
        # Hiển thị text6, sau đó text7
        self.play(Write(text6))
        self.wait(1)  # Chờ một chút sau khi hiển thị text6
        self.play(Write(text7))
        self.wait(3)  # Chờ một lúc trước khi tiếp tục
        self.play(FadeOut(unique_dict),FadeOut(c_surrounding),FadeOut(code_surrounding))
        #animation Dictinonary có thể có 2 khóa có cùng giá trị
        text8=Text("Khóa trong Dictinonary được có cùng giá trị",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text8)
        unique_dict1 = MarkupText('<span color="white">unique_dict</span> = <span color="green">{</span>'
                                      '<span color="green">\'A\'</span>:<span color="green">\'Apple\'</span>, '
                                      '<span color="green">\'C\'</span>:<span color="green">\'Code\'</span>, '
                                      '<span color="green">\'D\'</span>:<span color="green">\'Code\'</span>'
                                      '<span color="green">}</span>',font_size=24)
        unique_dict1.move_to(2 * UP + ORIGIN)
        self.play(Write( unique_dict1))
        text9=MarkupText('<span color="yellow">print</span> (unique_dict) <span color="white"></span>',font_size=14)
        text10=Text("output={'A': 'Apple', 'C': 'Code','D':Code}",font_size=14)
        text9.move_to(0.75 * UP + 5 * LEFT)  
        text10.move_to(0.5 * UP+ 3.8 * LEFT) 
        
        self.play(Write(text9))
        self.wait(1)  
        self.play(Write(text10))
        self.wait(3)
        self.play(FadeOut( unique_dict1))
        #play o vuong thu 7 chua text11 
        text11=Text("khóa là kiểu dữ liệu có thể thay đổi",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text11)
        list_dict = MarkupText(
            "<span color=\"white\">list_dict</span> = {"
            + f"<span color=\"magenta\">{[1, 1]}</span>: <span color=\"green\">'a'</span>, "
            + f"<span color=\"magenta\">{[1, 2]}</span>: <span color=\"green\">'b'</span>"
            + "}",font_size=24
        )   
        list_dict.move_to(2 * UP + ORIGIN)
        self.play(Write(list_dict))
        self.wait(2)
        text12=Text("Run/excute list_dict",font_size=14)
        text12.move_to(0.25*UP+ 5 * LEFT) 
        self.play(Write(text12))
        text13 = Text("ERROR!\n"
              "Traceback (most recent call last):\n"
              "File \"<string>\", line 3, in <module>\n"
              "TypeError: unhashable type: 'list'\n"
              "Khóa nên là kiểu dữ liệu có tính không thay đổi\n"
              "Các khóa [1, 1] và [1, 2] được sử dụng làm key trong dictionary\n"
              "là nguyên nhân dẫn đến lỗi. Vì các khóa này là các danh sách (list), và danh sách là một kiểu dữ liệu có tính thay đổi (mutable) trong Python.\n"
              "Fix Error trên: list_dict = { (1, 1): 'a', (1, 2): 'b' } dùng tuplet vì tuple là kiểu dữ liệu có tính thay đổi (immutable)",font="AlegreyaSans",font_size=24)
        create_rectangle_infor(self,text13 )
        #rec9
        text14=Text("key được tích hợp sẵn như các loại và chức năng",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text14)
        self.play(FadeOut(list_dict))
        func_key_dict = MarkupText(
            "<span color=\"white\">func_key_dict</span> = {"
            + f"<span color=\"yellow\">int</span>: <span color=\"magenta\">1</span>, "
            + f"<span color=\"yellow\">float</span>: <span color=\"magenta\">2</span>, "
            + f"<span color=\"yellow\">bool</span>: <span color=\"magenta\">3</span>"
            + "}",font_size=24
        )  
        func_key_dict.move_to(2 * UP + ORIGIN)
        self.play(Write(func_key_dict))
        self.wait(2)
        text15=Text("Output={<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}",font_size=14)
        text15.move_to(0*UP+ 3.5* LEFT) 
        self.play(Write(text15))
        text16 = Text(
        "Không khuyến khích dùng kiểu trên\n"
        "1. Khóa phải là duy nhất trong một thư mục\n"
        "2. Khóa phải là kiểu dữ liệu có tính không thay đổi (immutable)\n"
        "3. Nếu key là kiểu dữ liệu tuple, nó chỉ có thể chứa strings và numbers hoặc tuples",
        font="AlegreyaSans", font_size=24
        )
        create_rectangle_infor(self,text16 )
        self.play(FadeOut(text15),FadeOut(text12),FadeOut( func_key_dict),FadeOut(text6),FadeOut(text7),FadeOut(text9),FadeOut(text10))
        #ket noi cac phan tu tu dictinonry
        text17=Text("Truy câp các phàn tử trong Dictinonary",color="#FFFF00",font="AlegreyaSans",font_size=24)
        text18=Text("Sử dụng index",color="#FFFF00",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text17)
        create_text_with_rectangle(self,text18)
        third_dict = MarkupText('<span color="white">third_dict</span> = <span color="blue">dict</span>('
                            '<span color="green">name</span>=<span color="white">\'Huy\'</span>, '
                            '<span color="green">age</span>=<span color="white">\'21\'</span>, '
                            '<span color="green">IQ</span>=<span color="white">\'300\'</span>)',font_size=24)
        third_dict.move_to(2 * UP + ORIGIN)
        self.play(Write(third_dict))
        self.wait(2)
        text19=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict[</span><span color="green">\'name\'</span><span color="white">]</span>)',font_size=14)
        text20=Text("Output=Huy",font_size=14)
        text19.move_to(1.25 * UP +5 * LEFT)  
        text20.move_to(1 * UP+ 5 * LEFT) 
        self.play(Write(text19))
        self.wait(1)  
        self.play(Write(text20))
        self.wait(3)
        text21=Text("Sử dụng phương thức .get",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self,text21)
        text22 = MarkupText('<span color="yellow">print</span>(<span color="white">third_dict.</span>'
                            '<span color="yellow">get</span>(<span color="green">\'age\'</span>))', font_size=14)
        text23=Text("Output=21",font_size=14)
        text22.move_to(0.75 * UP + 5 * LEFT)  
        text23.move_to(0.50 * UP + 5 * LEFT) 
        self.play(Write(text22))
        self.wait(1)  
        self.play(Write(text23))
        text24=Text("Truy cập tới phàn tử khóa không có trong dictinonary",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self,text24)
        text25=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict[</span><span color="green">\'class\'</span><span color="white">]</span>)',font_size=14)
        text25.move_to(0.25 * UP + 5 * LEFT)  
        self.play(Write(text25))
        self.wait(1)
        text26=Text("Run/Excute print third_dict['class']\n"
                    "Traceback (most recent call last):\n"
                    "File \"<string>\", line n, in <module>\n"
                    "TypeError: unhashable type: 'list'\n"
                    "Nên dùng phương thức .get thay vì index"
                    "print(third_dict.get('class')) output sẽ là none và không bị lỗi",font="AlegreyaSans",font_size=24)
        create_rectangle_infor(self,text26)
        #PLAY dict.items
        text27=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict.</span>'
                            '<span color="yellow">items</span>(<span color="green"></span>))', font_size=14)
        text27.move_to(0*UP + 5 * LEFT)
        self.play(Write(text27))
        text27_surrounding=SurroundingRectangle( text27, color=YELLOW, buff=0.05)
        self.play(Create(text27_surrounding))
        conect_text27=Text("trả lại một giao diện mới của dicnonary items cặp (key,value) ",font="AlegreyaSans",font_size=14)
        conect_text27.move_to(0.50 * DOWN + 4.5* RIGHT)
        self.play(Write(conect_text27))
        arrow_conecttext27 = Arrow(text27_surrounding.get_right(), conect_text27.get_left(), color=YELLOW)
        self.play(Create(arrow_conecttext27))
        text28=Text("dict_items([('name', 'huy'), ('age', '21'), ('IQ', '300')])", font_size=14)
        text28.move_to(0.25* DOWN + 4.5 * LEFT)
        self.play(Write(text28))
        self.play(FadeOut(text27_surrounding),FadeOut(conect_text27),FadeOut(arrow_conecttext27))
        #dict.keys
        text29=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict.</span>'
                            '<span color="yellow">keys</span>(<span color="green"></span>))', font_size=14)
        text29.move_to(0.5*DOWN + 5 * LEFT)
        self.play(Write(text29))
        text29_surrounding=SurroundingRectangle( text29, color=YELLOW, buff=0.05)
        self.play(Create(text29_surrounding))
        conect_text29=Text("trả lại một giao diện mới của keys dicnonary",font="AlegreyaSans",font_size=14)
        conect_text29.move_to(0.75 * DOWN + 5* RIGHT)
        self.play(Write(conect_text29))
        arrow_conecttext29 = Arrow(text29_surrounding.get_right(), conect_text29.get_left(), color=YELLOW)
        self.play(Create(arrow_conecttext29))
        text30=Text("dict_keys(['name', 'age', 'IQ'])",font="AlegreyaSans",font_size=14)
        text30.move_to(0.75*DOWN + 5* LEFT)
        self.play(Write(text30))
        self.play(FadeOut(text29_surrounding),FadeOut(conect_text29),FadeOut(arrow_conecttext29))
        #dict.value
        text31=Text("Tương tự ta sẽ có dict_values(['Huy', '21', '300']) khi thay keys bằng values",font="AlegreyaSans",font_size=14)
        text31.move_to(0.95*DOWN + 3* LEFT)
        self.play(Write(text31))
        self.wait(2)
        text32 = Text("Khi sử dụng .items() và .keys(), .values() trong vòng for\n"
                "for key, value in third_dict.items():\n"
                "    print(f'{key}, {value}')\n"
                "output:\n"
                "    name, Huy\n"
                "    age, 21\n"
                "    IQ, 300\n"
                "for key in third_dict.keys():\n"
                "    print(f'{key}')\n"
                "output:\n"
                "    name\n"
                "    age\n"
                "    IQ\n"
                "for value in third_dict.values():\n"
                "    print(f'{value}')\n"
                "output:\n"
                "    Huy\n"
                "    21\n"
                "    300\n", font="AlegreyaSans", font_size=24)
        create_rectangle_infor(self,text32)
        self.play(FadeOut(text19,text20,text22,text23,text25,text27,text28,text29,text30,text31))
        # tạo animation Thêm các cặp khóa-giá trị
        text33=Text("Thêm các cặp khóa-giá trị",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text33)
        text34=MarkupText('<span color="white">third_dict[</span>'
                       '<span color="green">\'Nation\'</span>'
                       '<span color="white">]</span>'
                       '<span color="white"> = </span>'
                       '<span color="green">\'VietNam\'</span>', font_size=14)
        text34.move_to(1.25 * UP +5 * LEFT) 
        self.play(Write(text34))
        text35=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict</span>))', font_size=14)
        text35.move_to(1 * UP+ 5 * LEFT) 
        self.play(Write(text35))
        text36=Text("{'name': 'Huy', 'age': '21', 'IQ': '300', 'Nation': 'VietNam'}", font_size=14)
        text36.move_to(0.75 * UP + 4.5* LEFT)  
        self.play(Write(text36))
        # tạo animation Thêm các cặp khóa-giá trị
        text37=Text("Sửa đổi 1 cặp giá trị ",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text37)
        text38=MarkupText('<span color="white">third_dict[</span>'
                       '<span color="green">\'age\'</span>'
                       '<span color="white">]</span>'
                       '<span color="white"> = </span>'
                       '<span color="green">\'22\'</span>', font_size=14)
        text38.move_to(0.5*UP +5 * LEFT) 
        self.play(Write(text38))
        text39=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict</span>))', font_size=14)
        text39.move_to(0.25* UP+ 5 * LEFT) 
        self.play(Write(text39))
        text40=Text("{'name': 'Huy', 'age': '22', 'IQ': '300'}", font_size=14)
        text40.move_to(0*UP + 5 * LEFT)  
        self.play(Write(text40))
        #tạo ani mtion xóa 1 cạp khóa giá trị
        text41=Text(" xóa 1 cặp giá trị ",font="AlegreyaSans",font_size=24)
        create_text_with_rectangle(self, text41)
        text42=MarkupText('<span color="yellow">del[</span>'
                          '<span color="white">third_dict[</span>'
                            '<span color="green">\'age\'</span>'
                            '<span color="white">]</span>'
                            '<span color="white"> = </span>'
                            '<span color="green">\'22\'</span>', font_size=14)
        text42.move_to(0.25*DOWN +5 * LEFT) 
        self.play(Write(text42))
        text43=MarkupText('<span color="yellow">print</span>(<span color="white">third_dict</span>))', font_size=14)
        text43.move_to(0.5*DOWN+ 5 * LEFT) 
        self.play(Write(text43))
        text44=Text("{'name': 'Huy', 'IQ': '300'}", font_size=14)
        text44.move_to(0.75*DOWN + 5 * LEFT)  
        self.play(Write(text44))
        self.wait(2)
        #ending scene
        self.play(FadeOut(third_dict,text34,text35,text36,text38,text39,text40,text42,text43,text44))
        text45 = Text("Thank for watching",font_size=24)
        self.play(Write(text45))
        


        

        
       
        
       









       
        





