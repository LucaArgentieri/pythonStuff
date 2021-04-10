import random
 
max = 10
secretNumber = random.randrange(1, max)
 
rispostaUtente = int(input("Inserisci un numero: "))
 
if rispostaUtente == secretNumber:
    print("Indovinato! \^o^/")
elif rispostaUtente < secretNumber:
    print("Il numero è troppo basso, hai perso. ╯︿╰")
else:
    if rispostaUtente > max:
        print("Hai inserito un numero fuori range.")
    else:
        print("Il numero è troppo alto, hai perso. ＞﹏＜")


