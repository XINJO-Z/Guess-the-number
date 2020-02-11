import random
s = input('請決定隨機數字範圍開始值：')
e = input('請決定隨機數字範圍結束值：')
s = int(s)
e = int(e)
r = random.randint(s, e)
x = 0
while True :
	num = input('請猜數字：')
	num = int(num)
	if num == r :
		print('恭喜猜對！答案為：',r,' 共花了',x,'次')
		x = x + 1
		break
	elif num > r:
		print('猜錯囉，比答案大')
		x = x + 1
	elif num < r:
		print('猜錯囉，比答案小')
		x = x + 1