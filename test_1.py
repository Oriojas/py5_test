import py5
import random


def setup():
    py5.size(800, 800)
    py5.rect_mode(py5.CENTER)
    py5.frame_rate(500)


def draw():
    if py5.is_mouse_pressed:
         py5.stroke(py5.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
         py5.stroke_weight(random.randint(0, 20))
         py5.point(py5.mouse_x - random.randint(0, 30) , py5.mouse_y - random.randint(0, 30))

py5.run_sketch()
  
