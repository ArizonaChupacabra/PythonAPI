class ConfigWidgets:
    def config_cpu_bar(self):
        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f"core {i+1} usage: {r[i]}%")
            self.list_pbar[i].configure(value=r[i])

        r2 = self.cpu.ram_return()
        self.ram_lab.configure(text=f"RAM usage: {r2[2]}%, used {round(r2[3]/1048576)} Mb,\
            \n available: {round(r2[1]/1048576)} Mb")
        self.ram_bar.configure(value=r2[2])


        self.wheel = self.after(1000, self.config_cpu_bar)

    def config_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def config_min_win(self):
        self.bar_one.configure(value=self.cpu.cpu_one_return())
        self.ram_bar.configure(value=self.cpu.ram_return()[2])
        self.wheel = self.after(1000, self.config_min_win)



    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()
