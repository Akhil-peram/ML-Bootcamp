def check_nulls(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def validate_schema(df,expected_columns):
    missing = set(expected_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
