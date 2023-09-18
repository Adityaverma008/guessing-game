


# os.listdir(os.getcwd())
import random
human = int(input("enter the number b/w 1 to 100 :- "))


#x = [1,2,3,4,5,6,7,8,9]
computer = random.randint(1,100)
# print(human)


if human == computer :
    print("both are printing {} ".format (human))

elif human > computer :
    print(" hint - please guess low")

elif human < computer :
    print("hint - please guess high ")

else :
    print("hint - wrong approch")

print("computer chooses :- {}".format(computer))