class DataWrangler:
    import pandas as pd
    
    common_countries = []

    def clean_temp_data(self, start_date, end_date, data):
        # Removing non-common countries and undesired columns
        data = data.loc[data["Country"].isin(self.common_countries)]
        data = data.drop(columns=["AverageTemperatureUncertainty"])

        # Changing 'Year' column type to datetime and filtering dates
        data["dt"] = self.pd.to_datetime(data["dt"])
        data = data.loc[(data["dt"] >= start_date) & (data["dt"] <= end_date)]

        # Reformating temperature data
        aux = data.loc[data["Country"] == self.common_countries[0]]
        aux.rename(columns={"dt":"Date","AverageTemperature":self.common_countries[0]}, inplace=True)
        aux.drop(columns="Country", inplace = True)

        # Adding all countries
        for i in range(len(self.common_countries)):
            aux[self.common_countries[i]] = list(data.loc[data["Country"] == self.common_countries[i]]["AverageTemperature"])
        
        # Resetting dataframe indexes
        aux.set_index("Date", inplace=True)

        # Checking message
        print(">> Temperature data is cleaned and ready.")

        # Return cleaned dataframe
        return aux


    def common_countries_check(self, CO2_data, temp_data):
        CO2_country_list = list(CO2_data["Country Name"])
        temp_country_list = list(temp_data["Country"].unique())

        for country in CO2_country_list:
            if country in temp_country_list:
                self.common_countries.append(country)

        print(">> The list with common countries has been generated with", len(self.common_countries), "elements.")


    def clean_CO2_data(self, data):
        """

        """
        #Deleting undesired columns from CO2_data_raw
        CO2 = data.drop(columns=["Country Code", "Indicator Name", "Indicator Code"]).iloc[:,:-5]

        #Deleting rows with NaN values from CO2_data
        CO2.dropna(axis=0, how="any", inplace=True)
        CO2.reset_index(inplace=True, drop=True)

        #Transposing data and setting Country names as column label
        columns = list(CO2["Country Name"])
        CO2 = CO2.transpose()
        CO2.columns = columns
        CO2.drop(index="Country Name", inplace = True)
        CO2["Year"] = CO2.index

        #Reordering columns
        CO2 = CO2[["Year"]+columns]

        #Changing 'Year' column type to datetime
        CO2["Year"] = self.pd.to_datetime(CO2["Year"])

        #Resetting and ordering dataframe indexes
        CO2.set_index("Year", inplace=True)
        CO2.sort_index(axis=1, inplace=True)

        #Dropping columns with not common countries
        CO2 = CO2.loc[:, CO2.columns.isin(self.common_countries)]

        #Update common countries list
        self.common_countries = list(CO2.columns)

        #Checking message
        print(">> CO2 data is cleaned and ready.")

        #Return cleaned dataframe
        return CO2

    
    def clean_coord_data(self, data):
        pass