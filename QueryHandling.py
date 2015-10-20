def queryHandling():
    i = 0
    k = 0
    itemQuery = raw_input("Enter the item you wish to query")
    #location is the array of different locations
    #locations is the singular location
    #items is the different elements inside a singular location
    #items[0] is the item number
    #items[1] is the item quantity
    for locations in location:
        for items in locations:
            if items[0] == itemQuery:
                print items[1]
                print "Item"+i" is in location"+k
                i+=1
                return
            else:
                print "There is none of this item in location"+k
                i+=1
                return
        k+=1;
    
