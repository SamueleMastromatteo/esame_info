# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

account_list = []
professione = []
professione_follower = []

def leggi_file(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            account_list.append({
                "nickname": campi[0],
                "nome": campi[1],
                "follower": float(campi[2]),
                "professione": campi[3]
            })
    return account_list

def follower_professione(account_list):
    follower_tot = 0
    for riga in account_list:
        
        follower_tot += riga["follower"]
        for i in range(len(account_list)):
            #se la professione non è stata ancora salvata nella lista professione, la salvo, e salvo i valori nel dict professione_follower
            if riga["professione"] not in professione:
                professione.append(riga["professione"])
                professione_follower.append({"professione": riga["professione"], "follower": float(riga["follower"])})
            #altrimenti sommo il valore di follower all'interno di professione_follower["follower"], per avere il totale dei follower per professione
            else:
                #professione_follower[i]["follower"] += float(riga["follower"])
                pass
    print(professione_follower)


def main():
    leggi_file("instagram.csv")
    follower_professione(account_list)

if __name__ == "__main__":
    main()