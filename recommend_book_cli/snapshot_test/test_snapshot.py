import pandas as pd
import pytest
from pathlib import Path

class TestOptimizeBookToBuy:
    @pytest.fixture
    def target(self):
        from recommend_books import optimize_book_to_buy

        return optimize_book_to_buy

    @pytest.mark.parametrize(
        "name, money",
        [
            ("altnight", 5000),
            ("kashew", 4000),
            ("susumuis", 3000),
        ]
    )
    def test_it_snapshot(self, target, snapshot, name, money):
        # arrange
        input_df = pd.read_csv(Path(__file__).parent / "test_input.csv")

        # act
        actual = target(input_df, name, money)

        # assert
        snapshot.assert_match(actual, f"result-{name}-{money}")
