import pandas as pd


def salary_stripper(dataframe, column):
    """
    Function that takes salary as string and convert it to a number,
    averaging a salary range if necessary
    :param dataframe:dataframe to be cleaned
    :param column:salary string column
    :return: dateframe:cleaned dataframe with salary number
    """
    dataframe[str(column)] = dataframe[str(column)].replace({'\$': ''}, regex=True)
    dataframe[str(column)].replace(regex=True, inplace=True, to_replace=r'\D', value=r' ')
    dataframe[str(column)] = dataframe[str(column)].str.replace(' ', ',')
    dataframe = dataframe.join(
        dataframe[str(column)].str.split(',,,', 1, expand=True).rename(columns={0: 'Low', 1: 'High'}))
    dataframe['Low'] = dataframe['Low'].str.replace(',', '')
    dataframe['Low'] = dataframe['Low'].astype('float64')
    dataframe.drop(str(column), axis=1, inplace=True)
    dataframe['High'] = dataframe['High'].str.replace(',', '')
    dataframe['High'] = dataframe['High'].apply(pd.to_numeric)
    dataframe['Average'] = dataframe[['Low', 'High']].mean(axis=1)
    return dataframe
