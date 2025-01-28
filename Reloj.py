print("""Introduce la funcion que desees usar:
      1 - Reloj (Indica la hora actual
      2 - Alamarma (Te notificara cuando haya transcurrido cierto tiempo)
      3 - Cronometro (Mide el tiempo transcurrido)
      4 - Temporizador (Te notificara cuando haya trnascurrido cieto tiempo y se detendra)
      5 - Salir """)

while True:
    function = input("> ")
    if function == "1":
        from datetime import datetime
        print(datetime.now().time())
    elif function == "2":
        from datetime import datetime
        import time
        print("Introduce el tiempo en segundos")
        tiempo = int(input("> "))
        time.sleep(tiempo)
        print("Alarma")
    elif function == "3":
        from datetime import datetime
        import time 
        print("Presiona enter para iniciar el tiempo")
        input("*Enter*")
        inicio = datetime.now()
        print("Presiona enter para detener el tiempo")
        input("*Enter*")
        final = datetime.now()
        print(final - inicio)
    elif function == "4":
        print("Salir")
        break
