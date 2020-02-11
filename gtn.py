import random
r = random.randint(1, 100)
x = 0
while True :
	num = input('請輸入數字：')
	num = int(num)
	if num == r :
		print('恭喜猜對！答案為：',r,' 共花了',x,'次')
		x = x + 1
		break
	elif num != r and num > r:
		print('猜錯囉，比答案大')
		x = x + 1
	elif num != r and num < r:
		print('猜錯囉，比答案小')
		x = x + 1