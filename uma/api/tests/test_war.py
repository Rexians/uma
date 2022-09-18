import unittest
import requests

class TestWar(unittest.TestCase):
    
    def test_expert(self):
        """
        Test Expert difficulty (Tier 2)
        """

        URL = "https://mcoc-uma.herokuapp.com/war/2"

        war_info = requests.get(URL).json()
        self.assertEqual(war_info['tier'], 2)
        self.assertEqual(war_info['difficulty'], 'Expert')
        self.assertEqual(war_info['tier_multiplier'], "7.0")
        self.assertEqual(war_info['tier_rank'], r"0.16%-0.50%")
        self.assertEqual(war_info['nodes']['16'], ["Vivified - I", "Brute Force"])

    def test_challenger(self):
        """
        Test Challenger difficulty (Tier 4)
        """

        URL = "https://mcoc-uma.herokuapp.com/war/4"

        war_info = requests.get(URL).json()
        self.assertEqual(war_info['tier'], 4)
        self.assertEqual(war_info['difficulty'], 'Challenger')
        self.assertEqual(war_info['tier_multiplier'], "4.5")
        self.assertEqual(war_info['tier_rank'], r"2%-3%")
        self.assertEqual(war_info['nodes']['3'], ["COMBAT DÉJÀ VU - PROWESS", "Prowess Puncture - 2"])

    def test_hard(self):
        """
        Test Hard difficulty (Tier 2)
        """

        URL = "https://mcoc-uma.herokuapp.com/war/8"

        war_info = requests.get(URL).json()
        self.assertEqual(war_info['tier'], 8)
        self.assertEqual(war_info['difficulty'], 'Hard')
        self.assertEqual(war_info['tier_multiplier'], "3.0")
        self.assertEqual(war_info['tier_rank'], r"10%-11%")
        self.assertEqual(war_info['nodes']['48'], ["Feat of Vigilance 1", "Power Efficiency", "Missing in Action 1"])

    def test_intermediate(self):
        """
        Test Intermediate difficulty (Tier 10)
        """

        URL = "https://mcoc-uma.herokuapp.com/war/10"

        war_info = requests.get(URL).json()
        self.assertEqual(war_info['tier'], 10)
        self.assertEqual(war_info['difficulty'], 'Intermediate')
        self.assertEqual(war_info['tier_multiplier'], "2.4")
        self.assertEqual(war_info['tier_rank'], r"14%-15%")
        self.assertEqual(war_info['nodes']['23'], ["Mix Master", "Aggression: Prowess"])

    def test_normal(self):
        """
        Test Normal difficulty (Tier 15)
        """

        URL = "https://mcoc-uma.herokuapp.com/war/15"

        war_info = requests.get(URL).json()
        self.assertEqual(war_info['tier'], 15)
        self.assertEqual(war_info['difficulty'], 'Normal')
        self.assertEqual(war_info['tier_multiplier'], "1.8")
        self.assertEqual(war_info['tier_rank'], r"36%-40%")
        self.assertEqual(war_info['nodes']['1'], ["Cornered"])
    
    def test_easy(self):
        """
        Test Easy difficulty (Tier 21)
        """

        URL = "https://mcoc-uma.herokuapp.com/war/21"

        war_info = requests.get(URL).json()
        self.assertEqual(war_info['tier'], 21)
        self.assertEqual(war_info['difficulty'], 'Easy')
        self.assertEqual(war_info['tier_multiplier'], "1.1")
        self.assertEqual(war_info['tier_rank'], r"81%-90%")
        self.assertEqual(war_info['nodes']['21'], ["Plagued Mind", "Immunity (Bleed)"])

if __name__ == "__main__":
    unittest.main()