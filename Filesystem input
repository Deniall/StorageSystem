itemData = []
storageData = []

with open("itemList.txt","r") as tempItemData:
	pair = []
	value = []
	global itemData
	for line in tempItemData:
		pair = pair + line.split(";")
		for elem in pair:
			subElem = elem.split(",")
			itemData.append([int(subElem[0]),int(subElem[1])])

with open("storageList.txt","r") as tempStorageData:
	pair = []
	value = []
	global storageData
	for line in tempStorageData:
		pair = pair + line.split(";")
		for elem in pair:
			subElem = elem.split(",")
			storageData.append([int(subElem[0]),int(subElem[1])])
