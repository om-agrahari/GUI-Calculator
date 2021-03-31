from tkinter import *

def click_button(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)

def equal_button():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def clear_button():
    global operator
    operator=""
    text_input.set(operator)
    
    
    
    
   
top=Tk()
top.geometry("700x450+200+200")
top.title("CALCULATER")

operator=""
text_input=StringVar()

entry=Entry(top,bd=20,width=60,font="bold",justify="right",bg="skyblue",textvariable=text_input)
entry.grid(columnspan=4)

button7=Button(top,text=7,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(7))
button7.grid(row=1,column=0)
button8=Button(top,text=8,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(8))
button8.grid(row=1,column=1)
button9=Button(top,text=9,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(9))
button9.grid(row=1,column=2)
buttondivide=Button(top,text="/",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button("/"))
buttondivide.grid(row=1,column=3)
#--------------------------------------------------------------------------------------

button4=Button(top,text=4,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(4))
button4.grid(row=2,column=0)
button5=Button(top,text=5,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(5))
button5.grid(row=2,column=1)
button6=Button(top,text=6,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(6))
button6.grid(row=2,column=2)
buttonmultiply=Button(top,text="x",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button("*"))
buttonmultiply.grid(row=2,column=3)

#--------------------------------------------------------------------------------------


button1=Button(top,text=1,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(1))
button1.grid(row=3,column=0)
button2=Button(top,text=2,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(2))
button2.grid(row=3,column=1)
button3=Button(top,text=3,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(3))
button3.grid(row=3,column=2)
buttonsubtract=Button(top,text="-",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button("-"))
buttonsubtract.grid(row=3,column=3)

#---------------------------------------------------------------------------------------

button0=Button(top,text=0,width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button(0))
button0.grid(row=4,column=0)
buttonpoint=Button(top,text=".",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button("."))
buttonpoint.grid(row=4,column=1)
buttonaddition=Button(top,text="+",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=lambda:click_button("+"))
buttonaddition.grid(row=4,column=2)
buttonequal=Button(top,text="=",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=equal_button)
buttonequal.grid(row=4,column=3)
buttonclear=Button(top,text="clear",width=10,font="bold",padx=5,pady=5,bg="yellow",bd=10,activeforeground="blue",command=clear_button)
buttonclear.grid(row=5,column=2)

top.mainloop()
