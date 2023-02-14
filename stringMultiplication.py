# Recreating the string multiplication thing
strVar1 = input("Enter the string: ")
strVar2 = strVar1
multVar = int(input("Enter how many times you want to repeat it: "))

for x in range(multVar - 1):
    strVar1 += strVar2

print(strVar1)