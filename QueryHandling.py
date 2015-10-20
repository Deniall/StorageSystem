def queryHandling():
    location = [[(1,2),(2,1),(3,3)],[(1,9),(3,8),(2,4)]]
    item = [(6,2),(9,3),(10,5)]
    i = 0
    k = 0
    itemQuery = int(raw_input("Enter the item number you wish to query: "))
    #location is the array of different locations
    #locations is the singular location
    #items is the different elements inside a singular location
    #items[0] is the item number
    #items[1] is the item quantity
    for locations in location:
        for items in locations:
            if items[0] == itemQuery:
                print "Item "+str(i)+" is in Location "+str(k)
                print "There is "+str(items[1])+" of Item"+str(i)+" in Location"+str(k)
                i+=1
            
        k+=1;
    
