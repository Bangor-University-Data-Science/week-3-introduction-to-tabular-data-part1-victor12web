def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values_dict = {}
    
    for feature in categorical_features:
        if feature in df.columns:  # Check if the feature exists in the DataFrame
            unique_values_dict[feature] = df[feature].unique().tolist()  # Get unique values and convert to list
    
    return unique_values_dict
