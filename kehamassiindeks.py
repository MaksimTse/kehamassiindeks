from math import *
from random import *
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Kuidas sinu nimi on? ")
print(nimi,"oi kui ilus nimi!")
vastus = input(f"{nimi}! Kas leian Sinu keha indeksi?(jah või ei)")
if vastus=="jah":
    vastus=1
    pikkus=float(input("kui pikk sa oled?(cm) "))
if vastus ==1:
    if pikkus>=140 and pikkus<=190:
        print("ok")
        mass=float(input("mis on su kaal?(kg) "))
        if mass>=30 and mass<=120:
            print("ok")
            indeks=mass/(0.01*pikkus)**2
            print(f"{nimi}! Sinu keha indeks on:",round(indeks,2))
            if indeks <16:
                print("Tervisele ohtlik alakaal	")
            elif indeks >=16 and indeks==18:
                print("Alakaal")
            elif indeks >=19 and indeks==24:
                print("Normaalkaal")
            elif indeks >=24 and indeks==29:
                print("Ülekaal")
            elif indeks >=29 and indeks==34:
                print("Rasvumine")
            elif indeks >=34 and indeks==39:
                print("Tugev rasvumine")
            elif indeks >=39:
                print("Tervisele ohtlik rasvumine")
            else:
                print("??")
        else:
            print("ebasobiv mass!")
    else:
        print("ebasobiv kõrgus")

elif vastus=="ei":
    vastus=0
    print("Kahju! See on väga kasulik info!")
else:
    print("palun vastake jah või ei!")