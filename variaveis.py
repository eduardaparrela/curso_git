#Variáveis e tipos de dados "básicos"
#Uma variável é um espaço na memória onde armazenamos um valor.

#<nome da var> = <valor>

nome = "Steph" # variável do tipo string (texto), sempre entre aspas ("" OU '')
idade = 29   #var do tipo inteiro(núm sem casas decimais)
altura = 1.61 #var do tipo float (núm com casas decimais) 
dev = True  #var do tipo booleana, valores lógicos (true/false)

nome = input("Digite seu nome: ") #entrada de texto
idade = int(input("Digite sua idade: ")) #entrada de texto convertida pra int
altura = float(input("Digite sua altura: ")) #entrada convertida pra float

print (f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")