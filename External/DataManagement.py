import pandas as pd
import numpy as np

class DataManagement:
    @classmethod
    def convert_to_str(cls, values: list) -> list:
        return [str(x) for x in values]

    @classmethod
    def add_row_to_data_frame(cls, frame, values: list) -> pd.DataFrame:
        row = pd.DataFrame([values], columns=frame.columns)
        return pd.concat([frame, row], ignore_index=True)

    @classmethod
    def transpose_range(cls, data):
        pd_arr = np.array(data)
        return pd_arr.T.tolist()




if __name__ == '__main__':
    df = pd.DataFrame()
    df['name'] = ['John', 'Steve', 'Sarah']
    df['test'] = [1, 2, 3]
    df = (DataManagement.add_row_to_data_frame(df, ['Sup', 12]))
    print(df)
