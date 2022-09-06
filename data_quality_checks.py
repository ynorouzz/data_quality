# Measure basic statictics

def df_quality(df):
    """
    Data quality checks per dataframe
    :param df: dataframe that includes raw data
    :return data_describe: dataframe that includes statistics of df such as min, max, std, count, ...
    """

    def null_count(df):
        """
        Percentage of Null values
        :param df: dataframe
        :return: number of nulls per column
        """

        return df.isna().sum()

    def dtypes(df):
        """
        Dataframe data types
        :param df: dataframe
        :return: datatypes of columns
        """
        return df.dtypes

    def uniqueness(df):
        """
        Dataframe unique values per column
        :param df: dataframe
        :return: numbre of unique values per column
        """
        return df.nunique()

    def df_describe(df):
        """
        Dataframe statistics
        :param df: dataframe
        :return: desription of dataframe such as min, max, std, ... per column
        """
        return df.describe(include='all')

    
    df = df.copy()
    # collect desciption, datatypes, and number of uniq values per column
    data_describe = df_describe(df)
    data_types = dtypes(df)
    data_unique = uniqueness(df)

    # create a new column to show number of nulls of each column in original data
    data_describe.loc['nulls'] = null_count(df)
    # create a new column to show data type of each column in original data
    data_describe.loc['dtypes'] = data_types
    
    # create a new column to show number of unique values of each column in original data
    data_describe.loc['unique'] = data_unique

    return data_describe


df_preproc_qa = df_quality(df)
print("\n Raw data statistics:", df_preproc_qa)


# Columns with null values
mask = df_preproc_qa.loc['nulls', :]!=0
col_null = df_preproc_qa.columns[mask]
print(col_null)
