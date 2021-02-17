password = 'a123456'
i = 3; #剩餘機會
while True:
	i = i-1
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登入成功')		
		break
	else:
		if i > 0:
			print('密碼錯誤! 還有', i,'次機會')
		else:
			print('錯誤3次，請重置密碼!')
			break

