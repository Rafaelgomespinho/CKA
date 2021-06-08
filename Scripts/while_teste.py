'''
Criação de certificado auto Assinado SSl

'''
import subprocess
import os
from pathlib import Path
from datetime import date, timedelta
import teste

print("Script de Criação Chave Auto Assinada")


diretorio = "/tmp"
#cliente = 'teste'
#ispb = input("Digite o ISPB: ")
Vencimento = "18250"
data_atual = date.today()
dtvenc = str(data_atual + timedelta(days=int(Vencimento)))
cont1 = cont = int(teste.lista_if(0)[2])
a = i = 0
ambiente = input("Homologação ou Produção? ").strip().upper()[
    0]  # Validar Ambinte melhori


while True:
    if ambiente in "Hh":
        ambiente = "HML"
        break
    if ambiente in "Pp":
        ambiente = "PROD"
        break
    else:
        print("Opção Invalida Tente Novamente ")
        ambiente = input("Homologação ou Produção? ").strip().upper()[
            0]

# Bexs_ISPB_Vencimento_HML.pfx
# 11970623
# 50 anos = 18250 dias
# Montar um while para repetir a execução ate o fim do CSV

while a <= cont1:
    if Path(diretorio + "/" + teste.lista_if(a)[1] + "/" + ambiente).is_dir():
        print("Diretorio já existe")
        a += 1
    else:
        print("Criando Diretorio")
        os.system("mkdir -p " + diretorio + "/" +
                  teste.lista_if(a)[1] + "/" + ambiente)
        a += 1


while i <= cont:

    diretorio1 = diretorio + "/"+teste.lista_if(i)[1] + "/" + ambiente + "/"
    password = str(teste.lista_if(i)[1].capitalize() + "@123")
    cliente = teste.lista_if(i)[1]
    ispb = teste.lista_if(i)[0]

    print("Criando a Key Digite a senha desejada")
    os.system("openssl genrsa -des3 -passout pass:" + password +
              " -out " + diretorio1 + cliente + "_" + ispb + ".key 2048")
    
    print("Criando Chave Publica CRT")

    os.system("openssl req -passin pass:"+ password+ " -new -x509 -nodes -sha1 -days "+ Vencimento+ " -key "+
          diretorio1+ cliente+ "_"+ ispb+ ".key > "+ diretorio1+ cliente+ "_"+ ispb+ ".crt -subj '/C=BR/ST=Sao paulo/L=Sao paulo/O="+cliente+"/OU="+cliente+ambiente+"/CN=www."+cliente+".com'" )

    os.system("openssl rsa -passin pass:" + password + " -in " + diretorio1 + cliente + "_" + ispb +
              ".key -out " + diretorio1 + "no.pwd." + cliente + "_" + ispb + ".key")

    #print("Criando Backup ")
    # os.system("cp "+diretorio+"/"+cliente+"_"+ispb+".key " +
    #         diretorio+"/"+cliente+"_"+ispb+".key_backup")

    print("Exportando p12")

    os.system("openssl pkcs12 -export -passout pass:" + password+" -in " + diretorio1 + cliente + "_" + ispb + ".crt -inkey " + diretorio1 +
              "no.pwd." + cliente + "_" + ispb + ".key -out " + diretorio1 + cliente + "_" + ispb + "_" + dtvenc + "_" + ambiente + ".pfx")

    i += 1


print("Fim da execução")
