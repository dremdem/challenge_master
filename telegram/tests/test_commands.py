"""
Сommands tests
"""

from io import StringIO

from django.core.management import call_command


def test_set_webhook_command() -> None:
    """
    Test set_webhook command
    """

    out = StringIO()
    call_command('set_webhook', stdout=out)
    print(out.getvalue())
    assert 'status_code: 200' in out.getvalue()


def test_clear_webhook_command() -> None:
    """
    Test set_webhook command
    """

    out = StringIO()
    call_command('clear_webhook', stdout=out)
    print(out.getvalue())
    assert 'status_code: 200' in out.getvalue()


def test_get_webhook_info_command() -> None:
    """
    Test set_webhook command
    """

    out = StringIO()
    call_command('get_webhook_info', stdout=out)
    print(out.getvalue())
    assert 'status_code: 200' in out.getvalue()
