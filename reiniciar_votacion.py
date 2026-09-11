import json

def reiniciar_votacion(votos):
    if len(votos) > 0:
        # Guarda el historial en un archivo agregando una nueva línea
        with open("historial_votacion.txt", "a") as archivo:
            archivo.write(json.dumps(votos) + "\n")
        votos.clear()
        print("Votación reiniciada. El historial se ha guardado en 'historial_votacion.txt'.")
    else:
        print("No hay votos para reiniciar.")   
        #
