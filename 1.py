    tkinter.Label(window, text='Intrument name', height=2).pack()
    def get_instr_name(*args):
        print(comboxlist_3.get())
    comvalue_3 = tkinter.StringVar()
    comboxlist_3 = ttk.Combobox(window, textvariable=comvalue_3)
    instr_list =['keithley','SR830','hp34461A','PicoVNA108','vna']
    comboxlist_3['values'] = tuple(instr_list)
    comboxlist_3.current(0)
    comboxlist_3.bind("<<ComboboxSelected>>",get_instr_name)
    comboxlist_3.pack()