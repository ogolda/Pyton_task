a=float(input("Введите результат спортсмена, км "))
b=float(input("Введите желаемый результат "))
i=1
print("Результат: ")
print("1-й день: ",  a)
while a<b:
    i=i+1
    a=a*1.1
    print("%d-й день: " % i,  '%.2f' % a)
print("Ответ: на ", i , "-й день спортсмен достиг результата — не менее " , b , " км.  ")