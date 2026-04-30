import os
os.system("cls")

plan_dental = 80000
radiografia_dental = 12000
edad = 0
quintil = 0
descuento_radiografia = 0.0

while True:
    try:
        while edad <= 0:
            edad = int(input("ingrese la edad: "))
        while quintil not in [1,2,3,4,5]:
            quintil = int(input("ingrese el quintil que pertenece (1-5): "))
        #plan
        if edad <= 25:
            if quintil == 1 or quintil == 2:
                valor_plan = plan_dental * (1 - 0.18)
            elif quintil == 3 or quintil == 4:
                valor_plan = plan_dental * (1 - 0.12)
            else:
                valor_plan = plan_dental
        elif 26 <= edad <= 45:
            if quintil == 1 or quintil == 2:
                valor_plan = plan_dental * (1 - 0.12)
            elif quintil == 3 or quintil == 4:
                valor_plan = plan_dental * (1 - 0.08)
            else:
                valor_plan = plan_dental
        else:
            valor_plan = plan_dental
        #radiografia
        if quintil in [1,2,3]:
            descuento_radiografia += 0.1
        else:
            descuento_radiografia += 0
        if edad >= 40:
            descuento_radiografia += 0.05
        else:
            descuento_radiografia += 0
            
        valor_radiografia = radiografia_dental - (radiografia_dental * descuento_radiografia)
        print("--resumen--")
        print(f"Ingrese edad: {edad}")
        print(f"Ingrese quintil (1 a 5): {quintil}")
        print(f"El valor del plan es: {valor_plan}")
        print(f"El valor de la radiografía es: {valor_radiografia}")
        break
    except:
        print("Valores no validos, intente denuevo")