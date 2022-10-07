import time
import winsound
winsound.Beep(1000, 200)

x = 150

while True:

	time.sleep(120)

	winsound.Beep(2500, 100)

	print("A minute got over!")

	if x <= 0:
		break

	x -= 1