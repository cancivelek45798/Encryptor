import tkinter
import base64

#functions
def combine_and_encode(text, password):
    combined_text = text + password
    encoded_data = base64.b64encode(combined_text.encode('utf-8'))
    return encoded_data.decode('utf-8')

def decode_and_extract(encoded_data, password):
    decoded_data = base64.b64decode(encoded_data.encode('utf-8'))
    text = decoded_data[:-len(password)]
    return text.decode('utf-8')


def button_save_and_encrypt():
    title = entry_title.get()
    text = text_note.get("1.0", tkinter.END) #Bir satırlık boşluk bırakıyor.
    masterkey = entry_masterkey.get()

    encoded_text = combine_and_encode(text, masterkey)

    save_data(title, encoded_text)

def button_decrypt():
    encoded_text = text_note.get("1.0", tkinter.END)
    masterkey = entry_masterkey.get()

    decoded_text = decode_and_extract(encoded_text, masterkey)
    change_text_content(decoded_text)

def save_data(title, text):
    with open('data.txt', 'a') as f:
        data = f"{title}:\n{text}\n\n" #data en son buraya gelecek.
        f.write(data)

def change_text_content(decoded_text):
    text_note.delete("1.0", tkinter.END)
    text_note.insert("1.0", decoded_text)

#window
window = tkinter.Tk()
window.minsize(width=400, height=500)
window.config(pady=50)
window.title("ENCRYPTOR")

#===== ui =====
#image
image = tkinter.PhotoImage(file="topsecret.png")
label_image = tkinter.Label(image=image)
label_image.pack()
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
label_se_button = tkinter.Button(text="Save & Encrypt", command=button_save_and_encrypt)
label_se_button.pack()

label_d_button = tkinter.Button(text="Decrypt", command=button_decrypt)
label_d_button.pack()


window.mainloop()