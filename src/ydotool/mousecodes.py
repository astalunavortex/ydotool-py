"""
Mouse button and action code mappings for ydotool.

ydotool 1.0.4 uses hexadecimal bit masks for mouse buttons:
- Lower bits (0x00-0x07): button identifier
- Upper bits (0x40=DOWN, 0x80=UP, 0xC0=CLICK): action

0x can be omitted.
"""

MOUSECODES = {
	"left": "0",
	"right": "1",
	"middle": "2",
	"side": "3",
	"extra": "4",
	"forward": "5",
	"back": "6",
	"task": "7",
}

ACTIONCODES = {
	"click": "C",
	"down": "4",
	"up": "8",
}

def get_mousecode(button: str, action: str) -> str | None:
	buttoncode = MOUSECODES.get(button)
	actioncode = ACTIONCODES.get(action)

	if buttoncode and actioncode:
		return f"{actioncode}{buttoncode}"

	return None
