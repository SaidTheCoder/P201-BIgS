from tkinter import *
window=Tk()

window.title('Simple Interest Calculator')
window.geometry("400x400")
window.configure(bg='red')


app_label=Label(window, text="Simple Interest Calculator", fg = "black", bg = "lightgreen", font=("Ariel", 20),bd=5)
app_label.place(x=50, y=20)

principal_label=Label(window, text="Enter Principal Amount (in ₹)", fg = "black", bg = "lightgreen", font=("Ariel", 12),bd=1)
principal_label.place(x=20, y=90)

principal_entry=Entry(window, text="", bd=2, width=20)
principal_entry.place(x=225, y=92) 

rate_label=Label(window,text="Enter Rate (in %)", fg="black",bg="lightgreen",font=("Ariel",11))
rate_label.place(x=20,y=140)

rate_entry=Entry(window,text="",bd=2,width=20)
rate_entry.place(x=150,y=142)

time_label=Label(window,text="Enter Time (in years)",fg="black",bg="lightgreen",font=("Ariel",11))
time_label.place(x=20,y=185)

time_entry= Entry(window,text="",bd=2,width=20)
time_entry.place(x=180,y=187)


def calculate_si():
    time=float(time_entry.get())
    rate=float(rate_entry.get())
    principal=float(principal_entry.get())
    si=(principal*rate*time)/100
    si=round(si,2)
    SI_label.destroy()
    output_msg=Label(SI_frame,text="Simple Interest is ₹ "+str(si),bg="lightgreen",font=("Ariel",12),width=42)
    output_msg.place(x=20,y=40)
    output_msg.pack()
    
calculate_button=Button(window,text="Calculate",fg="black",bg="lightgreen",bd=4,command=calculate_si)
calculate_button.place(x=20,y=250)


SI_frame = LabelFrame(window,text="Simple Interest", bg = "lightgreen", font=("Ariel", 12))
SI_frame.pack(padx=20, pady=20)
SI_frame.place(x=20,y=300)

SI_label=Label(SI_frame,text=" ", bg = "lightgreen", font=("Ariel", 12), width=33)
SI_label.place(x=20,y=20)
SI_label.pack()

window.mainloop()