class FileManager:
    import pandas as pd

    def file_to_df(self, file_path):
        """ Reads a csv file and generates a dataframe

            Args: 
                "file_path" [(str)] - Relative path where the file is stored

            Returns:
                The generated dataframe
        """

        #return pd.read_csv(file_path)

    def df_to_file(self, data, file_path):
        """ Saves df to csv file

            Args:
                "data" [(pandas.dataframe)] - Dataframe to be saved
                "file_path" [(str)] - Relative path where the data is saved

            Returns:
                None
        """

