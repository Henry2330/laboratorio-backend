def evaluar_tc_cliente(edad, ingresos):
    # Edad on ingresos no suficientes
    if edad < 18 or ingresos < 1000:
        return {"califica": False, "categoria": None, "linea":0}
    
    # Premiun: ingresos altos y edad mayor/igual a 25
    if ingresos >= 5000 and edad >=25:
        return {"califica": True, "categoria": "Tarjeta OH Premium", "linea":10000}
    
    # Defecto
    return {"califica": True, "categoria": "Tarjeta OH", "linea":2000}

print(evaluar_tc_cliente(16, 2000))