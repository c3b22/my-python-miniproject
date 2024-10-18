'bug list'
"1. hit' auto win"
"2. stand' auto burn"


import random
money = int(input("Enter your money :"))
"loop"
while money > 0 :
    n = random.randint(1,11)
    n1 = random.randint(1,11)
    n2 = random.randint(1,11)
    n3 = random.randint(1,11)
    bet = int(input("Enter your bet :"))
    e_money = money - bet
    if e_money >= 0 :
        print (n,n1)
        bot = n2 + n3
        print ('bot : x,',n2)

        "bot"
        if bot <= 15 :
            bot_n = random.randint(1,11)
            bot = n2 + n3 + bot_n
            print ("bot : x,",n2,",",n3)
            if bot <= 15 :
                bot_n1 = random.randint(1,11)
                bot = n2 + n3 + bot_n + bot_n1
            else :
                bot_n1 = 0 
        else :
            bot_n = 0
            bot_n1 = 0
            bot = n2 + n3
    
        a = str(input("hit[1] or stand[2] :"))
        "\\ใช้strเพราะกำหนดตัวเเปรเป็นตัวอักษร"

        "player"
        if a == 'hit' :
            n_1 = random.randint(1,11)
            print (n,n1,n_1)
            b = str(input("hit or stand :"))
            if b == 'hit' :
                n_2 = random.randint(1,11)
                print (n,n1,n_1,n_2)
                total_n = n+n1+n_1+n_2
                c = str(input("hit or stand :"))
                if c == 'hit' :
                    n_3 = random.randint(1,11)
                    print (n,n1,n_1,n_2,n_3)
                    total_n = n+n1+n_1+n_2+n_3

            if b == 'stand' :
                total_n = n+n1+n_1
                print ("\n")
        if a == 'stand' :
            total_n = n+n1
            print ("\n")

        "money"    
        if total_n and bot <= 21 :
            if total_n < bot:
                total = money - bet
                print ('bot :',n2,",",n3,",",bot_n,",",bot_n1)
                print ("your lose")
                print ("money :",total)
            if total_n == bot :
                total = money
                print ('bot :',n2,",",n3,",",bot_n,",",bot_n1)
                print ("money :",money)
                print ("draw")
            if bot < total_n :
                if total_n == 21 :
                    print ('bot :',n2,",",n3,",",bot_n,",",bot_n1)
                    total = money + 2*bet
                    print ("blackjack!")
                    print ('money :',total)
                if total_n < 21 :
                    print ('bot :',n2,",",n3,",",bot_n,",",bot_n1)
                    total = money + bet
                    print ("win")
                    print ("money :",total)
        if bot > 21 :
            print ('bot :',n2,",",n3,",",bot_n,",",bot_n1)
            total = money + bet
            print ("bot burn")
            print ("money :",total)
        if total_n > 21 :
            print ('bot :',n2,",",n3,",",bot_n,",",bot_n1)
            total = money - bet
            print ("burn")
            print ("money :",total)
        if bot and total_n > 21 :
            if bot > total_n :
                print ("you win")
                total = money + bet
                print (total)
            if total_n > bot :
                print ("you lose")
                total = money - bet
                print (total)
        money = total
        print ("\n")
    else :
        print ("a little cheater")
else :
    print ("see you next time")
