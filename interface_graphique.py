from tkinter import *
#import PySimpleGUI as sg
#import os
#import PyQt5 as pq

# global settings
window = Tk()
window.title('My Desk Reader')
window.geometry("900x600")
window.minsize(900, 600)
window.maxsize(900, 600)
window.iconbitmap('logo.ico')
window.config(background='#C0C0C0')
bg_1 = '#C0C0C0'
bg_2 = '#fffffe'
tx_1 = '#36596E'
tx_2 = '#4F4F4F'

# frame_1
frame_1 = Frame(window, bd=1, bg=bg_1, height=40)
frame_1.pack(padx=5, fill=X)
btn1 = Button(frame_1, text='Bibliotheque',)
btn1.grid(row=1, column=1, padx=10, pady=10)
btn2 = Button(frame_1, text='Browse Folder',)
btn2.grid(row=1, column=3, padx=10, pady=10)
btn3 = Button(frame_1, text='Exit', command=window.destroy)
btn3.grid(row=1, column=5, padx=10, pady=10)

# frame_2
frame_2 = Frame(window, bd=1, bg=bg_1, height=40)
frame_2.pack(padx=5, fill=X, pady=5)
ent1 = Entry(frame_2)
ent1.grid(row=1, columnspan=2, padx=10, pady=10)
btn4 = Button(frame_2, text='Search',)
btn4.grid(row=1, column=3, padx=10, pady=10)
btn4 = Button(frame_2, text='Refresh',)
btn4.grid(row=1, column=5, padx=10, pady=10)

# frame_3
frame_3 = Frame(window, bd=1, bg=bg_1, height=485)
frame_3.pack(padx=5, fill=X, pady=0)

#frame_4
frame_4 = Frame(frame_3, bd=1, bg=bg_2, height=480, width=600)
frame_4.pack(padx=5, pady=5, side=LEFT)

#frame_5
frame_5 = Frame(frame_3, bd=5, bg=bg_2, height=480, width=258)
frame_5.pack(padx=5, pady=5, side=RIGHT)

#frame_5 content
title = 'Book title'
book_img = PhotoImage(file='vis.png').zoom(10).subsample(32)
img_place = Canvas(frame_5, width = 180, height=250, bg=bg_1 )
img_place.create_image(90, 125, image=book_img)
img_place.grid(row=1, column=1, padx=10, pady=10)
btn5 = Button(frame_5, text='Mode lecture')
btn6 = Button(frame_5, text='Mode audio')



# main page
#title = Label(window, text='My Desk Reader',background='#355675', font='Helevetica 14', foreground='#D6D6D6')
#title.pack(expand=YES)



window.mainloop()