import sys
import calculos
import texto
import chatbot

API_KEY = "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"

def mostrar_menu():
    print("\nSoy Ari, tu asistente de AI. ¿En qué puedo ayudarte?")
    print("1. Cálculos matemáticos")
    print("2. Manipulación de texto")
    print("3. Preguntas con IA")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            expresion = input("Ingrese una expresión matemática sumar, restar, multiplicar, dividir: ")
            calculos.realizar_calculo(expresion)
        elif opcion == "2":
            texto_usuario = input("Ingrese un texto: ")
            texto.manipular_texto(texto_usuario)
        elif opcion == "3":
            pregunta = input("Ingrese su pregunta: ")
            chatbot.preguntar_ia(pregunta, API_KEY)
        elif opcion == "4":
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
