    def setvar():
            
        newlevel = Toplevel()
        newlevel.title("Configure Variables")
        newlevel.resizable(width=False, height=False)
        newlevel.configure(background="lightblue")
        
        top_frame = Frame(newlevel)
        top_frame.configure(background="lightblue")
        top_frame.pack()
        
        mid_frame = Frame(newlevel)
        mid_frame.configure(background="lightblue")
        mid_frame.pack()
        
        bottom_frame = Frame(newlevel)
        bottom_frame.configure(background="lightblue")
        bottom_frame.pack()
        
        text_1 = Label(top_frame, text='Configure each variable by typing in a new number in the box, and then clicking "Apply"...', wraplength=300, font=("Unispace", 8))
        text_1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        text_1.configure(background="lightblue")
        
        x_label = Label(mid_frame, text="x", font=("Unispace", 8))
        x_entry = Entry(mid_frame, width=20)
        x_label.grid(row=1, column=0, padx=5, pady=5)
        x_label.configure(background="lightblue")
        x_entry.grid(row=1, column=1, padx=5, pady=5)
        
        y_label = Label(mid_frame, text="y", font=("Unispace", 8))
        y_entry = Entry(mid_frame, width=20)
        y_label.grid(row=2, column=0, padx=5, pady=5)
        y_label.configure(background="lightblue")
        y_entry.grid(row=2, column=1, padx=5, pady=5)
        
        z_label = Label(mid_frame, text="z", font=("Unispace", 8))
        z_entry = Entry(mid_frame, width=20)
        z_label.grid(row=3, column=0, padx=5, pady=5)
        z_label.configure(background="lightblue")
        z_entry.grid(row=3, column=1, padx=5, pady=5)
        
        a_label = Label(mid_frame, text="a", font=("Unispace", 8))
        a_entry = Entry(mid_frame, width=20)
        a_label.grid(row=4, column=0, padx=5, pady=5)
        a_label.configure(background="lightblue")
        a_entry.grid(row=4, column=1, padx=5, pady=5)
        
        b_label = Label(mid_frame, text="b", font=("Unispace", 8))
        b_entry = Entry(mid_frame, width=20)
        b_label.grid(row=5, column=0, padx=5, pady=5)
        b_label.configure(background="lightblue")
        b_entry.grid(row=5, column=1, padx=5, pady=5)
        
        c_label = Label(mid_frame, text="c", font=("Unispace", 8))
        c_entry = Entry(mid_frame, width=20)
        c_label.grid(row=6, column=0, padx=5, pady=5)
        c_label.configure(background="lightblue")
        c_entry.grid(row=6, column=1, padx=5, pady=5)
        
        d_label = Label(mid_frame, text="d", font=("Unispace", 8))
        d_entry = Entry(mid_frame, width=20)
        d_label.grid(row=7, column=0, padx=5, pady=5)
        d_label.configure(background="lightblue")
        d_entry.grid(row=7, column=1, padx=5, pady=5)
        
        t_label = Label(mid_frame, text="t", font=("Unispace", 8))
        t_entry = Entry(mid_frame, width=20)
        t_label.grid(row=8, column=0, padx=5, pady=5)
        t_label.configure(background="lightblue")
        t_entry.grid(row=8, column=1, padx=5, pady=5)
        
        def apply(): #when called, the json file opens, edits the data, then closes.
            
            with open("settings/variables.json", "r") as f: #opens json file.
                var = json.load(f) 
                
            var["x"] = float(x_entry.get())
            var["y"] = float(y_entry.get())
            var["z"] = float(z_entry.get())
            var["a"] = float(a_entry.get())
            var["b"] = float(b_entry.get())
            var["c"] = float(c_entry.get())
            var["d"] = float(d_entry.get())
            var["t"] = float(t_entry.get())
            
            with open("settings/variables.json", "w"): #overwrites and closes file.
                json.dump(var, f, indent=4)
            
        def exit():
            newlevel.destroy()
        
        apply_button = Button(bottom_frame, text="Apply", font=("Unispace", 8), width=9, height=2, command=apply)
        apply_button.grid(row=0, column=0, padx=5, pady=5)
        exit_button = Button(bottom_frame, text="Exit", font=("Unispace", 8), width=9, height=2, command=exit)
        exit_button.grid(row=0, column=1, padx=5, pady=5)
