import pytest

from ydotool.client import do_click, do_key, do_mousemove, do_type, do_wheel


class TestDoClick:
	def test_left_click(self, last_cmd):
		do_click("left", "click")
		assert last_cmd() == ["ydotool", "click", "C0"]

	def test_right_click(self, last_cmd):
		do_click("right", "click")
		assert last_cmd() == ["ydotool", "click", "C1"]

	def test_down_and_up(self, last_cmd):
		do_click("left", "down")
		assert last_cmd() == ["ydotool", "click", "40"]
		do_click("left", "up")
		assert last_cmd() == ["ydotool", "click", "80"]

	def test_repeat(self, last_cmd):
		do_click("left", "click", repeat=3)
		assert last_cmd() == ["ydotool", "click", "--repeat=3", "C0"]

	def test_repeat_one_omitted(self, last_cmd):
		do_click("left", "click", repeat=1)
		assert last_cmd() == ["ydotool", "click", "C0"]

	def test_repeat_zero_omitted(self, last_cmd):
		do_click("left", "click", repeat=0)
		assert last_cmd() == ["ydotool", "click", "C0"]

	def test_next_delay(self, last_cmd):
		do_click("left", "click", next_delay=100)
		assert last_cmd() == ["ydotool", "click", "--next-delay=100", "C0"]

	def test_repeat_and_delay_combined(self, last_cmd):
		do_click("left", "click", repeat=2, next_delay=50)
		assert last_cmd() == ["ydotool", "click", "--repeat=2", "--next-delay=50", "C0"]

	def test_invalid_button_raises(self, mock_subprocess):
		with pytest.raises(ValueError):
			do_click("nope", "click")
		mock_subprocess.assert_not_called()

	def test_invalid_action_raises(self, mock_subprocess):
		with pytest.raises(ValueError):
			do_click("left", "nope")
		mock_subprocess.assert_not_called()


class TestDoMousemove:
	def test_absolute(self, last_cmd):
		do_mousemove(500, 300)
		assert last_cmd() == ["ydotool", "mousemove", "--absolute", "500", "300"]

	def test_relative(self, last_cmd):
		do_mousemove(100, -50, absolute=False)
		assert last_cmd() == ["ydotool", "mousemove", "100", "-50"]

	def test_negative_absolute(self, last_cmd):
		do_mousemove(-10, -20)
		assert last_cmd() == ["ydotool", "mousemove", "--absolute", "-10", "-20"]


class TestDoWheel:
	def test_vertical_up(self, last_cmd):
		do_wheel(vertical=3)
		assert last_cmd() == ["ydotool", "mousemove", "--wheel", "0", "3"]

	def test_vertical_down(self, last_cmd):
		do_wheel(vertical=-5)
		assert last_cmd() == ["ydotool", "mousemove", "--wheel", "0", "-5"]

	def test_horizontal(self, last_cmd):
		do_wheel(horizontal=2)
		assert last_cmd() == ["ydotool", "mousemove", "--wheel", "2", "0"]

	def test_both_axes(self, last_cmd):
		do_wheel(vertical=-2, horizontal=1)
		assert last_cmd() == ["ydotool", "mousemove", "--wheel", "1", "-2"]

	def test_defaults(self, last_cmd):
		do_wheel()
		assert last_cmd() == ["ydotool", "mousemove", "--wheel", "0", "0"]


class TestDoType:
	def test_simple(self, last_cmd):
		do_type("hello")
		assert last_cmd() == ["ydotool", "type", "hello"]

	def test_with_spaces(self, last_cmd):
		do_type("hello world")
		assert last_cmd() == ["ydotool", "type", "hello world"]

	def test_key_delay(self, last_cmd):
		do_type("hello", key_delay=100)
		assert last_cmd() == ["ydotool", "type", "--key-delay=100", "hello"]

	def test_key_hold(self, last_cmd):
		do_type("hello", key_hold=50)
		assert last_cmd() == ["ydotool", "type", "--key-hold=50", "hello"]

	def test_both_flags(self, last_cmd):
		do_type("hi", key_delay=10, key_hold=20)
		assert last_cmd() == ["ydotool", "type", "--key-delay=10", "--key-hold=20", "hi"]

	def test_zero_delay_omitted(self, last_cmd):
		do_type("hi", key_delay=0, key_hold=0)
		assert last_cmd() == ["ydotool", "type", "hi"]


class TestDoKey:
	def test_enter(self, last_cmd):
		do_key(["enter:1", "enter:0"])
		assert last_cmd() == ["ydotool", "key", "28:1", "28:0"]

	def test_ctrl_s(self, last_cmd):
		do_key(["ctrl:1", "s:1", "s:0", "ctrl:0"])
		assert last_cmd() == ["ydotool", "key", "29:1", "31:1", "31:0", "29:0"]

	def test_invalid_key_raises(self, mock_subprocess):
		with pytest.raises(ValueError):
			do_key(["nope:1"])
		mock_subprocess.assert_not_called()

	def test_invalid_format_raises(self, mock_subprocess):
		with pytest.raises(ValueError):
			do_key(["ctrl"])
		mock_subprocess.assert_not_called()

	def test_invalid_state_raises(self, mock_subprocess):
		with pytest.raises(ValueError):
			do_key(["ctrl:2"])
		mock_subprocess.assert_not_called()

	def test_empty_list_raises(self, mock_subprocess):
		with pytest.raises(ValueError):
			do_key([])
		mock_subprocess.assert_not_called()
