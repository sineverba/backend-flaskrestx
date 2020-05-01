# Test the configuration


def test_testing_config(test_app):
    test_app.config.from_object("project.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] != "my_precious"
