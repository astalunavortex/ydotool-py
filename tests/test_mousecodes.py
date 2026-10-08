from ydotool.mousecodes import get_mousecode


class TestGetMousecode:
	def test_click_all_buttons(self):
		expected = {
			"left": "C0",
			"right": "C1",
			"middle": "C2",
			"side": "C3",
			"extra": "C4",
			"forward": "C5",
			"back": "C6",
		}
		for button, code in expected.items():
			assert get_mousecode(button, "click") == code

	def test_down_codes(self):
		assert get_mousecode("left", "down") == "40"
		assert get_mousecode("right", "down") == "41"
		assert get_mousecode("middle", "down") == "42"

	def test_up_codes(self):
		assert get_mousecode("left", "up") == "80"
		assert get_mousecode("right", "up") == "81"
		assert get_mousecode("middle", "up") == "82"

	def test_invalid_button(self):
		assert get_mousecode("nope", "click") is None

	def test_invalid_action(self):
		assert get_mousecode("left", "nope") is None

	def test_both_invalid(self):
		assert get_mousecode("nope", "nope") is None
