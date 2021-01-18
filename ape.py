# Jacob Gerlach
# jwgerlach00@gmail.com
# 1/17/2021
# ape.py

# File sorting tool to send files of certain MIME types in pre-determined locations.

import os
import mimetypes
import shutil
import sys
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
username = os.getlogin()

sourcePath = 'C:\\Users\\' + username + '\\Desktop\\fileApe'
imgDest = 'C:\\Users\\' + username + '\\Pictures'
vidDest = 'C:\\Users\\' + username + '\\Videos'
docDest = 'C:\\Users\\' + username + '\\Documents'


def send(name, destination):
    path = 'C:\\Users\\' + username + '\\' + destination
    if os.path.exists(path):
        try:
            shutil.move(sourcePath + '\\' + name, path)
        except shutil.Error:
            messagebox.showerror('UH OH!', '\"' + name + '\"' + '\nis already located in desired destination:\n'
                                 + '\"' + path + '\"')
    else:
        messagebox.showerror('UH OH!', '\"' + path + '\"' +
                             '\nis not a directory.\nEnter a new destination for:\n' + '\"' + name + '\"')


def sort(name):
    sort_label = tk.Label(root, text='Enter destination:')
    sort_label.grid(row=3, column=0)

    dir_label = tk.Label(root, text='C:\\Users\\' + username + '\\')
    dir_label.grid(row=4, column=0)

    sort_entry = tk.Entry(root)
    sort_entry.grid(row=4, column=1)

    send_button = tk.Button(root, text='SEND', command=lambda: send(name, sort_entry.get()))
    send_button.grid(row=4, column=2)


def gui(name):
    root_label = tk.Label(root, text='FILE: ' + name + ' IS UN-SORTABLE')
    root_label.grid(row=0, column=0)

    quit_button = tk.Button(root, text='ok', command=root.destroy)
    quit_button.grid(row=1, column=0, padx=15)

    sort_button = tk.Button(root, text='manual sort', command=lambda: sort(name))
    sort_button.grid(row=2, column=0, padx=15)

    root.mainloop()


try:
    if len(sys.argv) > 1:
        droppedFiles = sys.argv[1:]
        for file in droppedFiles:
            fileMime = mimetypes.guess_type(file)
            try:
                fileExt = mimetypes.guess_extension(fileMime[0])

                if fileExt == '.jpg' or fileExt == '.png' or fileExt == '.jpeg' or fileExt == '.gif' or \
                        fileExt == '.tiff':
                    shutil.move(file, imgDest)
                elif fileExt == '.mov' or fileExt == '.mp4' or fileExt == '.avi':
                    shutil.move(file, vidDest)
                elif fileExt == '.doc' or fileExt == '.pdf' or fileExt == '.docx' or fileExt == '.xls':
                    shutil.move(file, docDest)
                else:
                    gui(os.path.split(file)[1])
            except AttributeError:
                gui(os.path.split(file)[1])
    else:
        for file in os.listdir(sourcePath):
            fileMime = mimetypes.guess_type(file)
            try:
                fileExt = mimetypes.guess_extension(fileMime[0])

                if fileExt == '.jpg' or fileExt == '.png' or fileExt == '.jpeg' or fileExt == '.gif' or \
                        fileExt == '.tiff':
                    shutil.move(sourcePath + '\\' + file, imgDest)
                elif fileExt == '.mov' or fileExt == '.mp4' or fileExt == '.avi':
                    shutil.move(sourcePath + '\\' + file, vidDest)
                elif fileExt == '.doc' or fileExt == '.pdf' or fileExt == '.docx' or fileExt == '.xls':
                    shutil.move(sourcePath + '\\' + file, docDest)
                else:
                    gui(file)
            except AttributeError:
                gui(file)
except shutil.Error:
    messagebox.showerror('UH OH!', 'File is already located in desired destination')
