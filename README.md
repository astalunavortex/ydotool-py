# ydotool-py

[![PyPI version](https://img.shields.io/pypi/v/ydotool.svg)](https://pypi.org/project/ydotool/)
[![Python versions](https://img.shields.io/pypi/pyversions/ydotool.svg)](https://pypi.org/project/ydotool/)
[![License: MIT](https://img.shields.io/badge/License-MIT-gren.svg)](https://opensource.org/licenses/MIT)

Python wrapper for [ydotool](https://github.com/ReimuNotMoe/ydotool) - a generic command-line automation tool that works on **Wayland**, **X11**, and even **TTY**.

Unlike `pyautogui`, `ydotool` operates at the kernel level via `/dev/uinput`, making it compatible with any Linux desktop environment.

## Features

- **Mouse**: move, click, scroll
- **Keyboard**: type text, press keys, hotkey combinations

## Installation

### 1. Install ydotool

```bash
# Debian/Ubuntu
sudo apt install ydotool

# Arch Linux
sudo pacman -S ydotool

# Fedora
sudo dnf install ydotool
```
If your distro doesn't have `ydotool`, you can build it from source [ydotool](https://github.com/ReimuNotMoe/ydotool)

### 2. Start the daemon

```bash
# Enable for current user
systemctl --user enable --now ydotool.service

# Or run manually
ydotoold
```

### 4. Install Python package

```bash
# Add with uv
uv add ydotool

# Or install with pip
pip install ydotool
```

## Quick Start

```python
from ydotool import do_click, do_mousemove, do_type, do_key, do_wheel

# Move mouse and click
do_mousemove(500, 300)
do_click('left', 'click')

# Type text
do_type("Hello, Wayland!")

# Press key combination (Ctrl+S)
do_key(['ctrl:1', 's:1', 's:0', 'ctrl:0'])

# Scroll down
do_wheel(vertical=-3)

# Double-click
do_click('left', 'click', repeat=2)
```

## API Reference

### Mouse Control

#### `do_click(button, action, repeat=None, next_delay=None)`

Perform mouse click action.

- **button**: `'left'`, `'right'`, `'middle'`, `'side'`, `'extra'`, `'forward'`, `'back'`
- **action**: `'click'`, `'down'`, `'up'`
- **repeat**: Number of repetitions
- **next_delay**: Delay between events in milliseconds

```python
do_click('left', 'click')               # Single left click
do_click('right', 'click', repeat=2)    # Double right click
do_click('left', 'down')                # Press and hold
do_click('left', 'up')                  # Release
```

#### `do_mousemove(x, y, absolute=True)`

Move mouse cursor.

```python
do_mousemove(500, 300)                    # Absolute position
do_mousemove(100, -50, absolute=False)    # Relative movement
```

#### `do_wheel(vertical=0, horizontal=0)`

Scroll mouse wheel.

```python
do_wheel(vertical=3)      # Scroll up
do_wheel(vertical=-5)     # Scroll down
do_wheel(horizontal=2)    # Scroll right
```

### Keyboard Control

#### `do_type(text, key_delay=None, key_hold=None)`

Type text string. Handles special characters automatically.

```python
do_type("Hello, World!")
do_type("Slow typing", key_delay=100)
```

#### `do_key(keys)`

Press keyboard keys in sequence.

Keys are specified as `'keyname:state'` where state is `'1'` (down) or `'0'` (up).

```python
# Press Enter
do_key(['enter:1', 'enter:0'])

# Ctrl+S
do_key(['ctrl:1', 's:1', 's:0', 'ctrl:0'])

# Alt+Tab
do_key(['alt:1', 'tab:1', 'tab:0', 'alt:0'])
```

See [keycodes.py](src/ydotool/keycodes.py) for the complete list of key names.


## Troubleshooting

### "Failed to connect to ydotoold"

Make sure the daemon is running:

```bash
systemctl --user status ydotool.service
# or
pgrep -a ydotoold
```

### "Permission denied" on `/dev/uinput`

Check udev rules and log out/in:

```bash
ls -l /dev/uinput
# Should show your user has access
```

### Mouse coordinates are wrong

Disable mouse acceleration and set mouse sensetivity to default in your desktop environment settings.

### Keys not working

Check that you're using the correct format: `'keyname:state'` (e.g., `'ctrl:1'`, not just `'ctrl'`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.

[ydotool](https://github.com/ReimuNotMoe/ydotool) is licensed under [AGPL-3.0](https://github.com/ReimuNotMoe/ydotool/blob/master/LICENSE).
