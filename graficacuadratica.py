import turtle

#Constantes

UNO_X = turtle.window_width()/16
UNO_Y = turtle.window_height()/16

turtle.screensize(500,500)
turtle.speed(0)

def dibujar_ejes_cartesianos():
	mY = turtle.window_height()/2
	mX = turtle.window_width()/2
	tY = turtle.window_height()
	tX = turtle.window_width()
	turtle.pu()
	turtle.setx(-mX)
	turtle.sety(-mY)
	turtle.pen(pencolor="black", pensize=1)
	while(340 > turtle.xcor()):
		turtle.pd()
		turtle.forward(UNO_X)
		while(288 > turtle.ycor()):
			turtle.left(90)
			turtle.forward(UNO_Y)
			turtle.left(90)
			turtle.forward(UNO_X)
			turtle.right(180)
			turtle.forward(UNO_X)
		turtle.right(90)
		turtle.forward(tY)
		turtle.left(90)
	turtle.setx(-mX)
	turtle.sety(0)
	turtle.pen(pencolor="blue", pensize=3)
	turtle.forward(tX)
	turtle.setx(0)
	turtle.sety(-mY)
	turtle.left(90)
	turtle.forward(tY)
	turtle.right(90)
	turtle.setx(0)
	turtle.sety(0)
	
def parabola_cuadratica(a, b, c):
	puntos = {'-3' : a**2, '-2' : (a+2)**2, '-1' : (a+3)**2, '0' : (a+4)**2, '1' : (a+5)**2, '2' : (a+6)**2, '3' : (a+7)**2}
	print puntos
	turtle.setx(0)
	turtle.sety(0)
	turtle.pu()
	turtle.pen(pencolor="red", pensize=5)
	turtle.goto(turtle.pos() + (UNO_X*-3, UNO_Y*puntos['-3']))
	turtle.pd()
	turtle.goto(UNO_X*-2, UNO_Y*puntos['-2'])
	turtle.goto(UNO_X*-1, UNO_Y*puntos['-1'])
	turtle.goto(UNO_X*0, UNO_Y*puntos['0'])
	turtle.goto(UNO_X*1, UNO_Y*puntos['1'])
	turtle.goto(UNO_X*2, UNO_Y*puntos['2'])
	turtle.goto(UNO_X*3, UNO_Y*puntos['3'])

dibujar_ejes_cartesianos()
#Por ahora lo que seria 'a' solo funciona con negativos
parabola_cuadratica(-3, 2, -5)
raw_input()
