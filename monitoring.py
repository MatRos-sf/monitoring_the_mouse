from pynput import mouse 
import math
import time
CLICK = 0
def euclidean_distance():
	#euclidean_distance
	d = 0
	# arr with distaces	
	tab = []
	
	#open file with all distances
	with open('distances.txt','r') as f:
		for i in f:
			x,y= (int(j) for j in i.strip().split(';'))
			tab.append((x,y))

	#https://en.wikipedia.org/wiki/Distance#:~:text=The%20distance%20between%20two,plane%20is%20given%20by
	x1, y1 = tab[0][0], tab[0][1]
	for i in range(1,len(tab)):
		
		X = pow(x1 - tab[i][0],2)
		Y = pow(y1 - tab[i][1],2)
		d += math.sqrt(X + Y)
		
		x1, y1 = tab[i][0], tab[i][1]

	return d

def on_move(x,y):
	global CLICK
	with open('distances.txt', 'a') as f:
		f.write(f"{x};{y}\n")
	
	CLICK = 0

def on_click(x,y,button, pressed):
	global CLICK
	if pressed:
		CLICK += 1
	if CLICK == 4:
		return False

def clean_file(name='distances.txt'):
	
	f = open(name,'w')
	f.close()

def main():

	clean_file()
	start_time = time.time()

	with mouse.Listener(on_move=on_move,
		on_click=on_click) as listener:
		listener.join()
	print('Calculating ')
	whole_time = time.time() - start_time
	distance = euclidean_distance()
	print(f"Whole distance: {distance} unit.")
	print(f"Speed moving: {round(distance/whole_time,5)} unit/s")

if __name__ == '__main__':
	main()


