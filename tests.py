import io

import pytest


@pytest.mark.parametrize(
    "input_, output",
    [
        ("10,20;20,10", "[{'x': 100.0, 'y': 400.0}, {'x': 400.0, 'y': 100.0}]"),
        ("-12,20", "[{'x': 144.0, 'y': 400.0}]"),
        ("1.234,0;10,20", "[{'x': 1.522756, 'y': 0.0}, {'x': 100.0, 'y': 400.0}]"),
        ("1.234,0;10,20;1.234,0;10,20", "[{'x': 1.522756, 'y': 0.0}, {'x': 100.0, 'y': 400.0}, {'x': 1.522756, 'y': 0.0}, {'x': 100.0, 'y': 400.0}]"),
    ],
)
def test_output(script_runner, input_, output):
    ret = script_runner.run("points_input.py", stdin=io.StringIO(input_))

    assert ret.success
    assert output in ret.stdout
    assert ret.stderr == ""
