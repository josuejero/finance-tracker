import pytest
from unittest.mock import patch, mock_open
from test_problem import clear_file_content, append_problem_message, run_subprocess

def test_append_problem_message():
    m_open = mock_open()
    with patch("builtins.open", m_open):
        append_problem_message("fake_path.txt", "Test problem message")
    m_open.assert_called_once_with("fake_path.txt", "a")
    m_open().write.assert_any_call("Test problem message\n\n")

def test_run_subprocess():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "tree output"
        result = run_subprocess(["tree", "-I", "venv"])
        assert result == "tree output"

def test_clear_file_content():
    m_open = mock_open()
    with patch("builtins.open", m_open):
        clear_file_content("fake_path.txt")
    m_open.assert_called_once_with("fake_path.txt", "w")
