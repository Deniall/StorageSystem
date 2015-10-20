def queryHandling():
    locations = [[(1,2),(2,1),(3,3)],[(1,9),(3,8),(2,4)]]
    #items = [(6,2),(9,3),(10,5)]
    i = 0
    k = 0
    itemQuery = int(raw_input("Enter the item you wish to query: "))
    #location is the array of different locations
    #locations is the singular location
    #items is the different elements inside a singular location
    #items[0] is the item number
    #items[1] is the item quantity
    for location in locations:
        for item in location:
            if item[0] == itemQuery:
                print "Item"+str(i)+" is in location"+str(k)
                print "There is "+str(item[1])+" of item"+str(i)+" in location"+str(k)
            i+=1
        i = 0
        k+=1;
    
