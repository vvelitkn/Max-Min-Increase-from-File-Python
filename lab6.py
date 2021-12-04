try:
	year = 1950
	liste = [int(line.rstrip()) for line in open('USPopulation.txt', 'r')]
	dic = {}
	valuedic = {}
	for i in range (0, len(liste)-1):
		temp = liste[i+1]-liste[i]
		dic[temp] = year+1		#1 ekliyoruz çünkü ikinci eksi birinci eşittir ikinci yılın büyümesi ama i=0 iken temp değeri ikinci yıl için değer alıyor
		year +=1
	a = max(dic)
	b = min(dic)

	print('The greatest increase in population was', dic[a])
	print('The smallest increase in population was', dic[b])

except IndexError:
	print('The line number is outside of the range, please try again')