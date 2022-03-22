
from crgm.planning import do_plan
from tests.fsa_goal_model import get_model

model = get_model()


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
