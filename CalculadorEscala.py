#Universidad del Valle de Guatemala
#Juan Guillermo Sandoval Lacayo - 17577


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

def calcularEscala(nota):
    nextNoteIndex = notasHalfFull.index(escala)
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
        siguienteNotaAcorde = escala[i]
        siguienteNotaAcordeDos = escala[(i+2)%len(escala)]
        siguienteNotaAcordeTres = escala[(i+4)%len(escala)]
        print("El acorde de " + siguienteNotaAcorde + ": " + siguienteNotaAcorde + " " + siguienteNotaAcordeDos + " " + siguienteNotaAcordeTres)

print('Ingrese su nota en formato A, B, C, D, E, F, G')
print('Ingrese la nota de la cual quiere su escala mayor:')
escala = input()
calcularEscala(escala)