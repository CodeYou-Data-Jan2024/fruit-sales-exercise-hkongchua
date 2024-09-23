import os
import pandas as pd
import pytest

CSV_FILE = "fruit.csv"

# Fixture to load the CSV file once for all tests
@pytest.fixture(scope="module")
def df():
    return pd.read_csv(CSV_FILE)

# Test to check if the CSV file exists
def test_file_exists():
    assert os.path.exists(CSV_FILE), "CSV file does not exist"

# Test to check if the expected columns exist in the CSV file
def test_columns_exist(df):
    expected_columns = ['Apples', 'Bananas']
    for col in expected_columns:
        assert col in df.columns, f"Column {col} does not exist"

# Parameterized test to check if expected values exist in the respective columns
@pytest.mark.parametrize("column_name,expected_values", [
    ('Apples', [35, 41]),
    ('Bananas', [21, 34])
])
def test_values_exist(df, column_name, expected_values):
    for val in expected_values:
        assert val in df[column_name].values, f"Value {val} not found in column {column_name}"
