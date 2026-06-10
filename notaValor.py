notaValor = {'C': 1, 'C#': 2, 'Db': 2, 'D': 3, 'D#': 4, 'Eb': 4, 'E': 5, 'F': 6,'F#': 7, 'Gb': 7, 'G': 8, 'G#': 9, 'Ab': 9, 'A': 10, 'A#': 11, 'Bb': 11, 'B': 12 }
valorNota = {}
for nota, valor in notaValor.items():
    if valor not in valorNota:
        valorNota[valor] = [] # cria uma lista se não existir
    valorNota[valor].append(nota) # permite varias notas para um valor
