import requests
try:
   url = "https://www.sp.senai.br/patrono---suzana-dias"
   resposta = requests.get(url)
   status = resposta.status_code
   if status == 200:
       
     print("o site está mui safe",status)
   else:
     print("o site está uma merda e não foi encontrado!! Status: ", status)
except:
    print("está dando erro,deve ser sua internet de merda resolva")