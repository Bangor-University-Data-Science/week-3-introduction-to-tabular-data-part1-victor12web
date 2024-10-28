import pandas as pd

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],
            'discrete': []
        },
        'categorical': {
            'nominal': [],
            'ordinal': []
        }
    }
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            # Check if the numerical feature is continuous or discrete
            if df[column].nunique() > 10:  # Example condition for continuous
                feature_types['numerical']['continuous'].append(column)
            else:  # Otherwise, consider it discrete
                feature_types['numerical']['discrete'].append(column)
        else:
            # For categorical features, we'll classify them as nominal or ordinal
            # Here we assume that 'Survived' is ordinal; you can modify this logic as needed
            if column == 'Survived':
                feature_types['categorical']['ordinal'].append(column)
            else:
                feature_types['categorical']['nominal'].append(column)
    
    return feature_types
