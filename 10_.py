Decimal = int(input("Введите десятичное которое хотите перевести-->"))
Notation = int(input("Введите в какую систему перевести-->"))
n10 = Decimal
n=n10
t16 =""
while (n>0):
    ostatok=n%16
    if (ostatok<10):
        s=str(ostatok)
    else:
        s=chr(ord('A')+ostatok-10)
    t16=s+t16
    n=n//16
if Notation == 16:
    print("В шеснадцатиричной системе")
elif not(2 <= Notation <= 9):
    print("Error!")
    quit()
newDecimal = ''
while Decimal > 0:
    newDecimal = str(Decimal % Notation) + newDecimal
    Decimal //= Notation
if Notation == 16:
    print(t16)
else:
    print(newDecimal)

