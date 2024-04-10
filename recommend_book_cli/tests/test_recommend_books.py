import pandas as pd
import pandera as pa
import pytest
from pandas.testing import assert_frame_equal

class TestValidateInputDf:

    @pytest.fixture
    def target(self):
        from recommend_books import validate_input_df
        return validate_input_df

    @pytest.mark.parametrize(
        "input_df_data, expected_message_pattern",
        [
            (
                {},
                "column 'name' not in"
            ),
            (
                {
                    "name": ["test_name"],
                    "title": ["test_title"],
                    "price": ["12345"],
                },
                "expected series 'price' to have type int64"
            )
        ]
    )
    def test_invalid_data_raises_schema_error(
        self,
        target,
        input_df_data,
        expected_message_pattern,
    ):
        """不正な値を指定するとSchemaErrorが発生すること。"""

        # arrange
        input_df = pd.DataFrame(input_df_data)

        # act
        with pytest.raises(pa.errors.SchemaError, match=expected_message_pattern):
            target(input_df)

    def test_valid_data_returns_dataframe(self, target):
        """正常な値を指定するとDataFrameを返すこと"""

        # arrange
        input_df_data = {
            "name": ["test_name", "test_name2"],
            "title": ["test_title", "test_title2"],
            "price": [1000, 2000]
        }
        input_df = pd.DataFrame(input_df_data)
        expected_df = pd.DataFrame(input_df_data)

        # act
        actual = target(input_df)

        # assert
        assert_frame_equal(actual, expected_df)