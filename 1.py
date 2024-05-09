from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import pearsonr

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.scatter(np.log2(cnts['clip_enrichment']),
                      np.log2(cnts['rden_change']),
            s=1, alpha=.4, color='k')
ax.grid()
ax.set_xlabel('CLIP enrichment (log₂)')
ax.set_ylabel('Ribosome density change (log₂)')

mask = np.isfinite(cnts['clip_enrichment']) & np.isfinite(cnts['rden_change']) & (cnts['clip_enrichment'] > 0) & (cnts['rden_change'] > 0)
r, _ = pearsonr(np.log2(cnts['clip_enrichment'][mask]), np.log2(cnts['rden_change'][mask]))
plt.text(0.1, 0.9, f'r = {r:.4f}', transform=plt.gca().transAxes)