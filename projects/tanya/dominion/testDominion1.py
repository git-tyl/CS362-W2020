# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:42:42 2020

@author: tanya
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

#Define box
box = testUtility.GetBoxes(nV)

supply_order = testUtility.GetSupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.pick10CardsToBeInSupply(box)

#Update the supply have these cards
testUtility.updateSupply(supply, player_names, nV,nC)

#Costruct the Player objects
players = testUtility.ConstructPlayers(player_names)

testUtility.PlayGame(supply, supply_order, players)

#Final score
testUtility.FinishGame(players)