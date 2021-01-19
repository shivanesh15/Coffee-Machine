a = 400
b = 540
c = 120
d = 9
e = 550
while(True):
    print("")
    print("Write action (buy, fill, take, remaining, exit):")
    x = input()
    if x == "remaining":
        print("The coffee machine has:")
        print(str(a)+" of water")
        print(str(b)+" of milk")
        print(str(c)+" of coffee beans")
        print(str(d)+" of disposable cups")
        print("$"+str(e)+" of money")
    elif x == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        n = input()
        if n == "back":
            continue
        
        elif n == "1":
            if a < 250:
                print("Sorry, not enough water!")
                continue
            else:
                a = a - 250
                c = c - 16
                d = d - 1
                e = e + 4
        elif n == "2":
            if a < 350:
                print("Sorry, not enough water!")
                continue
            else:
                a = a - 350
                b = b - 75
                c = c - 20
                d = d - 1
                e = e + 7
        elif n == "3":
            if a < 200:
                print("Sorry, not enough water!")
                continue
            else:
                a = a - 200
                b = b - 100
                c = c - 12
                d = d - 1
                e = e + 6
        else:
            print("invalid")
                
        print("I have enough resources, making you a cofee!")
    elif x == "fill":
        print("Write how many ml of water do you want to add:")
        f = int(input())
        print("Write how many ml of milk do you want to add:")
        g = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        h = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        i = int(input())
        a = a + f
        b = b + g
        c = c + h
        d = d + i
      
    elif x == "take":
        print("I gave you $"+str(e))
        e = 0
        print("")
        
    else:
        break




