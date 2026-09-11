votos_registrados = {} 

def registrar_voto(nombre_votante, opcion):
    if nombre_votante in votos_registrados:
        print(f"Error: {nombre_votante} ya ha votado. No se permiten votos duplicados.")
    else:
        votos_registrados[nombre_votante] = opcion
        print(f"Voto de {nombre_votante} por '{opcion}' registrado exitosamente.")