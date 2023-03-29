import tkinter as tk
#importar alguna libreria para la conexion a la base de datos o con funciones para el login

class Aplicacion(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        master.title("Login")
        master.geometry("800x600")
        self.master = master
        self.pack()
        
        self.crear_widgets()
        
    
    def crear_widgets(self):
        
        #Aca iria el label del usuario
        self.label = tk.Label(self, text="Usuario", font=("Helvetica", 16), width=20)
        self.label.pack(side="top")

        #Esto seria el input del usuario
        self.input_usuario = tk.Entry(self, font=("Helvetica", 16), width=20)
        self.input_usuario.pack(side="top")

        #Aca iria el label de la contraseña
        self.label = tk.Label(self, text="Contraseña",  font=("Helvetica", 16), width=20)
        self.label.pack(side="top")

        #Esto seria el input de la contraseña
        self.input_password = tk.Entry(self, font=("Helvetica", 16), width=20) 
        self.input_password.pack(side="top")
        
        #Aca iria el boton de login
        #Comando para que al presionar el boton se ejecute la funcion x
        self.login = tk.Button(self, text="Login", fg="green", command=self.ingresar)
        self.login.pack(side="bottom", fill="x", expand=True)
               

    def crear_input(self, text, side, width):
        self.input = tk.Entry(self, text=text, width=width)
        self.input.pack(side=side)

    def crear_boton(self, text, side, width):
        self.boton = tk.Button(self, text=text, width=width)
        self.boton.pack(side=side)

    def ingresar(self):
        print("Usuario: ", self.input_usuario.get())
        print("Password: ", self.input_password.get())

root = tk.Tk()
app = Aplicacion(master=root)
app.mainloop()