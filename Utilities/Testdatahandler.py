import pandas as pd


class testdataHandler:
    def __init__(self, driver):
        self.driver = driver

    # file_path = '.\\TestData\\Teatcase.xlsx'
    # sh1 = sheet['Personal Details']
    df = pd.read_excel('D:\pythonProject1\TestData\Testcase.xlsx', sheet_name='PersonalDetails')
    # df.to_dict()
    # print(df.iloc[0])

    pf = df.iloc[0]
    print(pf['User'])

    # df.to_dict()
