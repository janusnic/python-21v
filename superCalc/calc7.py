# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add,
 subtract, multiply and divide using functions
'''
# импортирование модулей python
try:
    # for Python2
    from Tkinter import *   # notice capitalized T in Tkinter
    import tkFont
    import tkMessageBox
except ImportError:
    # for Python3
    from tkinter import *   # notice lowercase 't' in tkinter here
    from tkinter import font
    from tkinter import messagebox


class Application(Frame):
    def click(self, key):
        if key == '=':
            # avoid division by integer
            if '/' in self.entry.get() and '.' not in self.entry.get():
                self.entry.insert(END, ".0")
            # guard against the bad guys abusing eval()
            str1 = "-+0123456789."
            if self.entry.get()[0] not in str1:
                self.entry.insert(END, "first char not in " + str1)
            # here comes the calculation part
            try:
                result = eval(self.entry.get())
                self.entry.insert(END, " = " + str(result))
            except:
                self.entry.insert(END, "--> Error!")
        elif key == 'C':
            # clear entry
            self.txt = self.entry.get()[:-1]
            self.entry.delete(0, END)
            self.entry.insert(0, self.txt[:-1])

        elif key == 'AC':
            self.entry.delete(0, END)  # clear all entry
        elif key == '-x':
            if '=' in self.entry.get():
                self.entry.delete(0, END)
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        else:
            # previous calculation has been done, clear entry
            if '=' in self.entry.get():
                self.entry.delete(0, END)
            if '÷'.decode('utf-8') in self.entry.get():
                div = self.entry.get().replace('÷'.decode('utf-8'), '/')
                self.entry.delete(0, END)
                self.entry.insert(END, div)
            self.entry.insert(END, key)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        btn_list = [
          '7',  '8',  '9',  '*', '%',  'M',
          '4',  '5',  '6',  '÷', '√ ', 'MS',
          '1',  '2',  '3',  '-',  'x²', 'MR',
          '0',  '.',  '=',  '+',  '-x', 'MC'
          ]
        # create all buttons with a loop
        r = 1
        c = 0
        for b in btn_list:
            rel = RIDGE
            cmd = lambda x=b: self.click(x)
            Button(master, text=b, width=5, relief=rel, command=cmd).grid(row=r, column=c)
            c += 1
            if c > 5:
                c = 0
                r += 1

        # use Entry widget for an editable display
        self.entry = Entry(master, width=33, bg="yellow")
        self.entry.grid(row=0, column=0, columnspan=5)

        Button(master, text='C', width=3, command=lambda x='C': self.click(x)).grid(row=0, column=4)
        Button(master, text='AC', width=3, command=lambda x='AC': self.click(x)).grid(row=0, column=5)


def main():
    # Создать приложение
    app = Application()
    # Вызов методов класса менеджера окон (Wm)
    app.master.title("Super Calculator")
    app.master.maxsize(1000, 400)
    # Запуск программы
    app.mainloop()


if __name__ == '__main__':
    main()
