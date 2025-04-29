import tkinter as tk
window=tk.Tk()  
window.title("MY window")
label1 =tk.Label(window,text="tkinter1!",font=("Time New Roman","20"),fg="black",bg="red")   
label2 =tk.Label(window,text="tkinter2!",font=("Time New Roman","24"),fg="pink",bg="blue")   
label1.pack() 
label2.pack() 
#def button_click():
def show(): 
   print("button clicked!")
b =tk.Button(window, text ="Click ME", command = show)
b.place(x=100,y=100)             
window.mainloop()