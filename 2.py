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

# type별 산점도 그리기
from matplotlib import pyplot as plt
import numpy as np

x_i = np.log2(merged_int['clip_enrichment'])
y_i = np.log2(merged_int['rden_change'])

x_n = np.log2(merged_nu['clip_enrichment'])
y_n = np.log2(merged_nu['rden_change'])

x_c = np.log2(merged_cyt['clip_enrichment'])
y_c = np.log2(merged_cyt['rden_change'])

fig, pl = plt.subplots(figsize=(5, 5))
pl.scatter(x_i, y_i, s=1, alpha =.3, color = 'r', label = 'integral membrane')
pl.scatter(x_n, y_n, s=1, alpha =.3, color = 'b', label = 'nucleus')
pl.scatter(x_c, y_c, s=1, alpha =.3, color = 'g', label = 'cytoplasm')

ax.grid()
ax.set_xlabel('CLIP enrichment (log₂)')
ax.set_ylabel('Ribosome density change (log₂)')