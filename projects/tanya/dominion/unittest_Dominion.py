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

        #setup game, player
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

        #setup game, player
        self.setUp()
        #setupCard
        self.setupCard()
        self.player.hand = []
        self.player.actions = 0
        self.player.buys = 0
        self.player.purse = 0
        # self.player.actions = 0
        # self.player.turn(self.players, self.supply, self.trash)
        # self.player.turn(self.players, [], [])

        self.actionCard.augment(self.player)

        # checks if cost is initialized properly
        self.assertEqual(1, self.player.actions)
        # checks if actions is initialized properly
        self.assertEqual(5, self.player.buys)
        # checks if cards is initialized properly
        self.assertEqual(4, self.player.purse)
        # checks if coins is initialized properly
        self.assertEqual(4, self.actionCard.coins)
        # checks if the player's hand is equal to 2
        self.assertEqual(2, self.player.hand)


class TestPlayer(TestCase):

    #initialize variables
    def setUp(self):
        self.player = Dominion.Player('Annie')

    def setupLaboratoryCard(self):
        name = "Laboratory"
        cost = 5
        actions = 1
        cards = 2
        buys = 5
        coins = 4
        return Dominion.Action_card(name, cost, actions, cards, buys, coins)

    def setupFestivalCard(self):
        name = "Festival"
        cost = 5
        actions = 2
        cards = 0
        buys = 1
        coins = 2
        return Dominion.Action_card(name, cost, actions, cards, buys, coins)

    def setUpDeckStack(self):
        self.player.deck.append(self.setupFestivalCard())

    def test_stack(self):
        self.setUp()
        self.assertEqual(10,len(self.player.stack()))
        #change the deck and check the stack to verify it increased
        self.player.deck = [Dominion.Copper()] * 10 + [Dominion.Estate()] * 3
        self.assertEqual(18, len(self.player.stack()))

    def test_action_balance(self):
        self.setUp()

        balance = self.player.action_balance()
        #check since no action cards have been added
        self.assertEqual(0, balance)

        #test if one action card is present in the stack
        self.setUpDeckStack()
        balance = self.player.action_balance()
        #check if the balance is correct based on the 11 card stack having 1 action card with 2 points
        self.assertAlmostEqual(70/11, balance)

        #test if another action card is present in the hand
        self.player.hand.append(self.setupFestivalCard())
        balance = self.player.action_balance()
        self.assertAlmostEqual(70*2 / 12, balance)

        # test if another action card is present in played
        self.player.played.append(self.setupFestivalCard())
        balance = self.player.action_balance()
        self.assertAlmostEqual(70 * 3 / 13, balance)

        # test if another action card is present in the player's discard
        self.player.discard.append(self.setupFestivalCard())
        balance = self.player.action_balance()
        self.assertAlmostEqual(70 * 4 / 14, balance)

        # test if another action card is present in the player's aside
        self.player.aside.append(self.setupFestivalCard())
        balance = self.player.action_balance()
        self.assertAlmostEqual(70 * 5 / 15, balance)

        # test if another action card is present in the player's hold
        self.player.hold.append(self.setupFestivalCard())
        balance = self.player.action_balance()
        self.assertAlmostEqual(70 * 6 / 16, balance)

    def test_calcpoints(self):
        self.setUp()

        #clear all card's in player's deck and hand on setup
        self.player.deck = []
        self.player.hand = []

        # check the case where the player has no victory card
        points = self.player.calcpoints()
        self.assertEqual(0, points)

        #add 1 estate card to player's deck
        #check the case where the player has only 1 victory card in the stack
        self.player.deck.append(Dominion.Estate())
        points = self.player.calcpoints()
        self.assertEqual(1, points)

        # add 1 estate card to player's deck and hand each
        # check the case where the player has only 2 victory cards in the stack
        self.player.hand.append(Dominion.Estate())
        points = self.player.calcpoints()
        self.assertEqual(2, points)

        # add 1 duchy card to player's deck and hand each
        # check the case where the player has only 3 victory cards in the stack
        # and has a different type of victory card
        self.player.played.append(Dominion.Duchy())
        points = self.player.calcpoints()
        self.assertEqual(5, points)

        # add 1 Province card to player's discard pile
        # check the case where the player has only 4 victory cards in the stack
        # and has a different type of victory card
        self.player.discard.append(Dominion.Province())
        points = self.player.calcpoints()
        self.assertEqual(11, points)

        # add another estate card to player's aside
        # check the case where the player has only 5 victory cards in the stack
        # and has a different type of victory card
        self.player.aside.append(Dominion.Estate())
        points = self.player.calcpoints()
        self.assertEqual(12, points)

        # add another estate card to player's aside
        # check the case where the player has only 6 victory cards in the stack
        self.player.hold.append(Dominion.Estate())
        points = self.player.calcpoints()
        self.assertEqual(13, points)

        # add a garden card to player's hand
        # check the case where the player has the garden card in the stack
        self.player.deck.append(Dominion.Gardens())
        points = self.player.calcpoints()
        self.assertEqual(13, points)

        # add 4 other victory cards so that the Garden card is calculated in the points
        self.player.deck.append(Dominion.Estate())
        self.player.deck.append(Dominion.Estate())
        self.player.deck.append(Dominion.Estate())
        self.player.deck.append(Dominion.Estate())
        points = self.player.calcpoints()
        self.assertEqual(18, points)

        # add another garden card to player's hand
        # check the case where the player has the garden card in the stack
        self.player.deck.append(Dominion.Gardens())
        points = self.player.calcpoints()
        self.assertEqual(19, points)

    def test_draw(self):
        self.setUp()
        # test scenario where none of the draw function if statments are executed
        self.player.discard = []
        self.player.draw(self.player.discard)




    def test_cardsummary(self):
        # self.fail()
        pass




