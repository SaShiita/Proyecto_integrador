votos_registrados = {} 

def registrar_voto(nombre_votante, opcion):
    if nombre_votante in votos_registrados:
        print(f"Error: {nombre_votante} ya ha votado. No se permiten votos duplicados.")
    else:
        votos_registrados[nombre_votante] = opcion
        print(f"Voto de {nombre_votante} por '{opcion}' registrado exitosamente.")
    
def mostrar_ganador(votos):
    if not votos:
        print("\nAún no hay votos registrados.")
        return


    max_votos = max(votos.values())
    
    ganadores = [candidato for candidato, cantidad in votos.items() if cantidad == max_votos]

    print("\n--- RESULTADO DE LA VOTACIÓN ---")
    if len(ganadores) == 1:
        print(f" El ganador es: {ganadores[0]} con {max_votos} votos.")
    else:
        print(f" Hubo un empate entre: {', '.join(ganadores)} con {max_votos} votos cada uno.")