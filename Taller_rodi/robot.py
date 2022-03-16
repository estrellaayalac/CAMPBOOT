import rodi
import time

robot = rodi.RoDI()

while True:
    robot.move_backward()
    time.sleep(3)

    if robot.see() < 10:
        robot.move_stop()
        robot.move_left()
        time.sleep(0.5)
        robot.move_forward()
        time.sleep(2)
        break



 #Creamos un objeto rodi con todos los parametros de la libreria. traemos de otro archivo la clase que es rodi.py

'''
robot = rodi.RoDI() 
robot.move_backward()
time.sleep(2)
robot.move_right()
time.sleep(0.5)
robot.move_backward()
time.sleep(2)
robot.move_right()
time.sleep(0.5)
robot.move_backward()
time.sleep(2)
robot.move_right()
time.sleep(0.5)
robot.move_backward()
time.sleep(2)
robot.move_right()
time.sleep(0.5)
robot.move_stop()
''
robot = rodi.RoDI() 
robot.move_backward()
time.sleep(40)
robot.move_left()
time.sleep(1)
robot.move_backward()
time.sleep(40)
robot.move_stop()
'''

'''
robot = rodi.RoDI()
robot.move_backward()
time.sleep(5)
robot.move_stop()
'''

'''
#que cante
def estrellita_song():
    robot.move_backward()
    robot.sing(523.25,500) #500 esta en milisegundos
    time.sleep(0.5)
    robot.sing(523.25,500)
    time.sleep(0.5)
    robot.sing(783.99,500)
    time.sleep(0.5)
    robot.sing(783.99,500)
    time.sleep(0.5)
    robot.sing(880,500)
    time.sleep(0.5)
    robot.sing(880,500)
    time.sleep(0.5)
    robot.sing(783.99,1000)
    time.sleep(1)
    robot.sing(698.46,500)
    time.sleep(0.5)
    robot.sing(698.46,500)
    time.sleep(0.5)
    robot.sing(659.26,500)
    time.sleep(0.5)
    robot.sing(659.26,500)
    time.sleep(0.5)
    robot.sing(587.33,500)
    time.sleep(0.5)
    robot.sing(587.33,500)
    time.sleep(0.5)
    robot.sing(523.25,1000)
    time.sleep(1)
estrellita_song()
'''
'''
#Sensor de distancia 
while True: 
    print(robot.see())
    time.sleep(0.1) #tiempo de que lea 
'''


"""
while True:
    try:
        robot.move_backward()
        ""print (robot.see())
        time.sleep(0.1)""
    except KeyboardInterrupt: #Control C
        robot.move_stop()
        break
"""

while True:
    linea = robot.sense()
    print(linea[0]) #Sensor de linea izquierdo
                   #(0== Negro y 1023 ==blanco)
    print(linea[1]) #Sensor de linea derecho
                   #(0== Negro y 1023== blanco)
    time.sleep(0.1)

    if linea[0] < 50 and linea[1] < 50:
        robot.move_backward()
    elif linea[0]
