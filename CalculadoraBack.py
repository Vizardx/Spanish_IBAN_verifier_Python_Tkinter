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

codigo_pais = 'ES'  # Código del país para España
codigos_banco = ['0049', '2100', '2100', '0182', '2100', '3005', '1465', '1465', '3058', '1465', '2100', '0049', '0081', '0049', '3058', '2100', '0128', '0049', '1465', '3183', '2100', '0081', '2100', '3058']
codigos_oficina = ['4361', '2310', '8258', '7402', '3958', '0011', '0100', '0100', '0290', '0100', '3864', '4612', '7362', '6816', '0277', '4456', '0650', '2450', '0100', '3000', '6007', '1498', '7838', '0236']
digitos_control = ['77', '85', '08', '52', '79', '60', '97', '91', '71', '91', '27', '60', '11', '52', '49', '14', '14', '54', '91', '44', '93', '36', '63', '08']
numeros_cuenta = ['x']

for i in range(len(codigos_banco)):
    iban = calcular_iban(codigo_pais, codigos_banco[i], codigos_oficina[i], digitos_control[i], numeros_cuenta[i])
    print(iban)
