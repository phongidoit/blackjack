#blakc jack game
import random as rd
class Card:
    def __init__(self, rank=None, suit=None):
        self.rank=(rd.randint(0,12))
        self.suit=(rd.randint(0,3))
        print("index:", self.rank, self.suit)

    def  generate(self):
        self.rank=(rd.randint(0,12))
        self.suit=(rd.randint(0,3))


    def displaycard(self):
        suits = {0: "SPADE", 1: "HEART", 2: "DIAMOND", 3: "CLUB"}
        ranks = {0: "A", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8", 8: "9",
                 9: "10", 10: "J", 11: "Q", 12: "K"}
        print(ranks[self.rank]+f"({suits[self.suit]})",end="\t")

def card_generator(used):
    new =Card()
    #new.generate()
    for card in used:
        if card.rank==new.rank and card.suit==new.suit:
            new=card_generator(used) #make a new card if existed
    used.append(new)
    return new

def check_2A_or_10A(player,enemy):
    #if they got double A after receive card, they win
    r_p,r_e=0,0
    if player[0].rank==0 and player[1].rank==0:
        r_p=2
    elif (player[0].rank==0 and player[1].rank>=9) or (player[1].rank==0 and player[0].rank>=9):
        r_p=1
    if enemy[0].rank==0 and enemy[1].rank==0:
        r_e=2
    elif  (enemy[0].rank==0 and enemy[1].rank>=9) or (enemy[1].rank==0 and enemy[0].rank>=9):
        r_p=1

    if r_p==0 and r_p==r_e:
        return 0
    elif r_p==r_e: #either both got double A or double A&10
        return 1
    elif r_p<r_e:  #player lose
        return 2
    elif r_p>r_e:  #player win
        return 3

def display(player, enemy, sum1,sum2):
    print("player: ",end='\t')
    for card in player:
        card.displaycard()
    print("\nenemy: ",end='\t')
    for i in range(len(enemy)):
        '''if i==0:
            print("?(?)",end='\t')
            continue'''
        enemy[i].displaycard()
    print()
    print("your count: ",sum1)
    print("enemy count: ", sum2)

def enemy_hit_ver1(enemy,sum2,used):

    while sum2<14:
        card=card_generator(used)
        used.append(card)
        enemy.append(card)
        sum2=card_sum(enemy)
    while sum2>=14 and sum2<=17:
        # first version i just want that there is 0.5 chance that enemy will hit if their sum in this range
        chance=rd.randint(0,1)
        if chance==1:
            card = card_generator(used)
            used.append(card)
            enemy.append(card)
            sum2 = card_sum(enemy)
    return sum2

def reveal_all(player, enemy, sum1,sum2):
    print("player: ", end='\t')
    for card in player:
        card.displaycard()

    print("\nenemy: ", end='\t')
    for i in range(len(enemy)):
        card.displaycard()
    print()
    print("your count: ",sum1,"\tenemycount: ",sum2)

def card_sum(player):
    A_exist=0
    A=[11,10,1]
    sum=0
    for card in player:
        if card.rank==0: #card rank == A deal with them later on
            A_exist+=1
            continue
        if card.rank>=10:
            sum+=10
        else:
            sum+=card.rank+1
    #since A has 3 value so I only want to deal with it now
    #take maximum value of A unless sum over 21
    while A_exist>0:
        i=0
        while sum+A[i]>21:
            i+=1
            if i==2:
                break
        sum+=A[i]
        A_exist-=1
    return sum

def continue_playing(Y):
    Y=int(input("For another game, type 1: "))
    if Y!=1:
        print("thank you, End dame")
    return Y

def result(sum1,sum2):
    # 0:draw, 1:win, 2:lose
    if sum1>21 and sum2>21:
        return 0
    elif sum1>21 or sum2>21:  # only over 21
        if sum1>21:
            return 2
        elif sum2>21:
            return 1
    else:
        if sum1>sum2:
            return 1
        elif sum1<sum2:
            return 2
        else:
            return 0

def printallcard(list):
    for card in list:
        card.displaycard()

print("Start the game:")
Y=3013
while (Y == 1):
    player= []; sum_pl= 0
    enemy= []; sum_en=0
    used= [] #all the card that has been use

    # draw 2 card for both player and enemy
    for i in range (2):
        card = card_generator(used)
        #print(card.rank, card.suit)
        player.append(card)
        #for the enemy
        card = card_generator(used)
        #print(card.rank, card.suit)
        enemy.append(card)

    result_code=check_2A_or_10A(player,enemy)
    if result_code!=0:
        if result_code==1:
            print("You both draw")
        elif result_code==2:
            print("You lost")
        else:
            print("You win")
        Y=int(input("Start again (1 for yes): "))
        if continue_playing(Y)!=1:
            break
        else:
            continue
    sum_pl = card_sum(player)
    display(player, enemy, sum_pl,sum_en)
    #Hit or Stay
    while True:
        more=int(input("type 1 for hit: "))
        if more != 1:
            break
        card = card_generator(used)
        print(card.rank, card.suit)
        player.append(card)
        sum_pl = card_sum(player)
        display(player,enemy,sum_pl,sum_en)
    print("number of card used: ",len(used))
    print("enemy turn: ",end=": ")
    sum_en=enemy_hit_ver1(enemy,sum_en,used)
    #print(player, enemy)
    result_code=result(sum_pl, sum_en)
    print("--the result--")
    reveal_all(player, enemy, sum_pl, sum_en)
    if result_code==0:
        print("You both draw")
    elif result_code==1:
        print("You win")
    elif result_code==2:
        print("You lose")
    Y=int(input("Start again (1 for yes): "))

if Y == 3013: #test branches
    used=[]
    player=[];enemy=[]
    for i in range(2):
        card = card_generator(used)
        # print(card.rank, card.suit)
        player.append(card)
        # for the enemy
        card = card_generator(used)
        # print(card.rank, card.suit)
        enemy.append(card)
    printallcard(used)
    print(card_sum(used))
















