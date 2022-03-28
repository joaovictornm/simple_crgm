
from typing import List
from crgm.model import Context, Node, Refinement, RefinementType, LeafTask


def do_plan(initial_node: Node, context_state: List[Context]):
    """  For a given model and context and model, create a plan """
    if is_leaf_task(initial_node):
        if is_applicable(initial_node, context_state):
            return [initial_node]
        else:
            return None
    else:
        refinement: Refinement = initial_node.refinement
        if refinement.type is RefinementType.OR:
            for child in refinement.children:
                for child in refinement.children:
                    sub_plan = do_plan(child, context_state)
                    if sub_plan:
                        return sub_plan
        # TODO implement AND refinement
        if refinement.type is RefinementType.AND:   # Without context
            return refinement.children


def is_applicable(node, context_state):
    """ check if the current context state satisfies \
        the restrictions of the node
    """
    if not node.restriction or node.restriction in context_state:
        return True


def is_leaf_task(node):
    return isinstance(node, LeafTask)
