from telegram.utils import set_commands, send_message


def test_set_commands():
    response = set_commands()

    assert False


def test_send_message():
    response = send_message("735269853", "Hello *STRANGER*!!!")
    assert False
