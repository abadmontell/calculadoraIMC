# Función para calcular el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Ciclo principal para calcular el IMC para una o más personas
calcular_otra_persona = True
while calcular_otra_persona:
      
    # Pedir al usuario que ingrese su nombre completo, edad, altura y peso y que sean guardados en variables
    nombre = ""
    while not nombre:
        try:
                nombre = input("Por favor, ingrese su nombre: ")
        except ValueError:
                print("Por favor, ingrese un nombre válido.")

    apellido_paterno = ""
    while not apellido_paterno:
        try:
                apellido_paterno = input(
                    "Por favor, ingrese su apellido paterno: ")
        except ValueError:
                print("Por favor, ingrese su apellido paterno:")

    apellido_materno = ""
    while not apellido_materno:
        try:
                apellido_materno = input(
                    "Por favor, ingrese su apellido materno: ")
        except ValueError:
                print("Por favor, ingrese su apellido materno:")

    edad = None
    while edad is None:
        try:
            edad = int(input("Por favor, ingrese su edad: "))
        except ValueError:
            print("Por favor, ingrese un número entero para su edad.")

    altura = None
    while altura is None:
        try:
            altura = float(input("Por favor, ingrese su altura en metros: "))
        except ValueError:
            print("Por favor, ingrese un número para su altura en metros.")
    peso = None
    while peso is None:
        try:
            peso = float(input("Por favor, ingrese su peso en kilogramos: "))
        except ValueError:
            print("Por favor, ingrese un número para su peso en kilogramos.")

    #Convertir las variables de texto a mayusculas
    nombre = nombre.upper()
    apellido_paterno = apellido_paterno.upper()
    apellido_materno = apellido_materno.upper()

    # Calcular el IMC utilizando la función 'calcular_imc'
    imc = calcular_imc(peso, altura)

    # Imprimir el resultado del IMC junto con un mensaje personalizado
    mensaje = "Hola " + nombre + " " + apellido_paterno + " " + \
        apellido_materno + ", su IMC es de " + str(round(imc, 2)) + "."


    if imc >= 0 and imc <= 15.99:
            mensaje += " Usted tiene delgadez severa"
    elif imc >= 16.00 and imc <= 16.99:
            mensaje += " Usted tiene delgadez moderada"
    elif imc >= 17.00 and imc <= 18.49:
            mensaje += " Usted tiene delgadez leve"
    elif imc >= 18.50 and imc <= 24.99 :
            mensaje += " Su peso está en el rango saludable."
    elif imc >= 25.00 and imc <= 29.99:
            mensaje += " Usted tiene sobrepeso."
    elif imc >= 30.00 and imc <= 34.99:
            mensaje += " Usted tiene obesidad leve."
    elif imc >= 35.00 and imc <= 39.99:
            mensaje += " Usted tiene obesidad media."
    elif imc >= 40.00:
            mensaje += " Usted tiene obesidad morbida."

    # Imprimir el mensaje personalizado
    print(mensaje)

    #Preguntar si el usuario desea calcular el IMC de otra persona
    respuesta = input("¿Desea calcular el IMC para otra persona? (Y/N): ").upper()
    while respuesta != "Y" and respuesta != "N":
        respuesta = input("Por favor, ingrese 'Y' si desea calcular el IMC para otra persona, o 'N' para salir: ").upper()
    if respuesta == "N":
        calcular_otra_persona = False
    else:
        calcular_otra_persona = True
