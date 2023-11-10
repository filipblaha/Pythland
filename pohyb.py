import pygame


def movement(key1, key2, key3, key4, player_x, player_y, rychlost):
    if key1:
        player_x -= rychlost
    if key2:
        player_x += rychlost
    if key3:
        player_y -= rychlost
    if key4:
        player_y += rychlost

    return player_x, player_y
