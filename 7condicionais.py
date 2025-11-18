
#Estruturas conicionais

#São estruturas que permitem ao nosso programa tomar decisões com base
#em determinadas condições. Em outras palavras, o programa pode executar
#ações diferentes dependendo de uma situação específica. 

#Exemplo: 

#Você está em uma cafeteria e está ecom pouca grana. 
# O capuccino custa 10 reais, café com leite 7 e o café simples 4. 

#se vc tiver 10 reais ou mais na carteira, pode pedir o capuccino. 
#se vc tiver 7 reais ou mais pode pedir o café com leite. 
#se não, pede o café simples. 

#sintaxe básica no Python! 
# if - "se"
#else - "se não"
#elif - se + se não

 #if condição: 
    # código a ser executado se acondição for verdadeira
  #else outra_condição: 
    #código a ser executado se a primeira condição for falsa, mas se essa for verdadeira
   #elif: 
    #código executado se nenhuma das condições anteriores for verdadeira.

#exemplos
# verificando a idade para entrada em um evento (18 anos) 

#idade = int(input("Digite sua idade: ")) #Usuário digita a idade

#if idade >= 18: 
 # print ("Você pode entrar no evento!")
#else:
 # print("Desculpe, você ainda não tem idade suficiente para entrar. ")

#verificando a nota de um aluno 

#nota = float(input("Digite sua nota: ")) #Usuário insere a nota

#if  nota >= 7: 
#    print ("Parabens! Você passou de ano!")
#elif nota >= 5: 
#    print ("Você está de recuperação. Estude mais e tente novamente.")
#else: 
#    print("Infelizmente, você foi reprovado. Tente novamente no próximo ano.")

#if nota>= 7: 
#   print ("Parabéns, você foi aprovado")

#idade = int(input ("Digite sua idade:")) 
 
#if idade <18:
 #     print ("Menor de idade") 
#elif 18 <= idade <= 60:       
 #     print ("Adulto")
#else:
 #print ("idoso")

#classificar números (positivo, negativo, zero)

try: 
   
  numero = int(input("Digite um numero"))

  if  numero > 0: 
    print ("Positivo")
  elif numero < 0:
   print ("negativo")
    
  else:
   print ("Zero")
 
except ValueError:
   print("Por favor, digite um número inteiro válido.")

