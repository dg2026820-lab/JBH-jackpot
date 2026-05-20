GOLD   = vector(1.0, 0.84, 0.0)
SILVER = vector(0.75, 0.75, 0.75)
RED    = vector(0.9, 0.1, 0.1)
GREEN  = vector(0.1, 0.8, 0.2)
BLUE   = vector(0.1, 0.3, 0.9)
WHITE  = color.white
BLACK  = color.black
DARK   = vector(0.12, 0.12, 0.15)

SYMBOLS = [
    ("7",  RED),
    ("★",  GOLD),
    ("♠",  WHITE),
    ("♥",  RED),
    ("♦",  GOLD),
    ("BAR", GREEN),

body = box(
    pos=vector(0, 0, 0),
    size=vector(9, 11, 2),
    color=DARK,
    opacity=1
)
