def getLocations(items, locations):
    print items
    print locations

    done = False
    returnArray = [[]for _ in xrange(len(locations))]
    #while not done:
    #for i in range(len(locations)):
    #    location = locations[i]
    #    capacity = location[0]
    #    returnArray.append([])
    ###
    i = 0
    while not done:
        
        done = True
        for item in items:
            if item[0] != 0:
                print item
                print i
                print returnArray
                done = False
                break
        
        for j in range(len(items)):
            location = locations[i]
            item = items[j]
            if item[0] < item[1] and location[0] >= item[0]:
                returnArray[i].append([j, item[0]])
                location[0] -= item[0]
                item[0] = 0
            elif item[0] < item[1] and location[0] < item[0]:
                returnArray[i].append([j, location[0]])
                item[0] -= location[0]
                location[0] = 0
                i += 1
            elif item[0] < item[1] and location[0] > item[0]:
                returnArray[i].append([j, item[0]])
                location[0] -= item[0]
                item[0] = 0
            elif item[1] > location[0]:
                returnArray[i].append([j, location[0]])
                item[0] -= location[0]
                location[0] = 0
                i += 1
            else:
                returnArray[i].append([j, item[1]])
                location[0] -= item[1]
                item[0] -= item[1]

        
        
    print returnArray
    return returnArray
