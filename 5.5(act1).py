import tkinter as tk
window=tk.Tk()  
window.title("example")    
#create alable widgets
label =tk.Label(window,text="hello tkinter!",font=("Arial","16"),fg="blue",bg="yellow")  
label.pack()         #pack layout manager
# run tkinter
window.mainloop()