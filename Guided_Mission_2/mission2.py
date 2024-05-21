import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#파일 불러오기
data = pd.read_csv('fivepcounts-filtered-RPF-siLuc.txt', sep='\t', header=None)

#column 설정
data.columns = ['chr', 'start', 'end', 'count', 'chr_', 'transcript_start', 'transcript_end', 'transcript_id', 'start_codon_pos', 'strand']
data.head()

# start codon 위치 계산 
data['relative_pos'] = data['start'] - data['start_codon_pos']

# 히스토그램 범위
min_pos = data['relative_pos'].min()
max_pos = data['relative_pos'].max()
width = 1
range = (min_pos, max_pos + width)
num = (max_pos - min_pos) // width + 1

hist, graph = np.histogram(data['relative_pos'], bins=num, range=range)

# read count를 1000으로 나눔
hist = hist / 1000

# 히스토그램 그리기
plt.figure(figsize=(10, 5))
plt.bar(graph[:-1], hist, width=bin_width, align='edge')
plt.axvline(x=0, color='red', linewidth=1)
plt.grid(axis='y')
plt.show() 

#오류