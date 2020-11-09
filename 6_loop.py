# While Loop
# i = 1
# while i <=10:
#     print(i*2)
#     i += 1

# i = 1
# while i <=10:
#     if i <= 5:
#         print(i*2)
#     else:
#         print(i*3)

# i = 1
# while i <= 20:
#  if i %2==0:
#      print ('genap')
#  else :
#      print (i) 
#  i += 1


# password = '12345'
# attempt = 1
# while attempt <= 4:
#     masuk = input('Masukkan Password: ')
#     if masuk == password :
#         print('password correct')
#         break
#     else:
#         if attempt == 4:
#             print('Try again Later! ')
#             break
#         else:
#             if attempt == 3:
#                 print(f'password incorrect! you have {4-attempt} attempt left')
#             else:
#                 print(f'password incorrect! you have {4-attempt} attempt left')
#             attempt += 1

# def replace_o(kalimat):
#     kalimat= kalimat.replace('a','o')
#     kalimat= kalimat.replace('i','o')
#     kalimat= kalimat.replace('u','o')
#     kalimat= kalimat.replace('e','o')
#     return kalimat
# print(replace_o(input('masukkan kalimat :')))

# def factorial(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     elif n < 1
#         return 'must be positive digit'
#     else:
#         result = 1
#         i = n
#         while i != 1:
#             result *= 1
#             i -= 1
#         return result


# user_input = int(input('Masukkan angka :'))
# print(factorial(user_input))


# # For Loop and List
# listItem = list(range(1,11,2))
# print(listItem)
# for item in range(1,11,2):
#     print(item)

# y = 'Nomor urut '
# for item in range(1,11) :
#     print(y + str(item))

# y = 'Nomor urut '
# for item in range(0,21,2) :
#     print(y + str(item))

# y = 'Nomor urut '
# for item in range(1,21,2) :
#     print(y + str(item))


# z = ''
# for item in range(0,5):
#     z += ' * '
#     print(z)    

# z=''
# for item in range(1,4):
#     z += '*'
# print(z)


# z=''
# for item in range(0,5):
#     z += ' * \n'
# print(z)

# z='' 
# for item in range(5):
#     for item1 in range(5):
#         z += ' * '
#         z += '\n'

# print(z)


# rows = int(input("Please Enter the Total Number of Rows  : "))
# columns = int(input("Please Enter the Total Number of Columns  : "))

# print("Hollow Rectangle Star Pattern") 
# for i in range(rows):
#     for j in range(columns):
#         if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#     print()

# rows = int(input("Please Enter the Total Number of Rows  : "))
# columns = int(input("Please Enter the Total Number of Columns  : "))

# print("Rectangle Star Pattern") 
# for i in range(rows):
#     for j in range(columns):
#         print('*', end = '  ')
#     print()

# solve 3
# angka = 20
# baris = 0
# while baris<angka:
#     spasi = angka-baris-0
#     while spasi>0:
#         print(end=' ')
#         spasi = spasi-1
#     bintang = baris+2
#     while bintang>0:
#         print('*',end=' ')
#         bintang = bintang-1
#     baris = baris+2
#     print()
# print('=======================================')
# angka = 
# if angka%2 == 0:
#     bintang = angka//2
# else:
#     bintang = angka//2+1

# for i in reversed(range(0,bintang)):
#     for j in range(0,angka-i):
#         print(' ',end='')
#     for k in range(0,i+2):
#         print(' *',end="")
#     print(' * ')
# for i in range(0,bintang):
#     if i == 0 :
#         continue
#     else :
#         for j in range(0,bintang-i):
#             print(' ',end='')
#         for k in range(0,i*2):
#             print(' *',end='')
#         print(' * ')


# rows = int(input("Enter the number of rows : "))
  
# for i in range(1, rows + 1):
#     for j in range (1,(rows-i)+1):
#         print(end = ' ')
# n = 0
# while n != (2 * i - 1):
#     print('*', end = '')
# n = n + 1
# n = 0

# print()

# k = 1
# n = 1
# for i in range(1, rows):
# 	for j in range (1, k + 1):
# 		print(end = '')
# 		k = k + 1

