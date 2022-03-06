from tkinter import *
from tkinter import ttk

goal=200


root =Tk()
root.title('FinanceYourFuture Progress bar')
root.geometry('1000x400')

#display goal
def display_goal():
   message=('Target contribution goal per month: £'+str(goal))
   goallabel.configure(text=message)

goallabel=Label(root, text="", font=("Courier 15 bold"))
goallabel.pack()

display_goal()


#how much of progress bar is filled in+ call congrats function if all filled in
def step():
    global entry
    moneyin= float(entry.get())
    my_progress['value']+=((moneyin*100)/goal)
    display_progress(my_progress['value'])
    if my_progress['value']>=100:
        display_congrats('Congratulations! You have reached your target contribution goal for this month :D!')

#display progress bar
my_progress=ttk.Progressbar(root,orient=HORIZONTAL,length=500,mode='determinate')
my_progress.pack(pady=40)

#display % of progress made towards goal
def display_progress(my_progress):
   message=('You have achieved '+str(my_progress)+'% of your target contribution so far this month') 
   progresslabel.configure(text=message)

progresslabel=Label(root, text="", font=("Courier 10 bold"))
progresslabel.pack()

#display congrats message
def display_congrats(congratsmessage):
   congratslabel.configure(text=congratsmessage, pady=20)

congratslabel=Label(root, text="", font=("Courier 15 bold"))
congratslabel.pack()


#Create an Entry widget to accept User Input of their contribution
entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget (record pension payment)
ttk.Button(root, text= "Record payment into my pension",width= 100, command= step).pack(pady=20)

root.mainloop()
