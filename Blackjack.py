import random
class Decks:

    #order = []
    #numDecks = 1
    #numCards = 52
    #ps       = 0
    cardList = []
        
    def __init__(self,numDecks):
        self.numDecks = numDecks
        self.numCards = numDecks * 52
        self.order    = [x for x in range(self.numCards)]
        self.shuffle()
        self.pos = 0
        for i in range(self.numDecks):
            for j in range(13):
                for k in range(4):
                    self.cardList.append(j+1)
                
    def shuffle(self):
        random.shuffle(self.order)
        
    def draw(self):
        retValue = self.cardList[self.order[self.pos]]
        self.pos = self.pos+1
        return retValue

class BlackjackGame:
    results = []
    
    def simulate(self, ntimes):
        for x in range(ntimes):
            self.results.append(self.play())
            
        return self.results
        
    def play(self):
        d = Decks(6)
        hand = []
        hand.append(d.draw())
        
        score = [min(x,10) for x in hand]
        bust = 0
        while bust==0:
            hand.append(d.draw())
            score = sum([min(x,10) for x in hand])
            if 1 not in hand:
                if score > 21:
                    bust = 1
                elif score > 16:
                    return {'hand':hand,'res':bust}
            else:
                softScore = score + 10
                if score > 21:
                    bust = 1
                elif score > 16 or (softScore <= 21 and softScore > 16):
                    return {'hand':hand,'res':bust}
        
        return {'hand':hand, 'res':bust}