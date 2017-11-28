import argparse
import re
import copy
from collections import deque
from collections import defaultdict
from itertools import combinations

state_id = 0

def is_valid(generators, microchips):
    """
    A floor is valid if it has zero generators or zero microchips
    A floor is valid if all microchips have matching generators
    A microchip will fry if it is on a floor without its generator when another generator is present
    """
    global elem_num
    valid = True
    if generators == [False] * elem_num or microchips == [False] * elem_num:
        return valid

    for idx, val in enumerate(microchips):
        if val and not generators[idx]:
            valid = False

    return valid


def make_new_states(state):
    global state_id
    current_floor = state["current_floor"]
    new_states = []

    # number of items to move
    item_moves = [1, 2]
    # determine possible moves based on current floor
    if current_floor == 0:
        # can only move up
        moves = [1]
    elif current_floor == 3:
        # can only move down
        moves = [-1]
    else:
        # can move up or down
        moves = [1, -1]

    for move in moves:
        new_floor = current_floor + move
        true_gen_idx = []
        true_mc_idx = []
        # move 1 microchip and 1 generator up/down
        for idx, val in enumerate(state["generators"][current_floor]):
            # only need to do if the generator and microchip are true
            if state["generators"][current_floor][idx] and state["microchips"][current_floor][idx]:
                new_state = copy.deepcopy(state)
                new_state["generators"][current_floor][idx] = False
                new_state["microchips"][current_floor][idx] = False
                new_state["generators"][new_floor][idx] = True
                new_state["microchips"][new_floor][idx] = True
                is_valid_nf = is_valid(new_state["generators"][new_floor], new_state["microchips"][new_floor])
                is_valid_cf = is_valid(new_state["generators"][current_floor], new_state["microchips"][current_floor])
                if is_valid_nf and is_valid_cf:
                    state_id += 1
                    new_state["id"] = state_id
                    new_state["current_floor"] = new_floor
                    new_state["moves"] += 1
                    new_states.append(new_state)
            # Create lists of indexes that are true for use below
            if val == True:
                true_gen_idx.append(idx)
            if state["microchips"][current_floor][idx]:
                true_mc_idx.append(idx)

        # move 1 and 2 of each item up/down
        for item_move in item_moves:
            # move generators up/down
            for gidx in combinations(true_gen_idx, item_move):
                new_state = copy.deepcopy(state)
                for idx in gidx:
                    new_state["generators"][current_floor][idx] = False
                    new_state["generators"][new_floor][idx] = True
                is_valid_nf = is_valid(new_state["generators"][new_floor], new_state["microchips"][new_floor])
                is_valid_cf = is_valid(new_state["generators"][current_floor], new_state["microchips"][current_floor])
                if is_valid_nf and is_valid_cf:
                    state_id += 1
                    new_state["id"] = state_id
                    new_state["current_floor"] = new_floor
                    new_state["moves"] += 1
                    new_states.append(new_state)

            # move microchips up/down
            for midx in combinations(true_mc_idx, item_move):
                new_state = copy.deepcopy(state)
                for idx in midx:
                    new_state["microchips"][current_floor][idx] = False
                    new_state["microchips"][new_floor][idx] = True
                is_valid_nf = is_valid(new_state["generators"][new_floor], new_state["microchips"][new_floor])
                is_valid_cf = is_valid(new_state["generators"][current_floor], new_state["microchips"][current_floor])
                if is_valid_nf and is_valid_cf:
                    state_id += 1
                    new_state["id"] = state_id
                    new_state["current_floor"] = new_floor
                    new_state["moves"] += 1
                    new_states.append(new_state)

    return new_states


def input_parser(lines):
    """
    The first floor contains a promethium generator and a promethium-compatible microchip.
    The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
    The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
    The fourth floor contains nothing relevant.
    """

    legend = {"cobalt": 0, "curium": 1, "plutonium": 2, "promethium": 3, "ruthenium": 4}

    state = {"current_floor": 0, "id": 0, "moves": 0,
            "generators": [
                [False, False, False, True, False],
                [True, True, True, False, True],
                [False, False, False, False, False],
                [False, False, False, False, False]
            ],
            "microchips": [
                [False, False, False, True, False],
                [False, False, False, False, False],
                [True, True, True, False, True],
                [False, False, False, False, False]
            ]
            }

    # use ID or moves?
    """
    state = {"current_floor": 0, "id": 0, "moves": 0,
            "generators": [
                [False, False],
                [True, True],
                [False, False],
                [False, False]
            ],
            "microchips": [
                [True, True],
                [False, False],
                [False, False],
                [False, False]
            ]
            }
    """
    return state



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advent of code.')
    parser.add_argument('inputfile', type=argparse.FileType('r'), help='Path to input file')
    args = parser.parse_args()
    lines = args.inputfile.read().rstrip("\n").split("\n")

    # Set initial variables
    current_floor = 0
    total_moves = 0
    searched = defaultdict(list)

    state = input_parser(lines)
    elem_num = len(state["generators"][-1])
    search_queue = deque()
    search_queue.append(state)
    while search_queue:
        # Get the first state
        new_state = search_queue.popleft()

        if new_state["generators"] + new_state["microchips"] in searched[new_state["current_floor"]]:
            #print("ALREADY SEARCHED")
            #print(searched)
            continue

        #print(new_state)
        # Check if the state is complete...
        # when the fourth floor has 4 generators and 4 microchips
        if new_state["generators"][-1] == [True] * elem_num and new_state["microchips"][-1] == [True] * elem_num:
            print("DONE")
            print(new_state)
            break

        #searched.append([new_state["current_floor"],new_state["generators"],new_state["microchips"]])
        searched[new_state["current_floor"]].append(new_state["generators"] + new_state["microchips"])
        # Determine the new states and add them to the search_queue
        search_queue += make_new_states(new_state)
