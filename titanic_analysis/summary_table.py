import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': [df[col].dtype for col in df.columns],
        'Has Missing Values?': [df[col].isnull().any() for col in df.columns],
        'Number of Unique Values': [df[col].nunique() for col in df.columns]
    }
    
    summary_df = pd.DataFrame(summary_data)
    
    return summary_df
