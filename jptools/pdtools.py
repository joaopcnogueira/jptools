from typing import Any, Dict, List, Union

import numpy as np
import pandas as pd

def separate(df: pd.DataFrame, 
             col: List[str], 
             into: List[str], 
             sep: List[str], 
             remove = True) -> pd.DataFrame:
    
    df = df.copy()
    
    df[into] = df[col].str.split(sep, expand = True)
    if remove:
        df.drop(col, axis=1, inplace=True)
    
    return df


def separate_rows(df: pd.DataFrame, col: str, sep: str) -> pd.DataFrame:

    df = df.copy()

    df[col] = df[col].str.split(sep)

    df = df.explode(col)

    return df
