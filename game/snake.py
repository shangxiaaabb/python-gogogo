"""
实现基本操作:
1、蛇必须受到我的控制
2、在得到食物的时候蛇的长度必须增加
3、食物的位置必须随机出现
4、蛇在咬到自己的时候必须死掉

补充操作：
1、控制蛇的速度
2、开挂！！---我要无敌
"""

from turtle import *
from random import randrange
from gamebase import square

# 第一步设置边界
def square(x, y, size, color_name):
    up()
    goto(x, y)
    down()
    color(color_name)
    begin_fill()

    forward(size) # 前进步长
    left(90) # 旋转90度
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

    end_fill()

# 判断是否撞墙
def inside():
    if -200 <= snake[-1][0] <= 180 and -190 <= snake[-1][1] <= 190:
        return True
    else:
        return False

# 判断蛇是否咬自己
def inside_snake():
    for n in range(len(snake)-1):
        if snake[-1][0] == snake[n][0] and snake[-1][1] == snake[n][1]:
            return True
    return False
    
# 蛇的绘制函数
def gameLoop():
    global apple_x, apple_y
    snake.append([snake[-1][0]+aim_x, snake[-1][1]+aim_y])
    if (not inside()) or inside_snake():
        square(snake[-1][0], snake[-1][1], 10, "red")
        update()
        return
    if snake[-1][0] != apple_x or snake[-1][1] != apple_y:
        snake.pop(0)
    else:
        apple_x = randrange(-20, 18)*10
        apple_y = randrange(-19, 19)*10
    clear()
    square(-210, -200, 410, "black")
    square(-200, -190, 390, "white")
    square(apple_x, apple_y, 10, "red")
    for n in range(len(snake)):
        square(snake[n][0], snake[n][1], 10, "black")
    ontimer(gameLoop, 100)
    update()

# 蛇的方向改变
def change(x, y):
    global aim_x, aim_y
    aim_x = x
    aim_y = y

# 定义变量
snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]] # 蛇的最后一个元素代表蛇头
apple_x = randrange(-20, 18)*10
apple_y = randrange(-19, 19)*10
aim_x = 10
aim_y = 0

# 主体函数
setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(10, 0), "Right")
gameLoop()
done()
