from MediaAluno import mediaAluno
def mediaSalas(quantidade):
    print("")
    i = 0

    notaAlunos = [0.0] * quantidade
    nomeAlunos = [""] *  quantidade

    notaAlunoMaior = 0
    nomeAlunoMaior = ""

    media = 0

    while i < quantidade:
        print("")
        nomeAluno = input("Digite o nome do aluno: ")
        nomeAlunos[i] = nomeAluno
        notaAlunos[i] = mediaAluno()
        
        print("O aluno " , nomeAluno, f" tirou {notaAlunos[i]:,.3}")


        if notaAlunos[i] > notaAlunoMaior:
            notaAlunoMaior = notaAlunos[i]
            nomeAlunoMaior = nomeAluno
        

        media += notaAlunos[i]
        i += 1

    

    i = 0

    media /= quantidade
    
    print("")
    while i < quantidade:
        print("O aluno", nomeAlunos[i], f"tirou {notaAlunos[i]:,.3}")
        i+=1

    print("O aluno", nomeAlunoMaior, f"tirou a maior nota, que foi de {notaAlunoMaior:,.3}")

    print("\n")
    return media

