import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_app(runner):
    result = runner.invoke(app, ["Ashley"])
    assert result.exit_code == 0
    assert "Hello Ashley!" in result.stdout
    
    
def test_app_help(runner):
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "The name of the person to greet." in result.stdout