import tkinter as tk
def get_text():
    input_text = entry.get()                  #get text from fields
    print("you entered:",input_text) 
window=tk.Tk()
window.title("entry fields")    
# entery widgets
entry =tk.Entry(window,width=30)  
entry.pack()    
get_button =tk.Button(window,text="get text",command=get_text)
get_button.pack()                   #button to get input                     
window.mainloop()

