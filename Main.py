
print("Welcome to the game!")
LP_Player1 = 8000
LP_Player2 = 8000
TLane1 = 0
TLane2 = 0
TLane3 = 0
TLane4 = 0
TLane5 = 0
BLane1 = 0
BLane2 = 0
BLane3 = 0
BLane4 = 0
BLane5 = 0
T1Lane1 = 0
T2Lane2 = 0
T3Lane3 = 0
T4Lane4 = 0
T5Lane5 = 0
B1Lane1 = 0
B2Lane2 = 0
B3Lane3 = 0
B4Lane4 = 0
B5Lane5 = 0
ODeck = 40
PDeck = 40
TopLanes = [TLane1, TLane2, TLane3, TLane4, TLane5]
BottomLanes = [BLane1, BLane2, BLane3, BLane4, BLane5]
Top1Lanes = [T1Lane1, T2Lane2, T3Lane3, T4Lane4, T5Lane5]
Bottom2Lanes = [B1Lane1, B2Lane2, B3Lane3, B4Lane4, B5Lane5]

class S_Cards:
    def __init__(self, EFC, NME, DSC):
        self.EFC = EFC
        self.NME = NME
        self.DSC = DSC

    def effect(self):
        for effect in self.EFC:
            eval(effect)

class T_Cards:
    def __init__(self, EFC, NME, DSC):
        self.EFC = EFC
        self.NME = NME
        self.DSC = DSC

    def effect(self):
        for effect in self.EFC:
            eval(effect)

class M_Cards:
    def __init__(self, ATK , DEF, EFC, NME, DSC):
        self.ATK = ATK
        self.DEF = DEF
        self.EFC = EFC
        self.NME = NME
        self.DSC = DSC

    def __repr__(self):
        return "This card's name is " + self.NME + ". It has " + str(self.ATK) + " attack and " + str(self.DEF) + " defense. Its Effect is: " + str(self.EFC) + " and its description is: " + self.DSC

def Board_Top(lane1, lane2, lane3, lane4, lane5):
    global TLane1
    global TLane2
    global TLane3
    global TLane4
    global TLane5
    if isinstance(lane1, M_Cards) == True:
        TLane1 += 1
    if isinstance(lane2, M_Cards) == True:
        TLane2 += 1
    if isinstance(lane3, M_Cards) == True:
        TLane3 += 1
    if isinstance(lane4, M_Cards) == True:
        TLane4 += 1
    if isinstance(lane5, M_Cards) == True:
        TLane5 += 1
    else:
        raise Exception("Must be a Monster card!")

def Board_Bottom(lane1, lane2, lane3, lane4, lane5):
    global BLane1
    global BLane2
    global BLane3
    global BLane4
    global BLane5
    if isinstance(lane1, S_Cards) == True:
        BLane1 += 1
    elif isinstance(lane1, T_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane1, S_Cards) == True:
        BLane1 += 2
    if isinstance(lane2, S_Cards) == True:
        BLane2 += 1
    elif isinstance(lane2, M_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane2, T_Cards) == True:
        BLane2 += 2
    if isinstance(lane3, S_Cards) == True:
        BLane3 += 1
    elif isinstance(lane3, M_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane3, T_Cards) == True:
        BLane3 += 2
    if isinstance(lane4, S_Cards) == True:
        BLane4 += 1
    elif isinstance(lane4, M_Cards) == True:
         raise Exception("Must be spell or trap card")
    elif isinstance(lane4, T_Cards) == True:
        BLane4 += 2
    if isinstance(lane5, S_Cards) == True:
        BLane5 += 1
    elif isinstance(lane5, M_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane5, T_Cards) == True:
        BLane5 += 2

def Board1_Top(lane1, lane2, lane3, lane4, lane5):
    global T1Lane1
    global T2Lane2
    global T3Lane3
    global T4Lane4
    global T5Lane5
    if isinstance(lane1, M_Cards) == True:
        T1Lane1 += 1
    if isinstance(lane2, M_Cards) == True:
        T2Lane2 += 1
    if isinstance(lane3, M_Cards) == True:
        T3Lane3 += 1
    if isinstance(lane4, M_Cards) == True:
        T4Lane4 += 1
    if isinstance(lane5, M_Cards) == True:
        T5Lane5 += 1
    else:
        raise Exception("Must be a Monster card!")

