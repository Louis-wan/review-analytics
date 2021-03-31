data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count +1
		if count % 1000 == 0:#餘數
			print(len(data))
print(len(data)) 

print(data[3])
print(data[5])
