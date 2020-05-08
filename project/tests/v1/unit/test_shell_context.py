# Test the shell context


def test_shell_context(test_app):
    assert len(test_app.shell_context_processors) == 1
    sc = test_app.make_shell_context()
    assert sc["app"] == test_app
