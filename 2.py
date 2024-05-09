# cnts & mouselocal 병합하기

cnts['index_int'] = cnts.index.astype(str).str.extract(r'(\d+)', expand=False).astype(int)
mouselocal['index_int'] = mouselocal.index.astype(str).str.extract(r'(\d+)', expand=False).astype(int)
merged = pd.merge(cnts, mouselocal, on='index_int', how='inner')
merged.head()