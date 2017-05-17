from PIL import Image
im = Image.open("sidd1.jpg")
pix = im.load()
print (im.size) #Get the width and hight of the image for iterating over
x = im.size[0]
y = im.size[1]
for i in range(x):
  for b in range(y):
    print(pix[i,b])
    val1 = ((pix[i,b])[0])+100
    val2 = ((pix[i,b])[1])-100
    val3 = ((pix[i,b])[2])+150
    if(val1>200):
      val1 = 0
      val2 = 0
      val3 = 0
    pix[i,b] = (val1, val2, val3)
im.save("sidd2.png") # Save the modified pixels
