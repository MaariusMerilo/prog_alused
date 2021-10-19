nimi = input("Sisestage nimi")
lubatud_kiirus = int(input("Sisestage lubatud kiirus km/h: "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus km/h: "))
yletanud = tegelik_kiirus - lubatud_kiirus
arvutatud_trahv = yletanud * 3
trahv = min(arvutatud_trahv, 190)
print(nimi + ", kiiruse ületamise eest teie trahv on " + str(trahv) + " eurot.")



