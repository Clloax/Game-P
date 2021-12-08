from Main import M_Cards
from Main import S_Cards
from Main import T_Cards
monster_cards = [BlueEyes, DarkMagician, RedEyes, CosmoQueen, Trent]
BlueEyes = M_Cards(3000, 2500, None, "Blue Eyes White Dragon", "This legendary dragon is a powerful "
                                                               "engine of destruction. Virtually invincible, "
                                                               "very few have faced this awesome creature and lived "
                                                               "to tell the tale.")
DarkMagician = M_Cards(2500, 2000, None, "Dark Magician", "The ultimate wizard in terms of attack and defense.")
RedEyes = M_Cards(2400, 2000, None, "Red Eyes Black Dragon", "A ferocious dragon with a deadly attack.")
CosmoQueen = M_Cards(2900, 2450, None, "Cosmo Queen", "Queen of the galaxies and mistress of the stars.")
Trent = M_Cards(1500, 1800, None, "Trent", "A guarding of the woods, this massive tree is believed top be immortal.")
spell_cards = [DragonT]
DragonT = S_Cards(BlueEyes.ATK() and BlueEyes.DEF() + 300)


trap_cards = [Dmf]
DMF = T_Cards(None)