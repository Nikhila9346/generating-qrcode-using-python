from tkinter import messagebox
from pyqrcode import create
import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('QR Generator')
root.resizable(False,False)
root.iconbitmap('C:\\Users\\Admin\\Downloads\\favicon.ico')

#heading
heading = tkinter.Label(root, text="QR Code Generator", font="times 25",bg='white',fg='dark green')
heading.pack(side=TOP,pady=15)

#frame
frame=LabelFrame(root,padx=20,pady=50)
frame.pack(padx=10,pady=10)

def gen_qr():
    global dta
    dta = subtitle.get()
    dta = create(dta)
    test = dta.xbm(scale=2)
    global xbm_image
    #there may be a chance that the users will enter nothing and click make qr button it should show an error that the text or url is not entered
    if (subtitle.get() == "Enter URL or text here" or subtitle.get()==""):
        messagebox.showerror("ERROR", "Enter the URL or Text")
    else:
        xbm_image = BitmapImage(data=test, foreground="black", background='white')
        image_view.config(image=xbm_image)

def temp_text(e):
   subtitle.delete(0,"end")

#Entry frame text is deleted when we click that box
subtitle =Entry(frame,width=35,font=("Ubuntu Mono", 16))
subtitle.pack(padx=10,pady=10,anchor=W)
subtitle.insert(0,"Enter URL or text here")
subtitle.bind("<FocusIn>", temp_text)

make_button = Button(frame, text="Generate QR", font="italic", command=gen_qr,relief=SOLID,anchor=W,fg='dark green')
image_view =Label(frame)
statement = Label(frame)

# gui grid
subtitle.grid(row=1, column=0)
make_button.grid(row=50, column=0, columnspan=2)
image_view.grid(row=51, column=0, columnspan=2)
statement.grid(row=52, column=0, columnspan=2)

root.mainloop()