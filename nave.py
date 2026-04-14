for productos in range(1, 9):
    respuesta = input(f"El producto {productos} esta vencido? si/no: ").lower()
    
    if respuesta == "si":
        print("Alerta!! Retirar producto")
        break  # Se detiene solo si hay un vencido
else: 
    # Este bloque solo se ejecuta si el ciclo termina sin encontrar un 'break'
    print("Todo en orden")