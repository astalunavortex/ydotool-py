from importlib.metadata import version

from .client import do_click, do_mousemove, do_type, do_key, do_wheel

__all__ = ["do_click", "do_mousemove", "do_type", "do_key", "do_wheel"]

__version__ = version("ydotool")
