from obonet import read_obo
import networkx as nx
import copy


class Ontology:
    def __init__(self, path):
        """
        Initialize an ontology class by providing the path.
        :param path:
        """
        self.graph = read_obo(path)

    def nx_graph(self, deepcopy=False):
        """
        Return the networkx graph to the user to use functionalities
        supported by networkx. Note that the directions are opposite
        in networkx compare to ontologies. An edge in networkx graph is from a
        specific term to a generic term. So successors are more specific terms,
        for example, "red wine" is a successor of "wine".
        :param deepcopy: whether to create a deep copy
        :return: a copy of the ontology graph
        """
        if deepcopy:
            return copy.deepcopy(self.graph)
        else:
            return self.graph

    def ancestors(self, term_id):
        """
        Returns all the ancestor ontology terms (more generic terms). Note
        "ancestor" here is opposite to networkx "ancestor".
        :param term_id: query term
        :return: all ancestors
        """
        return nx.descendants(self.graph, term_id)

    def descendants(self, term_id):
        """
        Returns all the descendant ontology terms (more specific terms). Note
        "descendant" here is opposite to networkx "descendant".
        :param term_id: query term
        :return: all descendants
        """
        return nx.ancestors(self.graph, term_id)

    def parents(self, term_id):
        """
        Returns the immediate parents of a term
        :param term_id: query term
        :return: parents
        """
        return frozenset(self.graph[term_id].keys())

    def children(self, term_id):
        """
        Returns the immediate children of a term
        :param term_id: query term
        :return: children terms
        """
        return frozenset(self.graph.predecessors(term_id))

    def terms(self):
        """
        Return all ontology terms as a set
        :return:
        """
        all_terms = copy.deepcopy(self.graph.nodes)
        return all_terms

    def term_id_2_label_map(self):
        """
        Returns a map from term id to term label
        :return: an id => label map
        """
        id_2_label = copy.deepcopy(nx.get_node_attributes(self.graph, 'name'))
        return id_2_label
