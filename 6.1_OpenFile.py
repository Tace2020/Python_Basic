#讀取檔案是自訂名子，程式碼用到檔案可套用此

# r讀取模式/w寫入模式
# as f 當作 file(f是自訂名子，程式碼用到檔案可套用此) 
# pint本身換行,\n又換行
# .strip()去掉換行、結尾空格，只能對字串去做
# .append()只能對清單做
# open打開檔案，(以前程式需要開檔案、關檔案)
# with功能，會有自動close的功能，在with 的區塊中會開檔案，離開就自動關檔案

data = []
with open('6_ReadSource_food.txt', 'r') as f:
	for line in f:
		print(line)
		data.append(line)
		data.append(line.strip())

print(data)