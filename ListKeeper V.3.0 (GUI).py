import os
from tkinter import *
from tkinter.filedialog import askdirectory

from AllProjects.ListKeeper.configs.config import demos
from AllProjects.ListKeeper.configs.Funcs1 import finder, printfunc, readfile


class API(Frame):
    def __init__(self, parent, buttons=None):
        Frame.__init__(self, parent, background='white')
        self.pack()
        self.parent = parent
        self.parent.title('--ListKeeper--')
        self.parent.geometry('800x400')

        dirname = Entry(parent, width=50)
        name = StringVar()
        dirname.place(x=100, y=100)

        func = lambda: self.Start(name)
        Button(self.parent, padx="20", pady="8", font="16", bg="green",
               text='Start', command=func).place(x=450, y=310)

        Button(self.parent, padx="20", pady="8", font="16",
               text='Quit', command=self.parent.quit).place(x=270, y=310)

        func = lambda: self.directory1(name, dirname)
        Button(self.parent, padx="10", pady="8", font="10", bg="green",
               text='Browse', command=func).place(x=420, y=100)

    def directory1(self, name1, dirname):
        name1.set(askdirectory())
        if name1.get():
            dirname.delete(0, END)
        dirname.insert(0, name1.get())
        return name1.get()

    def Start(self, dir):
        TL1 = Toplevel()
        TL1.geometry('600x400')
        TL1.title('--ListKeeper--')

        dirname = os.listdir(dir.get())
        Files = []

        finder(dirname, Files, dir.get())
        printfunc(Files)

        Label(TL1, text="Your directory: {0} ".format(dir.get())).place(x=10, y=350)
        Label(TL1, text="Here are filenames: ").place(x=150, y=50)
        listbox = Listbox(TL1)
        listbox.configure(width=40, height=12)
        for names in Files:
            listbox.insert(END, names)
        listbox.place(x=150, y=75)

        Button(TL1, padx="10", pady="8", font="10", bg="pink",
               text='Open').place(x=420, y=75)
        Button(TL1, padx="10", pady="8", font="10", bg="red",
               text='Quit').place(x=420, y=125)
        #Button(TL1, padx="10", pady="8", font="10", bg="green",
               #text='Browse').place(x=420, y=175)
        #Button(TL1, padx="10", pady="8", font="10", bg="yellow",
               #text='Browse').place(x=420, y=225)

        TL1.grab_set()
        TL1.focus_set()
        TL1.wait_window()


def main():
    root = Tk()
    app = API(root, buttons=demos)
    root.mainloop()


if __name__ == '__main__':
    main()
