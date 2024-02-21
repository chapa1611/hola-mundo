from random import randint
n1 = randint (1 , 10)
n2 = randint (1 , 10)
if n1 > n2:
    print (n1, "Es mayor")
elif n2 > n1:
    print (str(n2) + "Es mayor")
else:
    print (str(n1) + "=" + str(n2))