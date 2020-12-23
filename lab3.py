from tkinter import *


def rotate(A,B,C):
    return(B[0]-A[0])*(C[1]-B[1]) - (B[1]-A[1])*(C[0]-B[0])


root = Tk()
c = Canvas(root, width=540, height=960, bg='white')
c.pack()
data = []
with open('DS7.txt') as f:
    for line in f:
        data.append([int(x) for x in line.split()])
for i in range(len(data)):
    image = c.create_oval(data[i][0],data[i][1], data[i][0], data[i][1], fill='black')


pixel_count = len(data)
P = list(range(pixel_count))
  # start point
for i in range(1,pixel_count):
  if data[P[i]][0]<data[P[0]][0]: 
    P[i], P[0] = P[0], P[i]  
res = [P[0]]
P.append(P.pop(0))


while True:
  right = 0


  for i in range(1,len(P)):
    if rotate(data[res[-1]],data[P[right]],data[P[i]])<0:
      right = i
  
  if P[right]==res[0]: 
    break
  
  else:
    res.append(P.pop(right))
      


for i in range(len(res)-1):
    dot1 = data[res[i-1]]
    dot2 = data[res[i]]
    
    # малюємо відрізок синього кольору між 2 точками
    image = c.create_line((dot1[0], dot1[1], dot2[0], dot2[1]), fill='blue')

root.mainloop()


with open('convex hull.txt', 'w') as file:
    for i in res:
        file.write(f"{data[i][0]} {data[i][1]}\n")
   
image.save('res.jpg')

