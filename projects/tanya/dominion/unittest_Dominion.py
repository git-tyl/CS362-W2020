from unittest import TestCase
import testUtility
import Dominion

class TestCard(TestCase):

    def setUp(self):
        self.players = testUtility.GetPlayerNames()
        self.nV = testUtility.GetNumVictoryCards(self.players)
        self.nC = testUtility.GetNumCursesCards(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        # Pick n cards from box to be in the supply
        self.supply = testUtility.pick10CardsToBeInSupply(self.box)
        testUtility.updateSupply(self.supply, self.players, self.nV, self.nC)
        self.player = Dominion.Player("Annie")

    def test_init(self):
        #initialize_test_data
        self.setUp()
        cost = 1
        buypower = 5

        #instantiate the card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        #verify that the class variables have the expected values

        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass

    def TestPlayer(TestCase):
        def test_stack(self):
            player = Dominion.Player('Annie')
            self.assertEqual(10,len(player.stack()))
            #change the deck and check the stack to verify it increased
            player.deck = [Dominion.Copper()] * 10 + [Dominion.Estate()] * 3
            self.assertEqual(18, len(player.stack()))

