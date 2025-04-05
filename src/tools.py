from langchain.tools import tool

@tool
def get_column_stats(df,column: str) -> str:
    """Return stats for a given column in a pandas dataframe"""
    if column not in df.columns:
        return f"{column} not available in given pandas Dataframe"
    else:
        stats=df[column].describe()
        return stats.to_string()
    
