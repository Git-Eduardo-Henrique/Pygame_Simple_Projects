import tkinter as tk

print(f"Modulo iniciado: {__name__}")

class Windows:
    def __init__(self):
        pass

    def choose_name_window():
        def save_name():
            global name
            name = entry_name.get().upper()
            name_window.destroy()
        
        name_window = tk.Tk()
        name_window.title("Pytale.py")
        name_window.geometry("250x100")

        tk.Label(name_window, text="Name the fallen human:").pack(pady=5)

        entry_name = tk.Entry(name_window)
        entry_name.pack(pady=5)
        done_button = tk.Button(name_window, text="Done", command=save_name)
        done_button.pack(pady=5)

        name_window.mainloop()

        return name
    
