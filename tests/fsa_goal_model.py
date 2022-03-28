
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
    c3 = Context('On board computer - distance to empty')
    c4 = Context('On board computer - fuel and mileage')
    c5 = Context('Internet Connection')
    c6 = Context('Available Storage')
    c7 = Context('Navigation System')
    c8 = Context('Voice Synthesizer')
    c9 = Context('Audio Player')
    c10 = Context('Visible Graphical Interface')
    # TODO issue 1 - instantiate other contexts

    # leaf tasks
    p1 = LeafTask("Get Position using GPS", restriction=c1)
    p2 = LeafTask("Get Position using antenna triangulation", restriction=c2)

    # TODO issue 1 - instantiate other leaf tasks
    p3 = LeafTask("Use data from onboard computer", restriction=c3)
    p5 = LeafTask("Access fuel level and mileage", restriction=c5)
    p6 = LeafTask("Calculate distance to empty")
    p8 = LeafTask("Get user input on tank capacity, mileage and fuel level")
    p9 = LeafTask("Track distance using GPS", restriction=c1)
    p10 = LeafTask("Query online", restriction=c5)
    p11 = LeafTask("Query offline", restriction=c6)
    p12 = LeafTask("Get constraints")
    p13 = LeafTask("Choose filling station")
    p14 = LeafTask("Alert using navigation system", restriction=c7)
    p16 = LeafTask("Use synthesized voice", restriction=c8)
    p17 = LeafTask("Use pre-recorded voice", restriction=c9)
    p18 = LeafTask("Alert user by visual sign", restriction=c10)

    p4 = Goal("Calculate based on fuel level",
                refinement=Refinement(
                    type=RType.AND,
                    children=[p5, p6]))

    p7 = Goal("Use user input and distance track",
                refinement=Refinement(
                    type=RType.AND,
                    children=[p8, p9]))

    p15 = Goal("Alert user by sound",
                refinement=Refinement(
                    type=RType.OR,
                    children=[p16, p17]))

    # goals
    g1 = Goal("Get Position",
                refinement=Refinement(
                    type=RType.OR,
                    children=[p1, p2]))

    # TODO issue 1 - instantiate othergoals
    g2 = Goal("Asses Distance to Empty",
                refinement=Refinement(
                    type=RType.OR,
                    children=[p3, p4, p7]))

    g3 = Goal("Recover information about nearby filling station",
                refinement=Refinement(
                    type=RType.OR,
                    children=[p10, p11]))

    g4 = Goal("Decide more convenient",
                refinement=Refinement(
                    type=RType.AND,
                    children=[p12, p13]))

    g5 = Goal("Driver is notified",
                refinement=Refinement(
                    type=RType.OR,
                    children=[p14, p15, p18]))

    # root goal
    g0 = Goal("Vehicle refueling is assisted",
                refinement=Refinement(
                    type=RType.AND,
                    children=[g1, g2, g3, g4, g5]))


def get_model():
    model_inst = SimpleNamespace()
    for enum_item in fsa_model:
        # set id in each element
        setattr(enum_item.value, 'id', enum_item.name)
        setattr(model_inst, enum_item.name,
                enum_item.value)    # set in the model
    return model_inst
