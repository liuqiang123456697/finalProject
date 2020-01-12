
import pandas as pd
from sklearn.preprocessing import LabelEncoder
'''
    class for cleaning the data before using it
'''
class data_processing():
    def __init__(self,dataset_path,sep,number_of_bins):
        self.dataset = pd.read_csv(dataset_path,sep=sep)
        self.number_of_bins = number_of_bins

    def remove_index_col(self):
        self.dataset = self.dataset.loc[:,"0":"30"]   #remove the index

    def clear_na(self):
        self.dataset.dropna(inplace=True)

    def caterogical_to_numeric(self):
        le = LabelEncoder()
        self.dataset["30"] = le.fit_transform(self.dataset["30"])   #convert class from catagory to int

    def discritsize_columns(self,cols_to_discrit="all"):
        if cols_to_discrit == "all":
            for col_name in self.dataset.loc[:, "0":"29"].columns.values:
                self.dataset[col_name] = pd.qcut(self.dataset[col_name], q=self.number_of_bins)
        else:
            for col_name in cols_to_discrit:
                self.dataset[col_name] = pd.qcut(self.dataset[col_name], q=self.number_of_bins)

    def prepare_data(self):
        #clean
        self.remove_index_col()
        self.clear_na()
        self.caterogical_to_numeric()
        self.discritsize_columns()
        self.base_features =self.dataset.loc[:,"0":"9"]
        self.classes = self.dataset.loc[:,"30"]
        return self.base_features, self.classes