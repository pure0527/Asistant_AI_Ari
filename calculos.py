def realizar_calculo(expresion):
    try:
        resultado = eval(expresion)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Error en el cálculo, expresión inválida")