name = input('請輸入名子:' )
print('Hi', name)

# input輸入內容會自動轉會為字串，會自動加''字串符號，需要casting
age = input('輸入年齡:')
age = int(age)
if age >= 20:
	print(age, '歲可以投票')
elif age >= 13 and age <18:
	print('您是國小生 ', age ,'歲，還未到達投票年紀20，再等等吧')
else:
	print('還沒上學呢!等上學後再想投票的事吧')