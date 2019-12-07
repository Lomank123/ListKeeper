import os
import sys

#path = "D:\\Python\\PyCharm\\WORKSPACE\\AllProjects\\ListKeeper"
#dirs = os.listdir(path)

#def main():
    #print('\n List Keeper v.2.0 \n')
    #finder(dirs, Files)
    #printfunc(Files)
    #selectfile(Files)


def finder(dirr, files, path):
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
        filecreator(newfile, path)


def printfunc(items):
    if not items:
        print('Empty file')
    for number, name in enumerate(items):
        if name == '':
            continue
        else:
            print(number + 1, '.  ', name)


def selectfile(files):
    print('Now select a file or [A]dd or [E]xit')
    while True:
        answer = input('Input:  ')
        if answer == 'a':
            addfilename(files)
        elif answer == 'e':
            print('Exiting programm...')
            sys.exit(0)
        elif int(answer) <= len(files):
            break
        else:
            print('Invalid number, try again ')
    readfile(files[int(answer)-1], names=[])


def addfilename(files):
    print('Enter a new filename:')
    filename = input('Input filename: ')
    if not filename.endswith('.txt'):
        filename += '.txt'
    files.append(filename)
    filecreator(filename)
    printfunc(files)
    selectfile(files)


def readfile(filename, names=[], change=False):
    print('\nfilename: ', filename, '\n')
    if not change:
        if not names:
            with open(filename, 'r+') as file:
                for line in file:
                    names.append(line[4:])
    printfunc(names)
    #menu(filename, names, change)


def menu(filename, names, change1=False):
    while True:
        print('\nNow select one of these options\n'
              '[A]dd  [D]elete  [S]ave  [Q]uit')
        answer = input('Input: ')
        if answer not in ['q', 'd', 's', 'a']:
            print('Try again')
        else:
            break
    if answer == 'a':
        addfunc(filename, names)
    if answer == 'd':
        deletefunc(filename, names)
    if answer == 's':
        savefunc(filename, names)
    if answer == 'q':
        quitfunc(filename, names, change1)


def addfunc(file, names1):
    answer = input('Enter a new name: ')
    names1.append(answer + '\n')
    print('Done! (Add)')
    readfile(file, names1, True)


def deletefunc(file, names2):
    print('Select a number ')
    answer = input('Input number: ')
    names2.pop(int(answer)-1)
    print('Done! (Delete)')
    readfile(file, names2, True)


def savefunc(file, list1, mainfunc=True):
    print('\nSaving...')
    with open(file, 'w+') as savedfile:
        for number, item in enumerate(list1):
            savedfile.write('{0} : {1}'.format(number + 1, item))
    print('Done! (Save)')
    if mainfunc:
        readfile(file, names=[])


def quitfunc(file, real, changes=False):
    if changes:
        print('\nDo you want to save changes?\n')
        while True:
            answer = input('[Y]es  [N]o ')
            if answer == 'y':
                savefunc(file, real, False)
                break
            if answer == 'n':
                print('Undo changes...')
                break
            else:
                print('Try again')
    print('Exiting file... (Quit)')
    printfunc(file)
    selectfile(file)


def filecreator(filename, path):
    pathwithfile = path + '\\{0}'.format(filename)  # This part of code creates a new file in a current folder
    with open(pathwithfile, 'w+'):
        print('Filename: "{0}" is successfully created in '.format(filename), pathwithfile)
