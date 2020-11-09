## LAMBDA ##

def perkalian(a, b):
    print(a*b)

perkalian(2,3)

x = lambda a, b: a*b
print(x(2,3))

y = lambda a,b,c: (a/b)*c
print(y(1,2,3))

z = lambda a: 'genap' if a%2==0 else 'ganjil'
print(z(4))
print(z(3))

def penjumlahan(a,b) :
    y = lambda a,b : a+b
    return y(a,b)
print(penjumlahan(1,2)) 

## MAP ##

nama_list = 'andi Budi Caca'.split()
def function(a):
    return len(a)
len_list = list(map(function, nama_list))
print(len_list)

len_list2 = list(map(lambda a: len(a), nama_list))
print(len_list2)

list_1 = 'cokelat melon nangka'.split()
list_2 = [10000,5000,20000]
couple_list =list(map(lambda a,b: a+str(b), list_1,list_2))
print(couple_list)

## FIlTER ##

h = range(11)
def kurang_lima(x):
    if x<5:
        return True
    else:
        return False

j = list(filter(kurang_lima,h))

print(j)
print(list(h))


m = list(filter(lambda a: a%2==0,range(1,101)))
print(m)

## EXERCISE ##


y = list(map(lambda a:a**2,m))
print(y)

my_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']

cari = str(input('Masukkan Huruf Anda:'))
hasil= list(filter(lambda a: cari in a, my_list))
print(hasil)

## REDUCE ##
from functools import reduce

numbers = [6,2,3,4,5]
numbers_sum = reduce(lambda a,b: a+b,numbers)
print(numbers_sum)

kata = ['ini','ibu', 'budi']
o = reduce(lambda a,b: a+b,kata)
print(o)
from functools import reduce

print(reduce(lambda a,b: a+b, map(lambda a:a*2, filter(lambda a: a%2==0,range(1,101)))))

