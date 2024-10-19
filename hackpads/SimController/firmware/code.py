print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.row_pins = (board.GP10, board.GP9, board.GP8)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [KC.F13, KC.F14, KC.F15, KC.F16, KC.KP_1, ],
    [KC.F17, KC.F18, KC.F19, KC.F20, KC.KP_2, ],
    [KC.F21, KC.F22, KC.F23, KC.F24, KC.KP_3, ]
]

if __name__ == '__main__':
    keyboard.go()