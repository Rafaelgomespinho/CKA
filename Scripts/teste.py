'''
Criação de certificado auto Assinado SSl


def lista_if(i):
        import csv

        with open('Teste.csv', encoding='utf-8') as ficheiro:
            tabela = csv.reader(ficheiro, delimiter=';')
            lista=list(tabela)
            c=len(lista)-1
            lista2=lista[i]
            ispb=lista2[0]
            IF=lista2[1]
            #print(ispb,IF)
            return ispb , IF , c


'''