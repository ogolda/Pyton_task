
sec = int(input("Введите секунды :"))
chas = sec//3600
ost_sec = sec - chas*3600

minutes = ost_sec//60
sec1 = ost_sec - minutes*60

print ("Время :", chas, ":" , minutes , ":" , sec1)