import os
import sys
# определяет таблицу имя:обработчик с демонстрационными примерами
from tkinter.filedialog import askdirectory  # импортировать стандартные
from tkinter.colorchooser import askcolor # диалоги из Lib\tkinter
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
 'Open': askdirectory
 #'Query': lambda: askquestion('Warning', 'You typed “rm *”\nConfirm?'),
 #'Error': lambda: showerror('Error!', "He’s dead, Jim"),
 #'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

Files = []
