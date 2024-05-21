#base 수 세기
base_count = pileup.groupby(['pos'])['matches'].apply(lambda x: pd.Series(list(''.join(x))).value_counts()).unstack().fillna(0)
base_count.head(10)

