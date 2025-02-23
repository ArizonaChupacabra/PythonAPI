import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import ConfigWidgets


class App(tk.Tk, ConfigWidgets):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title("CPU-RAM-Monitor")
        self.cpu = CpuBar()
        self.run_set_ui()

    def run_set_ui(self):
        self.set_ui()
        self.make_bar_cpu_usage()
        self.config_cpu_bar()

    def set_ui(self):
        exit_butt = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_butt.pack(fill=tk.X)

        self.bar2 = ttk.LabelFrame(self, text="Manual")
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2,
                                      values=["hide", "show", "min"],
                                      width=5, state="readonly")
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text='move', command=self.config_win).pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text="Power")
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.combo_win.bind('<<ComboboxSelected>>', self.choice_combo)

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text=f"physical cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logical}",
                  anchor=tk.CENTER).pack(fill=tk.X)

        self.list_label = []
        self.list_pbar = []

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100))

        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry("")

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f"{self.winfo_width()}x1")

    def make_min_win(self):
        self.bar_one = ttk.Progressbar(self, length=100)
        self.bar_one.pack(side=tk.LEFT)

        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        ttk.Button(self, text="full", command=self.make_full_win, width=5).pack(side=tk.RIGHT)
        ttk.Button(self, text="move", command=self.config_win, width=5).pack(side=tk.RIGHT)

        self.update()
        self.config_min_win()

    def choice_combo(self, event):
        if self.combo_win.current() == 2:
            self.enter_mouse('')
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.combo_win.unbind('<<ComboboxSelected>>')
            self.after_cancel(self.wheel)
            self.clear_win()
            self.update()
            self.make_min_win()

    def make_full_win(self):
        self.after_cancel(self.wheel)
        self.clear_win()
        self.update()
        self.run_set_ui()
        self.enter_mouse('')
        self.combo_win.current(1)

    def app_exit(self):
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = App()
    root.mainloop()



