class InternalCommandException(Exception):
    pass


class ExitReplException(InternalCommandException):
    pass


class InvalidGroupFormat(Exception):
    pass


# Handle click.exceptions.Exit introduced in Click 7.0
try:
    from click.exceptions import Exit as ClickExit
except (ImportError, ModuleNotFoundError):

    class ClickExit(RuntimeError):
        pass
