import os
from tkinter import *
from tkinter.filedialog import askdirectory


class API(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.pack()
        self.parent = parent
        self.parent.title('--ListKeeper--')
        self.parent.geometry('800x400')
        self.first(self.parent)

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
        for number, name in enumerate(items):
            if name == '':
                continue
            else:
                print(number + 1, '.  ', name)

# NEED TO CORRECT THIS
    def addfilename(self, files):
        print('Enter a new filename:')
        filename = input('Input filename: ')
        if not filename.endswith('.txt'):
            filename += '.txt'
        files.append(filename)
        self.filecreator(filename)
        self.printfunc(files)

    def readfile(self, filename, names=[], change=False):
        if not change:
            if not names:
                with open(filename, 'r+') as file:
                    for line in file:
                        names.append(line[4:])
        self.printfunc(names)
        self.openedf(names)
        # menu(filename, names, change)

    def openedf(self, names):
        TL2 = Toplevel()
        TL2.geometry('600x400')
        TL2.title('--ListKeeper--')
        listbox1 = Listbox(TL2)
        listbox1.configure(width=40, height=12)
        for name in names:
            listbox1.insert(END, name)
        listbox1.place(x=150, y=75)
        Button(TL2, padx="10", pady="8", font="10", bg="pink",
               text='Open').place(x=420, y=75)
        Button(TL2, padx="10", pady="8", font="10", bg="red",
               text='Quit', command=TL2.destroy).place(x=420, y=125)
        Button(TL2, padx="10", pady="8", font="10", bg="green",
               text='Browse').place(x=420, y=175)
        Button(TL2, padx="10", pady="8", font="10", bg="yellow",
               text='Browse').place(x=420, y=225)
        # Button(TL1, padx="10", pady="8", font="10", bg="green",
        # text='Browse').place(x=420, y=175)
        # Button(TL1, padx="10", pady="8", font="10", bg="yellow",
        # text='Browse').place(x=420, y=225)

    def menu(self, filename, names, change1=False):
        while True:
            print('\nNow select one of these options\n'
                  '[A]dd  [D]elete  [S]ave  [Q]uit')
            answer = input('Input: ')
            if answer not in ['q', 'd', 's', 'a']:
                print('Try again')
            else:
                break
        if answer == 'a':
            self.addfunc(filename, names)
        if answer == 'd':
            self.deletefunc(filename, names)
        if answer == 's':
            self.savefunc(filename, names)
        if answer == 'q':
            self.quitfunc(filename, names, change1)

    def addfunc(self, file, names1):
        answer = input('Enter a new name: ')
        names1.append(answer + '\n')
        print('Done! (Add)')
        self.readfile(file, names1, True)

    def deletefunc(self, file, names2):
        print('Select a number ')
        answer = input('Input number: ')
        names2.pop(int(answer) - 1)
        print('Done! (Delete)')
        self.readfile(file, names2, True)

    def savefunc(self, file, list1, mainfunc=True):
        print('\nSaving...')
        with open(file, 'w+') as savedfile:
            for number, item in enumerate(list1):
                savedfile.write('{0} : {1}'.format(number + 1, item))
        print('Done! (Save)')
        if mainfunc:
            self.readfile(file, names=[])

    def quitfunc(self, file, real, changes=False):
        if changes:
            print('\nDo you want to save changes?\n')
            while True:
                answer = input('[Y]es  [N]o ')
                if answer == 'y':
                    self.savefunc(file, real, False)
                    break
                if answer == 'n':
                    print('Undo changes...')
                    break
                else:
                    print('Try again')
        print('Exiting file... (Quit)')
        self.printfunc(file)

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
