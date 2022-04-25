import random as rann
print("*************************")
print("SPAMMER TERMUX 1.0")
print("*************************")
print("Начать(start), свой текст(mytext)")
whatspam = input("Command:")
if whatspam == "start":
  while whatspam:
    av = rann.randint(100,80000000000)
    print(str(av))
elif whatspam == "mytext":
  whatmytext = input("Ваш текст:")
  whatmytext1 = input("Начать? yes/no:")
  if whatmytext1 == "yes":
    while whatmytext1:
      print(str(whatmytext))
  else:
    print(":D")
    exit()
else:
  print ("Errrrrr :D")
input()