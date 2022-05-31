# pylint: disable=C0114,C0116,C0103
import math

from pydagogy_brent import Settings, brent


def test_convergence():
    s = Settings(1e-12, 1e-12, 1e-12, False)
    assert abs(brent(math.cos, 0.0, 3.0, s) - math.pi / 2) < 1e-12
