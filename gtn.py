import random
r = random.randint(1, 100)
while True :
	num = input('請輸入數字：')
	num = int(num)
	if num == r :
		print('恭喜猜對！')
		break
	elif num != r and num > r:
		print('猜錯囉，比答案大')
	elif num != r and num < r:
		print('猜錯囉，比答案小')