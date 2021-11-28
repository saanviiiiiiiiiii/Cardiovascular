#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:19:48 2021

@author: macbook
"""
from tkinter import*

root = Tk()
root.title("CRDIOVASCULAR REPORT")
root.geometry("600x600")
root.configure(bg ="light blue")

question1_radioButton = StringVar(value="0")

question1 = Label(root, text="1.Do you experience shortness of breath during routine activities?",bg="light pink")
question1.place(relx=0.3,rely=0.3,anchor=CENTER)
question1_r1=Radiobutton(root, text="yes",variable=question1_radioButton, value = "yes",bg="light pink")
question1_r1.pack()
question1_r2=Radiobutton(root, text="no",variable=question1_radioButton, value = "no",bg="light pink")
question1_r2.pack()

question2_radioButton = StringVar(value="0")

question2 = Label(root, text="2.Do you experience shortness of breath while at rest/lying down?",bg="light pink")
question2.place(relx=0.5,rely=0.3,anchor=CENTER)
question2_r1=Radiobutton(root, text="yes",variable=question1_radioButton, value = "yes",bg="light pink")
question2_r1.pack()
question2_r2=Radiobutton(root, text="no",variable=question1_radioButton, value = "no",bg="light pink")
question2_r2.pack()

question3_radioButton = StringVar(value="0")

question3 = Label(root, text="3.Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",bg="light pink")
question3.place(relx=0.7,rely=0.3,anchor=CENTER)
question3_r1=Radiobutton(root, text="yes",variable=question1_radioButton, value = "yes",bg="light pink")
question3_r1.pack()
question3_r2=Radiobutton(root, text="no",variable=question1_radioButton, value = "no",bg="light pink")
question3_r2.pack()

question4_radioButton = StringVar(value="0")

question4 = Label(root, text="4.Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?",bg="light pink")
question4.place(relx=0.10,rely=0.3,anchor=CENTER)
question4_r1=Radiobutton(root, text="yes",variable=question1_radioButton, value = "yes",bg="light pink")
question4_r1.pack()
question4_r2=Radiobutton(root, text="no",variable=question1_radioButton, value = "no",bg="light pink")
question4_r2.pack()

question5_radioButton = StringVar(value="0")

question5 = Label(root, text="5.Have you experienced loss of appetite (frequent feeling of being full) or nausea recently?",bg="light pink")
question5.place(relx=0.14,rely=0.3,anchor=CENTER)
question5_r1=Radiobutton(root, text="yes",variable=question1_radioButton, value = "yes",bg="light pink")
question5_r1.pack()
question5_r2=Radiobutton(root, text="no",variable=question1_radioButton, value = "no",bg="light pink")
question5_r2.pack()

def fever_score():
    
       score=0
    
       if  question1_radiobutton.get()=="yes":
           score = score+20
           print(score)
       if  question2_radiobutton.get()=="yes":
           score = score+20
           print(score)
       if  question3_radiobutton.get()=="yes":
           score = score+20
           print(score)
           if  question4_radiobutton.get()=="yes":
               score = score+20
               print(score)
               if  question5_radiobutton.get()=="yes":
                   score = score+20
                   print(score)
           
       if score <= 20:
          messagebox.showinfo("Report","There is no need for visiting a doctor.")
       elif score <20 and score <=40:
           messagebox.showinfo("Report","You might have to visit the doctor.")
       else :
            messagebox.showinfo("Report"," I know you have to visist the doctor.")
btn = Button(root, text = 'click me',command= fever_score)
btn.pack()
