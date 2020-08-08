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
    call_command('set_webhook', port='80', stdout=out)
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
