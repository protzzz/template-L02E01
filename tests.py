import io

import pytest


@pytest.mark.parametrize(
    "input_, output",
    [
        ("10,20", "x^2: 100.0, y^2: 400.0"),
        ("-12,20", "x^2: 144.0, y^2: 400.0"),
        ("1.234,0", "x^2: 1.522756, y^2: 0.0"),
        ("-12.324,-12313", "x^2: 151.880976, y^2: 151609969.0"),
    ],
)
def test_output(script_runner, input_, output):
    ret = script_runner.run("points_input.py", stdin=io.StringIO(input_))

    assert ret.success
    assert f"{output}\n" in ret.stdout
    assert ret.stderr == ""
