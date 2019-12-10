print('最多輸入三次密碼')
x = 2
while True:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	elif x == 0:
		print('密碼錯誤，鎖定')
		break
	else:
		print('密碼錯誤! 還有',x,'次機會')
		x = x - 1
	