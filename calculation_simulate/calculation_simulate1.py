import tkinter
import tkinter.font
import numpy as np
from sympy import *
import math

np.set_printoptions(precision=8)


class Calculator(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.all_press_list = []  # total elements
        self.temp_elem = '0'  # temporarily save the element
        self.cur_cond = 'n'  # judge condition
        self.is_computed = False
        self.show_num = tkinter.StringVar()  # been changed only when the
        self.record = tkinter.StringVar()  # temporary elem is added into list
        self.record.set('')

    def press_number(self, num):
        if self.is_computed:
            self.show_num.set(num)
            self.is_computed = False
            self.cur_cond = 'n'

            return
        print(num)
        old_num = self.show_num.get()
        if old_num == '0':
            self.temp_elem = num
        else:
            self.temp_elem = old_num + num
        self.show_num.set(self.temp_elem)
        self.temp_elem = '0'
        self.cur_cond = 'n'

        return

    def press_comp_char(self, sign):
        cond = self.cur_cond
        if cond == 'c':
            return
        if cond == 'n':
            self.all_press_list.append(self.show_num.get())
            self.all_press_list.append(sign)
            self.show_num.set('0')
            self.cur_cond = 'c'

            return

    def press_clear_char(self, sign):
        if self.is_computed or sign == 'C':
            self.all_press_list.clear()
            self.show_num.set('0')
            self.cur_cond = 'n'
            self.is_computed = False

            return

        if sign == 'CE':
            self.show_num.set('0')
            self.cur_cond = 'n'

            return

        if sign == 'B':
            num = self.show_num.get()
            if len(num) == 1:
                self.show_num.set('0')
            else:
                self.show_num.set(num[0:-1])

            return

    def press_equal_char(self, sign):
        if self.cur_cond == 'n':
            self.is_computed = True
            self.all_press_list.append(self.show_num.get())

            comp_string = ''.join(self.all_press_list)
            try:
                self.show_num.set(sign + str(eval(comp_string)))
            except:
                self.show_num.set("error")
            self.all_press_list.clear()

            return
        if self.cur_cond == 'c':
            return

    def press_func(self, func):
        if func == "sin(x)":
            self.show_num.set(np.sin(float(self.show_num.get())))
        if func == "cos(x)":
            self.show_num.set(np.cos(float(self.show_num.get())))
        if func == "tan(x)":
            self.show_num.set(np.tan(float(self.show_num.get())))
        if func == "n!":
            self.show_num.set(math.factorial(int(self.show_num.get())))

    """
    -----------------------------------------------------------------------------------------------------------
    """

    def create_obj(self, c=4, r=6):
        list_obj = list(symbols(f"x1:{c * r + 1}"))
        single = []
        all = []
        for i in range(r):
            for j in range(c):
                single.append(list_obj[i * c + j])
            all.append(single)
            single = []
        # print(all)
        return all

    default_text_1D = ['%', "CE", "C", "<<",
                       "sin(x)", "cos(x)", "tan(x)", "÷",
                       '7', '8', '9', 'x',
                       '4', '5', '6', '-',
                       '1', '2', '3', '+',
                       "n!", '0', '.', '=']

    default_command_text = [['%', 'CE', 'C', 'B'],
                            ["sin(x)", "cos(x)", "tan(x)", "/"],
                            ['7', '8', '9', '*'],
                            ['4', '5', '6', '-'],
                            ['1', '2', '3', '+'],
                            ["n!", '0', '.', '=']]



    def create_text(self, text_list_1D=default_text_1D, c=4, r=6):
        single = []
        all = []
        for i in range(r):
            for j in range(c):
                single.append(text_list_1D[i * c + j])
            all.append(single)
            single = []
        return all

    default_number_list = [[2, 3, 3, 3], [5, 5, 5, 2], [1, 1, 1, 2], [1, 1, 1, 2], [1, 1, 1, 2], [5, 1, 2, 4]]

    def create_command(self, text_list=default_command_text, number_list=default_number_list, c=4, r=6):
        output_list = []
        single = []
        for i in range(r):
            for j in range(c):
                single.append(self.get_command(text_list[i][j], number_list[i][j]))
            output_list.append(single)
        return output_list

    def get_command(self, text, n_judge):
        if n_judge == 1:
            return lambda: self.press_number(text)
        elif n_judge == 2:
            return lambda: self.press_comp_char(text)
        elif n_judge == 3:
            return lambda: self.press_clear_char(text)
        elif n_judge == 4:
            return lambda: self.press_equal_char(text)
        elif n_judge == 5:
            return lambda: self.press_func(text)


    def draw_the_button(self, c=4, r=6, **kwargs):
        obj_list = self.create_obj(c=c, r=r)
        command_list = self.create_command(c=c, r=r)
        text_list = self.create_text(c=c, r=r)
        for i in range(r):
            for j in range(c):
                obj_list[i][j] = tkinter.Button(self.root, text=text_list[i][j],
                                                font=kwargs['font'], bg=kwargs['bg'], fg=kwargs['fg'], bd=kwargs['bd'],
                                                command=command_list[i][j])
                obj_list[i][j].place(x=kwargs['width'] * j, y=200 + kwargs['height'] * i,
                                     width=kwargs['width'], height=kwargs['height'])

        return obj_list

    """
    -----------------------------------------------------------------------------------------------------------
    """

    def operate(self):
        self.root.minsize(300, 620)
        self.root.title('computer')
        self.root.iconbitmap()
        self.show_num.set('0')

        input_bg, num_fg, btn_fg, btn_bg = "#393943", "#DCDCDC", "#909194", "#22222C"  # 各种颜色
        btn_w, btn_h = 75, 70

        my_font1 = tkinter.font.Font(family='Arial', size=14)
        my_font2 = tkinter.font.Font(family='Arial', size=20)
        label = tkinter.Label(self.root, font=my_font1, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                              textvariable=self.record)
        label.place(width=300, height=120)
        label2 = tkinter.Label(self.root, font=my_font2, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                               textvariable=self.show_num)
        label2.place(y=120, width=300, height=80)

        self.draw_the_button(c=4, r=6, font=my_font2, bg=btn_bg, fg=btn_fg, bd=0,
                             width=btn_w, height=btn_h)

        self.root.mainloop()

        return


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.operate()
