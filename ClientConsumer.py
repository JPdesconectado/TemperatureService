import requests
import datetime


while True:

    print("---------- Menu ----------\n")
    print("(1) Última Leitura")
    print("(2) Pesquisar leitura")
    print("(3) Sair.")
    print("--------------------------\n")
    opcao = int(input("Escolha:"))

    if(opcao == 1):
        r = requests.get("http://127.0.0.1:5000/dados")
        info = r.json()
        tam = len(info['dados']) - 1
        print(info['dados'][tam])

    elif(opcao == 2):
        print("---------- Pesquisar ----------\n")
        print("(1) ID")
        print("(2) DATA e HORA")
        decisao = int(input("Escolha:"))

        if(decisao == 1):
            r = requests.get("http://127.0.0.1:5000/dados")
            info = r.json()
            id =  int(input("Digite o ID:"))
            if (len(info['dados'])-1 < id):
                print("ID inexistente.")
            else:    
                print(info['dados'][id])

        elif(decisao == 2):
            r = requests.get("http://127.0.0.1:5000/dados")
            info = r.json()
            data = input("Digite a data no formato ->'dd/mm/yyyy':")
            hora = input("Digite a hora no formato -> 'hh:mm':")
            for i in range(len(info['dados'])):
                jsoninfo = info['dados'][i]['date']
                jsonhora = info['dados'][i]['hour']
                if(jsoninfo == data and jsonhora == hora):
                    print(info['dados'][i])
                else:
                    continue    

    elif(opcao == 3):
        break       