import pytest

from unittest.mock import patch

@pytest.fixture
def mock_subprocess():
	with patch("subprocess.run") as mock_run:
		yield mock_run

@pytest.fixture
def last_cmd(mock_subprocess):
	def _last_cmd() -> list[str]:
		assert mock_subprocess.called, "subprocess.run was not called"
		return list(mock_subprocess.call_args.args[0])
	return _last_cmd
