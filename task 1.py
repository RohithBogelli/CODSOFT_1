print(" welcome to the password generator");
import random
letter=['a','b','c','d','e','f','g','h','i','j','k'
        ,'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K'
        ,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}']
n_letter=int(input("how many cap letters do u want:\n "))
n_symbols=int(input("how many   symbols  do u want:\n"))
n_number=int(input("how many numbers do u wants:\n"))
password=" "
for i in range(1,n_letter+1):
        char = random.choice(letter)
        password = password+char 
for i in range(1,n_number+1):
                char=random.choice(number)
                password=password+char
for i in range(1,n_symbols+1):
        char=random.choice(symbol)
        password=password+char
print(password)