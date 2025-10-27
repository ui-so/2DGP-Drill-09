from pico2d import *
from boy import Boy
from grass import Grass
import game_world


# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global boy

    boy = Boy()
    game_world.add_object(boy,1)  # 게임 월드에 소년 객체 추가

    grass_1 = Grass(400, 30)
    game_world.add_object(grass_1,0) # 게임 월드에 잔디 객체 추가

    grass_2 = Grass(400, 10)
    game_world.add_object(grass_2,2) # 게임 월드에 잔디 객체 추가


def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
