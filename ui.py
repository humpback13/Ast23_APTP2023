from tkinter import *
num=0
root =Tk()
root.geometry("1000x1400")
root.title("알록달록시간표") #창 설정
root.config(bg="light blue")

img = PhotoImage(file = "C:/Users/user/Desktop/aptp/min.png")
tl = Label(root)
tl.config(image = img)
tl2= Label(root)
tl2.config(text="알록달록 시간표")
tl2.config(width=20,height=3)
tl2.config(bg="red")
tl.grid(row=3, column=2)
tl2.grid(row=1, column=2) #레이블

def submit():
    input_text = ent1.get()
    num = int(input_text)

ent = Text(root) #root라는 창에 입력창 생성
ent.config(width=30, height=20)
ent.grid(row=4,column=1) #입력 강의


ent1 = Entry(root)
ent1.grid(row=2,column=2) #강의 수

btn1 = Button(root)
btn1.config(padx=20, pady=20)
btn1.config(text = "들을 강의의 개수")
btn1.config(fg="black", bg="orange") #fg - 글자색 , bg-배경색
btn1.config(command=submit)
btn1.grid(row=2,column=1) #버튼
def save_to_file():
    input_text= ent.get("1.0",END)
    with open("C:/Users/user/Desktop/aptp/input.txt","w") as file:
        file.write(input_text)

btn=Button(root)
btn.config(text="입력")
btn.config(command=save_to_file)
btn.config(width=10, height=2)
btn.config(bg="yellow")
btn.grid(row=4,column=2)

def load_from_file():
    with open("C:/Users/user/Desktop/aptp/output.txt","r") as file:
        content = file.read()
        ent3.delete("1.0",END)
        ent3.insert(END,content)


ent3 = Text(root)
ent3.config(width=50,height=20)
ent3.grid(row=4,column=4)

btn2 = Button(root)
btn2.config(text="시간표 보기")
btn2.config(command=load_from_file)
btn2.config(width=10,height=3)
btn2.config(bg="green")
btn2.grid(row=4,column=3)

root.mainloop()