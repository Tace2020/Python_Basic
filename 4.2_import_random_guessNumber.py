#決定範圍
#猜數字

import random
start = input('請決定隨機數字\'開始\'值: ')
start = int(start) 
end = input('請決定隨機數字\'結束\'值: ')
end = int(end)

while end<start:
	end = input('結束值須比開始值大，請重新輸入結束值: ')
	end = int(end)

print('猜數字範圍 ',start ,' ~ ', end)
r = random.randint(start,end)
print(r)
count = 0
while True:
	count += 1
	num = input('請猜數字 ' )
	num = int(num)
	if num > r:
		print('比答案大')
	elif num < r :
		print('比答案小')
	else:
		print('終於猜對了!!')
		print('你總共猜了', count,'次')
		break
	print('這是你猜的第', count,'次')
