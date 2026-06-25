import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

def cr_label(row, text):
    frame = tk.Frame(root, bg=label_bg, relief=SOLID)
    frame.grid(row=row, column=0, sticky="nsew", padx=(8,0), pady=1)

    tk.Label(frame, text=text, font=font, bg=label_bg,
             width=22, anchor="nw", justify="left",
             wraplength=160, padx=6, pady=6).pack(fill="both",
                                                  expand=True)

def cr_cell(row):
    frame = tk.Frame(root, bg=cell_bg, relief=SOLID)
    frame.grid(row=row, column=1, sticky="nsew", padx=(0,8), pady=4, ipadx=4, ipady=4)

    return frame

def register():
    name = entry_name.get()
    password = entry_pass.get()
    password2 = entry_pass2.get()

    if not name:
        messagebox.showwarning("ошибка", "введите имя")
        return
    if password != password2:
        messagebox.showwarning("ошибка", "пароли не совпадают")
        return
    messagebox.showinfo("успкх",f"пользователь {name} зарегестрирован")

def clear():
    entry_name.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    entry_pass2.delete(0, tk.END)
    combo_p.current(0)
    g.set("М")
    for var in checkboxes:
        var.set(False)
    text_i.delete("1.0", tk.END)

bg = "#B8CEB7"
cell_bg = "#49B644"
label_bg = "#3070AC"
font = ("Arial", 9)
font_bold = ("Arial", 11, "bold")

root = Tk()
root.title("Анкета Разработчика")
root.resizable(False, False)
root.configure(bg=bg)

header = tk.Label(master=root, text="Анкета разраба",
              font=font_bold,
              bg=bg,
              anchor="w",
              padx=12,
              pady=6)
header.grid(row=0, column=0, columnspan=2, sticky="ew")

tk.Frame(root, bg="", height=1).grid(row=1, column=0, columnspan=2, sticky="ew")

root.columnconfigure(0, weight=0) #только 1
root.columnconfigure(1, weight=1) #все пространство себе

cr_label(2,"Рег имя")
cell= cr_cell(2)
entry_name = tk.Entry(cell, font=font, width=24)
entry_name.pack(anchor="w", padx=6, pady=4)

cr_label(3,"Пароль")
cell3 = cr_cell(3)

entry_pass = tk.Entry(cell3, font=font, width=24, show="*")
entry_pass.pack(anchor="w", padx=6, pady=(4,2))

frame = tk.Frame(cell3, bg=cell_bg)
frame.pack(anchor="w", padx=6, pady=(0,4))

entry_pass2 = tk.Entry(frame, font=font, width=24, show="*")
entry_pass2.pack(side="left")

tk.Label(frame, text=": подтвердите пароль", font=font, bg=cell_bg).pack(side="left", padx=4)

cr_label(4, "ваша специализация")
cell4 = cr_cell(4)
prof = ["веб мастер", "дизайдер", "фронтент", "trtyl hfphf"]

combo_p = ttk.Combobox(cell4, values=prof, state="readonly", font=font, width=24)
combo_p.current(0)
combo_p.pack(anchor="w", padx=6, pady=4)

cr_label(5,"Пол")
cell5 = cr_cell(5)
g = tk.StringVar(value="М")
g_f = tk.Frame(cell5, bg=cell_bg)
g_f.pack(anchor="w", padx=6, pady=4)

tk.Radiobutton(g_f, text="М", variable=g, value="М",
               font=font, bg=cell_bg).pack(side="left")
tk.Radiobutton(g_f, text="Ж", variable=g, value="Ж",
               font=font, bg=cell_bg).pack(side="left")

cr_label(6, "ваши навыки")
cell6 = cr_cell(6)

skills = ["штмлксс","перл","асп","адоп фотошоп","джава","джава скрипт","флеш"]

checkboxes = []

for skill in skills:
    var = tk.BooleanVar()
    checkboxes.append(var)
    tk.Checkbutton(cell6, text=skill, variable=var, font=font, bg=cell_bg).pack(anchor="w", padx=6)

cr_label(7, "доп \nсведения о себе")
cell7 = cr_cell(7)

text_f = tk.Frame(cell7,bg=cell_bg)
text_f.pack(fill="both", expand=True, padx=6, pady=4)

text_i = tk.Text(text_f, font=font, width=36, height=5)
scrolbar = tk.Scrollbar(text_f,command=text_i.yview)
text_i.configure(yscrollcommand=scrolbar.set)
text_i.pack(side="left",fill="both")
scrolbar.pack(side="left",fill="y")

tk.Frame(root, height=1).grid(row=8, column=0, columnspan=2, sticky="ew", pady=(4,0))

b_f = tk.Frame(root, bg=bg)
b_f.grid(row=9, column=0, columnspan=2, pady=8, sticky="w")

tk.Button(b_f, text="Зарегестрировать", command=register, font=font, width=18).pack(
    side="left")

tk.Button(b_f, text="очистить форму", command=clear, font=font, width=18).pack(
    side="left")

root.mainloop()
