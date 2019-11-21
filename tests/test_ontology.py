import unittest
import obonet.ontology as ontology


class TestOntologyClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.onto = ontology.Ontology(path='data/taxrank.obo')
        cls.root = 'TAXRANK:0000000'

    def test_constructor(self):
        self.assertIsNotNone(self.onto)

    def test_ancestors(self):

        self.assertTrue(len(self.onto.ancestors(self.root)) == 0)

        term_id = 'TAXRANK:0000003'
        self.assertEqual(self.onto.ancestors(term_id), {'TAXRANK:0000000'})

    def test_descendants(self):
        self.assertTrue(len(self.onto.descendants(self.root)) > 0)

    def test_parents(self):
        term_id = 'TAXRANK:0000004'
        self.assertTrue(self.onto.parents(term_id), {'TAXRANK:0000000'})

    def test_children(self):
        self.assertTrue(len(self.onto.children(self.root)) > 0)

    def test_term_id2label_map(self):
        self.assertTrue(len(self.onto.term_id_2_label_map()) > 0)
        self.assertEqual(self.onto.term_id_2_label_map()[self.root], 'taxonomic_rank')
        self.assertEqual(self.onto.term_id_2_label_map()['TAXRANK:0000001'], 'phylum')

if __name__=='__main__':
    unittest.main