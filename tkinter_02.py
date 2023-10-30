#tkinter 임포트
import tkinter as tk

#기본창을 생성
root = tk.Tk()
root.title("practice first!")
#창 크기 조절
root.geometry("300x200")

#버튼 기능을 넣어보자!
def push():
    print("pushed!")

redBtn = tk.Button(root, text = "push here", command=push , bg = "red" , width=10 , height = 3)
redBtn.place(relx=0.5,rely=0.5,anchor="center")

#루프 실행
root.mainloop()