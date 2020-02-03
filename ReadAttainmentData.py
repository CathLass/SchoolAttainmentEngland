import pandas as pd
import pytest

class LA_ud:
    """
    Helper class for reading in '___la_ud.csv' files
    
    """
    # the file has a few worksheets
    # worksheet 'la ud' has the data, worksheet 'la ud metadata' gives info about the data columns and values
    data_sheet_name = 'la ud'
    meta_sheet_name = 'la ud metadata'

    def __init__(self,filepath,filename):
        self.filepath = filepath
        self.filename = filename
    
    def read_file(self):  
        """
        read the data and the metadata in
        returns: pandas dataframes - data, metadata
        """

        df_la_ud = pd.read_excel(self.filepath+self.filename,sheet_name=self.data_sheet_name)
        df_la_ud_meta = pd.read_excel(self.filepath+self.filename,sheet_name=self.meta_sheet_name)

        return df_la_ud, df_la_ud_meta


def test_LA_ud_init():
    LA_data = LA_ud('./data/','ks2_2019_revised_la_ud.xlsx')
    assert LA_data.filepath == './data/'
    assert LA_data.filename == 'ks2_2019_revised_la_ud.xlsx'
    assert LA_data.data_sheet_name == 'la ud'
    assert LA_data.meta_sheet_name == 'la ud metadata'

def test_LA_ud_read_file():
    LA_data = LA_ud('./data/','ks2_2019_revised_la_ud.xlsx')
    data, meta = LA_data.read_file()
    assert data.shape[1] == 90
    assert meta.shape[0] == 90
