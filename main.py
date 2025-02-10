import sys

def mostrar_menu():
    print("\nSoy Ari, tu asistente de AI")
    print("\n¿En qué puedo ayudarte hoy?")
    print("1. Cálculos matemáticos")
    print("2. Manipulación de texto")
    print("3. Realizar pregutas")
    print("4. Salir")

def realizar_calculo():
    try:
        expresion = input("Ingrese una expresión matemática (ej. 2 + 2): ")
        resultado = eval(expresion)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Error en el cálculo: {e}")