def Board2_Bottom(lane1, lane2, lane3, lane4, lane5):
    global B1Lane1
    global B2Lane2
    global B3Lane3
    global B4Lane4
    global B5Lane5
    if isinstance(lane1, S_Cards) == True:
        B1Lane1 += 1
    elif isinstance(lane1, T_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane1, S_Cards) == True:
        B1Lane1 += 2
    if isinstance(lane2, S_Cards) == True:
        B2Lane2 += 1
    elif isinstance(lane2, M_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane2, T_Cards) == True:
        B2Lane2 += 2
    if isinstance(lane3, S_Cards) == True:
        B3Lane3 += 1
    elif isinstance(lane3, M_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane3, T_Cards) == True:
        B3Lane3 += 2
    if isinstance(lane4, S_Cards) == True:
        B4Lane4 += 1
    elif isinstance(lane4, M_Cards) == True:
         raise Exception("Must be spell or trap card")
    elif isinstance(lane4, T_Cards) == True:
        B4Lane4 += 2
    if isinstance(lane5, S_Cards) == True:
        B5Lane5 += 1
    elif isinstance(lane5, M_Cards) == True:
        raise Exception("Must be spell or trap card")
    elif isinstance(lane5, T_Cards) == True:
        B5Lane5 += 2


BlueEyes = M_Cards(3000, 2500, None, "Blue Eyes White Dragon", "This legendary dragon is a powerful "
                                                               "engine of destruction. Virtually invincible, "
                                                               "very few have faced this awesome creature and lived "
                                                               "to tell the tale.")
DarkMagician = M_Cards(2500, 2000, None, "Dark Magician", "The ultimate wizard in terms of attack and defense.")
RedEyes = M_Cards(2400, 2000, None, "Red Eyes Black Dragon", "A ferocious dragon with a deadly attack.")
CosmoQueen = M_Cards(2900, 2450, None, "Cosmo Queen", "Queen of the galaxies and mistress of the stars.")
Trent = M_Cards(1500, 1800, None, "Trent", "A guarding of the woods, this massive tree is believed top be immortal.")
DragonT = BlueEyes.ATK + 300
DragonT2 = RedEyes.ATK + 300
Spellcaster = DarkMagician.ATK + 400
Tree = Trent.ATK + 400
QueenBoost = CosmoQueen.ATK + 500
dragont = S_Cards(DragonT, "DragonT", "Blah")
reddragont = S_Cards(DragonT2, "DragonT2", "Blah")
Spellcaster1 = S_Cards(Spellcaster, "Dark", "Blah")
Tree2 = S_Cards(Tree, "Tree", "Blah")
Queen = S_Cards(QueenBoost, "Queen", "Blah")
def game(card1, *cards):


    print("        /===YU-GI-OH!===\ ")
    print("   --------------------------")
    print(str([ODeck]) + " | " + str([BLane4]) + " | " + str([BLane2]) + " | " + str([BLane1]) + " | " + str([BLane3]) + " | " + str([BLane5]) + "|")
    print("   |------------------------|")
    print(" | " + str([TLane4]) + " | " + str([TLane2]) + " | " + str([TLane1]) + " | " + str([TLane3]) + " | " + str([TLane5]) + "|")
    print("   |------------------------|")
    print(" | " + str([T4Lane4]) + " | " + str([T2Lane2]) + " | " + str([T1Lane1]) + " | " + str([T3Lane3]) + " | " + str([T5Lane5]) + "|")
    print("   |------------------------|")
    print(" | " + str([B4Lane4]) + " | " + str([B2Lane2]) + " | " + str([B1Lane1]) + " | " + str([B3Lane3]) + " | " + str([B5Lane5]) + "| " + str([PDeck]))
    print("   --------------------------")

if LP_Player1 == 0:
    print("Player 2 Wins!")
if LP_Player2 == 0:
    print("Player 1 Wins!")
Board_Top(DarkMagician, dragont, Trent, CosmoQueen, RedEyes)
Board_Bottom(dragont, reddragont, Tree2, Queen, Spellcaster1)
game1 = game(BlueEyes)
print(game1)
