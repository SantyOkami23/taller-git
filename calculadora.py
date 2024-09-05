# calculadora.py
from operaciones import Operaciones

class Calculadora:
    def __init__(self):
        self.operaciones = Operaciones()

    def mostrar_menu(self):
        print("=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "5":
                print("Saliendo de la calculadora...")
                break

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                resultado = self.operaciones.sumar(num1, num2)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == "2":
                resultado = self.operaciones.restar(num1, num2)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == "3":
                resultado = self.operaciones.multiplicar(num1, num2)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == "4":
                resultado = self.operaciones.dividir(num1, num2)
                print(f"Resultado de la división: {resultado}")
            else:
                print("Opción inválida, intente nuevamente.")
