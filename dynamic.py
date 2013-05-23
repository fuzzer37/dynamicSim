#Created by Colin Murphy
#You are free to distribute or change this code as you wish, but you may not sell it
#TODO:
#    add population
#    add tax system based on population
#    get rid of a>b>c>d>e progression and change to a command based program
#    use random numbers from the random library
from random import randint
money = 100
res_total = 0
com_total = 0
ind_total = 0
res_population = 0
com_population = 0
ind_population = 0
i = 0
print "Welcome to SimCity CLI version"
while i==i:
    print `res_total` + " residential squares"
    print `com_total` + " commercial squares"
    print  `ind_total` + " industrial squares"
    print "you have " + `money` + " money" 
    cmd = raw_input("Enter your command") 
    if cmd == "build":
        RCI = raw_input("what type of land do you want to build?")
        if RCI == "r":
            #start residential buy
            print "You have " + `money` + " money"
            print "How much residential land do you want to buy?"
            print "Residential is 10 per square"
            res_b = int(raw_input("How much do you want to buy?"))
            money = money-(10*res_b)
            res_total = res_total +res_b
            
        if RCI == "c":
            
                
            #start commercial buy
            print "You have " + `money` + " money"
            print "Commercial is 20 per square"
            com_b = int(raw_input("How much do you want to buy?"))
            money = money-(20*com_b)
            com_total = com_total +com_b
        if RCI == "i":
                
            #start industrial buy 
            print "You have " + `money` + " money"
                
            print "Industrial is 30 per square"
            ind_b = int(raw_input("How much do you want to buy?"))
            money = money-(30*ind_b)
            ind_total = ind_total +ind_b
        if RCI == "road":
            #start all things that create multiplyers.
            print "You have " + `money` + " money"
            print "roads cost 5 dollars each"
            print "roads increase the population"
            roads = int(raw_input("how many peices of road do you want to buy?"))
            
    #residential population
    if i > 0:
        res_population += res_population * randint(1, 2) + ( .5 * res_b)
        print "You have " + `res_population` + " residential population"
        
    else:
        res_population = res_total * randint(1, 2)
        
        
    #commercial population
    if i > 0:
        com_population += com_population * randint(1, 2) + ( .5 * com_b)
        print "You have " + `com_population` + " commercial population"
        
    else:
        com_population = com_total * randint(1, 2)
        print "You have " + `com_population` + " commercial population"
        
        
    #industrial population
    if i > 0:
        ind_population += ind_population * randint(1, 2) + ( .5 * ind_b)
        print "You have " + `ind_population` + " industrial population"
        
    else:
        res_population = res_total * randint(1, 2)
        print " You have " + `ind_population` + " industrial population"
        
    money += (res_population * 1)
    money += (com_population * 2)
    money += (ind_population * 3)
        
    #money += res_population * 1
        
        
    i+=i
