from turtle import*

n=int(input())
shape("turtle")
ang=(n-2)*180/n
for i in range(n):
    forward(200)
    left(180-ang)

mainloop()
