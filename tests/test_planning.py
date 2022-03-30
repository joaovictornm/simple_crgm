
from crgm.planning import do_plan
from tests.fsa_goal_model import get_model

model = get_model()

# G0
def test_planning_g0_with_context():
    plan = do_plan(initial_node=model.g0, context_state=[model.c1, model.c3, model.c5, model.c8])
    assert plan == [model.p1, model.p3, model.p10, model.p12, model.p13, model.p16]

def test_planning_g0_without_context():
    plan = do_plan(initial_node=model.g0, context_state=[])
    assert plan == [model.p6, model.p12, model.p13]

# G1
def test_planning_or_with_valid_context_tasks():
    plan = do_plan(initial_node=model.g1, context_state=[model.c1])
    assert plan == [model.p1]

def test_planning_or_with_alternative_tasks():
    plan = do_plan(initial_node=model.g1, context_state=[model.c2])
    assert plan == [model.p2]

def test_planning_or_no_possible_task():
    plan = do_plan(initial_node=model.g1, context_state=[])
    assert not plan

def test_planning_or_many_alternatives():
    plan = do_plan(initial_node=model.g1, context_state=[model.c1, model.c2])
    assert plan == [model.p1], 'the plan was not the one expected'

# G2
def test_planning_g2_with_context():
    plan = do_plan(initial_node=model.g2, context_state=[model.c3])
    assert plan == [model.p3]

def test_planning_g2_to_p4_without_context():
    plan = do_plan(initial_node=model.g2, context_state=[])
    assert plan == [model.p6]

def test_planning_g2_to_p4_with_context_from_p4():
    plan = do_plan(initial_node=model.g2, context_state=[model.c4])
    assert plan == [model.p5, model.p6]

# G3
def test_planning_g3_with_context_c1():
    plan = do_plan(initial_node=model.g3, context_state=[model.c5])
    assert plan == [model.p10]

def test_planning_g3_with_context_c6():
    plan = do_plan(initial_node=model.g3, context_state=[model.c6])
    assert plan == [model.p11]

def test_planning_g3_without_context():
    plan = do_plan(initial_node=model.g3, context_state=[])
    assert not plan

def test_planning_g3_with_context():
    plan = do_plan(initial_node=model.g3, context_state=[model.c5, model.c6])
    assert plan == [model.p10], 'the plan was not the one expected'

# G4
def test_planning_g4():
    plan = do_plan(initial_node=model.g4, context_state=[])
    assert plan == [model.p12, model.p13]

# G5
def test_planning_g5_with_context():
    plan = do_plan(initial_node=model.g5, context_state=[model.c7, model.c10])
    assert plan == [model.p14]

def test_planning_g5_with_context_c7():
    plan = do_plan(initial_node=model.g5, context_state=[model.c7])
    assert plan == [model.p14]

def test_planning_g5_with_context_c10():
    plan = do_plan(initial_node=model.g5, context_state=[model.c10])
    assert plan == [model.p18]

def test_planning_g5_to_p15_without_context_from_p15():
    plan = do_plan(initial_node=model.g5, context_state=[])
    assert not plan

def test_planning_g5_to_p15_with_context_from_p15():
    plan = do_plan(initial_node=model.g5, context_state=[model.c8, model.c9])
    assert plan == [model.p16]

def test_planning_g5_to_p15_with_context_c8_from_p15():
    plan = do_plan(initial_node=model.g5, context_state=[model.c8])
    assert plan == [model.p16]

def test_planning_g5_to_p15_with_context_c9_from_p15():
    plan = do_plan(initial_node=model.g5, context_state=[model.c9])
    assert plan == [model.p17]

# P7
def test_planning_p7_with_context():
    plan = do_plan(initial_node=model.p7, context_state=[model.c1])
    assert plan == [model.p8, model.p9]

def test_planning_p7_without_context():
    plan = do_plan(initial_node=model.p7, context_state=[])
    assert plan == [model.p8]

# G2 - AND
# def test_planning_g2_with_context():
#     plan = do_plan(initial_node=model.g2, context_state=[model.c3, model.c4, model.c1])
#     print(plan)
#     assert plan == [model.p3, model.p5, model.p6, model.p8, model.p9]
################################################################################