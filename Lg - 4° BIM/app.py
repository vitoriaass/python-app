import os

numero = []
nomes = []

def cadastro(num, nome):    
    numero.append(num)
    nomes.append(nome)
    return "A chapa foi cadastrada com sucesso"
    
def pesquisar():  
    limpar()  
    cont = 0
    while cont < len(nomes):
        print(numero[cont])
        print(nomes[cont])                  
        cont += 1

def atualizar(num):
    novonumero = int(input("Digite o novo número"))
    novonome = "Israel"
    if num in numero:
        posicao = numero.index(num)
        numero[posicao] = novonumero
        nomes[posicao] = novonome
        return "Chapa atualizada com sucesso"


    return 0
def deletar(num):       
    if num in numero:       
       posicao = numero.index(num)       
       numero.pop(posicao)
       nomes.pop(posicao)
       return "A chapa de número", num, " ", "foi removida com sucess"
    else:
        return  ("Não existe esta chapa com esse número" , num)
    
def msn():
    print("Opção inválida")
def limpar():
    os.system('cls')      

op = 10
while op != 0:
   
    op = int(input("Digite sua opção:"+ 
                   "\n 1 - Cadastrar uma chapa"+
                   "\n 2 - Pesquisar uma chapa"+
                   "\n 3 - Atualize uma chapa"+
                   "\n 4 - Delete uma chapa"+
                   "\n 0 - Feche o sistema"))