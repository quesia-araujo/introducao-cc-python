def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > m or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():

    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa")
        jogador_atual = "usuario"
    else:
        print("O computador começa!")
        jogador_atual = "computador"
    
    while n > 0:
        if jogador_atual == "computador":
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"O computador tirou {jogada} peça(s).")
            jogador_atual = "usuario"
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"Você tirou {jogada} peça(s).")
            jogador_atual = "computador"
        print(f"Agora restam {n} peça(s) no tabuleiro.")
    
    if jogador_atual == "usuario":
        print("Fim do jogo! O computador ganhou!")
        return "computador"
    else:
        print("Fim do jogo! Você ganhou!")
        return "usuario"

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****")
        vencedor = partida()
        if vencedor == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

opcao = int(input())

if opcao == 1:
    print("Você escolheu uma partida isolada!\n")
    partida()
elif opcao == 2:
    print("Você escolheu um campeonato!\n")
    campeonato()
else:
    print("Opção inválida. Escolha 1 ou 2.")
