import os
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno


class API(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.pack()
        self.parent = parent
        self.parent.title('--ListKeeper--')
        self.parent.geometry('800x400')
        self.first(self.parent)
        self.changes = False

    def first(self, parent):
        name = StringVar()
        dirname = Entry(parent, width=50, textvariable=name)
        dirname.place(x=100, y=100)

        func = lambda: self.Start(name)
        btn1 = Button(self.parent, padx="20", pady="8", font="16", bg="green",
                      text='Start', command=func)
        btn1.place(x=450, y=310)

        btn2 = Button(self.parent, padx="20", pady="8", font="16",
                      text='Quit', command=self.parent.quit)
        btn2.place(x=270, y=310)

        func = lambda: self.directory1(name)
        btn3 = Button(self.parent, padx="10", pady="8", font="10", bg="green",
                      text='Browse', command=func)
        btn3.place(x=420, y=100)

    def directory1(self, name1):
        text = askdirectory()
        if text:
            name1.set(text)

    def Start(self, dir1):
        TL1 = Toplevel()
        TL1.geometry('600x400')
        TL1.title('--ListKeeper--')

        dirname = os.listdir(dir1.get())
        Files = []

        self.finder(dirname, Files, dir1.get())
        self.printfunc(Files)

        Label(TL1, text="Your directory: {0} ".format(dir1.get())).place(x=10, y=350)
        Label(TL1, text="Here are filenames: ").place(x=150, y=50)

        listbox = Listbox(TL1)
        listbox.configure(width=40, height=12)
        for names in Files:
            listbox.insert(END, names)
        listbox.place(x=150, y=75)

        func = lambda: self.openf(listbox, dir1.get())
        Button(TL1, padx="10", pady="8", font="10", bg="pink",
               text='Open', command=func).place(x=420, y=75)

        Button(TL1, padx="10", pady="8", font="10", bg="red",
               text='Quit', command=TL1.destroy).place(x=420, y=125)

        TL1.grab_set()
        TL1.focus_set()
        TL1.wait_window()

    def openf(self, lb, name):
        selection = name + "/{0}".format(lb.get(lb.curselection()[0]))
        self.readfile(selection, names=[])

    # Functions from Listkeeper V.2.0
    def finder(self, dirr, files, path):
        for filename in dirr:
            if filename.endswith('.txt'):
                files.append(filename)
        if not files:
            print("There are no files in this directory. \n"
                  "Creating a new one...")
            newfile = input("Please, enter a new filename: ")
            if not newfile.endswith('.txt'):
                newfile += '.txt'
            files.append(newfile)
            self.filecreator(newfile, path)

    def printfunc(self, items):
        if not items:
            print('Empty file')

    # NEED TO CORRECT THIS
    def addfilename(self, files):
        print('Enter a new filename:')
        filename = input('Input filename: ')
        if not filename.endswith('.txt'):
            filename += '.txt'
        files.append(filename)
        self.filecreator(filename)
        self.printfunc(files)

    def readfile(self, filename, names=[]):
        if not names:
            with open(filename, 'r+') as file:
                for line in file:
                    names.append(line[4:])
        self.printfunc(names)
        self.openedf(names, filename)

    def openedf(self, names, filename):
        TL2 = Toplevel()
        TL2.geometry('600x400')
        TL2.title('--ListKeeper--')

        listbox1 = Listbox(TL2, selectmode=EXTENDED)
        listbox1.configure(width=40, height=12)
        for name in names:
            listbox1.insert(END, name)
        listbox1.place(x=150, y=75)

        self.changes = listbox1.get(0, END)

        func = lambda: self.addfunc2(TL2, listbox1)
        Button(TL2, padx="10", pady="8", font="10", bg="pink",
               text='Add', command=func).place(x=420, y=75)

        func = lambda: self.quitfunc2(TL2, filename, listbox1, self.changes)
        Button(TL2, padx="10", pady="8", font="10", bg="red",
               text='Quit', command=func).place(x=420, y=125)

        func = lambda: self.deletefunc2(listbox1.curselection(), listbox1)
        Button(TL2, padx="10", pady="8", font="10", bg="green",
               text='Delete', command=func).place(x=420, y=175)

        func = lambda: self.savefunc2(filename, listbox1)
        Button(TL2, padx="10", pady="8", font="10", bg="yellow",
               text='Save', command=func).place(x=420, y=225)
        Label(TL2, text="Your filename: {0} ".format(filename)).place(x=10, y=350)
        TL2.grab_set()
        TL2.focus_set()
        TL2.wait_window()

    def addfunc2(self, parent, lb):
        tladd = Toplevel(parent)
        tladd.geometry('300x200')
        tladd.title('--ListKeeper--')
        name = StringVar()
        dirname = Entry(tladd, width=30, textvariable=name)
        dirname.place(x=20, y=20)
        func = lambda : self.addsupp(tladd, lb, name)
        btn = Button(tladd, padx="6", pady="6", font="6", bg="yellow",
                     text='Add name', command=func).place(x=100, y=125)

        tladd.grab_set()
        tladd.focus_set()
        tladd.wait_window()

    def addsupp(self, parent, lb, name):
        if name:
            lb.insert(END, name.get() + "\n")
            print(lb.get(0, END))
            parent.destroy()
        else:
            print("No name")

    def deletefunc2(self, indexes, lb):
        if indexes:
            check = askyesno("Delete or not", "Do you REALLY want to delete these notes?")
            if check:
                lb.delete(indexes[0], indexes[len(indexes)-1])
        else:
            print("You don't choose notes")

    def savefunc2(self, filename, lb, quitask=False):
        if not quitask:
            check = askyesno("Saving", "Do you want to save these notes?")
            if check:
                with open(filename, 'w+') as savedfile:
                    for number, item in enumerate(lb.get(0, END)):
                        savedfile.write('{0} : {1}'.format(number + 1, item))
                self.changes = lb.get(0, END)
        else:
            check = askyesno("Quitting and Saving", "Oh, you quitting... Do you want to save changes?")
            if check:
                with open(filename, 'w+') as savedfile:
                    for number, item in enumerate(lb.get(0, END)):
                        savedfile.write('{0} : {1}'.format(number + 1, item))

    def quitfunc2(self, parent, filename, lb, firstlist):
        secondlist = lb.get(0, END)
        if firstlist != secondlist:
            self.savefunc2(filename, lb, quitask=True)
        parent.destroy()

    def filecreator(self, filename, path):
        pathwithfile = path + '\\{0}'.format(filename)  # This part of code creates a new file in a current folder
        with open(pathwithfile, 'w+'):
            print('Filename: "{0}" is successfully created in '.format(filename), pathwithfile)


def main():
    root = Tk()
    app = API(root)
    root.mainloop()


if __name__ == '__main__':
    main()
