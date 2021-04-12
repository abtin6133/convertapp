import tkinter as tk
import pyttsx3

convert = pyttsx3.init()
convert.setProperty('rate',100)
convert.setProperty('volume',0.7)
admin = tk.Tk()

hi=tk.Entry(admin)
hi.pack()
def con():
    nam=hi.get()
    convert.say(nam)
    convert.runAndWait()
filename=tk.Entry(admin)
filename.pack()
def save():
    nam2=hi.get()
    saven=filename.get()
    convert.save_to_file(nam2, saven+".mp3")
    convert.runAndWait()
    
btnsave=tk.Button(admin,text="save",command=save)
btnsave.pack()
btn2=tk.Button(admin,text='btn2',command=con)
btn2.pack()


admin.mainloop()



































