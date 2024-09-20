import random

#Variabel input
letter = ['A','B','C','D','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['@','#','$','%','^','&','*','(',')','_','+','=']

input_letter = int(input('How many characters do you want to add? '))
input_number = int(input('How many numers do you want to add? '))
input_symbol = int(input('How many symbol do you want to add? '))

#Algoritma password
password = ''
for char in range(1, input_letter+1):
    password += random.choice(letter)

for char in range(1,input_number+1):
    password += random.choice(number)

for char in range(1,input_symbol+1):
    password += random.choice(symbol)

print(f'password anda adalah {password}')