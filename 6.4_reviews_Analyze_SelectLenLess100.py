#讀取reviews.txt檔案中100萬筆留言
#因每筆print動作太耗時
#改以 % 取餘數方式
# 每1000筆印一次，已印資料長度

data = []
count = 0
sumDataString = 0
tmp = 0
with open('6.3r_reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 1000 == 0:
			#print(len(data)) 每1000筆，印出當前印到的留言行數

			# 去倒個別留言中的'字元'
			# for s in data[1].strip():
			# 	print(s)

		# 計算平均留言長度 方法1
		sumDataString += len(data[count-1])
		if len(data[count-1])<100:
			tmp += 1
			print('第 ',len(data),' 筆資料，留言長度小於100')
			print('留言內容: ', data[count-1])

print('共', tmp,'筆留言小於100')
print('總共留言長度: ', sumDataString)		
print('留言平均長度: ', sumDataString/len(data))
print('檔案讀取玩了, 總共有', len(data), '筆資料.')


# d 字串 , data 清單
# 篩選出留言字數小於100的留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d) #把小於100了留言，放入新清單中
print('一共有',len(new),'筆留言長度小於100')

# 內容有good的留言
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),' 筆留言提到good')
print(good[0])

# 字串運用
# 'a' in 'abc' -> TRUE
# '1' in 'abc' -> False

