
from tkinter import *

# تحديد التابع 
def f(x):
    return x**3 - 5*x - 9
#تحديد المشتق 
def g(x):
    return 3*x**2 - 5

# تنفيذ طريقة نيوتن رافسون

def newtonRaphson(x0,e,N):
    a = float(inp1.get())
    b = float(inp2.get())
    c = float(inp3.get())
    newtonRaphson= '%s,%s,%s' % (a, b, c)
    txt.insert(END, newtonRaphson)   # نتائج حساب عرض إضافية
    inp1.delete(0, END)  # مدخلات واضحة
    inp2.delete(0, END)  # مدخلات واضحة
    inp3.delete(0, END)  # مدخلات واضحة
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) ==float(0.0):
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > int(N):
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is : %0.8f' % x1)
    else:
        print('\nNot Convergent.')


root = Tk()
root.geometry('460x240')
root.title("NEWTON RAPHSON")

inp1 = (Entry(root))
inp1.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.1)

inp2 = (Entry(root))
inp2.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)

inp3 =(Entry(root))
inp3.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.1)

btn2 = Button(root, text="Go Newton", command=lambda: int(newtonRaphson(inp1.get(), inp2.get(), inp3.get())))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

# قم بتخطيط مربع نص أعلى بنسبة 40٪ من ارتفاع النموذج بدءًا من 60٪ من الوضع الرأسي للنموذج
txt = Text(root)
txt.place(rely=0.6, relheight=0.4)

root.mainloop()
