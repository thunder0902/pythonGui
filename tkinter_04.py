#tkinter 임포트
import tkinter as tk
from tkinter import ttk
#psutil을 사용하여 cpu와 ram의 사용량을 가져오기
import psutil
from tkinter import font


#기본창을 생성
root = tk.Tk()
root.overrideredirect(1)
root.configure(bg="black")
root.title("practice first!")
# 화면의 너비와 높이를 얻습니다.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 창의 위치를 계산합니다.
x_position = screen_width - 300  # 창의 너비
y_position = screen_height - 200  # 창의 높이

# 창의 위치와 크기를 설정합니다.
root.geometry(f"{300}x{200}+{x_position}+{y_position}")

#창 크기 조절
root.geometry("300x150")

#frame을 생성 (디자인)
frame = tk.Frame(root,bg="black",padx=10,pady=10)
frame.pack(padx=10,pady=10,fill=tk.BOTH, expand=True)


#CPU와 RAM의 사용량을 가져오는 함수
def get_view():
    cpu_view = psutil.cpu_percent()
    ram_info = psutil.virtual_memory()
    ram_view = ram_info.percent
    return cpu_view,ram_view

#progress style
style = ttk.Style()
style.layout('custom.myBar',
             [('myBar.trough',
               {'children': [('myBar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}),
              ('myBar.label', {'sticky': ''})])
style.configure('custom.myBar',
                thickness=10,
                background='orange',
                troughcolor='gray', 
                troughrelief='ridge',
                relief='raised',
                bordercolor='white',
                lightcolor='white',
                darkcolor='gray'
               )
available_fonts = font.families()

for f in available_fonts:
    print(f)
#CUP&RAM 사용량 라벨 생성 함수
def create_label_bar(parent,text):
    label = tk.Label(parent, font=("SF Pro Regular", 10), fg="white" , text=text, bg="black", anchor="w")

    label.pack(fill=tk.X)
    progress = ttk.Progressbar(parent, style='custom.myBar', orient=tk.HORIZONTAL, length=100, mode='determinate', maximum=100)
    progress.pack(fill=tk.X, pady=5)
    return label, progress

#CPU & RAM 사용량 라벨&바 생성
cpu_label,cpu_bar = create_label_bar(frame,"cpu : ")
ram_label,ram_bar = create_label_bar(frame,"ram : ")


#업데이트 기능을 넣어보자!
def update():
    cpu_view,ram_view = get_view()
    cpu_label.config(text=f"CPU : {cpu_view}%")
    ram_label.config(text=f"RAM : {ram_view}%")

    cpu_bar["value"] = cpu_view
    ram_bar["value"] = ram_view

    root.after(1000,update)


update()
#루프 실행
root.mainloop()