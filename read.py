data = []
with open ('reviews.txt', 'r') as f :
	for line in f :
		data.append (line)
#print(len(data))
#print(data) 顯示全部的比數
print(data[0])
print('------------------')
print(data[1])


sum_len=0
for d in data:
	sum_len = sum_len + len(d)
print ('留言的平均長度', sum_len/len(data))
# 讀取data 架構 
#需要再理解一下 在length 中 長data  跟在 最外層不同