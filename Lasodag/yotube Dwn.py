from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading
from tkinter import filedialog, messagebox

root = Tk()
root.title('Youtube Downloader')
root.geometry('600x320')
root.resizable(False, False)

#my function:

def browse():
    directory = filedialog.askdirectory(title='Save Vidio')
    folderLink.delete(0, 'end')
    folderLink.insert(0, directory)

def down_yt():
    status.config(text='Status downloading...')
    link = ytlink.get()
    folder = folderLink.get()
    YouTube(link, on_complete_callback=Finish).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(folder)
    messagebox.showinfo(title='Successfully completed')
def Finish(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text='Status : complete')

#Youtube logo:
ytlogo = PhotoImage(file='Youtube_L200.png')
ytTitle = Label(root, image=ytlogo)
ytTitle.place(relx=0.5, rely=0.25, anchor='center')

#Youtube link:

ytLabel = Label(root, text='Youtube Link')
ytLabel.place(x=25, y=150)

ytlink = Entry(root, width=60)
ytlink.place(x=140, y=150)

#Downloader folder :

folderLabel = Label(root, text='Download folder')
folderLabel.place(x=25, y=183)

folderLink = Entry(root, width=50)
folderLink.place(x=140, y=183)

#Browse Button :

browse = Button(root, text='Browse', bg='green',fg='white', command=browse)
browse.place(x=455, y=180,)

# Download Buttun :

Download = Button(root, text='Download', bg='#FF6103', fg='#FFF8DC', command=threading.Thread(target=down_yt).start)               # w r adding anothor Lib 2 opperate behind the scense
Download.place(x=280, y=220)

#Status bar :

status = Label(root, text='Status Ready', font='calibre 10 italic', fg='black', bg='white', anchor='w')
status.place(rely=1, anchor='sw', relwidth=1)



root.mainloop()
