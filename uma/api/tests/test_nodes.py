import unittest
import requests

class TestNodes(unittest.TestCase):


    def test_all_nodes(self):
        """
        Grab all nodes and test node 160
        """
        
        URL = 'https://mcoc-uma.herokuapp.com/nodes'

        nodes = requests.get(URL).json()['data']
        self.assertEqual(nodes['160']['node_name'], 'Energy Adoption: Lightning - 2')
        self.assertEqual(nodes['160']['node_info'], r"The Defender has a 50% chance to inflict the Attacker with Shock on contact. These effects will not trigger while the Defender is suffering from a Poison Debuff. The Defender also takes 100% reduced damage from Shock effects and gains a Regeneration Buff healing 1% of max health per second until the Shock expires.")

    def test_one_node(self):
        """
        Grab specific node (164) and test
        """

        URL = 'https://mcoc-uma.herokuapp.com/nodes/165'

        node = requests.get(URL).json()
        self.assertEqual(node['node_name'], 'Enhanced Abilities')
        self.assertEqual(node['node_info'], r"All abilities trigger 20% more often.")


if __name__ == "__main__":
    unittest.main()