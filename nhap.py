import os
import pygame


# Cars_path = b'C:\Users\DELL\Desktop\Support QA\CarRace\Cars'
# os.chdir(path)
# print(os.getcwd())
# print(os.listdir(os.path.join(path, "Cars")))
# paths = []
# cars = []
# for i in os.listdir(Cars_path):
#    paths.append(os.path.join(Cars_path, i))
# for i in paths:
#     cars.append(pygame.image.load(i))

# global BADDIEMINSIZE

BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 13
BADDIEMAXSPEED = 15
ADDNEWBADDIERATE = 40
PLAYERMOVERATE = 10



print(BADDIEMINSIZE)
print(BADDIEMAXSIZE)
print(BADDIEMINSPEED)
print(BADDIEMAXSPEED)
print(ADDNEWBADDIERATE)
print(PLAYERMOVERATE)
print("\n")

def easy_mode():
   global BADDIEMINSIZE
   BADDIEMINSIZE = 14
   BADDIEMAXSIZE = 41
   BADDIEMINSPEED = 23
   BADDIEMAXSPEED = 79
   ADDNEWBADDIERATE = 41
   PLAYERMOVERATE = 17

easy_mode()
print(BADDIEMINSIZE)
print(BADDIEMAXSIZE)
print(BADDIEMINSPEED)
print(BADDIEMAXSPEED)
print(ADDNEWBADDIERATE)
print(PLAYERMOVERATE)