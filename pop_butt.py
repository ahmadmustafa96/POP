import tkinter as tk
from pop_func import pop_func

root = tk.Tk()
root.geometry("120x50")
#root.geometry("300x300")

'''text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)'''

btn_pop = tk.Button(root, text="POP!!!", command=lambda: pop_func(), width=10, font=("Arial, 14"))
btn_pop.grid()

root.mainloop()