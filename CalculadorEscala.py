#Universidad del Valle de Guatemala
#Juan Guillermo Sandoval Lacayo - 17577

#Para calcular la calidad de los acordes se hace lo siguiente
#1Tono + 1/2 Tono = Menor
#2Tonos = Mayor
#2Mayores = Aumentado
#2Menores = Disminuido
#Si tengo un menor y un mayor el primero manda 

#Do Mi Sol - Do Mayor
#Re Fa La - Re Menor
#Mi Sol Si - Mi Menor
#Fa La Do - Fa Mayor
#Sol Si Re - Sol Mayor
#La Do Mi - La Menor
#Si Re Fa - Si disminuido
notasFull = ['Ab','A','A#','Bb','B','C','C#','Db','D','D#','Eb','E','F','F#','Gb','G','G#']
notasHalfFull = ['Ab','A','Bb','B','C','Db','D','Eb','E','F','Gb','G']
notas = ['A','B','C','D','E','F','G']
calidad = ['Mayor', 'Menor', 'Aumentado', 'Disminuido']

def calcularEscala(nota):
    if(nota in notasFull and not nota in notasHalfFull):
        nuevaNota = notasHalfFull[(notasFull.index(nota)+1)%len(notasFull)]
        nextNoteIndex = notasHalfFull.index(nuevaNota)
    else:
        nextNoteIndex = notasHalfFull.index(nota)
    scale = []
    scale.append(nota)
    for i in range(1,7):
        if (i == 3 or i == 7):
            nextNoteIndex += 1
            nextNote = notasHalfFull[nextNoteIndex%len(notasHalfFull)]
        else:
            nextNoteIndex += 2
            nextNote = notasHalfFull[nextNoteIndex%len(notasHalfFull)]
        scale.append(nextNote)
    print(scale)
    calcularAcordes(scale)

def calcularAcordes(escala):
    for i in range(0,7):
        notasEscala = []
        notasEscala.append(escala[i])
        notasEscala.append(escala[(i+2)%len(escala)])
        notasEscala.append(escala[(i+4)%len(escala)])
        #siguienteNotaAcorde = escala[i]
        #siguienteNotaAcordeDos = escala[(i+2)%len(escala)]
        #siguienteNotaAcordeTres = escala[(i+4)%len(escala)]        
        calidadAcorde = calcularCalidad(notasEscala)
        print("El acorde de " + notasEscala[0] + ": " + notasEscala[0] + " " + notasEscala[1] + " " + notasEscala[2] + " -------- Calidad de acorde: " + calidadAcorde)

def calcularCalidad(notas):
    #calidad = ['Mayor', 'Menor', 'Aumentado', 'Disminuido']
    distancia1 = 0
    distancia2 = 0
    posiciones = []
    for nota in notas:
        posiciones.append(notasHalfFull.index(nota))
    if(posiciones[0]>posiciones[1]):
        posiciones[1] = posiciones[1]+len(notasHalfFull)
    if(posiciones[1]>posiciones[2]):
        posiciones[2] = posiciones[2]+len(notasHalfFull)
    distancia1 = posiciones[1]-posiciones[0]
    distancia2 = posiciones[2]-posiciones[1]
    #2 tonos de distancia
    if(distancia1 == 4 and distancia2 == 4):
        return calidad[2]
    elif(distancia1 == 3 and distancia2 == 3):
        return calidad[3]
    elif(distancia1 != distancia2):
        if(distancia1 == 3):
            return calidad[1]
        elif(distancia1 == 4):
            return calidad[0]

print('Ingrese su nota en formato A, B, C, D, E, F, G')
print('Ingrese la nota de la cual quiere su escala mayor:')
escala = input()
calcularEscala(escala)