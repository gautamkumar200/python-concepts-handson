from unittest import mock

from calculator import dnd


#@mock.patch("calculator.dnd.randint", return_value=5, autospec=True)
def test_attack_dnd():
    with mock.patch("calculator.dnd.randint", return_value=5):
        assert dnd.attack_dnd(1) == 6


if __name__ == "__main__":
    test_attack_dnd()