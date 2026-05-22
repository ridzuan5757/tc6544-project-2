import math
from pathlib import Path

import numpy as np
import pytest

from ga.instance import load_tsp

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TEST4 = DATA_DIR / "test4.tsp"


class TestLoadTsp:
    def test_returns_coords_and_dist_matrix(self):
        coords, dist = load_tsp(TEST4)
        assert isinstance(coords, np.ndarray)
        assert isinstance(dist, np.ndarray)

    def test_coords_shape(self):
        coords, _ = load_tsp(TEST4)
        assert coords.shape == (4, 2)

    def test_coords_values(self):
        coords, _ = load_tsp(TEST4)
        expected = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float64)
        np.testing.assert_array_equal(coords, expected)

    def test_dist_matrix_shape(self):
        _, dist = load_tsp(TEST4)
        assert dist.shape == (4, 4)

    def test_dist_matrix_diagonal_is_zero(self):
        _, dist = load_tsp(TEST4)
        np.testing.assert_array_equal(np.diag(dist), 0.0)

    def test_dist_matrix_symmetric(self):
        _, dist = load_tsp(TEST4)
        np.testing.assert_array_equal(dist, dist.T)

    def test_dist_matrix_known_values(self):
        _, dist = load_tsp(TEST4)
        assert dist[0, 1] == pytest.approx(1.0)
        assert dist[0, 2] == pytest.approx(math.sqrt(2))
        assert dist[0, 3] == pytest.approx(1.0)
        assert dist[1, 2] == pytest.approx(1.0)
        assert dist[1, 3] == pytest.approx(math.sqrt(2))
        assert dist[2, 3] == pytest.approx(1.0)

    def test_file_not_found(self):
        with pytest.raises(Exception):
            load_tsp("nonexistent.tsp")
