from PIL import ImageGrab,Image
import pyautogui,time
#a=input()
#b=input()
img=ImageGrab.grab([249, 717,623, 267])
#img.save("D:\\aww.png")
#img=Image.open("D:\\aww.png")
width, height = img.size
#img=img.crop((135,296,274,386))
#img.save("D:\\aww.png")
time.sleep(4)
rgb_im = img.convert('RGB')
for x in range(width):
	for y in range(height):
		r,g,b=rgb_im.getpixel((x,y))
		#print (r,g,b)
		if (r==0 and b==0 and g==0):
			print(x,y)
			pyautogui.click(249+x, 717+y, button='left')