try:
 nome = input(f"Qual é seu nome?")
 peso = float(input(f"Qual  é seu peso?"))
 altura = float(input(f"Qual é sua altura?"))
 imc = peso/(altura*altura)

 if imc <=18.5:
   print(f"{nome} está abaixo do peso")
 elif imc >=18.5 and imc <= 24.9:
     print(f"{nome} está com o peso normal")
 elif imc >=29.9 and imc <=34.9:
     print(f"{nome} está com sobre peso")
 elif imc >=34.9 and imc <=34.9:
     print(f"{nome} está com obesidade com 2 grau")
 else:
     print(f"eitaaaaa {nome} vaiii morrerrr miseravel")     
 with open("pessoa.txt","a") as beraldo:
    beraldo.write(nome + " | " + imc + "\n")
except:
    print("Seu peso está errado: ")