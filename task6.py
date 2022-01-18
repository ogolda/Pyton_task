vyr=float(input("Введите значение выручки, д.е.  "))
izd=float(input("Введите значение издержек, д.е. "))
if vyr>izd:
    print("Вы работаете успешно")
    prib=vyr-izd
    rentab=(prib/vyr)*100
    print("Рентаблельность предприятия составляет ", '%.2f' % rentab, "%")
    chisl=int(input("Введите численность сотрудников, чел "))
    prib_na_sotr=prib/chisl
    print("Прибыль фирмы в расчёте на одного сотрудника составляет ", '%.2f' % prib_na_sotr, "д.е.")
else:
    print("Вы работаете без прибыли")