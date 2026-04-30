#atividade 01
#print("teste")

#atividade 02
#print("teste 2")
#print("teste 3")
#print("teste 4")
#print("teste 5")

# #BREAk
# #exemplo 1
# contador = 0
# while contador <= 10:
#     print(contador)
#     if contador ==5:
#         break
#     contador +=1

# #exemplo 2
# senha = ""

# while True:
#     senha = input("Digite a senha: ")

#     if senha == "1234":
#        print ("Acesso liberdo: ")    
#        break
#     print ("Senha incorreta: ")

# #refazer
#  num = ""
# while num <= 10:
#     num = input("Digite om numero: ")
#     if num <0:
#         print (num)    
#         break
     
##Exemplo 3 - Continue
# numero = 1

# while numero <= 5:
    
#     if numero == 2:
#         numero += 1
#         continue

#     print(numero)
#     numero += 1

##exemplo 4 - continue
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 1:
# ##  if contador % 2 == 0:
#         continue

#     print(contador)

#atividade 1
#Mostre números de 1 a 10, mas pare no 6.
# numero = 1
# while numero <=10:

#     print (numero)
#        if numero == 6
#        break
#      numero +=1

# #Mostre números de 1 a 10, pulando o número 5.   
# numero = 1
# while numero <=10:
#     if numero == 5:
#         numero += 1
#         continue
#     print(numero)
#     numero += 1

# #Mostre números de 1 a 20, pulando pares e encerrando no 15.
# numero = 1
# while numero <=20:
#     if numero == 15 + 1: ## a adicao de mais um digito fez o codigo mostrar o numero 15
#         break
#     if numero % 2 ==0:
#         numero += 1
#         continue
#     print(numero)
#     numero += 1

#Atividade 04
# Uma loja deseja cadastrar produtos até o funcionário digitar fim.
# Pedir nome do produto
# Se digitar fim, encerrar cadastro
# Mostrar cada produto cadastrado
# Usar break

# produto =""
# while True: 
#    produto = input("Digite o produto: ")
#    if produto == "fim":
#      print("Cadastro finalizado")                
#      break
#    print ("Produto cadastrado com sucesso: ", produto)  

# #atividade 5
# #Parar quando soma chegar em 20
# soma = 0
# while True:
#     numero = int(input("Digite o numero: "))
#     soma += numero

#     if soma >= 20:
#         break
# print ("Total da soma: ", soma)    

# #atividade 6
# #Crie um sistema que receba números digitados pelo usuário e vá somando os
# #valores informados.
# #Quando a soma total atingir ou ultrapassar 50, o programa deverá encerrar
# #automaticamente utilizando o comando break.

# soma = 0
# while True:
#     numero = int(input("Digite um numero: "))
#     soma += numero

#     if soma >= 50:
#          print("Limite atingido")
#          print ("Total da Soma", soma)
#          break

# #atividade 7
# # Crie um programa que peça uma senha ao usuário até ele acertar.
# # A senha correta será:
# # Teste
# # Quando acertar, mostrar:
# # Acesso liberado

# while True:
#     senha = input("Digite a senha: ")

#     if senha == "teste":
#         print("Acesso liberado")
#         break
#     else:
#         print("Senha incorreta: ")