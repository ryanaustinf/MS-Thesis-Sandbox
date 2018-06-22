def collate(filename,expertId):
	expert1 = True;
	ratings = []
	for x in expertId:
		file = open("%s - %02d.csv" % (filename,x),"r")
		first = True;
		i = 1
		for line in file:
			if first:
				first = False
				continue
			else:
				temp = line.split(",")
				if expert1:
					ratings.append({"image":temp[0],"ratings":[]})
					for j in range(1,5):
						ratings[i-1]['ratings'].append(int(temp[j].strip()))
				else:
					for j in range(1,5):
						ratings[i - 1]['ratings'][j-1] += int(temp[j].strip())
			i += 1
		if expert1:
			expert1 = False
		file.close()
	file = open(filename + ".csv","w")
	file.write("Screenshot,Visibility of System Status,Match Between System and Real World,Error Prevention,Minimalist Design\n")
	for rating in ratings:
		file.write(rating['image'])
		for x in rating['ratings']:
			file.write("," + str(int(round(x * 1.0 /len(expertId)))))
		file.write("\n")

collate("Expedia",[4,11,23])