from obonet import read_obo
import networkx as nx
import copy


class Ontology:
    def __init__(self, path):
        self.graph = read_obo(path)

    def ancestors(self, term_id):
        return nx.descendants(self.graph, term_id)

    def descendants(self, term_id):
        return nx.ancestors(self.graph, term_id)

    def parents(self, term_id):
        return frozenset(self.graph[term_id].keys())

    def children(self, term_id):
        return frozenset(self.graph.predecessors(term_id))

    def terms(self):
        all_terms = copy.deepcopy(self.graph.nodes)
        return all_terms

    def term_id_2_label_map(self):
        id_2_label = copy.deepcopy(nx.get_node_attributes(self.graph, 'name'))
        return id_2_label
