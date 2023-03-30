import tkinter as tk
from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.mode = 1
        self.create_widgets()

    def create_widgets(self):
        # Creating buttons for the keyboard
        self.help_button = tk.Button(self.master, text="Help", padx=41, command=self.show_help)
        self.help_button.grid(row=0, column=0, columnspan=2, sticky="W", padx=0, pady=0)

        self.input_field = tk.Entry(self.master, justify="right")
        self.input_field.grid(row=1, column=0, rowspan=2, columnspan=3, sticky="WE", padx=5, pady=0)

        self.mode_button1 = tk.Button(self.master, text="Regular", command=lambda: self.switch_mode(1))
        self.mode_button1.grid(row=1, column=3, sticky="E",padx=5, pady=5)

        self.mode_button2 = tk.Button(self.master, text="Time", padx=8, command=lambda: self.switch_mode(2))
        self.mode_button2.grid(row=2, column=3, sticky="E", padx=5, pady=5)

        self.button_ac = tk.Button(self.master, text="AC", padx=36, pady=20, command=self.button_ac)
        self.button_open_bracket = tk.Button(self.master, text="(", padx=40, pady=20, command=lambda: self.button_click("(")) 
        self.button_close_bracket = tk.Button(self.master, text=")", padx=42, pady=20, command=lambda: self.button_click(")"))
        self.button_divide = tk.Button(self.master, text="÷", padx=40, pady=20, command=self.button_divide)
        
        self.button_ac.grid(row=3, column=0, padx=0, pady=0)
        self.button_open_bracket.grid(row=3, column=1, padx=0, pady=0)
        self.button_close_bracket.grid(row=3, column=2, padx=0, pady=0)
        self.button_divide.grid(row=3, column=3, padx=0, pady=0)

        self.button_7 = tk.Button(self.master, text="7", padx=41, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(self.master, text="8", padx=39, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(self.master, text="9", padx=41, pady=20, command=lambda: self.button_click(9))
        self.button_multiply = tk.Button(self.master, text="*", padx=41, pady=20, command=self.button_multiply)

        self.button_7.grid(row=4, column=0, pady=0, padx=0)
        self.button_8.grid(row=4, column=1, pady=0, padx=0)
        self.button_9.grid(row=4, column=2, pady=0, padx=0)
        self.button_multiply.grid(row=4, column=3, pady=0, padx=0)

        self.button_4 = tk.Button(self.master, text="4", padx=41, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(self.master, text="5", padx=39, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(self.master, text="6", padx=41, pady=20, command=lambda: self.button_click(6))
        self.button_subtract = tk.Button(self.master, text="-", padx=41, pady=20, command=self.button_subtract)
        
        self.button_4.grid(row=5, column=0, pady=0, padx=0)
        self.button_5.grid(row=5, column=1, pady=0, padx=0)
        self.button_6.grid(row=5, column=2, pady=0, padx=0)
        self.button_subtract.grid(row=5, column=3, pady=0, padx=0)

        self.button_1 = tk.Button(self.master, text="1", padx=41, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(self.master, text="2", padx=39, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(self.master, text="3", padx=41, pady=20, command=lambda: self.button_click(3))
        self.button_add = tk.Button(self.master, text="+", padx=40, pady=20, command=self.button_add)

        self.button_1.grid(row=6, column=0, pady=0, padx=0)
        self.button_2.grid(row=6, column=1, pady=0, padx=0)
        self.button_3.grid(row=6, column=2, pady=0, padx=0)
        self.button_add.grid(row=6, column=3, pady=0, padx=0)

        self.button_0 = tk.Button(self.master, text="0", padx=41, pady=20, command=lambda: self.button_click(0))
        self.button_decimal = tk.Button(self.master, text=",", padx=40, pady=20, command=lambda: self.button_click("."))
        self.button_delete = tk.Button(self.master, text="Del", padx=35, pady=20, command=self.button_delete)
        self.button_equal = tk.Button(self.master, text="=", padx=40, pady=20, command=self.button_equal)

        self.button_0.grid(row=7, column=0, pady=0, padx=0)
        self.button_decimal.grid(row=7, column=1, pady=0, padx=0)
        self.button_delete.grid(row=7, column=2, pady=0, padx=0)
        self.button_equal.grid(row=7, column=3, pady=0, padx=0)

        self.button_tax = tk.Button(self.master, text="Tax (19%)", padx=64, pady=6, command=self.calculate_tax)
        self.button_volume = tk.Button(self.master, text="Volume(x³)", padx=63, pady=6, command=self.calculate_volume)
        self.button_tax.grid(row=8, column=0, columnspan=2, pady=0, padx=0)
        self.button_volume.grid(row=8, column=2, pady=0, columnspan=2, padx=0)

        # Creating input fields for mode 2
        self.distance_label = tk.Label(self.master, text="Enter travel length(km):")
        self.input_distance = tk.Entry(self.master)
        self.speed_label = tk.Label(self.master, text="Enter average speed(km/h):")
        self.input_speed = tk.Entry(self.master)

        self.distance_label.grid(row=4, column=0, padx=10, pady=5, sticky="W")
        self.input_distance.grid(row=5, column=0, padx=10, pady=5, sticky="E")
        self.speed_label.grid(row=4, column=1, padx=10, pady=5, sticky="W")
        self.input_speed.grid(row=5, column=1, padx=10, pady=5, sticky="E")

        # Создание кнопки для вычисления результата
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_time)
        self.calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Создание метки для вывода результата
        self.result_label = tk.Label(self.master, text="")
        self.result_label.config(cursor="xterm")
        self.result_label.grid(row=7, column=0, columnspan=2)
        
        # Setting the initial state
        self.update_mode()

    def switch_mode(self, mode):
        self.mode = mode
        self.update_mode()

    def update_mode(self):
        if self.mode == 1:
            # Show input fields for mode 1
            self.help_button.grid()
            self.mode_button1.grid()
            self.mode_button2.grid()
            self.input_field.grid()
            self.button_9.grid()
            self.button_8.grid()
            self.button_7.grid()
            self.button_6.grid()
            self.button_5.grid()
            self.button_4.grid()
            self.button_3.grid()
            self.button_2.grid()
            self.button_1.grid()
            self.button_0.grid()
            self.button_ac.grid()
            self.button_open_bracket.grid()
            self.button_close_bracket.grid()
            self.button_divide.grid()
            self.button_add.grid()
            self.button_multiply.grid()
            self.button_delete.grid()
            self.button_subtract.grid()
            self.button_decimal.grid()
            self.button_equal.grid()
            self.button_tax.grid()
            self.button_volume.grid()
            # Hide input fields for mode 2
            self.distance_label.grid_remove()
            self.input_distance.grid_remove()
            self.speed_label.grid_remove()
            self.input_speed.grid_remove()
            self.calculate_button.grid_remove()
            self.result_label.grid_remove()
            
        elif self.mode == 2:
            # Show input fields for mode 2
            self.help_button.grid()
            self.distance_label.grid()
            self.input_distance.grid()
            self.speed_label.grid()
            self.input_speed.grid()
            self.calculate_button.grid()
            self.result_label.grid()
            # Hide input fields for mode 1
            self.input_field.grid_remove()
            self.button_9.grid_remove()
            self.button_8.grid_remove()
            self.button_7.grid_remove()
            self.button_6.grid_remove()
            self.button_5.grid_remove()
            self.button_4.grid_remove()
            self.button_3.grid_remove()
            self.button_2.grid_remove()
            self.button_1.grid_remove()
            self.button_0.grid_remove()
            self.button_ac.grid_remove()
            self.button_open_bracket.grid_remove()
            self.button_close_bracket.grid_remove()
            self.button_divide.grid_remove()
            self.button_add.grid_remove()
            self.button_multiply.grid_remove()
            self.button_delete.grid_remove()
            self.button_subtract.grid_remove()
            self.button_decimal.grid_remove()
            self.button_equal.grid_remove()
            self.button_tax.grid_remove()
            self.button_volume.grid_remove()

    def button_click(self, number):
        current = self.input_field.get()
        self.input_field.delete(0, END)
        self.input_field.insert(0, str(current) + str(number))

    def button_ac(self):
        self.input_field.delete(0, END)

    def button_add(self):
        first_number = self.input_field.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        self.input_field.delete(0, END)

    def button_multiply(self):
        first_number = self.input_field.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        self.input_field.delete(0, END)

    def button_divide(self):
        first_number = self.input_field.get()
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        self.input_field.delete(0, END)

    def button_subtract(self):
        first_number = self.input_field.get()
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        self.input_field.delete(0, END)

    def button_delete(self):
        current = self.input_field.get()
        self.input_field.delete(len(current)-1, END)
    
    def button_equal(self):
        second_number = self.input_field.get()
        self.input_field.delete(0, END)

        if math == "addition":
            self.input_field.insert(0, f_num + float(second_number))
        elif math == "subtraction":
            self.input_field.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            self.input_field.insert(0, f_num * float(second_number))
        elif math == "division":
            self.input_field.insert(0, f_num / float(second_number))
        

    def calculate_tax(self):
        # Получение значения из поля ввода
        value = float(self.input_field.get())
        # Вычисление налога
        tax = value * 0.19
        # Вычисление новой стоимости с учетом налога
        total_cost = value + tax
        # Вывод результатов
        result_text = f"Cost: {value:.2f}\nTax (19%): {tax:.2f}\nTotal: {total_cost:.2f}"
        dialog = tk.Toplevel(self.master)
        dialog.title("Result:")
        dialog.geometry("400x300")
        text = tk.Text(dialog, wrap="word")
        text.insert("1.0", result_text)
        text.pack(expand=True, fill="both")

    def calculate_volume(self):
        side = float(self.input_field.get())
        volume = side ** 3
        self.input_field.delete(0, END)
        if isinstance(volume, str):
            self.input_field.insert(0,"Error")
        else:
            self.input_field.insert(0,f"{volume}")

    def calculate_time(self):
        distance = float(self.input_distance.get())   
        speed = float(self.input_speed.get())
        time = distance / speed
        self.result_label.config(text=f"The approximate time is {time} h.")

    def show_help(self):
        info_window = tk.Toplevel(self.master)
        info_window.title("About this app")
        help_text = "This calculator can be used both as a standard calculator and as a tool for calculating tax, cube volume, and travel time.\nIts user-friendly interface allows you to perform various mathematical operations with ease.\nWith the tax calculator feature, you can easily calculate the tax amount at a rate of 19% from the input number.\nThe cube volume calculator allows you to find the volume of a cube by simply entering its side length.\nAnd with the travel time calculator, you can calculate the estimated time of arrival for a given distance and speed.\nThis versatile calculator is a handy tool for anyone who needs to perform quick calculations on a regular basis."
        info_label = tk.Label(info_window, text=help_text, padx=10, pady=10)
        info_label.pack()

root = tk.Tk()
root.title("Calculator(3 in 1)")
root.geometry("380x454")
app = App(root)
root.mainloop()