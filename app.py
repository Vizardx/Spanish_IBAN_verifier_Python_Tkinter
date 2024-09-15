import tkinter as tk
from tkinter import messagebox

def calcular_iban(codigo_pais, codigo_banco, codigo_oficina, codigo_control, numero_cuenta):
    # Convertir letras a números (A=10, B=11, ..., Z=35)
    codigo_pais_numerico = str(ord(codigo_pais[0]) - 55) + str(ord(codigo_pais[1]) - 55)

    # Concatenar el código del banco, el código de la oficina, el código de control y el número de cuenta
    iban_temporal = codigo_banco + codigo_oficina + codigo_control + numero_cuenta + codigo_pais_numerico + '00'

    # Calcular el módulo 97
    modulo = int(iban_temporal) % 97

    # Calcular los dígitos de control
    digitos_control = 98 - modulo

    # Asegurarse de que los dígitos de control son dos dígitos
    if digitos_control < 10:
        digitos_control = '0' + str(digitos_control)
    else:
        digitos_control = str(digitos_control)

    # Crear el IBAN
    iban = codigo_pais + digitos_control + codigo_banco + codigo_oficina + codigo_control + numero_cuenta

    return iban

def calcular():
    codigo_pais = entry_codigo_pais.get()
    codigo_banco = entry_codigo_banco.get()
    codigo_oficina = entry_codigo_oficina.get()
    codigo_control = entry_codigo_control.get()
    numero_cuenta = entry_numero_cuenta.get()

    iban = calcular_iban(codigo_pais, codigo_banco, codigo_oficina, codigo_control, numero_cuenta)

    messagebox.showinfo("IBAN", "El IBAN es " + iban)

root = tk.Tk()

label_codigo_pais = tk.Label(root, text="Código del país:")
label_codigo_pais.pack()

entry_codigo_pais = tk.Entry(root)
entry_codigo_pais.pack()

label_codigo_banco = tk.Label(root, text="Código del banco:")
label_codigo_banco.pack()

entry_codigo_banco = tk.Entry(root)
entry_codigo_banco.pack()

label_codigo_oficina = tk.Label(root, text="Código de la oficina:")
label_codigo_oficina.pack()

entry_codigo_oficina = tk.Entry(root)
entry_codigo_oficina.pack()

label_codigo_control = tk.Label(root, text="Código de control:")
label_codigo_control.pack()

entry_codigo_control = tk.Entry(root)
entry_codigo_control.pack()

label_numero_cuenta = tk.Label(root, text="Número de cuenta:")
label_numero_cuenta.pack()

entry_numero_cuenta = tk.Entry(root)
entry_numero_cuenta.pack()

button_calcular = tk.Button(root, text="Calcular IBAN", command=calcular)
button_calcular.pack()

root.mainloop()
