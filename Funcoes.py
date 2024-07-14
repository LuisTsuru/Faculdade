##Funcoes
# Lista de ex

##########################################################################################

# Ex 1 - Crie as funções:
# max_(): maior elemento de um vetor
def max_(vet):
    temp = vet[0]
    for i in range(vet):
        if vet[i] > temp:
            temp = vet[i]

def min_(vet):
    temp = vet[0]
    for i in range(vet):
        if vet[i] < temp:
            temp = vet[i]

# Ex2 - Crie uma função que dado um vetor, retorna todos os índices que contenham números pares
def index_finder(x):
    matriz_par = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            matriz_par.append(i)
    return matriz_par
x = [10,11,12,13,14]
print(index_finder(x))

##########################################################################################

# Ex 3 - Crie uma função que retorna à frequência dos elementos. Dica, o retorno é uma matriz

def contar_frequencias(vetor):
    # Passo 1: Contar frequências usando um dicionário
    frequencias = {}
    for numero in vetor:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
            
    matriz_frequencias = []
    for numero, frequencia in frequencias.items():
        matriz_frequencias.append([numero, frequencia])
    
    matriz_frequencias.sort(key=lambda x: x[0])

    return matriz_frequencias


# Exemplo de uso
# x = [1, 4, 2, 1, 3, 3, 4, 3, 1, 2, 1, 1]
# resultado = contar_frequencias(x)
# print(resultado)

##########################################################################################

#Recursao

def recursao_soma(N):

    print(N)
    if N == 0:
        return 0
    s = N + recursao_soma(N-1)
    print(N)
    return s
