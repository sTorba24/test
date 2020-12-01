from tkinter import *
root = Tk()
c = Canvas(root, width=540, height=960, bg='white')
c.pack()
data = []
with open('DS7.txt') as f:
    for line in f:
        data.append([int(x) for x in line.split()])

for i in range(len(data)):
    image = c.create_oval(data[i][0],data[i][1], data[i][0], data[i][1], fill='black')

root.mainloop()
image.save('res.png')
