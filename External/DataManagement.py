import pandas as pd


def convert_to_str(values: list) -> list:
    return [str(x) for x in values]


def add_row_to_data_frame(frame, values: list) -> pd.DataFrame:
    row = pd.DataFrame([values], columns=frame.columns)
    return pd.concat([frame, row], ignore_index=True)


if __name__ == '__main__':
    df = pd.DataFrame()
    df['name'] = ['John', 'Steve', 'Sarah']
    df['test'] = [1, 2, 3]
    print(add_row_to_data_frame(df, ['Sup', 12]))
