import tkinter as tk
from typing import Text
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schrijf hier tussen je code
button.config(text='switch light on')
window['bg'] = 'black'

def addition(a):
    file = open('actions.log','a')
    file.write(a)
    file.write('\n')
    file.close()

def clickButton(event):
    if button.config('text')[-1] == 'switch light on':
        button.config(text='switch light off')
        window['bg'] = 'yellow'
        addition('Light has been switched on.')
    else:
        button.config(text='switch light on')
        addition('Light has been switched off.')
        window['bg'] = 'black'

button.bind("<Button-1>", clickButton)
# schrijf hier tussen je code
window.mainloop()