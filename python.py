print("olá tudo bem?😊")
print("Estou aqui para lhe dizer quantos numeros pares tem de acordo com a quantidade de numeros você digitar😉")

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
tem_par = False
soma = 0

for numero in range(inicio, fim +1):
    if numero % 2 == 0: 
        print(f"Numero par encontrado: {numero}")
        soma += numero
        tem_par = True
        

    
if tem_par:
    print(f"A soma dos números pares é: {soma}")   
if not tem_par:
    print("Não foram encontrados nenhum numero pares na sequencia 😕")



            
