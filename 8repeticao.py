#laços de repetição(for e while)

#imagine que você precisa pedir para alguém contar de 1 a 100
#e escrever cada número em um papel. Fazer isso manualmente seria muito cansativo e demorado, né? 

#Agora, imagine que um programa pode fazer essa contagem automaticamente, 
#sem precisar repetir o mesmo comando 100 vezes. É exatamente isso 
#que os laços de repetição fazem!

#Os laços de repetição são usados para executar um bloco de código
#várias vezes, até que uma condição seja atingida. 

#Python tem dois tipos principais de laços:

#for - quando sabemos quantas vezes queremos repetir algo. 
#while - Quando queremos repetir algo até que uma condição se torne falsa 
# FOR
#o FOR é usado quando sabemos quantas vezes queremos repetir um bloco de código. 
#Ele percorre uma sequência de valores, como uma lista, um intervalo de números
# ou até mesmo letras de uma palavra. 

#Estrutura: 

#for variavel in sequência: 
#  Código a ser repetido

#Contando de 1 a 5 com o FOR
#[1,2,3,4,5]

#for  numero in range(1,20): 
#   print(numero)

#percorrendo uma lista de Strings 

# compras = ["Arroz", "Feijão", "Leite", "Ovos"]

# for item in compras: 
#    print(f" Comprar: {item}")

#Percorrendo uma palavra 

#palavra = "COMUNIDADE"

#for letra in palavra: 
#    print(letra) 


#  WHILE 

# O while é usado quando não sabemos quantas vezes a repetição vai acontecer,
#mas sabemos a condição que deve ser atendida para continuar. 

#while condição: 
#  #código a ser repetido enquanto a condição for verdadeira

#OBS: Cuidado com loops infinitos!
#Se a condição nunca mudar para False, o código nunca para de rodar. 

#Contagem regressiva

# contador = 5

# while contador > 0: 
#    print(contador)
#    contador -=1

# print ("fogo!")

# Pedindo senha até acertar 

senha_correta = "1234"
senha = ""

while senha != senha_correta: 
     senha = input("Digite a senha: ")

print("Acesso permitido!")     