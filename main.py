import random
import re
from encrypt_decrypt import Coder
from tkinter import *

# Window
window = Tk()
window.title("Coder")
window.minsize(width=600, height=450)


# Entry 1
filename = Entry(width=40)
filename.insert(END, string="File name")
filename.place(x=175, y=40)

# Entry 2
password = Entry(width=40)
password.insert(END, string="Password")
password.place(x=175, y=65)

# multiline text box and scroll bar
text = Text(height=15, width=50)
text.focus()
text.insert(END, "")
scroll = Scrollbar(window, width=15)
text.configure(yscrollcommand=scroll.set)
text.place(x=100, y=100)
scroll.configure(command=text.yview)
scroll.place(x=502, y=100, height=246)


# Encrypt function
def encrypt():
    u_input = text.get("0.0", END)
    u_shift = password.get()
    file_name = filename.get()
    coder = Coder(u_input, u_shift)
    coder.user_input()
    encrypted_message = coder.encrypt()
    with open(f"./{file_name}.txt", mode="w", encoding='utf-8') as encrypted_file:
        encrypted_file.write(encrypted_message)



# Decrypt function
def decrypt():
    u_shift = password.get()
    file_name = filename.get()
    with open(f"./{file_name}.txt", encoding='utf-8') as coded_file:
        file_content = coded_file.read()
    coder1 = Coder(file_content, u_shift)
    decrypted_message = coder1.decrypt(file_content)
    text.insert(END, f"{decrypted_message}")


# Encrypt button
encrypt_b = Button(width=25, text="Encrypt", command=encrypt)
encrypt_b.place(x=110, y=355)

# Decrypt button
decrypt_b = Button(width=25, text="Decrypt", command=decrypt)
decrypt_b.place(x=310, y=355)

window.mainloop()
