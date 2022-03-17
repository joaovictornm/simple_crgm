from enum import Enum
from typing import List


class Node:
    """ Node is a base class for either goals as tasks """

    def __init__(self, identification, restriction=None):
        self.identification = identification
        self.restriction = restriction


class Context:
    """ A context is a partial state of the world."""

    def __init__(self, identification):
        self.identification = identification


class RefinementType(Enum):
    AND = 0
    OR = 1


class Refinement:
    """ children is a set of sub goals or subtasks. Each element is a
        Node """

    def __init__(self, type: RefinementType, children: List[Node] = []):
        self.type = type
        self.children = children
        self.parent = None


class AbstractTask(Node):
    """ A task that is refined in other tasks by a refinement """

    def __init__(self, id: str, refinement: Refinement,  **kargs):
        Node.__init__(self, id, **kargs)
        self.refinement = refinement
        self.refinement.parent = self


class Goal(AbstractTask):
    """ A goal is a result that the user whats to achieve """
    pass


class LeafTask(Node):
    """ This represents a concrete tasks
        ie., an effort that can be executed an
        can contribute to achieving a goal """

    def __init__(self, id, **kargs):
        Node.__init__(self, id, **kargs)
