from action.open_program_action import OpenProgramAction
from action.wait_action import WaitAction
from action.type_action import TypeAction
from action.press_action import PressAction



ACTIONS = {
    "open": OpenProgramAction,
    "wait": WaitAction,
    "type": TypeAction,
    "press": PressAction
}