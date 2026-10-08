"""
Python wrapper for ydotool CLI commands.

Requires ydotool 1.0.4 to be installed and ydotoold daemon running.

See:
- https://github.com/ReimuNotMoe/ydotool
- https://github.com/ReimuNotMoe/ydotool/releases/tag/v1.0.4
"""

import subprocess

from .keycodes import get_keycodes
from .mousecodes import get_mousecode

def _run(*args: str) -> None:
	subprocess.run(
		["ydotool", *args],
		check=True
	)

def do_click(button: str, action: str, repeat: int | None = None, next_delay: int | None = None) -> None:
	"""
	Perform mouse click action.

	Args:
		button: Button name ('left', 'right', 'middle', 'side',
				'extra', 'forward', 'back', 'task').
		action: Action name ('click', 'down', 'up').
		repeat: Number of times to repeat the sequence (default: 1).
		next_delay: Delay in milliseconds between events.
					Full click takes 2x this value.

	Raises:
		ValueError: If button or action is invalid.
	"""

	mousecode = get_mousecode(button, action)

	if mousecode:
		args = []

		if repeat and repeat > 1:
			args.append(f"--repeat={repeat}")
		if next_delay and next_delay > 0:
			args.append(f"--next-delay={next_delay}")

		_run("click", *args, mousecode)
	else:
		raise ValueError("Invalid button or action")

def do_mousemove(x: int, y: int, absolute: bool = True) -> None:
	"""
	Move mouse cursor to coordinates.

	Args:
		x: X coordinate in pixels.
		y: Y coordinate in pixels.
		absolute: If True, move to absolute position.
				  If False, move relative to current position.

	Note:
		For correct movement, disable mouse acceleration
		and set mouse sensitivity to default
		in your desktop environment settings.
	"""

	args = []

	if absolute:
		args.append("--absolute")

	_run("mousemove", *args, str(x), str(y))

def do_type(text: str, key_delay: int | None = None, key_hold: int | None = None) -> None:
	"""
	Type text string.

	Args:
		text: Text to type. Handles special characters automatically.
		key_delay: Delay in milliseconds between key events (default: 20).
		key_hold: Hold time in milliseconds for each key (default: 20).
	"""

	args = []

	if key_delay and key_delay > 0:
		args.append(f"--key-delay={key_delay}")
	if key_hold and key_hold > 0:
		args.append(f"--key-hold={key_hold}")

	_run("type", *args, text)

def do_key(keys: list[str]) -> None:
	"""
	Press keyboard keys in sequence.
	Key names are defined in `keycodes.KEYCODES`

	Args:
		keys: List of 'key:state' strings where state is '1' (down)
			  or '0' (up). Order matters for combinations.

	Raises:
		ValueError: If any key is invalid or format is wrong.
	"""

	keycodes = get_keycodes(keys)

	if keycodes:
		_run("key", *keycodes)
	else:
		raise ValueError("Invalid keys")

def do_wheel(vertical: int = 0, horizontal: int = 0) -> None:
	"""
	Scroll mouse wheel.

	Args:
		vertical: Scroll ticks (positive=up, negative=down).
		horizontal: Scroll ticks (positive=right, negative=left).
	"""

	_run("mousemove", "--wheel", str(horizontal), str(vertical))
