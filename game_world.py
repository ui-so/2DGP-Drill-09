# gmae 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.

from pico2d import *

# world[0] = 0 layer
# world[1] = 1 layer
world = [[],[]] # 게임 내의 모든 객체를 담는 리스트

def add_object(o, depth = 0): # 게임 내에 객체를 추가하는 함수
    world.append(o)

def add_objects(ol, depth=0): # 게임 내에 객체 리스트를 추가하는 함수
    world[depth] += ol

def update(): # 게임 내의 모든 객체를 업데이트하는 함수
    for layer in world:
        for o in layer:
            o.update()

def render(): # 게임 내의 모든 객체를 그리는 함수
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o): # 게임 내에서 객체를 제거하는 함수
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise Exception("월드에 존재하지 않는 객체를 삭제하려고 합니다.")