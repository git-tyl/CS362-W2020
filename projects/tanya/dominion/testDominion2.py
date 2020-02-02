# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:42:42 2020

@author: tanya

This file test if the supply has no victory cards that are initialized
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = testUtility.GetPlayerNames()
#number of curses and victory cards
nV = testUtility.GetNumVictoryCards(player_names)
nC = testUtility.GetNumCursesCards(player_names)
#get all the boxes with action cards
box = testUtility.GetBoxes(nV)
#update the order in the supply
supply_order = testUtility.GetSupplyOrder()
#Pick 10 cards from box to be in the supply.
supply = testUtility.pick10CardsToBeInSupply(box)
#get all the treasure, victory and curse cards added to the supply
testUtility.updateSupplyWithoutVictoryCards(supply, player_names, nV,nC)
#Costruct the Player objects
players = testUtility.ConstructPlayers(player_names)
#Start the game
testUtility.PlayGame(supply, supply_order, players)
#Get the Final score once the game is finished
testUtility.FinishGame(players)