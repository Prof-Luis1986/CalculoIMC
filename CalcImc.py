import tkinter as tk
from tkinter import messagebox

def calcular_IMC():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    masa = peso / altura**2
    lblResultado.config(text=f"El IMC es: {masa}")

    if masa < 18.5:
        messagebox.showinfo("Estado de Peso", "Actualmente estás bajo de peso")
    elif 18.5 <= masa <= 24.9:
        messagebox.showinfo("Estado de Peso", "Tu peso es normal")
    elif 25.0 <= masa <= 30:
        messagebox.showinfo("Estado de Peso", "Tienes sobrepeso, debes cuidarte")
    else:
        messagebox.showinfo("Estado de Peso", "Tienes obesidad, consulta a tu médico")

ventana = tk.Tk()
ventana.title("Calculo del IMC")
ventana.geometry("550x450") 
ventana.resizable(False, False)
ventana.configure(bg="#6C6206")

lblPeso = tk.Label(ventana, text="Peso (kg):", bg="#6C6206", fg="white")
lblPeso.pack(pady=5)

txtPeso = tk.Entry(ventana)
txtPeso.pack(pady=10)

lblAltura = tk.Label(ventana, text="Altura (m):", bg="#6C6206", fg="white")
lblAltura.pack(pady=5)

txtAltura = tk.Entry(ventana)
txtAltura.pack(pady=10)

lblResultado = tk.Label(ventana, text="Tu IMC es: ", bg="#6C6206")
lblResultado.pack(pady=10)

btnCalcular = tk.Button(ventana, text="Calcular", command=calcular_IMC, bg="#6C6206")
btnCalcular.pack(pady=10)

def borrar():
     txtPeso.delete(0,"end")
     txtAltura.delete(0,"end")

btnLimpiar=tk.Button(ventana,text="Limpiar",command=borrar)
btnLimpiar.pack(pady=10)

def salir():
    ventana.destroy()

btnSalir=tk.Button(ventana,text="Salir",command=salir)
btnSalir.pack(pady=10)


    

ventana.mainloop()
