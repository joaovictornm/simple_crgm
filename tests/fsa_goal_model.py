
from enum import Enum
from types import SimpleNamespace

from crgm.model import Context, Goal, LeafTask, Refinement, \
    RefinementType as RType


# Here, Filling Station Advisor goal model is instantiated
# as a Enum, so we have references for parts of the model
# such as contexts, tasks, and goals
# (i.e., we can reference context c1 as
#    'fsa_model.c1',  goal g1 as 'fsa_model.g1'.
# These references facilitates assertions in the tests. )
class fsa_model(Enum):
    # contexts
    c1 = Context('GPS')
    c2 = Context('Antenna Triangulation')
    # TODO issue 1 - instantiate other contexts

    # leaf tasks
    p1 = LeafTask("Get Position using GPS", restriction=c1)
    p2 = LeafTask("Get Position using antenna triangulation", restriction=c2)
    # TODO issue 1 - instantiate other leaf tasks

    # goals
    g1 = Goal("Get Position",
              refinement=Refinement(
                  type=RType.OR,
                  children=[p1, p2]))
    # TODO issue 1 - instantiate othergoals

    # root goal
    g0 = Goal("Vehicle refueling is assisted",
              refinement=Refinement(
                  type=RType.AND,
                  children=[g1]))


def get_model():
    model_inst = SimpleNamespace()
    for enum_item in fsa_model:
        # set id in each element
        setattr(enum_item.value, 'id', enum_item.name)
        setattr(model_inst, enum_item.name,
                enum_item.value)    # set in the model
    return model_inst