# while n <= (2 * (rows - i)-1):
# 	print("*", end = '')
# 	n = n + 1
# n = 1
# print()




# def fizzbuzz(i):
#     for n in range(1,i+1):
#         if n % 3 == 0 and n % 5 == 0:
#             print("Fizzbuzz")
#         elif n % 3 == 0:
#             print("Fizz")
#         elif n % 5 == 0:
#             print("Buzz")
        
#         else:
#             print(n)

# angka = int(input('masukkan angka :'))

# fizzbuzz(angka)



# string=input(("Enter a string:"))
# if(string==string[::-1]):
#       print("The string is a palindrome")
# else:
#       print("Not a palindrome")

# While Loops & For Loops
# Hanya akan menjalankan code ketika kondisinya True

# print(1*2)
# print(2*2)
# print(3*2)
# print(4*2)
# print(5*2)
# print(6*2)
# print(7*2)
# print(8*2)
# print(9*2)
# print(10*2)


# While Loops
# i = 1 
# while i <=10:  
#     print(i*2)
#     i += 1
    
# i = 1 
# while i <=10: # 10<=10 True
#     i += 1 # 2 => 11
#     if i <= 5: # 6<=5 False
#         print(i*2)
#     else:
#         print(i*3)

# i = 1 
# while i <=10:
#     i += 1
#     if i <= 5: 
#         print(i*2)
#     else: # 6 
#         continue

''' 
Menggunakan while loop buatlah program sederhana,
ketika bertemu dengan angka ganjil, maka print angkanya.
ketika bertemu dengan angka genap, maka print "GENAP"
1-20
'''

# i = 1
# while i <= 20:
#     if i%2 == 0:
#         print('Genap')
#     else:
#         print(i)
#     i += 1

'''
Quiz Password Attempt Poin 2

No. 1
password = '12345'

case 1:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Try again later'

case 2:
input 12345
'Password Correct'

case 3:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 12345
'Password Correct'
'''

# password = '12345'
# attempt = 1
# while attempt <= 4: # 5 => False
#     input_password = input('Masukkan Password: ')
#     if input_password == password:
#         print('Password Correct')
#         break
#     else:
#         if attempt == 4:
#             print('Try Again Later!')
#             break
#         else:
#             if attempt == 3:
#                 print(f'Password Incorrect! You have {4-attempt} attempt left!')
#             else:
#                 print(f'Password Incorrect! You have {4-attempt} attempts left!')
#             attempt +=1

'''
No. 2 poin 1
function untuk mengganti semua huruf vokal, dengan huruf "o"
input = ridho apa kabar
output = rodho opo kobor
replace_o
'''
# def replace_o(kalimat):
#     kalimat = kalimat.replace('a', 'o')
#     kalimat = kalimat.replace('i', 'o')
#     kalimat = kalimat.replace('u', 'o')
#     kalimat = kalimat.replace('e', 'o')
#     return kalimat

# print(replace_o('halo apa kabar kamu di sana'))

'''
No. 3
Factorial
input = 5
return 120
input = 10
return 3,628,800
input = 1
return 1
input = 0
return 1
input < 0
return 'must be positive digit'
'''
# def factorial(n): # n = 5
#     if n == 0: # 5 == 0 False
#         return 1
#     elif n == 1: # 5 == 1 False
#         return 1
#     elif n < 0: # 5 < 0 False
#         return 'must be positive digit'
#     else:
#         result = 1 # 5 // 20 // 60 // 120
#         i = n # 5 // 4 // 3 // 2 // 1
#         while i != 1: # 5 != 1 True // 4 != 1 True // 3 != 1 True // 2 != 1 True // i != 1 False
#             result *= i # 1*5=5 // 5*4=20 // 20*3=60 // 60*2=120
#             i -= 1 #5-1=4 // 4-1=3 // 3-1=2 // 2-1=1
#         return result

# d = 5
# print(factorial(d))

# def rec_factorial(n): # n = 5 // n = 4 // n = 3 // n = 2 // n = 1
#     if n == 0: # 5 == 0 False // 4 == 0 False // 3 == 0 False // 2 == 0 False // 1 == 0 False 
#         return 1
#     elif n == 1: # 5 == 1 False // 4 == 1 False // 3 == 1 False // 2 == 1 False // 1 == 1 True
#         return 1
#     elif n < 0: # 5 < 0 False // 4 < 0 False // 3 < 0 False // 2 < 0 False
#         return 'must be positive digit'
#     else:
#         return n*rec_factorial(n-1) # 5 * 24 = 120
# print(rec_factorial(d))

