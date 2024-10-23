from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def update():
    if held_keys['w']:
        player.y += num * 0.01
    elif held_keys['s']:
        player.y -= num * 0.01
    elif held_keys['d']:
        player.x += num * 0.01
    elif held_keys['a']:
        player.x -= num * 0.01
    elif held_keys['escape']:
        quit()

# sky()
num = 10
app = Ursina()

player = Entity(model='quad', color=color.green, position=(-6.7, -0.9), scale=(0.7, 0.7, 0.7))
ground0 = Entity(model='quad', color=color.white, position=(-6.7, -2.6), scale=(1, 2.6, 1))
ground1 = Entity(model='quad', color=color.white, position=(-5.2, -2.6), scale=(1, 2.6, 1))
ground2 = Entity(model='quad', color=color.white, position=(-3.7, -2.6), scale=(1, 2.6, 1))
ground3 = Entity(model='quad', color=color.white, position=(-1.7, -2.6), scale=(1, 2.6, 1))
ground4 = Entity(model='quad', color=color.white, position=(0.7, -2.6), scale=(1, 2.6, 1))
ground5 = Entity(model='quad', color=color.white, position=(2.7, -2.6), scale=(1, 2.6, 1))
ground6 = Entity(model='quad', color=color.white, position=(4.7, -2.6), scale=(1, 2.6, 1))
ground7 = Entity(model='quad', color=color.white, position=(6.7, -2.6), scale=(1, 2.6, 1))

app.run()
