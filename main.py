import binascii
import tkinter
import base64
from tkinter import messagebox
#functions
def combine_and_encode(text, password):
    enc = []
    for i in range(len(text)):
        key_c = password[i % len(password)]
        enc_c = chr((ord(text[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode_and_extract(encoded_data, password):
    dec = []
    encoded_data = base64.urlsafe_b64decode(encoded_data).decode()
    for i in range(len(encoded_data)):
        key_c = password[i % len(password)]
        dec_c = chr((256 + ord(encoded_data[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def button_save_and_encrypt():
    title = entry_title.get()
    text = text_note.get("1.0", tkinter.END)
    masterkey = entry_masterkey.get()
    if len(title) == 0 or len(text) == 0 or len(masterkey) == 0:
        messagebox.showerror(title="Error!", message="Please enter all info.")

    else:
        encoded_text = combine_and_encode(text, masterkey)
        save_data(title, encoded_text)

def button_decrypt():
    encoded_text = text_note.get("1.0", tkinter.END)
    masterkey = entry_masterkey.get()

    if len(encoded_text) == 0 or len(masterkey) == 0:
        messagebox.showerror(title="Error!", message="Please enter all info.")

    else:
        try:
            decoded_text = decode_and_extract(encoded_text, masterkey)
            text_note.delete("1.0", tkinter.END)
            text_note.insert("1.0", decoded_text)

        except:
            messagebox.showerror(title="Error!", message="Please enter encoded text.")
def save_data(title, text):
    try:
        with open('data.txt', 'a') as f:
            data = f"{title}:\n{text}\n\n"
            f.write(data)

    except FileNotFoundError:
        with open('data.txt', 'a') as f:
            data = f"{title}:\n{text}\n\n"
            f.write(data)

    finally:
        entry_title.delete(0, tkinter.END)
        text_note.delete("1.0", tkinter.END)
        entry_masterkey.delete(0, tkinter.END)

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