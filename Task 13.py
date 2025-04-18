import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Test App")
        self.root.geometry("360x320")
        self.child_windows = []

        self.main_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.main_frame.pack(padx=20, pady=20)

        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        self.btn_up = tk.Button(self.button_frame, text="Увеличить", command=self.click_up, bg="#008000", fg="black",
                                padx=10, pady=5)
        self.btn_up.pack(side=tk.LEFT, padx=5)

        self.btn_down = tk.Button(self.button_frame, text="Уменьшить", command=self.click_down, bg="red",
                                  fg="black", padx=10, pady=5)
        self.btn_down.pack(side=tk.LEFT, padx=5)

        self.value = 0
        self.label = tk.Label(self.main_frame, text=str(self.value), font=("Arial", 24, "bold"), fg="blue",
                              bg="#f0f0f0")
        self.label.pack(pady=10)

        self.text_frame = tk.Frame(self.main_frame)
        self.text_frame.pack(pady=10)
        self.display_label = tk.Label(self.text_frame, text="Введите текст", font=("Arial", 12))
        self.display_label.pack()
        self.text_entry = tk.Entry(self.text_frame, width=30, font=("Arial", 12))
        self.text_entry.pack(pady=5)
        self.text_entry.bind("<Return>", self.update_label)

        self.size_frame = tk.Frame(root)
        self.size_frame.pack()
        sizes = [("Маленький", 280, 320), ("Средний", 360, 320), ("Большой", 440, 320)]
        for text, width, height in sizes:
            btn = tk.Button(self.size_frame, text=text, command=lambda w=width, h=height: self.resize_frame(w, h))
            btn.pack(side=tk.LEFT, padx=5)

        self.window_btn = tk.Button(root, text="Открыть окна", command=self.create_child_windows)
        self.window_btn.pack(pady=10)


    def click_up(self):
        try:
            increment = int(self.entry.get())
        except:
            increment = 1
        self.value += increment
        self.label.config(text=str(self.value))


    def click_down(self):
        try:
            decrement = int(self.entry.get())
        except:
            decrement = 1
        self.value -= decrement
        self.label.config(text=str(self.value))


    def update_label(self, event):
        self.display_label.config(text=self.text_entry.get())
        self.text_entry.delete(0, tk.END)


    def resize_frame(self, width, height):
        self.root.geometry(f"{width}x{height}")


    def create_child_windows(self):
        child1 = tk.Toplevel(self.root)
        child1.title("Окно 1")
        tk.Label(child1, text="Дочернее окно 1", bg="lightyellow").pack(pady=15)
        tk.Button(child1, text="Кнопка 1", command=lambda: print("Нажата кнопка 1")).pack()

        child2 = tk.Toplevel(self.root)
        child2.title("Окно 2")
        tk.Label(child2, text="Дочернее окно 2", bg="lightgreen").pack(pady=15)
        tk.Entry(child2).pack()
        tk.Button(child2, text="Кнопка 2", command=lambda: print("Нажата кнопка 2")).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()