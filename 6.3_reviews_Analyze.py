#讀取reviews.txt檔案中100萬筆留言
#因每筆print動作太耗時
#改以 % 取餘數方式
# 每1000筆印一次，已印資料長度

data = []
count = 0
sumDataString = 0
with open('6.3r_reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

			# 去倒個別留言中的'字元'
			# for s in data[1].strip():
			# 	print(s)

		# 去平均留言長度
		sumDataString += len(data[count-1])
		
print('總共留言長度: ', sumDataString)		
print('留言平均長度: ', sumDataString/len(data))
print('檔案讀取玩了, 總共有', len(data), '筆資料.')
print(data[0])
print('----------------------------')
print(data[1])

print('----------------------------')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print(sum_len/len(data))