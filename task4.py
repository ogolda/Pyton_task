n=int(input('Enter number  '))
max=n%10
while n!=0:
    number=n%10
    if number>=max:
        max=number
    n//=10
print(f'Max number = {max}')