## FOR Loops ##
# i = 1
# while i <= 10:
#     print(i*2)
#     i+=1

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     if i == 5:
#         break
#     else:
#         print(i*2)

# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i*2)

# for i in range(6): # 0,1,2,3,4,5
#     print('*')

# for i in list(range(1,5)):
#     print(i)

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# for i in a_list:
#     print(f'Halo nama saya {i}!')

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# b_list = ['Kapiten', 'Data Scientist', 'Tour Guide', 'Montir', 'Reparasi AC']
# for i in range(len(a_list)): # range(5) => 0,1,2,3,4
#     print(f'Halo nama saya {a_list[i]}! Pekerjaan Saya adalah {b_list[i]}')

a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
b_list = ['Kapiten', 'Data Scientist', 'Tour Guide', 'Montir', 'Reparasi AC']


# for i, j in zip(b_list, a_list): #[('Budi', 'Kapiten'), ('Andi', 'Data Scientist'), ('Candi', 'Tour Guide')]
#     print(f'Halo nama saya {i}! Pekerjaan Saya adalah {j}')


'''
case 1
buat sebuah function untuk game fizz buzz!
function ini menerima 1 parameter.
ketika bertemu angka yang habis dibagi 3 maka dia akan print fizz [3,6,9,12]
ketika bertemu angka yang habis dibagi 5 maka dia akan print buzz [5,10,15,20,25]
ketika bertemu angka yang habis dibagi 3 dan 5 maka dia akan print fizz buzz [15, 30, 45]

contoh:
input : fizzbuzz(15)
output :
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
'''

'''
case 2
tanpa membuat function, buatlah sebuah program untuk reversing namun menggunakan for loop
input = [1,2,3,4,5,6,7]

output = [7,6,5,4,3,2,1]

'''

'''
case 3
PALINDROME
tanpa membuat function, buatlah sebuah program untuk mengecek apakah suatu kata palindrom atau bukan.
Palindrome: kondisi ketika suatu kata akan dieja sama, baik dieja dari depan maupun belakang.
contoh: "malam", dibalik juga "malam"
contoh: "kodok", dibalik juga "kodok"
contoh bukan palindrome: "kotak", dibalik jadi "katok"

input = malam
output = Is word malam a palindrome = True

input = malab
output = Is word malab a palindrome = False

input = kodok
output = Is word kodok a palindrome = True
'''

'''
case 4
buatlah sebuah function yang menerima 1 parameter, untuk membuat segitiga siku-siku menggunakan *

contoh:
segitiga_siku(5)

output =
 * 
 *  * 
 *  *  *
 *  *  *  *
 *  *  *  *  *

contoh:
segitiga_siku(7)

output = 
 * 
 *  *
 *  *  *
 *  *  *  *
 *  *  *  *  * 
 *  *  *  *  *  *
 *  *  *  *  *  *  * 
'''
z=''

# inp = [1,2,3,4,5,6,7]
# output = []
# a = 0

# for i in range(0,len(inp)):
#     a -= 1
#     output.append(inp[a])
    
# print(output)

# case 3
# nomor 3
# def cekkata():
#     kata = input('Masukkan kata: ').lower()
#     list2 = '' #l
#     # k = 0
#     for i in range(len(kata)): # 0
#         # k -= 1 # k = -2; k = -
#         #             -(1+1)
#         list2 += kata[-(i+1)] # list2 = lib --> libom
#     if list2 == kata:
#         print(f'{kata} is a palindrome')
#     else: print(f'{kata} is not a palindrome')

# cekkata()


# a_dict = {
#     'nama' : 'Andi',
#     'kelas' : '1C',
#     'status' : 'jomblo'
#     'penghasilan' : 'belum punya'
# }
# print(a_list)
# slice_list = 'kelas statu'.split()
# slice_dict = {i: a_dict[i] for i in slice_list}

# print(slice_list)

# print(a_list)