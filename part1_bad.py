RED = "red"
YELLOW = "yellow"
GREEN = "green"


def take_constant_action(light):
    match light:
        case RED:
            print("Stop")
        case YELLOW:
            print("Slow down")
        case GREEN:
            print("Go!")
        case _:
            raise RuntimeError
