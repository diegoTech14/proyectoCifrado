from tkinter import *
from tkinter import messagebox 
from funcionalidad import CifradoCesar


def mensaje_error(mensaje):
        messagebox.showerror('Error', mensaje)

def salida():

        respuesta_salida = messagebox.askokcancel(
                "Mensaje de salida",
                "¿Desea salir del programa?"
        )

        if respuesta_salida:
                ventana.destroy()

def limpiar():
    
    app.texto_cifrado_entry.delete(0, 'end')
    app.texto_descifrado_entry.delete(0, 'end')
    app.texto_original_entry.delete(0, 'end')
    
    
    
def mostrar_texto_original(cifrado):
        app.texto_original_entry.delete(0, END)
        app.texto_original.set(cifrado.texto_original)
    
def llamado_de_encriptado(nombre, desplazamiento):
        
        
        
        if int(desplazamiento.get()) > 25 or int(desplazamiento.get()) < 0:
                mensaje_error("Número de desplazamiento fuera del rango 0-26")
        else:   
                
                cifrado = CifradoCesar(nombre.get(), int(desplazamiento.get()))
                
                if cifrado.mensaje_estado_archivo != "":
                        mensaje_error(cifrado.mensaje_estado_archivo)
        
                mostrar_texto_original(cifrado)
                cifrado.encriptado()
                app.texto_cifrado.set(cifrado.mensaje_encriptado)
                
def llamado_de_desencriptado(nombre, desplazamiento):
        
        cifrado = CifradoCesar(nombre.get(), int(desplazamiento.get()))
        CifradoCesar.mensaje_encriptado = app.texto_cifrado_entry.get()
        
        if CifradoCesar.mensaje_encriptado:
                cifrado.desencriptado()
                app.texto_descifrado_entry.delete(0, END)
                app.texto_descifrado.set(cifrado.mensaje_desencriptado)
        else:
                mensaje_error("No hay mensaje encriptado")

class cifradoInterfaz:

        def __init__(self, ventana):

                self.ventana = ventana
                self.ventana.title("Cifrado y Decifrado Cesar")
                self.ventana.config(bg="#8A33FF")
                self.ventana.geometry('765x430')
                

                self.frame_uno = Frame(self.ventana)
                self.frame_uno.grid(row=0, column=0, padx=40)
                self.frame_uno.config(bg="#8A33FF")
                
                self.label_desplazamiento = Label(self.frame_uno, text="Desplazamiento: ")
                self.label_desplazamiento.grid(row=0, column=0, pady=25, sticky=W)
                self.label_desplazamiento.config(fg="white", bg="#8A33FF", font=('calibri', 13))

                self.numero_desplazamiento = Entry(self.frame_uno, width=5)
                self.numero_desplazamiento.grid(row=0, column=1, padx=5, sticky=W)

                self.archivo = Label(self.frame_uno, text="Nombre del archivo: ")
                self.archivo.grid(row=1, column=0)
                self.archivo.config(fg="white", bg="#8A33FF", font=('calibri', 13))

                self.nombre_del_archivo = Entry(self.frame_uno, width=40)
                self.nombre_del_archivo.grid(row=1, column=1, padx=5)



                self.frame_dos = Frame(self.ventana)
                self.frame_dos.grid(row=1, column=0)
                self.frame_dos.config(bg="#8A33FF")

                self.texto_original_label = Label(self.frame_dos, text="Texto original: ")
                self.texto_original_label.grid(row=0, column=0, pady=25, sticky=W)
                self.texto_original_label.config(fg="white", bg="#8A33FF", font=('calibri', 13))

                self.texto_original = StringVar()
                self.texto_original_entry = Entry(self.frame_dos, width=40, textvariable=self.texto_original)
                self.texto_original_entry.grid(row=1, column=0, padx=5)
                self.texto_original_entry.config(fg="white", bg="#8A33FF")

                self.texto_cifrado_label = Label(self.frame_dos, text="Texto cifrado: ")
                self.texto_cifrado_label.grid(row=2, column=0, pady=25, sticky=W)
                self.texto_cifrado_label.config(fg="white", bg="#8A33FF", font=('calibri', 13))
                

                self.texto_cifrado = StringVar()
                self.texto_cifrado_entry = Entry(self.frame_dos, width=40, textvariable=self.texto_cifrado)
                self.texto_cifrado_entry.grid(row=3, column=0, padx=6)
                self.texto_cifrado_entry.config(fg="white", bg="#8A33FF")

                self.texto_descifrado_label = Label(self.frame_dos, text="Texto descifrado: ")
                self.texto_descifrado_label.grid(row=4, column=0, pady=25, sticky=W)
                self.texto_descifrado_label.config(fg="white", bg="#8A33FF", font=('calibri', 13))
                

                self.texto_descifrado = StringVar()
                self.texto_descifrado_entry = Entry(self.frame_dos, width=40, textvariable=self.texto_descifrado)
                self.texto_descifrado_entry.grid(row=5, column=0, padx=6)
                self.texto_descifrado_entry.config(fg="white", bg="#8A33FF")


                self.frame_tres = Frame(self.ventana)
                self.frame_tres.grid(row=1, column=1, padx=80)
                self.frame_tres.config(pady=30, bg="#8A33FF")

                self.boton_cifrar = Button(self.frame_tres, text="Cifrar", command=lambda:llamado_de_encriptado(
                        self.nombre_del_archivo, 
                        self.numero_desplazamiento
                                )
                )
                self.boton_cifrar.config(bg="#6119F1", foreground="white", font=('calibri', 13))
                self.boton_cifrar.grid(padx=6, row=0, column=0, ipadx=32, sticky=E)

                self.boton_descifrar = Button(self.frame_tres, text="Descifrar", command=lambda:llamado_de_desencriptado(
                        self.nombre_del_archivo, 
                        self.numero_desplazamiento
                                )
                )
                self.boton_descifrar.config(bg="#F9906B", foreground="white", font=('calibri', 13))
                self.boton_descifrar.grid(padx=6, row=1, column=0, ipadx=20, pady=10, sticky=E)

                self.boton_cerrar = Button(self.frame_tres, text="Cerrar", command=lambda:salida())
                self.boton_cerrar.grid(padx=6, row=2, column=0, ipadx=29, sticky=E)
                self.boton_cerrar.config(bg="#F1CA19", foreground="white", font=('calibri', 13))
                
                
                self.boton_limpiar = Button(self.frame_tres, text="Limpiar", command=lambda:limpiar())
                self.boton_limpiar.grid(padx=6, row=3, column=0, ipadx=25, pady=10, sticky=E)
                self.boton_limpiar.config(bg="#6BF978", foreground="white", font=('calibri', 13))
                
                
if __name__ == '__main__':
        ventana = Tk()
        app = cifradoInterfaz(ventana)
        ventana.mainloop()


# que solo se vea una vez reflejado el mensaje_encriptado
# limpiar las pantallas