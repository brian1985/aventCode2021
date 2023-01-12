import numpy as np
from time import perf_counter

with open("data\\day9.txt") as f:
    data = f.read().split()
    for idx, d in enumerate(data):
        data[idx] = [int(d1) for d1 in list(d)]

    data = np.array(data)

#  essential part a find the locations of the lowest point of each basin which then is used to feed into part b
def part_a():
    counter = 0
    points_checked = []
    min_locations = []
    for i in np.arange(1,data.shape[0]-1):
        for j in np.arange(1,data.shape[1]-1):
            # points_checked.append([i,j])
            if data[i,j] < min(data[i,j+1],data[i,j-1],data[i+1,j],data[i-1,j]):
                counter += data[i,j]
                counter += 1
                min_locations.append([i,j])

                #top bottom lines
    for j in np.arange(1,data.shape[1]-1):
        points_checked.append([0, j])
        points_checked.append([data.shape[0]-1, j])

        if data[0,j] < min(data[0,j+1], data[1,j],data[0,j-1]):
            counter += data[0,j] + 1
            min_locations.append([0,j])
        if data[data.shape[0]-1,j] < min(data[data.shape[0]-1,j+1], data[data.shape[0]-2,j],data[data.shape[0]-1,j-1]):
            counter += data[data.shape[0]-1,j] + 1
            min_locations.append([data.shape[0]-1,j])

      # left right vert lines in case not square
    for i in np.arange(1,data.shape[0]-1):

        if data[i,0] < min(data[i+1,0], data[i,1],data[i-1,0]):
            counter += data[i,0] + 1
            min_locations.append([i,0])

        if data[i,data.shape[1]-1] < min(data[i+1,data.shape[1]-1], data[i,data.shape[1]-2],data[i-1,data.shape[1]-1]):
            counter += data[i,data.shape[1]-1] + 1
            min_locations.append([i,data.shape[1]-1])

               #top left
    if (data[0,0] < data[0,1]) & (data[0,0] < data[1,0]):
        counter += d[0,0] + 1
        min_locations.append([0,0])

    # top right
    if data[0, data.shape[1]-1] < data[0, data.shape[1]-2] & data[0, data.shape[1]-1] < data[1, data.shape[1]-1]:
        counter += data[0, data.shape[1]-1] + 1
        min_locations.append([0, data.shape[1]-1])

        #bottom left
    if data[data.shape[0]-1,0] < data[data.shape[0]-1,1] & data[data.shape[0]-1,0] < data[data.shape[0]-2,0]:
        counter += data[data.shape[0]-1,0] + 1
        min_locations.append([data.shape[0]-1,0])

        #bottom right
    if data[data.shape[0]-1,data.shape[1]-1] < data[data.shape[0]-1,data.shape[1]-2] & data[data.shape[0]-1,data.shape[1]-1] < data[data.shape[0]-2,data.shape[1]-1]:
        counter += data[data.shape[0]-1,data.shape[1]-1] + 1
        min_locations.append([data.shape[0]-1,data.shape[1]-1])

    return min_locations, counter


def part_b(basins, data, shape):
    def cumulator(i,j):
        right_cumulator = left_cumulator = up_cumulator = down_cumulator = 0
        # print("D",i,j)
        if mask[i,j] == 0:
            return 0
        else:
            mask[i,j] = 0
            if j < shape[1]-1:
                # print(i,j,"right")
                right_cumulator = cumulator(i,j+1)
            if j > 0:
                # print(i,j,"left")
                left_cumulator = cumulator(i,j-1)
            if i < shape[0]-1:
                # print(i,j,"up")
                up_cumulator = cumulator(i+1,j)
            if i > 0:
                # print(i,j,"down")
                down_cumulator = cumulator(i-1,j)
        return right_cumulator + left_cumulator + up_cumulator + down_cumulator + 1

    mask = np.where(data == 9,0,1)
    sizes = []
    for i,j in basins:
        # print(i,j)
        sizes.append(cumulator(i,j))

    sizes.sort()
    # print(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]

start = perf_counter()
basins, counts = part_a()
answer_b = part_b(basins, data,data.shape)
print(perf_counter() - start)


#
# # solution trying to understand from Megaboard:
# import numpy as np
# from scipy import ndimage as ndi
# hMap = np.array([list(map(int,list(r))) for r in data])
# mask = np.array([[0,1,0],[1,1,1],[0,1,0]])
# sinks = ndi.generic_filter(hMap,np.min,footprint=mask) == hMap
# print((hMap[sinks][hMap[sinks]<9]+1).sum()) # Part1
# basins = ndi.label(hMap<9)[0]
# bCounts = [basins[basins==i].size for i in range(basins.max()+1)]
# print (eval('*'.join(map(str,sorted(bCounts)[-4:-1])))) # Part2
# ######################################################
#
# import pygame
# from pygame.image import load
# import time
# pygame.init()
#
# player = pygame.image.load("player.bmp").convert()
# background = load("liquid.bmp").convert()
#
# window = pygame.display.set_mode((600,480))
# window.blit(background, (0,0))
#
# position = player.get_rect()
# window.blit(player, position)
# pygame.display.update()
# for x in range(100):
#     window.blit(background, (position, position))
#     position = position.move(2,0)
#     window.blit(player,position)
#     pygame.display.update()
#     pygame.time.delay(150)
#
# def set_text(string, coordx, coordy, fontSize): #Function to set text
#
#     font = pygame.font.Font('freesansbold.ttf', fontSize)
#     #(0, 0, 0) is black, to make black text
#     text = font.render(string, True, (0, 0, 0))
#     textRect = text.get_rect()
#     textRect.center = (coordx, coordy)
#     return (text, textRect)
#
# window.fill((255, 255, 255)) #Fills the whole window with white
# #Places "Text in Pygame!" with an x,y coord of 250, 250 and 60 font size
# for i in range(0,10):
#     print(i)
#     totalText = set_text(f"Text{i}!", 100, 100, 30)
#     window.blit(totalText[0], totalText[1])
#     pygame.display.update()
#     time.sleep(1.0)
#     font = pygame.font.Font('freesansbold.ttf', 30)
#     text = font.render(f"Text{i}!", True, (0, 255, 255))
#     textRect = text.get_rect()
#     textRect.center = (100, 100)
#     window.blit( (50,80,100,50))
#     pygame.display.update()
#     time.sleep(1.0)
#
#
# temp = textRect
# temp.bottom = 120
# temp.bottom = temp.bottom + 10
# temp.top = temp.top - 10