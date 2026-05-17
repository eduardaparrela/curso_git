 #Verificndo idade
 
 # #idade = int(input ("Digite sua idade:")) 
 
#if idade <18:
#    print ("Menor de idade") 
#elif 18 <= idade <= 60:       
 #     print ("Adulto")
#else:
 #print ("idoso")

#classificar números (positivo, negativo, zero)

#try: 
   
  #numero = int(input("Digite um numero"))

#if  numero > 0: 
  # print ("Positivo")
#elif numero < 0:
 #  print ("negativo")
    
  #else:
 #  print ("Zero")
 
#except ValueError:
#   print("Por favor, digite um número inteiro válido.")


# nota para conceito


#nota = float(input("Digite uma nota: "))
    
#if nota >=9: 
#  print ("nota A")

#elif nota >= 7: 
#  print ("nota B")

#elif nota >= 5: 
#  print("nota C")

#else: 
#  print("nota D")    

#Calculadora simples 

num1 = float(input("Digite um número "))
num2 = float(input("Digite um número "))
 
operacao = input("Digite a operacao (+, -,*, /):")

if operacao == "+": 
  print("Resultado:", num1 + num2)

elif operacao == "-":
  print ("Resultado:", num1 - num2)

elif operacao == "*": 
  print ("Resultado:", num1*num2)

elif operacao == "/": 
  print ("Resultado:", num1/num2)

else: 
   print("Operacao invalida!")

#Verificar tipo de triângulo

a = float(input("Digite o primeito lado:"))
b = float(input("Digite o segundo lado:"))
c = float(input("Digite o terceiro lado"))


if a < b + c and b < a + c and c < a + b:
  
  if a == b == c:
    print("Triângulo equilátero")

  elif a == b or a == c or b == c:
   print ("Triângulo Isósceles")

  else:
   print("Triangulo Escaleno")

else: 
  print("Os valores informados Não formam um triangulo.")