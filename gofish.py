from random import randint 
import random
card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = card*4
user = []
comp = []
print(deck)
def draw_card() :

    draw = random.choice(deck)
    deck.remove(draw)
    #print(draw)
    #print(deck)
    return draw

def deal_card() :

# users first 7 draw

    i = (len(user))
    print(i)
    
    user.insert(0, draw_card())
    comp.insert(0, draw_card())
    user.insert(1, draw_card())
    comp.insert(2, draw_card())
    user.insert(2, draw_card())
    comp.insert(3, draw_card())
    user.insert(3, draw_card())
    comp.insert(4, draw_card())
    user.insert(4, draw_card())
    comp.insert(5, draw_card())
    user.insert(5, draw_card())
    comp.insert(6, draw_card())
    user.insert(6, draw_card())
    comp.insert(0, draw_card())
    i = len(user)
    print(i)
