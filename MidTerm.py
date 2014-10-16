#1. 7 
#2.(b^n)
#3
def totalBill(x): 
  checkAmount=x +(.15*x)
  return checkAmount 
#4
def newpic(): 
  pic = makeEmptyPicture(200,200, (makeColor(18,52,86)))
  show(pic)

#5
def fib(n):
  if n<=0:
   return 
  if n>=1: 
    print 1 
    d1=1
  if n>=2:
    print 1
    d2=1
  for num in range (n-2):
     v = d1+ d2
     print v
     d1=d2
     d2 = v


#6 
def List():
  a=[1,2,3,4,5]
  print a
  
#7
def problem7():
  pic=makeEmptyPicture(800,800, white)
  pic2=makeEmptyPicture(100,100,black) 
  for x in range(0,8,2):
    for y in range(1,8,2):
      copyInto(pic2,pic, x*100,y*100)
  for x in range (1,8,2):
    for y in range (0,8,2):
       copyInto(pic2,pic,x*100,y*100)
  show(pic)
       
#8. Makes black and white tiles        

#9. function B is not defined      
def functionA(x,y):
   print functionB(x)
   print functionB(y)
def functionB(a):
    return a*a
#10. d= sqrt((100-50)2+(50-10)2+(150-50)2)=118.74

#11.     
def removeRed():
  pic=makePicture(pickAFile())
  for p in getPixels(pic):
    setRed(p,0)
  show(pic)

#12. 39, 49, 28 

#13
def colorSwap():
   pic=makePicture(pickAFile())
   for p in getPixels(pic): 
     red = getRed(p) 
     green=getGreen(p)
     blue=getBlue(p) 
     distance=sqrt((red*2)+(green*2)+(blue*2))
     if distance>222:
       setColor(p, white) 
     else: 
       setColor(p,black) 
   show(pic)
   
#14. Draws a circle at 150,150 

#15
def drawCircle(pic,diameter):
  for i in range(628):
    x=diameter*cos(2*pi*i/628)+150
    y=diameter*sin(2*pi*i/628)+150
    p=getPixel(pic,int(x),int(y))
    setColor(p,black)
def makeCircles():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  show(pic)  

#16. Makes the center circle red
 
#17   
def colorCenter(pic,diameter):
  for p in getPixels(pic):
    if sqrt(pow(getX(p)-150,2) + pow(getY(p)-150,2)) < diameter:
      setColor(p,red)
def makeCircle():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  colorCenter(pic,25)
  show(pic)  

#18. Write a program that draws an x on a 300x300 white square and use it to modify the picture
def drawX(pic):
      addLine(pic, 0, 0,300, 300)   
      addLine(pic, 300,0 ,0, 300)  
def xCircle():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  colorCenter(pic,25)
  drawX(pic)
  show(pic)
   
   

#19. Write a program that draws a vertical and horizontal line through the image
def makeX(pic):
      addLine(pic, 0, 0,300, 300)   
      addLine(pic, 300,0 ,0, 300)
      addLine(pic, 150,0 ,150,300)  
      addLine(pic, 0,150 ,300,150)      
def xCircle2():      
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  colorCenter(pic,25)
  makeX(pic)
  show(pic)
   

#20. 1,048,576 
 
