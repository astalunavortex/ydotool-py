import pytest

from ydotool.keycodes import KEYCODES, _split_key, get_keycode, get_keycodes


class TestGetKeycode:
	@pytest.mark.parametrize(("name", "code"), [
		("enter", "28"), ("tab", "15"), ("esc", "1"), ("space", "57"),
		("ctrl", "29"), ("shift", "42"), ("alt", "56"), ("super", "125"),
		("a", "30"), ("z", "44"), ("0", "11"), ("9", "10"),
		("f1", "59"), ("f12", "88"), ("up", "103"), ("down", "108"),
	])
	def test_known_keys(self, name, code):
		assert get_keycode(name) == code

	def test_unknown_key(self):
		assert get_keycode("definitely-not-a-key") is None

	def test_all_codes_numeric(self):
		for name, code in KEYCODES.items():
			assert code.isdigit(), f"key {name!r}: code {code!r} is not a number"


class TestSplitKey:
	def test_valid(self):
		assert _split_key("ctrl:1") == ("ctrl", "1")
		assert _split_key("enter:0") == ("enter", "0")

	@pytest.mark.parametrize("bad", ["ctrl", "ctrl:", "ctrl:2", "ctrl:1:0"])
	def test_invalid(self, bad):
		assert _split_key(bad) is None


class TestGetKeycodes:
	def test_single_key(self):
		assert get_keycodes(["enter:1", "enter:0"]) == ["28:1", "28:0"]

	def test_ctrl_s(self):
		keys = ["ctrl:1", "s:1", "s:0", "ctrl:0"]
		assert get_keycodes(keys) == ["29:1", "31:1", "31:0", "29:0"]

	def test_unknown_key(self):
		assert get_keycodes(["ctrl:1", "nope:1"]) is None

	def test_bad_format(self):
		assert get_keycodes(["ctrl"]) is None

	def test_bad_state(self):
		assert get_keycodes(["ctrl:5"]) is None

	def test_empty_name(self):
		assert get_keycodes([":1"]) is None

	def test_empty_list(self):
		assert get_keycodes([]) == []
