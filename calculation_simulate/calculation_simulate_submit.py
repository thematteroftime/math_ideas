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
        self.history_record = tkinter.StringVar()

    def press_number(self, num):
        if self.is_computed:
            self.show_num.set(num)
            self.is_computed = False
            self.cur_cond = 'n'
            self.record.set('None')

            return

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
            self.record.set('None')
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
            self.record.set(comp_string)
            self.history_record.set(self.history_record.get() + "\n\n")
            try:
                self.show_num.set(sign + str(eval(comp_string)))
                self.history_record.set(self.history_record.get() + comp_string + self.show_num.get())  #
            except:
                self.show_num.set("error")
            self.all_press_list.clear()

            return
        if self.cur_cond == 'c':
            return

    def press_func(self, func):
        if self.is_computed:
            return
        if func == "sin(x)":
            self.show_num.set(np.sin(float(self.show_num.get())))
        elif func == "cos(x)":
            self.show_num.set(np.cos(float(self.show_num.get())))
        elif func == "tan(x)":
            self.show_num.set(np.tan(float(self.show_num.get())))
        elif func == "n!":
            self.show_num.set(math.factorial(int(self.show_num.get())))
        elif func == "1/x":
            if self.show_num == '0':
                self.show_num.set('error')
                self.is_computed = True
                return
            self.show_num.set(1 / float(self.show_num.get()))
        elif func == "exp":
            self.show_num.set(np.exp(float(self.show_num.get())))
        elif func == "|x|":
            self.show_num.set(abs(float(self.show_num.get())))
        # self.is_computed = True

        return

    def press_coefficient(self, sign, num=1):
        if self.is_computed:
            return
        if self.show_num.get() != '0':
            num = float(self.show_num.get())
        if self.is_computed:
            self.press_clear_char('C')
        if sign == 'e':
            self.show_num.set(num * np.e)
        if sign == 'pi':
            self.show_num.set(num * np.pi)
        return

    """
    -----------------------------------------------------------------------------------------------------------
    """

    def create_obj(self, c, r):
        list_obj = list(symbols(f"x1:{c * r + 1}"))
        return list_obj

    default_text_2D = [['%', "CE", "C", "<<", 'x^y'],
                       ["sin(x)", "cos(x)", "tan(x)", "÷", '|x|'],
                       ['7', '8', '9', 'x', '1/x'],
                       ['4', '5', '6', '-', 'exp'],
                       ['1', '2', '3', '+', 'e'],
                       ["n!", '0', '.', '=', 'pi']]

    default_command_text = [['%', 'CE', 'C', 'B', '**'],
                            ["sin(x)", "cos(x)", "tan(x)", "/", '|x|'],
                            ['7', '8', '9', '*', '1/x'],
                            ['4', '5', '6', '-', 'exp'],
                            ['1', '2', '3', '+', 'e'],
                            ["n!", '0', '.', '=', 'pi']]

    default_command_number_list = [[2, 3, 3, 3, 2],
                                   [5, 5, 5, 2, 5],
                                   [1, 1, 1, 2, 5],
                                   [1, 1, 1, 2, 5],
                                   [1, 1, 1, 2, 6],
                                   [5, 1, 2, 4, 6]]

    def create_text(self, text_list_2D, c, r):
        output_list = []
        for i in range(r):
            for j in range(c):
                output_list.append(text_list_2D[i][j])

        return output_list

    def create_command(self, command_text_list, command_number_list, c, r):
        output_list = []
        for i in range(r):
            for j in range(c):
                output_list.append(self.get_command(command_text_list[i][j], command_number_list[i][j]))

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
        elif n_judge == 6:
            return lambda: self.press_coefficient(text)

    def draw_the_button(self, c, r, user_chose, text_list_2D=default_text_2D,
                        command_text_list=default_command_text,
                        command_number_list=default_command_number_list,
                        **kwargs):
        obj_list = self.create_obj(c=c, r=r)
        command_list = self.create_command(command_text_list=command_text_list, command_number_list=command_number_list,
                                           c=c, r=r) if user_chose == None else [self.get_command(i, j)
                                                                                 for i, j in zip(command_text_list,
                                                                                                 command_number_list)]
        text_list = self.create_text(text_list_2D=text_list_2D, c=c, r=r) if user_chose == None else text_list_2D
        j = 0

        for i in range(c * r):
            if i != 0 and i % c == 0:
                j += 1
            obj_list[i] = tkinter.Button(self.root, text=text_list[i],
                                         font=kwargs['font'], bg=kwargs['bg'], fg=kwargs['fg'], bd=kwargs['bd'],
                                         command=command_list[i])
            obj_list[i].place(x=kwargs['width'] * (i % c), y=kwargs['screen_height'] + kwargs['height'] * j,
                              width=kwargs['width'], height=kwargs['height'])

        return obj_list

    def create_user_list(self, user_choice, text_list_2D,
                         command_text_list,
                         command_number_list):
        text_list_2D = list(np.array(text_list_2D).flatten())
        command_text_list = list(np.array(command_text_list).flatten())
        command_number_list = list(np.array(command_number_list).flatten())
        output1 = []
        output2 = []
        output3 = []
        index_list = []

        for i in range(len(user_choice)):
            index_list.append(text_list_2D.index(user_choice[i]))
        for index in index_list:
            output1.append(text_list_2D[index])
            output2.append(command_text_list[index])
            output3.append(command_number_list[index])

        return output1, output2, output3

    """
    -----------------------------------------------------------------------------------------------------------
    """

    def operate(self, single_width=75, single_height=70, screen_height=200, c=5, r=6, text_list_2D=default_text_2D,
                command_text_list=default_command_text,
                command_number_list=default_command_number_list, user_chose=None):

        if user_chose != None:
            text_list_2D, command_text_list, command_number_list = self.create_user_list(user_chose,
                                                                                         text_list_2D,
                                                                                         command_text_list,
                                                                                         command_number_list)
        total_width = c * single_width
        total_length = r * single_height + screen_height
        self.root.minsize(int(total_width + total_width * 0.4), total_length)
        self.root.maxsize(2160, 1440)
        self.root.title('computer')
        self.root.iconbitmap()
        self.show_num.set('0')
        self.record.set('None')
        self.history_record.set('')

        input_bg, num_fg, btn_fg, btn_bg = "#393943", "#DCDCDC", "#909194", "#22222C"  # 各种颜色
        btn_w, btn_h = single_width, single_height

        my_font1 = tkinter.font.Font(family='Arial', size=int(screen_height * 0.1))
        my_font2 = tkinter.font.Font(family='Arial', size=22)
        my_font3 = tkinter.font.Font(family='Arial', size=int(screen_height * 0.15))
        my_font4 = tkinter.font.Font(family='Arial', size=int(screen_height * 0.08))
        label = tkinter.Label(self.root, font=my_font1, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                              textvariable=self.record)
        label.place(width=total_width, height=screen_height * 0.6)

        label2 = tkinter.Label(self.root, font=my_font3, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                               textvariable=self.show_num)
        label2.place(y=screen_height * 0.6, width=total_width, height=screen_height * 0.4)

        label3 = tkinter.Label(self.root, font=my_font4, bg=input_bg, bd='9', fg=num_fg, anchor='se',
                               textvariable=self.history_record)
        label3.place(x=total_width, width=total_width * 0.4, height=total_length)

        self.draw_the_button(c=c, r=r, user_chose=user_chose, text_list_2D=text_list_2D,
                             command_text_list=command_text_list,
                             command_number_list=command_number_list,
                             font=my_font2, bg=btn_bg, fg=btn_fg, bd=0,
                             width=btn_w, height=btn_h, screen_height=screen_height)

        self.root.mainloop()

        return


if __name__ == '__main__':
    user_list = ["CE", "C", "<<", 'x^y',
                 '7', '8', '9', 'x',
                 '4', '5', '6', '-',
                 '1', '2', '3', '+',
                 "n!", '0', '.', '=',
                 "sin(x)", "cos(x)", "tan(x)", "÷",
                 'pi', 'e', 'exp', '1/x']
    my_calculator = Calculator()
    my_calculator.operate(single_width=120, single_height=100, screen_height=250, c=4, r=7, user_chose=user_list)

"""
default_text_2D = [['%', "CE", "C", "<<", 'x^y'],
                       ["sin(x)", "cos(x)", "tan(x)", "÷", '|x|'],
                       ['7', '8', '9', 'x', '1/x'],
                       ['4', '5', '6', '-', 'exp'],
                       ['1', '2', '3', '+', 'e'],
                       ["n!", '0', '.', '=', 'pi']]
"""
