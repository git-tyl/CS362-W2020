from unittest import TestCase
import testUtility
import Dominion

# class TestCard(TestCase):
#
#     def setUp(self):
#         self.players = testUtility.GetPlayerNames()
#         self.nV = testUtility.GetNumVictoryCards(self.players)
#         self.nC = testUtility.GetNumCursesCards(self.players)
#         self.box = testUtility.GetBoxes(self.nV)
#         self.supply_order = testUtility.GetSupplyOrder()
#
#         # Pick n cards from box to be in the supply
#         self.supply = testUtility.pick10CardsToBeInSupply(self.box)
#         testUtility.updateSupply(self.supply, self.players, self.nV, self.nC)
#         self.player = Dominion.Player("Annie")
#
#     #test if initialization is working
#     def test_init(self):
#         #initialize_test_data
#         self.setUp()
#         cost = 1
#         buypower = 5
#
#         #instantiate the card object
#         card = Dominion.Coin_card(self.player.name, cost, buypower)
#
#         #verify that the class variables have the expected values
#
#         self.assertEqual('Annie', card.name)
#         self.assertEqual(buypower, card.buypower)
#         self.assertEqual(cost, card.cost)
#         self.assertEqual("coin", card.category)
#         self.assertEqual(0, card.vpoints)
#
#     def test_use(self):
#         # self.fail()
#         pass
#     def test_augment(self):
#         # self.fail()
#         pass

class TestAction_Card(TestCase):

    #setup the variables needed
    def setUp(self):
        #setup empty trash pile
        self.trash = []
        #setup players
        self.players = testUtility.GetPlayerNames()
        #setup victory cards
        self.nV = testUtility.GetNumVictoryCards(self.players)
        #setup curse cards
        self.nC = testUtility.GetNumCursesCards(self.players)
        #create the box of cards
        self.box = testUtility.GetBoxes(self.nV)
        #get the supply order
        self.supply_order = testUtility.GetSupplyOrder()

        # Pick n cards from box to be in the supply
        self.supply = testUtility.pick10CardsToBeInSupply(self.box)

        #update supply with all the victory and curse guards based
        #on the players
        testUtility.updateSupply(self.supply, self.players, self.nV, self.nC)

        #make current player annnie
        self.player = Dominion.Player("Annie")


    def setupCard(self):
        name = "Laboratory"
        cost = 5
        actions = 1
        cards = 2
        buys = 5
        coins = 4
        self.actionCard = Dominion.Action_card(name, cost, actions, cards, buys, coins)

    # test if initialization is working
    def test_init(self):
        self.setupCard()

        #checks if name is initialized properly
        self.assertEqual("Laboratory", self.actionCard.name)
        # checks if cost is initialized properly
        self.assertEqual(5, self.actionCard.cost)
        # checks if actions is initialized properly
        self.assertEqual(1, self.actionCard.actions)
        # checks if cards is initialized properly
        self.assertEqual(2, self.actionCard.cards)
        # checks if coins is initialized properly
        self.assertEqual(4, self.actionCard.coins)

    # test if use function works for action card
    def test_use(self):

        #setup player
        self.setUp()
        #setup card variables
        self.setupCard()
        # check if player's hand is zero
        self.assertEqual(5, len(self.player.hand))
        # remove one card from the deck
        self.player.hand.pop()
        # check if player's hand is zero
        self.player.hand.append(self.actionCard)
        # check if player's hand has increased to 5 cards
        self.assertEqual(5, len(self.player.hand))
        # check if player's hand has the card name
        self.assertEqual(self.actionCard, self.player.hand[4])
        # use the action card in the player's hand
        self.actionCard.use(self.player, self.trash)
        #check if card is removed for players hand
        self.assertEqual(4, len(self.player.hand))
        # check if card added to players appended
        self.assertEqual(1, len(self.player.played))
        # check if card added to players appended is the Laboratory card
        self.assertEqual(self.actionCard, self.player.played[0])

    # test augment function
    def test_augment(self):
        pass

class TestPlayer(TestCase):

    #initialize variables
    def setUp(self):
        self.player = Dominion.Player('Annie')

    def test_stack(self):
        self.setUp()
        self.assertEqual(10,len(self.player.stack()))
        #change the deck and check the stack to verify it increased
        self.player.deck = [Dominion.Copper()] * 10 + [Dominion.Estate()] * 3
        self.assertEqual(18, len(self.player.stack()))

    def test_action_balance(self):
        # self.fail()
        pass
    def test_draw(self):
        # self.fail()
        pass
    def test_cardsummary(self):
        # self.fail()
        pass




