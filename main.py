import tkinter

window = tkinter.Tk()
window.minsize(width=400, height=500)
window.config(pady=50)
window.title("ENCRYPTOR")

#===== ui =====
#title
label_title = tkinter.Label(text="Enter your title")
label_title.pack()

entry_title = tkinter.Entry(width=30)
entry_title.pack()
entry_title.focus()

#Note
label_note = tkinter.Label(text="Enter your note")
label_note.pack()

text_note = tkinter.Text(width=30)
text_note.pack()

#masterkey
label_masterkey = tkinter.Label(text="Enter masterkey")
label_masterkey.pack()

entry_masterkey = tkinter.Entry(width=30)
entry_masterkey.pack()

#buttons
label_se_button = tkinter.Button(text="Save & Encrypt")
label_se_button.pack()

label_d_button = tkinter.Button(text="Decrypt")
label_d_button.pack()


window.mainloop()