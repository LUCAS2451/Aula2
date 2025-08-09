from MediaSalas import mediaSalas
def main():
    nomeEscola = input("Digite o nome da escola: ")
    print("")

    numeroSalas = 0

    while numeroSalas <= 0:
        numeroSalas = int (input ("Digite a quantidade de salas: "))

        if numeroSalas <= 0:
            print("Valor inválido, digite novamente!\n")
    
    print("")
    mediasSalas = [0.0] * numeroSalas 
    nomeSalas = [""] * numeroSalas 

    notaSalaMaior = 0
    nomeSalaMaior = ""
    i = 0

    while i < numeroSalas:
        print("")
        quantidadeAlunos = 0

        nomeSala = input ("Digite o nome da sala: ")

        nomeSalas[i] = nomeSala

        while quantidadeAlunos <= 0:
            quantidadeAlunos = int ( input ("Digite a quantidade de alunos desta sala: "))

            if quantidadeAlunos <= 0:
                print("Número inválido, digite novamente\n")
        
        mediasSalas[i] = mediaSalas(quantidadeAlunos)

        if mediasSalas[i] > notaSalaMaior:
            notaSalaMaior = mediasSalas[i]
            nomeSalaMaior = nomeSala


        i += 1
        print("\n")
    
    i = 0

    print("Salas do ", nomeEscola)
    while i < numeroSalas:
        print("A sala ", nomeSalas[i], f" tirou a nota {mediasSalas[i]:,.2}" )
        i += 1
    
    print("A sala ", nomeSalaMaior, f"tirou a maior que foi {notaSalaMaior:,.2}")


    return 0
main()