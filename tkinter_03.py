#tkinter 임포트
import tkinter as tk
#psutil을 사용하여 cpu와 ram의 사용량을 가져오기
import psutil

#기본창을 생성
root = tk.Tk()
root.title("practice first!")

#창 크기 조절
root.geometry("300x200")

#CPU와 RAM의 사용량을 가져오는 함수
def get_view():
    cpu_view = psutil.cpu_percent()
    ram_info = psutil.virtual_memory()
    ram_view = ram_info.percent
    return cpu_view,ram_view

#업데이트 기능을 넣어보자!
def update():
    cpu_view,ram_view = get_view()
    cpu_label.config(text=f"CPU : {cpu_view}%")
    ram_label.config(text=f"RAM : {ram_view}%")
    
    root.after(1000,update)


#CUP&RAM 사용량 라벨 생성
cpu_label = tk.Label(root,text="CPU : %")
cpu_label.pack(pady=10)

ram_label = tk.Label(root,text="RAM : %")
ram_label.pack(pady=10)

update()

#루프 실행
root.mainloop()