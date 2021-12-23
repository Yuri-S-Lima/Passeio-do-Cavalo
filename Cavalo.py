# algoritmo de resolução para o passeio do cavalo
import os

Tabuleiro = [[], [], [], [], [], [], [], []] # Tabuleiro de no máximo tamanho 8x8
linha = [2, 1, -1, -2, -2, -1, 1, 2]
coluna = [1, 2, 2, 1, -1, -2, -2, -1]

os.system('clear')
tamanhoTab = int (input('Digite o tamanho do tabuleiro de no máximo 8: '))
lin = int(input('Digite a linha inicial do cavalo: '))
col = int(input('Digite a coluna inicial do cavalo: '))

for lin in range(tamanhoTab):
    for col in range(tamanhoTab):
        Tabuleiro[lin].append(0)

limite = tamanhoTab * tamanhoTab


def principal(l, c): # l = linha, c = coluna

    Tabuleiro[l][c] = 1

    resultado = correCavalinho(2, l, c) # 2 = id de movimento

    if(resultado): # apresenta o resultado se encontrado
        apresenta()
    else:
        print("Nao existe passeio possivel")


def correCavalinho(id, l, c): # função resposável por percorrer todas as possições e preenchelas

    resultado = id > limite # vai ser true ou false

    k = 0 # responsável por correr todos os possiveis movimentos

    while (not resultado and k < 8):
        x = l + linha[k]
        y = c + coluna[k] # x e y recebem o possível próximo movimento

        # testa os limites do tabuleiro e verifica se a casa já foi visitada
        if(movimentoAceitavel(x, y)):

            Tabuleiro[x][y] = id
            resultado = correCavalinho(id + 1, x, y) # tenta novo movimento
            if(not resultado): # não houve sucesso e descarta o movimento 'anterior'
                Tabuleiro[x][y] = 0 

        k += 1 # tenta próxima coordenada
    return resultado          


def movimentoAceitavel(x, y): # verifica se o movimento é aceitável
    if((x >= 0 and x < tamanhoTab) and (y >= 0 and y < tamanhoTab) and (Tabuleiro[x][y] == 0)):
        return True
    else:
        return False

def apresenta():
    os.system('clear')
    print('PERCURSSO DO CAVALO NO TABULEIRO:')
    for i in range(tamanhoTab):
        print(Tabuleiro[i])

principal(lin, col)