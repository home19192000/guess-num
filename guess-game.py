#import
import random
r = random.randint(1,100)
while True:
	num = input('請猜數字pls:')
	num = int (num)
	if num == r:
		print ('中左了.!!!!!')
		break
	elif num > r:
		print('比答案大呀')
	elif num < r:
		print('比答案小呀')	