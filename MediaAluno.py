import random

def mediaAluno():
    nota = [0.0] * 4

    i = 0
    media = 0
    while i < 4:
        nota[i] = random.uniform(0.0, 10.0)

        media += nota[i]

        i += 1
    
    media /= i

    return media


