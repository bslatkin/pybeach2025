def take_action(light):
    if light == "red":
        print("Stop")
    elif light == "yellow":
        print("Slow down")
    elif light == "green":
        print("Go!")
    else:
        raise RuntimeError


take_action("red")
take_action("yellow")
take_action("green")


def take_match_action(light):
    match light:
        case "red":
            print("Stop")
        case "yellow":
            print("Slow down")
        case "green":
            print("Go!")
        case _:
            raise RuntimeError


take_match_action("red")
take_match_action("yellow")
take_match_action("green")


RED = "red"
YELLOW = "yellow"
GREEN = "green"


def take_match_action(light):
    match light:
        case "red":
            print("Stop")
        case "yellow":
            print("Slow down")
        case "green":
            print("Go!")
        case _:
            raise RuntimeError


def take_truncated_action(light):
    match light:
        case RED:
            print("Stop")


take_truncated_action(GREEN)


def take_debug_action(light):
    match light:
        case RED:
            print(f"{RED=}, {light=}")


take_debug_action(GREEN)


def unpacking_action(light):
    try:
        (RED,) = (light,)
    except TypeError:
        # Did not match
        pass
    else:
        # Matched
        print(f"{RED=}, {light=}")


unpacking_action(GREEN)


import enum


class ColorEnum(enum.Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"


from typing import assert_never


def take_enum_action(light):
    match light:
        case ColorEnum.RED:
            print("Stop")
        case ColorEnum.YELLOW:
            print("Slow down")
        case ColorEnum.GREEN:
            print("Go!")
        case unreachable:
            assert_never(unreachable)


take_enum_action(ColorEnum.RED)  # "Stop"
take_enum_action(ColorEnum.YELLOW)  # "Slow down"
take_enum_action(ColorEnum.GREEN)  # "Go!"
