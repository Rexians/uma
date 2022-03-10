import unittest
import requests

class TestChampSInfo(unittest.TestCase):

    def test_tier_one(self):
        """
        Test case for random champion at tier 1 and rank 2
        """
        URL = "http://127.0.0.1:8000/champs/?champ=doctordoom&tier=1&rank=2"
        stats = requests.get(URL).json()
        self.assertEqual(stats['name'], 'DOCTOR DOOM')
        self.assertEqual(stats['class'], 'Mystic')
        self.assertEqual(stats['tier'], 1)
        self.assertEqual(stats['rank'], 2)
        self.assertEqual(stats['prestige'], 315)
        self.assertEqual(stats['hp'], 1096)
        self.assertEqual(stats['attack'], 116)
        self.assertEqual(stats['crit_rate'], 198)
        self.assertEqual(stats['crit_dmge'], 610)
        self.assertEqual(stats['armor'], 686)
        self.assertEqual(stats['block_prof'], 3562)
        self.assertEqual(stats['energy_resist'], 0)
        self.assertEqual(stats['physical_resist'], 0)
        self.assertEqual(stats['crit_resist'], 862)
        self.assertEqual(stats['sig_info'], None)
        self.assertEqual(stats['url_page'], 'https://auntm.ai/champions/doctordoom/tier/1')
        self.assertEqual(stats['img_portrait'], 'https://mcoc.rexians.tk/assets/potraits/doctordoom.png')
        self.assertEqual(stats['champid'], 'doctordoom+1+2')

    def test_tier_two(self):
        """
        Test case for random champion at tier 2 and rank 3
        """
        URL = "http://127.0.0.1:8000/champs/?champ=imiw&tier=2&rank=3"
        stats = requests.get(URL).json()
        self.assertEqual(stats['name'], 'IRON MAN (INFINITY WAR)')
        self.assertEqual(stats['class'], 'Tech')
        self.assertEqual(stats['tier'], 2)
        self.assertEqual(stats['rank'], 3)
        self.assertEqual(stats['prestige'], 588)
        self.assertEqual(stats['hp'], 2248)
        self.assertEqual(stats['attack'], 175)
        self.assertEqual(stats['crit_rate'], 764)
        self.assertEqual(stats['crit_dmge'], 629)
        self.assertEqual(stats['armor'], 148)
        self.assertEqual(stats['block_prof'], 4372)
        self.assertEqual(stats['energy_resist'], 0)
        self.assertEqual(stats['physical_resist'], 0)
        self.assertEqual(stats['crit_resist'], 0)
        self.assertEqual(stats['sig_info'], [r"Once per fight, Iron Man’s Model 50 suit executes an emergency protocol if attacked while 15% Health or less remains, creating a hardened exterior by instantly granting 1.07 to 8.01 stack(s) of Molecular Armor.",
                                             r"While 15% Health or less remains and Iron Man is under the effects of an Armor effect, the suit generates 3.63 to 6.6% Power per second and has a 100% chance to Auto-Block attacks without consuming Armor. This Auto-Block triggers Parry."])
        self.assertEqual(stats['url_page'], 'https://auntm.ai/champions/ironman_movie/tier/2')
        self.assertEqual(stats['img_portrait'], 'https://mcoc.rexians.tk/assets/potraits/ironman_movie.png')
        self.assertEqual(stats['champid'], 'ironman_movie+2+3')

    def test_tier_three(self):
        """
        Test case for random champion at tier 3 and rank 4
        """
        URL = "http://127.0.0.1:8000/champs/?champ=unstoppablecolossus&tier=3&rank=4"
        stats = requests.get(URL).json()
        self.assertEqual(stats['name'], 'UNSTOPPABLE COLOSSUS')
        self.assertEqual(stats['class'], 'Mystic')
        self.assertEqual(stats['tier'], 3)
        self.assertEqual(stats['rank'], 4)
        self.assertEqual(stats['prestige'], 1298)
        self.assertEqual(stats['hp'], 6427)
        self.assertEqual(stats['attack'], 472)
        self.assertEqual(stats['crit_rate'], 353)
        self.assertEqual(stats['crit_dmge'], 463)
        self.assertEqual(stats['armor'], 277)
        self.assertEqual(stats['block_prof'], 2775)
        self.assertEqual(stats['energy_resist'], 0)
        self.assertEqual(stats['physical_resist'], 0)
        self.assertEqual(stats['crit_resist'], 0)
        self.assertEqual(stats['sig_info'], 'Whenever Colossus starts the fight or launches a Special Attack, he calls upon the power of Cyttorak, becoming Unstoppable and shrugging off all enemy attacks for 2 to 4 seconds.')
        self.assertEqual(stats['url_page'], 'https://auntm.ai/champions/colossus_unstoppable/tier/3')
        self.assertEqual(stats['img_portrait'], 'https://mcoc.rexians.tk/assets/potraits/colossus_unstoppable.png')
        self.assertEqual(stats['champid'], 'colossus_unstoppable+3+4')

    def test_tier_four(self):
        """
        Test case for random champion at tier 4 and rank 5
        """
        URL = "http://127.0.0.1:8000/champs/?champ=spiderman_stealth&tier=4&rank=5"
        stats = requests.get(URL).json()
        self.assertEqual(stats['name'], 'SPIDER-MAN (STEALTH SUIT)')
        self.assertEqual(stats['class'], 'Skill')
        self.assertEqual(stats['tier'], 4)
        self.assertEqual(stats['rank'], 5)
        self.assertEqual(stats['prestige'], 3862)
        self.assertEqual(stats['hp'], 12163)
        self.assertEqual(stats['attack'], 1294)
        self.assertEqual(stats['crit_rate'], 598)
        self.assertEqual(stats['crit_dmge'], 632)
        self.assertEqual(stats['armor'], 273)
        self.assertEqual(stats['block_prof'], 2348)
        self.assertEqual(stats['energy_resist'], 0)
        self.assertEqual(stats['physical_resist'], 0)
        self.assertEqual(stats['crit_resist'], 0)
        self.assertEqual(stats['sig_info'], "Increases the Potency of Fury Passives by 10 to 30%.")
        self.assertEqual(stats['url_page'], 'https://auntm.ai/champions/spiderman_stealth/tier/4')
        self.assertEqual(stats['img_portrait'], 'https://mcoc.rexians.tk/assets/potraits/spiderman_stealth.png')
        self.assertEqual(stats['champid'], 'spiderman_stealth+4+5')

    def test_tier_five(self):
        """
        Test case for random champion at tier 5 and rank 1
        """
        URL = "http://127.0.0.1:8000/champs/?champ=doc_ock&tier=5&rank=1"
        stats = requests.get(URL).json()
        self.assertEqual(stats['name'], 'DOCTOR OCTOPUS')
        self.assertEqual(stats['class'], 'Tech')
        self.assertEqual(stats['tier'], 5)
        self.assertEqual(stats['rank'], 1)
        self.assertEqual(stats['prestige'], 2275)
        self.assertEqual(stats['hp'], 8347)
        self.assertEqual(stats['attack'], 625)
        self.assertEqual(stats['crit_rate'], 568)
        self.assertEqual(stats['crit_dmge'], 668)
        self.assertEqual(stats['armor'], 362)
        self.assertEqual(stats['block_prof'], 3236)
        self.assertEqual(stats['energy_resist'], 0)
        self.assertEqual(stats['physical_resist'], 0)
        self.assertEqual(stats['crit_resist'], 0)
        self.assertEqual(stats['sig_info'], [r"Doctor Octopus’s extensive academic background let him start the fight with each of his Research Categories at 60 and each Breakthroughs is replaced by a new effect.",
                                             r"Physics: Drain 100% of Power Gained and Steal 5.71 to 15% of the Power Drained.",
                                             r"Chemistry: Deal Direct Damage equal to 100% of Health Gained and Lifesteal 15.71 to 25% of the Damage done.",
                                             r"Biology: Gain the standard Biology Breakthrough Armor Up and 361.9 to 781.42 Armor Penetration while it's active."])
        self.assertEqual(stats['url_page'], 'https://auntm.ai/champions/doc_ock/tier/5')
        self.assertEqual(stats['img_portrait'], 'https://mcoc.rexians.tk/assets/potraits/doc_ock.png')
        self.assertEqual(stats['champid'], 'doc_ock+5+1')

    def test_tier_six(self):
        """
        Test case for random champion at tier 6 and rank 4
        """
        URL = "http://127.0.0.1:8000/champs/?champ=lukecage&tier=6&rank=4"
        stats = requests.get(URL).json()
        self.assertEqual(stats['name'], 'LUKE CAGE')
        self.assertEqual(stats['class'], 'Science')
        self.assertEqual(stats['tier'], 6)
        self.assertEqual(stats['rank'], 4)
        self.assertEqual(stats['prestige'], 10540)
        self.assertEqual(stats['hp'], 48995)
        self.assertEqual(stats['attack'], 3427)
        self.assertEqual(stats['crit_rate'], 420)
        self.assertEqual(stats['crit_dmge'], 665)
        self.assertEqual(stats['armor'], 329)
        self.assertEqual(stats['block_prof'], 3300)
        self.assertEqual(stats['energy_resist'], 0)
        self.assertEqual(stats['physical_resist'], 0)
        self.assertEqual(stats['crit_resist'], 0)
        self.assertEqual(stats['sig_info'], [r"Bullet-proof skin allows Luke Cage to become Indestructible and ignore all incoming damage for 1.7 to 3.7 seconds.",
                                             r"This ability can be activated again after a 44.97 to 25 second cooldown."])
        self.assertEqual(stats['url_page'], 'https://auntm.ai/champions/lukecage/tier/6')
        self.assertEqual(stats['img_portrait'], 'https://mcoc.rexians.tk/assets/potraits/luke_cage.png')
        self.assertEqual(stats['champid'], 'lukecage+6+4')

if __name__ == "__main__":
    unittest.main()