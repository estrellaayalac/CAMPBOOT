import rodi
import time

robot = rodi.RoDI()

while True:
    robot.move_forward()
    print(robot.see())
    time.sleep(0.1) 
    if robot.see() < 10:
        robot.move_left()
        time.sleep(0.5)
        robot.move_forward()
        time.sleep(2)

        ssssssssssssssss