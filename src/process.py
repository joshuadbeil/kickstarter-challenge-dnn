import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def num_cat_features(df, target=''):
    """Create two lists, each containing the column names of numerical (including. time) and categorical (object) data
    Args:
        target (str, optional): Define the name of the target variable to be ignored from the lists. Defaults to ''.
    Returns:
        numerical_features, categorical_features: two lists containing the names of the numerical and categorical columns.
            (optional: without the target variable)
    """

    numerical_features = [col for col in df.select_dtypes(exclude=['object', 'bool']) if col != target]    
    categorical_features = [col for col in df.select_dtypes(include=['object', 'bool']) if col != target]
    print("Categorical Features:", categorical_features, "\nNumerical Features:", numerical_features)

    return numerical_features, categorical_features