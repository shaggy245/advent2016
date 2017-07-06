import argparse
import re


def is_valid(floors):
    valid = True
    for floor in floors:
        if len(floor["generators"]) == 0 or len(floor["microchips"]) == 0:
            # If no generators or no microchips are on floor, valid
            valid = True
            continue
        elif sorted(floor["microchips"]) in sorted(floor["generators"]):
            # If all microchips have associated generators on floor, valid
            valid = True
            continue
        else:
            valid = False
            break
    return valid

    """
        for gen in floor["generators"]:
            if gen in floor["microchps"]:
                valid = True
            else:
                ## Raise exception, return False.....#####################
                valid = False
        for chip in floor["microchips"]:
            if chip in floor["generators"]:
                valid = True
            else:
                ## Raise exception, return False.....#####################
                valid = False
    """


def input_parser(lines):
    """
    The first floor contains a promethium generator and a promethium-compatible microchip.
    The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
    The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
    The fourth floor contains nothing relevant.
    """
    for line in lines:
        pass

    floors = [
            { "generators": ["promethium"], "microchips": ["promethium"]},
            { "generators": ["cobalt", "curium", "ruthenium", "plutonium"], "microchips": []},
            { "generators": [], "microchips": ["cobalt", "curium", "ruthenium", "plutonium"]},
            { "generators": [], "microchips": []}
            ]

    return floors


def elevator_mover(floors, currentfloor, totalmoves):
    # Possible elevator actions are
    # move 2 items down, move 1 item down, move 1 item up, move 2 items up
    if currentfloor == 0:
        elevator_actions = (1, 2)
    elif currentfloor == 3:
        elevator_actions = (-2, -1)
    else:
        elevator_actions = (-2, -1, 1, 2)

    



parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'), help='Path to input file')
args = parser.parse_args()
lines = args.inputfile.read().rstrip("\n").split("\n")

floors = input_parser(lines)
print(floors)
