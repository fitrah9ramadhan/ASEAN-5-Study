def specific_countries_time_series(data, country_list):
    
    '''
        # data        : world bank data (data frame)
        # country_list: list of countries
            e.g countries = ["France", "Japan", "Germany"]
    '''
    
    data.drop(columns = ["Country Code", "Indicator Code", "Indicator Name"], inplace = True)
    data = data[data["Country Name"].isin(country_list)]
    data = data.transpose()
    new_header = data.iloc[0]
    data = data[1:] 
    data.columns = new_header    
    return data.dropna().astype(float)