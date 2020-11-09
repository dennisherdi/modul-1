# def hello():
#     print('hallo cuuuuuk')
# hello()

# def power():
#     print(3**2)
# power()

# def data(x,y):
#     print(x+' Lahir th '+y)
# data('Adi','1990')
# data('Budi','1991')
# data('Caca','1992')
# data('Dedi','1993')

# def total(x,y):
#     z = x + y
# print(total(4,5))

# def total(x,y):
#     z = x + y
#     print(z)
# print(total(4,5))

# def kali(x):
#     if (x < 2):
#         return 1;
#     else :
#         return (x * tiga())
# def tiga():
#     return 3
# print(kali(5))

# def kali(angka1 = 5, angka2 = 2):
#     return angka1 * angka2
# print(kali(angka2=4))


# def tambah(x, y):
#     return x + y

# def kurang(x, y):
#     return x - y

# def kali(x, y):
#     return x * y

# def bagi(x, y):
#     return x / y

# def pangkat(x,y):
#     return x ** y

# print("Pilih kalkulator.")
# print("1.Penjumlahan")
# print("2.Pengurangan")
# print("3.Perkalian")
# print("4.Pembagian")
# print("5.Perpangkatan")
   
# pilihan = input("Masukkan Pilihan(1/2/3/4/5): ")

# if pilihan in ('1', '2', '3', '4', '5'):
#     num1 = int(input("Masukkan Angka Pertama: "))
#     num2 = int(input("Masukkan Angka Kedua: "))

#     if pilihan == '1':
#         print('hasil penjumlahan', num1, "+", num2, "adalah", tambah(num1, num2))

#     elif pilihan == '2':
#          print('hasil pengurangan', num1, "-", num2, "adalah", kurang(num1, num2))

#     elif pilihan == '3':
#         print('hasil perkalian', num1, "x", num2, "adalah", kali(num1, num2))

#     elif pilihan == '4':
#         print('hasil pembagian', num1, ":", num2, "adalah", bagi(num1, num2))
        
#     elif pilihan == '5':
#         print('hasil pemangkatan', num1, "^", num2, "adalah", pangkat(num1, num2))
        
#     else:
#         print("invalid input")
# else:
#     print('pilihan anda tidak tersedia')

# application = ['ABC for Kids١', 'asdsabdasd', 'asdas١assad', 'sada']
# english_app = []
# #   i = 'B'
# for app in application:
#     true_sum = 0 # 1 => 2 => 3 => 4 => 5 => 12
#     for i in app: # 'ABC for Kids'
#         #   (97 <= ord('A') <= 122) or (65 <= ord('A') <= 90) or (i == ' ')
#         #   (97 <= ord('B') <= 122) or (65 <= ord('B') <= 90) or (i == ' ')
#         #   (97 <= ord('C') <= 122) or (65 <= ord('C') <= 90) or (i == ' ')
#         #   (97 <= ord(' ') <= 122) or (65 <= ord(' ') <= 90) or (i == ' ')
#         #   (97 <= ord('f') <= 122) or (65 <= ord('f') <= 90) or (i == ' ')
#         #       False or False or True = True
#         if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')) or (i==' '):
#             true_sum += 1

#     print('true_sum:', true_sum)
#     print('len apps:', len(app))
#     if true_sum == len(app):
#         english_app.append(app)

# print(english_app)

 
# print(ord('A'))

# def apapun():
#     return 1

# a_list = [apapun, 'a', 'c']
# print(a_list[0]())


def c():
    return cicak

def cicak():
      return ['jaguar',['car','bob',{'test':aku}]]

def aku():
      print ('hello')
      
def beta():
    return {'hello':['a','b',c]}

beta()['hello'][2]()()[1][2]['test']()