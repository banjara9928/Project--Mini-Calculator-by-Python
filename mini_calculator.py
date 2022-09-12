from tkinter import*
expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
def calculate():
        global expression
        expression=str(eval(expression))
        equation.set(expression)
def c():
	global expression
	expression = ""
	equation.set("")
def back():
        global expression
        expression=expression[0:len(expression)-1]
        equation.set(expression)
if _name_ == "_main_":
	root = Tk()
	root.title("Simple Calculator")
	equation = StringVar()
	expression_field = Entry(root, textvariable=equation)
	expression_field.grid(columnspan=4,sticky=NSEW)
	root.geometry("400x400")

Button(root,text="1",command=lambda :press(1)).grid(row=2,column=0,sticky=NSEW)
Button(root,text="2",command=lambda :press(2)).grid(row=2,column=1,sticky=NSEW)
Button(root,text="3",command=lambda :press(3)).grid(row=2,column=2,sticky=NSEW)
Button(root,text="4",command=lambda :press(4)).grid(row=3,column=0,sticky=NSEW)
Button(root,text="5",command=lambda :press(5)).grid(row=3,column=1,sticky=NSEW)
Button(root,text="6",command=lambda :press(6)).grid(row=3,column=2,sticky=NSEW)
Button(root,text="7",command=lambda :press(7)).grid(row=4,column=0,sticky=NSEW)
Button(root,text="8",command=lambda :press(8)).grid(row=4,column=1,sticky=NSEW)
Button(root,text="9",command=lambda :press(9)).grid(row=4,column=2,sticky=NSEW)
Button(root,text="0",command=lambda :press(0)).grid(row=5,column=1,sticky=NSEW)
Button(root,text="00",command=lambda :press('00')).grid(row=5,column=0,sticky=NSEW)
Button(root,text=".",command=lambda :press(".")).grid(row=5,column=2,sticky=NSEW)
Button(root,text="c",command=c).grid(row=1,column=0,sticky=NSEW)
Button(root,text="%",command=lambda:press("%")).grid(row=1,column=1,sticky=NSEW)
Button(root,text="<X",command=back).grid(row=1,column=2,sticky=NSEW)
Button(root,text="/",command=lambda:press("/")).grid(row=1,column=3,sticky=NSEW)
Button(root,text="",command=lambda :press("")).grid(row=2,column=3,sticky=NSEW)
Button(root,text="-",command=lambda:press("-")).grid(row=3,column=3,sticky=NSEW)
Button(root,text="+",command=lambda:press("+")).grid(row=4,column=3,sticky=NSEW)
Button(root,text="=",command=calculate).grid(row=5,column=3,sticky=NSEW)

for i in range(6):
    root.rowconfigure(i,weight=1)
for j in range(4):
    root.columnconfigure(j,weight=1)
root.mainloop()