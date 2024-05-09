# cnts & mouselocal 병합하기

cnts['index_int'] = cnts.index.astype(str).str.extract(r'(\d+)', expand=False).astype(int)
mouselocal['index_int'] = mouselocal.index.astype(str).str.extract(r'(\d+)', expand=False).astype(int)
merged = pd.merge(cnts, mouselocal, on='index_int', how='inner')
merged.head()

# type 종류 확인
unique_values = merged['type'].unique()
print(unique_values)
#  = ['integral membrane' 'nucleus' 'cytoplasm']

# type별로 분류
merged_int = merged[merged['type'] == 'integral membrane']
merged_nu = merged[merged['type'] == 'nucleus']
merged_cyt = merged[merged['type'] == 'cytoplasm']