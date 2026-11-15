class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title is not None:
            print(title)

        rows, columns = df.shape
        duplicates = df.duplicated().sum()
        duplicate_share = duplicates / rows if rows else 0.0

        print('Количество столбцов:', columns)
        print('Количество строк:', rows)
        print('Количество дубликатов:', duplicates)
        print('Доля дубликатов:', format(duplicate_share, self.percent_format))

        print(df.describe(include='all' if self.include_all else None))

        missing = df.isna()
        print('Количество пропусков:', missing.sum().sum())
        print('Доля пропусков:', format(missing.mean(axis=None), self.float_format))