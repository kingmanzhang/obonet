import os
import obonet.ontology as ontology

directory = os.path.dirname(os.path.abspath(__file__))


class TestOntologyClass:

    def setup(self):
        self.onto = ontology.Ontology(path=os.path.join(
            directory, 'data/taxrank.obo'))
        self.root = 'TAXRANK:0000000'

    def test_constructor(self):
        assert(self.onto is not None)

    def test_ancestors(self):

        assert(len(self.onto.ancestors(self.root)) == 0)

        term_id = 'TAXRANK:0000003'
        assert(self.onto.ancestors(term_id) == {'TAXRANK:0000000'})

    def test_descendants(self):
        assert(len(self.onto.descendants(self.root)) > 0)

    def test_parents(self):
        term_id = 'TAXRANK:0000004'
        assert(self.onto.parents(term_id) == {'TAXRANK:0000000'})

    def test_children(self):
        assert(len(self.onto.children(self.root)) > 0)

    def test_term_id2label_map(self):
        assert(len(self.onto.term_id_2_label_map()) > 0)
        assert(self.onto.term_id_2_label_map()[self.root] == 'taxonomic_rank')
        assert (self.onto.term_id_2_label_map()['TAXRANK:0000001'] == 'phylum')
