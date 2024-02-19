## 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci = [1, 1]
while len(fibonacci) < 20:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)


# ## 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi = int(input("Bir sayi girin: "))
bolenlerToplami = 0

for i in range(1, sayi):
    if sayi % i == 0:
        bolenlerToplami += i

if bolenlerToplami == sayi:
    print(sayi, "mükemmel bir sayidir.")
else:
    print(sayi, "mükemmel bir sayi değildir.")

# ## 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

birinciSayi = int(input("Birinci Sayiyi Giriniz : "))
ikinciSayi = int(input("İkinci Sayiyi Giriniz : "))
 
if (birinciSayi > ikinciSayi):
    kucukSayi = ikinciSayi
else:
    kucukSayi = birinciSayi
for i in range(1,kucukSayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i
        ekok = (birinciSayi*ikinciSayi)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)


# # 2. yöntem 

import math
firstNum = int(input("Birinci Sayiyi Giriniz : "))
secondNum = int(input("İkinci Sayiyi Giriniz : "))
ebob=math.gcd(firstNum,secondNum)
ekok=(firstNum*secondNum)/ebob
print ("EBOB:", ebob)
print ("EKOK:", ekok)


# ## 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi = int(input("Bir sayi girin : "))

asalMi = True

for i in range(2, sayi // 2 + 1):
    if sayi % i == 0:
        asalMi = False
        break  

if asalMi:
    print(sayi, "asal bir sayidir.")
else:
    print(sayi, "asal bir sayi değildir.")


# ## 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
    
num = int(input("Bir sayi girin : "))
factor = 2
print(num, "asal sayi çarpanlari:")
while factor <= num:
    if num % factor == 0:
        print(factor)
        num //= factor
    else:
        factor += 1
