# Solitare
import random
# No! My comment is better
#Solitaire
import os
def main(reset):
    global deck
    global shown
    if reset:
        deck = []
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for i in range(13):
            deck.append(("B", "S", numbers[i]))
            deck.append(("B", "C", numbers[i]))
            deck.append(("R", "H", numbers[i]))
            deck.append(("R", "D", numbers[i]))
        random.shuffle(deck)
        clubs = [("B", "C", 0)]
        spades = [("B", "S", 0)]
        hearts = [("R", "H", 0)]
        diamonds = [("R", "D", 0)]
        pile1 = []
        for i in range(1):
            pile1.append(deck.pop())
        pile2 = []
        for i in range(2):
            pile2.append(deck.pop())
        pile3 = []
        for i in range(3):
            pile3.append(deck.pop())
        pile4 = []
        for i in range(4):
            pile4.append(deck.pop())
        pile5 = []
        for i in range(5):
            pile5.append(deck.pop())
        pile6 = []
        for i in range(6):
            pile6.append(deck.pop())
        pile7 = []
        for i in range(7):
            pile7.append(deck.pop())
        shown = [1, 1, 1, 1, 1, 1, 1, 1]
        deck = [deck, pile1, pile2, pile3, pile4, pile5, pile6, pile7, spades, clubs, diamonds, hearts]
    global showboard
    def displayCard(card):
        display = ""
        if card[2] == 0:
            display += "N"
        elif card[2] == 1:
            display += "A"
        elif card[2] < 11:
            display += str(card[2]%10)
        else:
            if card[2] == 11:
                display += "J"
            elif card[2] == 12:
                display += "Q"
            else:
                display += "K"
        display += card[1] + " "
        return display
    
    def showboard(localDeck, localShown):
        print("Aces:")
        line = ""
        for i in range(8, 12):
            line += displayCard(localDeck[i][0])
        print(line)
        print("1: 2: 3: 4: 5: 6: 7:")
        line = ""
        for i in range(1, 8):
            localDeck[i].reverse()
        localHidden = [0]
        for i in range(1, 8):
            localHidden.append(len(localDeck[i])-localShown[i])
        maxPileLength = 0
        for i in range(1, 8):
            maxPileLength = max(len(localDeck[i]), maxPileLength)
        for i in range(maxPileLength):
            line = ""
            for j in range(1, 8):
                if len(localDeck[j]) <= i:
                    line += "   "
                elif i < localHidden[j]:
                    line += "## "
                else:
                    line += displayCard(localDeck[j][i])
            print(line)
        print()
        print("Deck:")
        print("Length:", str(len(localDeck[0])))
        if len(localDeck[0]) > 0:
            print(displayCard(localDeck[0][0]))
        for i in range(1, 8):
            localDeck[i].reverse()
    
    def findTarget():
        king = ("N", "N", 14)
        if move[1] == -1:
            return ("N", "N", 0)
        if len(move) == 1:
            return
        for i in range(1, 8):
            if move[1] == i:
                if len(deck[i]) == 0:
                    return king
                return deck[i][0]
    def appendTarget(t):
        global deck
        global shown
        deck[t].reverse()
        deck[t] += moving
        deck[t].reverse()
        shown[t] += len(moving)
    global suitee
    def suitee(card):
        if card == "H":
            return 11
        if card == "D":
            return 10
        if card == "C":
            return 9
        if card == "S":
            return 8
    def shuffle():
        localDeck = deck
        localShown = shown
        localTotal = [1]
        for i in range(1, 8):
            localTotal.append(len(deck[i]))
        hidden = localDeck[0]
        for i in range(1, 8):
            for j in range(shown[i], len(deck[i])):
                hidden.append(localDeck[i].pop())
        random.shuffle(hidden)
        for i in range(1, 8):
            while len(localDeck[i]) < localTotal[i]:
                localDeck[i].append(hidden.pop())
        localDeck[0] = hidden
        return localDeck
    def save(localDeck, localShown):
        Saved = open("saved.py", "w")
        string = "deck = "+str(localDeck)
        string += "\nshown = "+str(localShown)
        Saved.write(string)
        Saved.close()
    def complete(localDeck):
        global shown
        loop = True
        cardsMoved = 0
        cardsTurned = 0
        while loop:
            loop = False
            for i in range(1, 8):
                if len(localDeck[i]) != 0:
                    suite = suitee(localDeck[i][0][1])
                    if localDeck[i][0][2]-1 == localDeck[suite][0][2]:
                        localDeck[suite].insert(0, localDeck[i].pop(0))
                        cardsMoved += 1
                        shown[i] -= 1
                        if shown[i] == 0 and len(localDeck[i]) != 0:
                            shown[i] += 1
                            cardsTurned += 1
                        loop = True
        print("Cards moved:",str(cardsMoved))
        print("Cards turned:",str(cardsTurned))
        print()
        return localDeck
    os.system("cls")
    def syntax():
        print("Syntax for usage:")
        print("Use [x, y] format to move a card from pile x to pile y.")
        print("Use [x, A] to move a card to an aces pile.")
        print("Use [D] to refresh the top of the deck.")
        print("Use [H] to place from the top of the deck.")
        print("Use [S] to shuffle all hidden cards, including the deck.")
        print("Use [C] to put all available cards into the aces piles.")
        print("Use [I] to view these instructions again.")
        print("Use [end] to end the game.\n")
    end = False
    while True:
        while True:
            try:
                save(deck, shown)
                showboard(deck, shown)
                move = input("\nWhich pile would you like to move to which pile?\n")
                os.system("cls")
                if len(move) == 0:
                    raise ValueError
                if move.lower() == "end":
                    end = True
                    break
                if move[:1].upper() == "D":
                    if move.lower() == "debug":
                        breakpoint()
                        continue
                    else:
                        deck[0].append(deck[0].pop(0))
                        continue
                if move.lower()[:1] == "i":
                    syntax()
                    continue
                if move.lower()[:1] == "c":
                    deck = complete(deck)
                    continue
                if move.lower()[:1] == "s":
                    deck = shuffle()
                    continue
                move = move.split(", ")
                if move[0][:1].upper() == "H":
                    move[0] = 0
                elif move[0][:1].upper() == "A":
                    move[0] = -1
                if move[1][:1].upper() == "A":
                    move[1] = -1
                if len(move) > 2 and move[2] != "debug":
                    raise IndexError
                move[0] = int(move[0])
                move[1] = int(move[1])
                if not (-2 < move[0] < 8 and -2 < move[1] < 8):
                    print("Those aren't listed decks.")
                    continue
                if move[0] == move[1]:
                    raise ValueError
                break
            except:
                print("Something went wrong. Ensure you use x, y formatting and that you use valid numbers.")
        if end:
            raise SystemExit
        target = findTarget()
        moving = []
        made = False
        if len(move) == 3:
            breakpoint()
        if move[1] == -1:
            suite = suitee(deck[move[0]][0][1])
            if deck[suite][0][2]+1 == deck[move[0]][0][2]:
                made = True
                deck[suite].insert(0, deck[move[0]].pop(0))
                shown[move[0]] -= 1
                if shown[move[0]] < 1 and len(deck[move[0]]) != 0:
                    shown[move[0]] = 1
            continue
        if move[0] == -1:
            for i in range(8, 12):
                if deck[i][0][0] != target[0] and deck[i][0][2]+1 == target[2]:
                    made = True
                    deck[move[1]].insert(0, deck[i].pop(0))
                    shown[move[1]] += 1
                    break
                
            continue
        for i in range(shown[move[0]]):
            if (deck[move[0]][i][0] != target[0] and deck[move[0]][i][2] + 1 == target[2]) or (deck[move[0]][i][2] == 13 and len(target) == 0):
                made = True
                for j in range(i+1):
                    moving.append(deck[move[0]].pop(0))
                    shown[move[0]] -= 1
                if shown[move[0]] < 1 and len(deck[move[0]]) != 0:
                    shown[move[0]] = 1
                moving.reverse()
                appendTarget(move[1])
                moving = []
                break
        if not made:
            print("Something went wrong. That's not a legal move.")
if __name__ == "__main__":
    if input("Continue saved game? Y/N ").lower()[:1] == "y":
        try:
            import saved
            from saved import *
        except:
            print("Saved file not found. Creating a new game and save.")
            main(True)
        main(False)
    else:
        main(True)








