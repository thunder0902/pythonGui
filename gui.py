import psutil
import tkinter as tk
from tkinter import ttk

def update_values():
    # CPU 사용률
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_label_var.set(f"CPU 사용률: {cpu_percent}%")

    # 사용 가능한 RAM
    available_memory = psutil.virtual_memory().available / (1024 ** 3)
    total_memory = psutil.virtual_memory().total / (1024 ** 3)
    ram_label_var.set(f"RAM 사용 가능: {available_memory:.2f} GB / {total_memory:.2f} GB")

    root.after(1000, update_values)

# GUI 설정
root = tk.Tk()
root.title("시스템 모니터")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

cpu_label_var = tk.StringVar()
cpu_label = ttk.Label(frame, textvariable=cpu_label_var)
cpu_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)

ram_label_var = tk.StringVar()
ram_label = ttk.Label(frame, textvariable=ram_label_var)
ram_label.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)

root.after(1000, update_values)
root.mainloop()
