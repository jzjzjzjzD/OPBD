import tkinter as tk
from tkinter import messagebox
import time


class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Таймер бера")

        self.minutes = 0
        self.seconds = 0
        self.is_running = False

        self.create_widgets()

    def create_widgets(self):
        self.minutes_label = tk.Label(self.root, text="Минуты:")
        self.minutes_label.pack()

        self.minutes_entry = tk.Entry(self.root)
        self.minutes_entry.pack()

        self.seconds_label = tk.Label(self.root, text="Секунды:")
        self.seconds_label.pack()

        self.seconds_entry = tk.Entry(self.root)
        self.seconds_entry.pack()

        self.start_button = tk.Button(self.root, text="Старт", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Стоп", command=self.stop_timer)
        self.stop_button.pack()

        self.timer_label = tk.Label(self.root, text="")
        self.timer_label.pack()

    def start_timer(self):
        if not self.is_running:
            try:
                self.minutes = int(self.minutes_entry.get())
                self.seconds = int(self.seconds_entry.get())

                total_seconds = self.minutes * 60 + self.seconds

                while total_seconds:
                    mins, secs = divmod(total_seconds, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    self.timer_label.config(text=timeformat)
                    self.root.update()

                    time.sleep(1)
                    total_seconds -= 1

                messagebox.showinfo("Таймер", "Время истекло!")

            except ValueError:
                messagebox.showwarning("Ошибка", "Пожалуйста, введите корректное время!")

        self.is_running = False

    def stop_timer(self):
        self.is_running = False


root = tk.Tk()
timer = Timer(root)
root.mainloop()