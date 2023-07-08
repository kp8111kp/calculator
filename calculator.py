from tkinter import *
from tkinter.messagebox import *
import numpy as np
root = Tk()
root.title("CALCULATOR BY KP")
root.geometry("350x475+200+200")
f = ("Arial", 15, "bold")
root.wm_attributes('-toolwindow', 'True')


def Btn_Click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def Bt_Clear():
    global expression
    expression = ""
    input_text.set("")

def Bt_Equal():
    try:
        global expression
        result = str(eval(expression))
        #print(expression)
        #print(result)
        input_text.set(result)

    except Exception as e:
        #print(e)
        e = str(e)
        if (e=="unexpected EOF while parsing (<string>, line 1)") or (e=="invalid syntax (<string>, line 1)"):
            input_text.set("U Entered only symbols")
        elif e == "unexpected EOF while parsing (<string>, line 0)":
            input_text.set("EMPTY")
        else:
            input_text.set(e)
            expression = ""

"""
    except Exception as e:
        print(e)
        e = str(e)
        if (e == "unexpected EOF while parsing (<string>, line 1)") or (e=="invalid syntax (<string>, line 1)"):
            raise Exception("u entered only symbols")
        else:
            raise Exception(e)

    except Exception as bi:

        bi = str(bi)
        input_text.set(bi)
        expression = ""
"""





expression = ""
input_text = StringVar()


input_frame = Frame(root,width=400,height=50,bd=0)
input_frame.pack(side=TOP)

input_field = Entry(input_frame,font=f,textvariable=input_text,width=26,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root,width=312,height=500)
btns_frame.pack()



bt_1 = Button(btns_frame, text="1", font=f, height=3,width=5,command=lambda :Btn_Click("1")).grid(row=2, column=0)

bt_2 = Button(btns_frame, text="2", font=f, height=3,width=5,command=lambda :Btn_Click("2")).grid(row=2, column=1)

bt_3 = Button(btns_frame, text="3", font=f, height=3,width=5,command=lambda :Btn_Click("3")).grid(row=2, column=2)

bt_4 = Button(btns_frame, text="4", font=f, height=3,width=5,command=lambda :Btn_Click("4")).grid(row=3, column=0)

bt_5 = Button(btns_frame, text="5", font=f, height=3,width=5,command=lambda :Btn_Click("5")).grid(row=3, column=1)

bt_6 = Button(btns_frame, text="6", font=f, height=3,width=5,command=lambda :Btn_Click("6")).grid(row=3, column=2)

bt_7 = Button(btns_frame, text="7", font=f,height=3,width=5,command=lambda :Btn_Click("7")).grid(row=4, column=0)

bt_8 = Button(btns_frame, text="8", font=f, height=3,width=5,command=lambda :Btn_Click("8")).grid(row=4, column=1)

bt_9 = Button(btns_frame, text="9", font=f,height=3,width=5,command=lambda :Btn_Click("9")).grid(row=4, column=2)

bt_0 = Button(btns_frame, text="0", font=f, height=3,width=5,command=lambda :Btn_Click("0")).grid(row=5, column=1)

bt_dot =Button(btns_frame,text=".",font=f,height=3,width=5,command=lambda :Btn_Click(".")).grid(row=5,column=0)

bt_eql = Button(btns_frame, text="=", font=f,height=3,width=5,bg="sky blue",command=lambda :Bt_Equal()).grid(row=5, column=2)

bt_plus = Button(btns_frame, text="+", font=f, height=3,width=5,bg="light pink",command=lambda :Btn_Click("+")).grid(row=2, column=3)

bt_minus = Button(btns_frame, text="-", font=f, height=3,width=5,bg="light pink",command=lambda :Btn_Click("-")).grid(row=3, column=3)

bt_milti = Button(btns_frame, text="*", font=f, height=3,width=5,bg="light pink",command=lambda :Btn_Click("*")).grid(row=4, column=3)

bt_div = Button(btns_frame, text="/", font=f,height=3,width=5,bg="light pink",command=lambda :Btn_Click("/")).grid(row=5, column=3)


bt_clear = Button(btns_frame, text="C", height=3,width=40,bg="light grey",command=lambda :Bt_Clear()).grid(row=6, column=0,columnspan=4)



mainloop()
