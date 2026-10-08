"""
Keyboard key code mappings based on `/usr/include/linux/input-event-codes.h`

All codes are decimal integers corresponding to `KEY_*` constants
in the Linux kernel header.

Unusual keys have not been added here.
"""

# exclamation         = shift + 1               ( ! ) = ( shift ) + ( 1 )
# at                  = shift + 2               ( @ ) = ( shift ) + ( 2 )
# hash                = shift + 3               ( # ) = ( shift ) + ( 3 )
# dollar              = shift + 4               ( $ ) = ( shift ) + ( 4 )
# percent             = shift + 5               ( % ) = ( shift ) + ( 5 )
# caret               = shift + 6               ( ^ ) = ( shift ) + ( 6 )
# ampersand           = shift + 7               ( & ) = ( shift ) + ( 7 )
# asterisk            = shift + 8               ( * ) = ( shift ) + ( 8 )
# leftparenthesis     = shift + 9               ( ( ) = ( shift ) + ( 9 )
# rightparenthesis    = shift + 0               ( ) ) = ( shift ) + ( 0 )
# underscore          = shift + minus           ( _ ) = ( shift ) + ( - )
# plus                = shift + equal           ( + ) = ( shift ) + ( = )
# leftcurlybracket    = shift + leftbracket     ( { ) = ( shift ) + ( [ )
# rightcurlybracket   = shift + rightbracket    ( } ) = ( shift ) + ( ] )
# verticalbar         = shift + backslash       ( | ) = ( shift ) + ( \ )
# colon               = shift + semicolon       ( : ) = ( shift ) + ( ; )
# doublequote         = shift + apostrophe      ( " ) = ( shift ) + ( ' )
# less                = shift + comma           ( < ) = ( shift ) + ( , )
# greater             = shift + dot             ( > ) = ( shift ) + ( . )
# question            = shift + slash           ( ? ) = ( shift ) + ( / )
# tilde               = shift + grave           ( ~ ) = ( shift ) + ( ` )

KEYCODES = {
	"0": "11",
	"1": "2",
	"2": "3",
	"3": "4",
	"4": "5",
	"5": "6",
	"6": "7",
	"7": "8",
	"8": "9",
	"9": "10",

	"a": "30",
	"b": "48",
	"c": "46",
	"d": "32",
	"e": "18",
	"f": "33",
	"g": "34",
	"h": "35",
	"i": "23",
	"j": "36",
	"k": "37",
	"l": "38",
	"m": "50",
	"n": "49",
	"o": "24",
	"p": "25",
	"q": "16",
	"r": "19",
	"s": "31",
	"t": "20",
	"u": "22",
	"v": "47",
	"w": "17",
	"x": "45",
	"y": "21",
	"z": "44",

	"esc": "1",
	"backspace": "14",
	"tab": "15",
	"enter": "28",
	"space": "57",
	"capslock": "58",

	"ctrl": "29",
	"leftctrl": "29",
	"rightctrl": "97",

	"shift": "42",
	"leftshift": "42",
	"rightshift": "54",

	"alt": "56",
	"leftalt": "56",
	"rightalt": "100",

	"super": "125",
	"leftsuper": "125",
	"rightsuper": "126",

	"menu": "127",
	"compose": "127",

	"f1": "59",
	"f2": "60",
	"f3": "61",
	"f4": "62",
	"f5": "63",
	"f6": "64",
	"f7": "65",
	"f8": "66",
	"f9": "67",
	"f10": "68",
	"f11": "87",
	"f12": "88",

	"up": "103",
	"down": "108",
	"left": "105",
	"right": "106",

	"home": "102",
	"end": "107",
	"pageup": "104",
	"pagedown": "109",

	"insert": "110",
	"delete": "111",

	"printscreen": "99",

	"scrolllock": "70",

	"pause": "119",

	"numlock": "69",

	"minus": "12",
	"equal": "13",
	"leftbracket": "26",
	"rightbracket": "27",
	"semicolon": "39",
	"apostrophe": "40",
	"grave": "41",
	"backslash": "43",
	"comma": "51",
	"dot": "52",
	"slash": "53",

	"np0": "82",
	"np1": "79",
	"np2": "80",
	"np3": "81",
	"np4": "75",
	"np5": "76",
	"np6": "77",
	"np7": "71",
	"np8": "72",
	"np9": "73",

	"npasterisk": "55",
	"npminus": "74",
	"npplus": "78",
	"npdot": "83",
	"npenter": "96",
	"npslash": "98",
	"npequal": "117",

	"mute": "113",
	"volumedown": "114",
	"volumeup": "115",
	"micmute": "248",

	"power": "116",
	"sleep": "142",
	"wakeup": "143",

	"playpause": "164",
	"nextsong": "163",
	"previoussong": "165",

	"back": "158",
	"forward": "159",
	"homepage": "172",
	"search": "217",
	"refresh": "173",

	"stop": "166",

	"brightnessup": "224",
	"brightnessdown": "225",

	"browser": "150",
	"mail": "155",
	"calc": "140",
}

def _split_key(key_str: str) -> tuple[str, str] | None:
	if key_str.count(":") != 1:
		return None
	key, state = key_str.split(":")
	if state in ("0", "1"):
		return key, state
	return None

def get_keycode(key: str) -> str | None:
	return KEYCODES.get(key)

def get_keycodes(keys: list[str]) -> list[str] | None:
	keycodes_list = []

	for key_str in keys:
		key_and_state = _split_key(key_str)

		if not key_and_state:
			return None
		
		key, state = key_and_state
		keycode = get_keycode(key)

		if not keycode:
			return None

		keycodes_list.append(f"{keycode}:{state}")

	return keycodes_list
