#base 수 세기
base_count = pileup.groupby(['pos'])['matches'].apply(lambda x: pd.Series(list(''.join(x))).value_counts()).unstack().fillna(0)
base_count.head(10)

#ACGT 이외의 알파벳이 나와서 제거
def filter_bases(matches):
    return ''.join(base for base in matches if base in 'ACGT')

pileup['matches'] = pileup['matches'].apply(filter_bases)