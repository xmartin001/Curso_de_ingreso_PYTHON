import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Martin Lionel
apellido:Escalante
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #con el prompt se interactua con la persona que esta detras de la pantalla
        resultado = prompt(title = "prompt",prompt ="ingrese su nombre")
        alert(title = "ejercicio 2",message= resultado)
        #el mensaje tiene que ser entendible para el usuario
        #pass
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()