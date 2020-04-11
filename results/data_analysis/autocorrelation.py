import numpy as np
import pandas as pd
import os
import matplotlib.cm as cm
from matplotlib import pyplot as plt
from scipy import stats as st
import seaborn as sns

#from IPython.core.pylabtools import figsize

import numpy.random as r
from pylab import *
from matplotlib.gridspec import GridSpec

import sys
sys.path.insert(0, '.')
sys.path.insert(0, '../../utils/')
import splicing_utils as spu
from splicing_utils import *
import single_cell_plots as scp
from single_cell_plots import *

plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.facecolor"] = 'white'

import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

mpl.rcParams["mathtext.fontset"] = "stix"
mpl.rcParams['pdf.fonttype'] = 42

data_dir = '/mnt/c/Users/ferna/Desktop/SingleCell/data/'

# PSI tables
chen_PSI = pd.read_csv(data_dir + 'chen/processed_tables/chen.skipped_exons_psi.tab', sep='\t', index_col=0)
#song_PSI = pd.read_csv(data_dir + 'song/processed_tables/song.skipped_exons_psi.tab', sep='\t',  index_col=0)
#das_PSI = pd.read_csv(data_dir + 'das/processed_tables/das.skipped_exons_psi.tab', sep='\t',  index_col=0)
#trapnell_PSI = pd.read_csv(data_dir + 'trapnell/processed_tables/trapnell.skipped_exons_psi.tab', 
#                    sep='\t',  index_col=0)
#lescroart_PSI = pd.read_csv(data_dir + 'lescroart/processed_tables/lescroart.skipped_exons_psi.tab', 
#                    sep='\t',  index_col=0)
#shalek_PSI = pd.read_csv(data_dir + 'shalek/processed_tables/shalek.skipped_exons_psi.tab', sep='\t', index_col=0)

# SJ read tables
chen_read_counts = pd.read_csv(data_dir + 'chen/processed_tables/chen.skipped_exons_SJreads.tab', sep='\t', index_col=0)
#song_read_counts = pd.read_csv(data_dir + 'song/processed_tables/song.skipped_exons_SJreads.tab', sep='\t', index_col=0)
# das_read_counts = pd.read_csv(data_dir + 'das/processed_tables/das.skipped_exons_SJreads.tab', sep='\t',  index_col=0)
#trapnell_read_counts = pd.read_csv(data_dir + 'trapnell/processed_tables/trapnell.skipped_exons_SJreads.tab', 
#                            sep='\t', index_col=0)
#lescroart_read_counts = pd.read_csv(data_dir + 'lescroart/processed_tables/lescroart.skipped_exons_SJreads.tab', 
#                             sep='\t', index_col=0)
# shalek_read_counts = pd.read_csv(data_dir + 'shalek/processed_tables/shalek.skipped_exons_SJreads.tab', 
#                           sep='\t', index_col=0)

# TPM tables
# chen_tpm_tab = pd.read_csv(data_dir + 'chen/chen.tpm.gene_symbols.tab', sep='\t', index_col=0)
# song_tpm_tab = pd.read_csv(data_dir + 'song/song.tpm.gene_symbols.tab', sep='\t', index_col=0)
# trapnell_tpm_tab = pd.read_csv(data_dir + 'trapnell/trapnell.tpm.gene_symbols.tab', sep='\t', index_col=0)
# lescroart_tpm_tab = pd.read_csv(data_dir + 'lescroart/lescroart.tpm.gene_symbols.tab', sep='\t', index_col=0)
# shalek_tpm_tab = pd.read_csv(data_dir + 'shalek/shalek.tpm.gene_symbols.tab', sep='\t', index_col=0)
# das_tpm_tab = pd.read_csv(data_dir + 'das/das.tpm.gene_symbols.tab', sep='\t', index_col=0)



chen_counts_tab = pd.read_csv(data_dir + 'chen/processed_tables/chen.rsemCounts.gene_symbols.tab', 
                       sep='\t', index_col=0)
#song_counts_tab = pd.read_csv(data_dir + 'song/processed_tables/song.rsemCounts.gene_symbols.tab', 
#                       sep='\t', index_col=0)
# das_counts_tab = pd.read_csv(data_dir + 'das/processed_tables/das.rsemCounts.gene_symbols.tab', 
#                       sep='\t', index_col=0)
#trapnell_counts_tab = pd.read_csv(data_dir + 'trapnell/processed_tables/trapnell.rsemCounts.gene_symbols.tab', 
#                           sep='\t', index_col=0)
#lescroart_counts_tab = pd.read_csv(data_dir + 'lescroart/processed_tables/lescroart.rsemCounts.gene_symbols.tab', 
#                            sep='\t', index_col=0)
# shalek_counts_tab = pd.read_csv(data_dir + 'shalek/processed_tables/shalek.rsemCounts.gene_symbols.tab', 
#                          sep='\t', index_col=0)

# mRNA tables
chen_mrna_counts = pd.read_csv(data_dir + 'chen/processed_tables/chen.mrna_counts.tab', sep='\t', index_col=0)
#song_mrna_counts = pd.read_csv(data_dir + 'song/processed_tables/song.mrna_counts.tab', sep='\t', index_col=0)
# das_mrna_counts = pd.read_csv(data_dir + 'das/processed_tables/das.mrna_counts.tab', sep='\t', index_col=0)
#trapnell_mrna_counts = pd.read_csv(data_dir + 'trapnell/processed_tables/trapnell.mrna_counts.tab', 
#                            sep='\t', index_col=0)
#lescroart_mrna_counts = pd.read_csv(data_dir + 'lescroart/processed_tables/lescroart.mrna_counts.tab', 
#                             sep='\t', index_col=0)
# shalek_mrna_counts = pd.read_csv(data_dir + 'shalek/processed_tables/shalek.mrna_counts.tab', 
#                           sep='\t', index_col=0)

# mRNA per event rables
mrna_per_event_chen = pd.read_csv(data_dir + 'chen/processed_tables/chen.mrna_counts_per_event.tab', sep='\t', index_col=0)
#mrna_per_event_song = pd.read_csv(data_dir + 'song/processed_tables/song.mrna_counts_per_event.tab', sep='\t', index_col=0)
# mrna_per_event_das = pd.read_csv(data_dir + 'das/processed_tables/das.mrna_counts_per_event.tab', sep='\t', index_col=0)
#mrna_per_event_trapnell = pd.read_csv(data_dir + 'trapnell/processed_tables/trapnell.mrna_counts_per_event.tab', 
#                           sep='\t', index_col=0)
#mrna_per_event_lescroart = pd.read_csv(data_dir + 'lescroart/processed_tables/lescroart.mrna_counts_per_event.tab', 
#                           sep='\t', index_col=0)
# mrna_per_event_shalek = pd.read_csv(data_dir + 'shalek/processed_tables/shalek.mrna_counts_per_event.tab', 
#                           sep='\t', index_col=0)

# read coverage tables
chen_coverage_tab = pd.read_csv(data_dir + 'chen/processed_tables/chen.read_coverage.tab', 
                          sep='\t', index_col=0)
#song_coverage_tab = pd.read_csv(data_dir + 'song/processed_tables/song.read_coverage.tab', 
#                          sep='\t', index_col=0)
#trapnell_coverage_tab = pd.read_csv(data_dir + 'trapnell/processed_tables/trapnell.read_coverage.tab', 
#                          sep='\t', index_col=0)
#lescroart_coverage_tab = pd.read_csv(data_dir + 'lescroart/processed_tables/lescroart.read_coverage.tab', 
#                          sep='\t', index_col=0)
# das_coverage_tab = pd.read_csv(data_dir + 'das/processed_tables/das.read_coverage.tab', 
#                           sep='\t', index_col=0)
# shalek_coverage_tab = pd.read_csv(data_dir + 'shalek/processed_tables/shalek.read_coverage.tab', 
#                           sep='\t', index_col=0)


chen_pca = pd.read_csv(data_dir + 'chen/chen.pca.tab', sep='\t', index_col=0)
chen_pca = chen_pca.sort_values('pseudotime')
chen_pca.PC2 = chen_pca.PC2
chen_pca.line_2 = chen_pca.line_2
chen_index = [x for x in chen_pca.sort_values('pseudotime').index if x in mrna_per_event_chen.columns]

chen_pca = chen_pca.loc[chen_index]
chen_PSI = chen_PSI[chen_index]
mrna_per_event_chen = mrna_per_event_chen[chen_index]
chen_read_counts = chen_read_counts[chen_index]
chen_coverage_tab = chen_coverage_tab.loc[chen_index]

chen_ES2i = chen_pca.loc[chen_pca.cell_type == 'ES2i'].index
chen_ES = chen_pca.loc[chen_pca.cell_type == 'ES'].index
chen_Epi = chen_pca.loc[chen_pca.cell_type == 'Epi'].index
chen_MN = chen_pca.loc[chen_pca.cell_type == 'Motor neuron'].index

###

#song_pca = pd.read_csv(data_dir + 'song/song.pca_top_fano.tab', sep='\t', index_col=0)
#song_pca = song_pca.sort_values('pseudotime')
#song_pca.PC2 = -song_pca.PC2
#song_index = [x for x in song_pca.sort_values('pseudotime').index if x in mrna_per_event_song.columns]

#song_pca = song_pca.loc[song_index]
#song_PSI = song_PSI[song_index]
#mrna_per_event_song = mrna_per_event_song[song_index]
#song_read_counts = song_read_counts[song_index]
#song_coverage_tab = song_coverage_tab.loc[song_index]

#song_iPSC = song_pca.loc[song_pca.cell_type == 'iPSC'].index
#song_NPC = song_pca.loc[song_pca.cell_type == 'NPC'].index
#song_MN = song_pca.loc[song_pca.cell_type == 'MN'].index

###

#trapnell_pca = pd.read_csv(data_dir + 'trapnell/trapnell.pca.tab', sep='\t', index_col=0)
#trapnell_pca = trapnell_pca.sort_values('pseudotime')
#trapnell_pca.PC2 = -trapnell_pca.PC2
#trapnell_pca.line_2 = -trapnell_pca.line_2
#trapnell_index = [x for x in trapnell_pca.sort_values('pseudotime').index if x in mrna_per_event_trapnell.columns]

#trapnell_pca = trapnell_pca.loc[trapnell_index]
#trapnell_PSI = trapnell_PSI[trapnell_index]
#mrna_per_event_trapnell = mrna_per_event_trapnell[trapnell_index]
#trapnell_read_counts = trapnell_read_counts[trapnell_index]
#trapnell_coverage_tab = trapnell_coverage_tab.loc[trapnell_index]

#trapnell_M00 = trapnell_pca.loc[trapnell_pca.cell_type==0].index
#trapnell_M24 = trapnell_pca.loc[trapnell_pca.cell_type==24].index
#trapnell_M48 = trapnell_pca.loc[trapnell_pca.cell_type==48].index
#trapnell_M72 = trapnell_pca.loc[trapnell_pca.cell_type==72].index


###
        
#lescroart_pca = pd.read_csv(data_dir + 'lescroart/lescroart.pca_meta.tab', sep='\t', index_col = 0)
#lescroart_index = [x for x in lescroart_pca.index if x in mrna_per_event_lescroart.columns]

#lescroart_pca = lescroart_pca.loc[lescroart_index]
#lescroart_PSI = lescroart_PSI[lescroart_index]
#mrna_per_event_lescroart = mrna_per_event_lescroart[lescroart_index]
#lescroart_read_counts = lescroart_read_counts[lescroart_index]
#lescroart_coverage_tab = lescroart_coverage_tab.loc[lescroart_index]

#lescroart_E6 = lescroart_pca.loc[lescroart_pca.cell_type=='E6.75'].index
#lescroart_E7 = lescroart_pca.loc[lescroart_pca.cell_type=='E7.25'].index

def process_subpop(subpop, psi, mrna, mrna_per_event, reads, cj, psi_min = 0.2, mrna_min=10, reads_min = 0, cell_min = 0.5, nbins=11,
                  filter_cj = True):

    int_genes, int_exons = spu.get_int_events(psi[subpop], mrna[subpop], psi_min)
    #print(len(int_genes))
    int_exons = [x for x in int_exons if x in mrna_per_event.index]
    PSI_filtered, PSI_mrna_filtered, good_exons, mrna_filtered, reads_filtered = filter_psi(psi[subpop], int_exons, 
                                                                     mrna_per_event[subpop], cj.loc[subpop], 
                                                                     reads[subpop], mrna_min, reads_min = reads_min,
                                                                                            cell_min=cell_min, filter_cj=filter_cj)


    good_cells = PSI_filtered.dropna(axis=1, how='all').columns
    good_subpop = [x for x in subpop if x in good_cells]
    PSI_good = PSI_filtered[good_cells]

    hist_complete, hist_intermediate = scp.get_bins_table2(PSI_filtered[good_subpop], mrna_filtered[good_subpop], nbins)
    hist_complete_exp, hist_intermediate_exp = scp.get_bins_table(PSI_filtered[good_subpop], mrna_filtered[good_subpop])

    
    return PSI_filtered, good_exons, mrna_filtered, reads_filtered, hist_complete, hist_complete_exp
    


##############################

###################
# Chen
ac = AgglomerativeClustering(n_clusters=5)
ac_clusters = ac.fit_predict(chen_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(chen_pca.PC1, chen_pca.PC2, c=ac_clusters)
# plt.show()

chen_pca_clust = chen_pca.copy()
chen_pca_clust['AC'] = ac_clusters

chen_clust_filter = []
for cluster in chen_pca_clust.groupby('AC')['pseudotime'].mean().sort_values().index:
    clust_subpop = chen_pca_clust.index[chen_pca_clust.AC == cluster]
    
    chen_filter = process_subpop(clust_subpop, chen_PSI, chen_mrna_counts, mrna_per_event_chen, 
                                 chen_read_counts, chen_coverage_tab['SJ_coverage'], 0.1, 10, 0, cell_min=0.5)
    
    chen_clust_filter.append(chen_filter)
    
###################
# Song
#ac = AgglomerativeClustering(n_clusters=3)
#ac_clusters = ac.fit_predict(song_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(song_pca.PC1, song_pca.PC2, c=ac_clusters)
# plt.show()

#song_pca_clust = song_pca.copy()
#song_pca_clust['AC'] = ac_clusters

#song_clust_filter = []
#for cluster in song_pca_clust.groupby('AC')['pseudotime'].mean().sort_values().index:
#    clust_subpop = song_pca_clust.index[song_pca_clust.AC == cluster]
#    
#    song_filter = process_subpop(clust_subpop, song_PSI, song_mrna_counts, mrna_per_event_song, 
#                                 song_read_counts, song_coverage_tab['SJ_coverage'], 0.1, 10, 0, cell_min=0.5)
#    
#    song_clust_filter.append(song_filter)
    
    
###################
# Lescroart
#ac = AgglomerativeClustering(n_clusters=3)
#ac_clusters = ac.fit_predict(lescroart_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(lescroart_pca.PC1, lescroart_pca.PC2, c=ac_clusters)
# plt.show()

#lescroart_pca_clust = lescroart_pca.copy()
#lescroart_pca_clust['AC'] = ac_clusters


#lescroart_clust_filter = []
#for cluster in lescroart_pca_clust.cell_type.unique():
#    clust_subpop = lescroart_pca_clust.index[lescroart_pca_clust.cell_type == cluster]
    
#    lescroart_filter = process_subpop(clust_subpop, lescroart_PSI, lescroart_mrna_counts, mrna_per_event_lescroart, 
#                                 lescroart_read_counts, lescroart_coverage_tab['SJ_coverage'], 0.1, 10, 0, cell_min=0.5)
    
#    lescroart_clust_filter.append(lescroart_filter)
    
    
###################
# Trapnell
#ac = AgglomerativeClustering(n_clusters=4)
#ac_clusters = ac.fit_predict(trapnell_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(trapnell_pca.PC1, trapnell_pca.PC2, c=ac_clusters)
# plt.show()

#trapnell_pca_clust = trapnell_pca.copy()
#trapnell_pca_clust['AC'] = ac_clusters

#trapnell_clust_filter = []
#for cluster in trapnell_pca_clust.groupby('AC')['pseudotime'].mean().sort_values().index:
#    clust_subpop = trapnell_pca_clust.index[trapnell_pca_clust.AC == cluster]
#    
#    trapnell_filter = process_subpop(clust_subpop, trapnell_PSI, trapnell_mrna_counts, mrna_per_event_trapnell, 
#                                 trapnell_read_counts, trapnell_coverage_tab['SJ_coverage'], 0.1, 10, 0, cell_min=0.5)
    
#    trapnell_clust_filter.append(trapnell_filter)

#####

from sklearn.decomposition import PCA
from scipy.stats import spearmanr
import rpy2
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects
import rpy2.robjects.numpy2ri as rpyn
from statsmodels.stats.multitest import multipletests
dt = rpy2.robjects.packages.importr('diptest')

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

from scipy.special import logit
from scipy.special import expit

from sklearn.metrics import adjusted_rand_score

from scipy.stats import chisquare
from scipy.stats import hypergeom
from scipy.stats import f_oneway
from scipy.stats import kruskal

from scipy.stats import combine_pvalues
from scipy.stats import probplot


###############

# For the sake of quantification, filter exons between 0.05 and 0.95

###################
# Chen
ac = AgglomerativeClustering(n_clusters=5)
ac_clusters = ac.fit_predict(chen_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(chen_pca.PC1, chen_pca.PC2, c=ac_clusters)
# plt.show()

chen_pca_clust = chen_pca.copy()
chen_pca_clust['AC'] = ac_clusters

chen_clust_filter_05 = []
for cluster in chen_pca_clust.groupby('AC')['pseudotime'].mean().sort_values().index:
    clust_subpop = chen_pca_clust.index[chen_pca_clust.AC == cluster]
    
    chen_filter = process_subpop(clust_subpop, chen_PSI, chen_mrna_counts, mrna_per_event_chen, 
                                 chen_read_counts, chen_coverage_tab['SJ_coverage'], 0.05, 10, 0, cell_min=0.5)
    
    chen_clust_filter_05.append(chen_filter)
    
###################
# Song
nothing = '''ac = AgglomerativeClustering(n_clusters=3)
ac_clusters = ac.fit_predict(song_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(song_pca.PC1, song_pca.PC2, c=ac_clusters)
# plt.show()

song_pca_clust = song_pca.copy()
song_pca_clust['AC'] = ac_clusters

song_clust_filter_05 = []
for cluster in song_pca_clust.groupby('AC')['pseudotime'].mean().sort_values().index:
    clust_subpop = song_pca_clust.index[song_pca_clust.AC == cluster]
    
    song_filter = process_subpop(clust_subpop, song_PSI, song_mrna_counts, mrna_per_event_song, 
                                 song_read_counts, song_coverage_tab['SJ_coverage'], 0.05, 10, 0, cell_min=0.5)
    
    song_clust_filter_05.append(song_filter)
    
    
###################
# Lescroart
ac = AgglomerativeClustering(n_clusters=3)
ac_clusters = ac.fit_predict(lescroart_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(lescroart_pca.PC1, lescroart_pca.PC2, c=ac_clusters)
# plt.show()

lescroart_clust_filter_05 = []
for cluster in lescroart_pca_clust.cell_type.unique():
    clust_subpop = lescroart_pca_clust.index[lescroart_pca_clust.cell_type == cluster]
    
    lescroart_filter = process_subpop(clust_subpop, lescroart_PSI, lescroart_mrna_counts, mrna_per_event_lescroart, 
                                 lescroart_read_counts, lescroart_coverage_tab['SJ_coverage'], 0.05, 10, 0, cell_min=0.5)
    
    lescroart_clust_filter_05.append(lescroart_filter)
    
    
    
###################
# Trapnell
ac = AgglomerativeClustering(n_clusters=4)
ac_clusters = ac.fit_predict(trapnell_pca[['PC1', 'PC2']])

# figsize(6,4)
# plt.scatter(trapnell_pca.PC1, trapnell_pca.PC2, c=ac_clusters)
# plt.show()

trapnell_pca_clust = trapnell_pca.copy()
trapnell_pca_clust['AC'] = ac_clusters

trapnell_clust_filter_05 = []
for cluster in trapnell_pca_clust.groupby('AC')['pseudotime'].mean().sort_values().index:
    clust_subpop = trapnell_pca_clust.index[trapnell_pca_clust.AC == cluster]
    
    trapnell_filter = process_subpop(clust_subpop, trapnell_PSI, trapnell_mrna_counts, mrna_per_event_trapnell, 
                                 trapnell_read_counts, trapnell_coverage_tab['SJ_coverage'], 0.05, 10, 0, cell_min=0.5)
    
    trapnell_clust_filter_05.append(trapnell_filter)

    

    
    
# das_sra = pd.read_csv(data_dir + 'das/SraRunTable.txt', sep='\t', index_col = 6)
# das_sra = das_sra.loc[das_PSI.columns]
# das_clust_filter_05 = []
# for cluster in sorted(das_sra.age.unique()):
#     clust_subpop = das_sra.index[das_sra.age == cluster]
    
#     das_filter = process_subpop(clust_subpop, das_PSI, das_mrna_counts, mrna_per_event_das, 
#                                  das_read_counts, das_coverage_tab['SJ_coverage'], 0.1, 10, 0, cell_min=0.5)
    
#     das_clust_filter_05.append(das_filter)#!/usr/bin/env python
# coding: utf-8

# In[4]:
'''

data_dir = '/mnt/c/Users/ferna/Desktop/SingleCell/data/'

#get_ipython().run_line_magic('run', "-i '../../utils/load_data_short.py'")



import sys
sys.path.insert(0, '../../utils/')
#import load_data_short
import importlib
import sys
#sys.path.insert(0, '.')
import splicing_utils as spu
from splicing_utils import *
import single_cell_plots as scp
from single_cell_plots import *
# importlib.reload(scp)
# importlib.reload(spu)
# sns.reset_orig()
from scipy.stats import chisquare
from scipy.stats import combine_pvalues
#get_ipython().run_line_magic('run', "-i '../../utils/test_functions.py'")
#from test_functions import *
import matplotlib as mpl
mpl.rcParams["mathtext.fontset"] = "stix"
mpl.rcParams['pdf.fonttype'] = 42

from tqdm import tqdm


# In[5]:


from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import pdist
from sklearn.metrics.pairwise import euclidean_distances

# def get_signature_score(PSI_tab, exon):
#     exon_score = (PSI_tab.loc[exon] - PSI_tab.mean())/(PSI_tab.std())
#     return exon_score.dropna()

def get_auto_correlation(exon_score, pca):
    N = len(exon_score)
    weights = euclidean_distances(pca.loc[exon_score.index][['PC1', 'PC2']])
    W = weights.sum().sum()
    
def get_signature_score(PSI_tab, exon):
    exon_score = (PSI_tab.loc[exon] - PSI_tab.mean())/(PSI_tab.std())
    return exon_score.dropna()


def get_distance_matrix(pca, k=10):
    nbrs = NearestNeighbors(n_neighbors=k).fit(pca[['PC1', 'PC2']])
    distances, indices = nbrs.kneighbors(pca[['PC1', 'PC2']])
    
    cells = list(pca.index)
    
    W = pd.DataFrame(np.zeros((len(cells), len(cells))))
    W.columns = cells
    W.index = cells
    
    for i in tqdm(range(len(cells))):
        cell_i = cells[i]
        sigma = np.max(distances[i])
        for j in range(len(distances[i])):
            
            cell_j = cells[indices[i][j]]
            
            d = distances[i][j]
            w = np.exp(-(d**2)/(sigma**2))
#             w = np.exp(-(d**2)/(sigma))
            
            W.loc[cell_i, cell_j] = w
    
    
    
    return W
    
# def get_C(PSI_tab, W, exon):
#     obs_cells = PSI_tab.loc[exon].dropna().index
#     x = (PSI_tab.loc[exon, obs_cells].values.reshape(-1, 1) - PSI_tab.loc[exon, obs_cells].values.reshape(1, -1))
#     w = W.loc[obs_cells, obs_cells]
#     num = (len(obs_cells)-1)*((w*(x**2)).sum().sum())
#     den = (2*w.sum().sum())*np.sum((PSI_tab.loc[exon, obs_cells] - PSI_tab.loc[exon, obs_cells].mean())**2)
#     C = num/den
#     score = 1 - C
#     return score

def get_C(PSI_tab, W, exon):
    
    exon_score = get_signature_score(PSI_tab, exon)
    
    
    obs_cells = exon_score.dropna().index
    x = (exon_score.values.reshape(-1, 1) - exon_score.values.reshape(1, -1))
    w = W.loc[obs_cells, obs_cells]
    num = (len(obs_cells)-1)*((w*(x**2)).sum().sum())
    den = (2*w.sum().sum())*np.sum((exon_score - exon_score.mean())**2)
    
    C = num/den
    score = 1 - C
    return score

def get_C_set(PSI_tab, W, exon_list):
    obs_cells = PSI_tab.loc[exon].dropna().index
    x = (PSI_tab.loc[exon, obs_cells].values.reshape(-1, 1) - PSI_tab.loc[exon, obs_cells].values.reshape(1, -1))
    w = W.loc[obs_cells, obs_cells]
    num = (len(obs_cells)-1)*((w*(x**2)).sum().sum())
    den = (2*w.sum().sum())*np.sum((PSI_tab.loc[exon, obs_cells] - PSI_tab.loc[exon, obs_cells].mean())**2)
    C = num/den
    score = 1 - C
    return score


# In[6]:


chen_int_genes, chen_int_exons = spu.get_int_events(chen_PSI, chen_mrna_counts, 0.05)
chen_int_exons = [x for x in chen_int_exons if x in mrna_per_event_chen.index]
chen_filtered_lax = filter_psi(chen_PSI, chen_int_exons, mrna_per_event_chen, chen_coverage_tab['SJ_coverage'], 
                           chen_read_counts, mrna_min=10, reads_min=0, cell_min=0.05)

chen_filtered_lax_reads = filter_psi(chen_PSI, chen_int_exons, mrna_per_event_chen, chen_coverage_tab['SJ_coverage'], 
                           chen_read_counts, mrna_min=0, reads_min=10, cell_min=0.05)

#song_int_genes, song_int_exons = spu.get_int_events(song_PSI, song_mrna_counts, 0.05)
#song_int_exons = [x for x in song_int_exons if x in mrna_per_event_song.index]
#song_filtered_lax = filter_psi(song_PSI, song_int_exons, mrna_per_event_song, song_coverage_tab['SJ_coverage'], 
#                           song_read_counts, mrna_min=10, reads_min=0, cell_min=0.05)

#song_filtered_lax_reads = filter_psi(song_PSI, song_int_exons, mrna_per_event_song, song_coverage_tab['SJ_coverage'], 
#                           song_read_counts, mrna_min=0, reads_min=10, cell_min=0.05)

#trapnell_int_genes, trapnell_int_exons = spu.get_int_events(trapnell_PSI, trapnell_mrna_counts, 0.05)
#trapnell_int_exons = [x for x in trapnell_int_exons if x in mrna_per_event_trapnell.index]
#trapnell_filtered_lax = filter_psi(trapnell_PSI, trapnell_int_exons, mrna_per_event_trapnell, trapnell_coverage_tab['SJ_coverage'], 
#                           trapnell_read_counts, mrna_min=10, reads_min=0, cell_min=0.05)

#trapnell_filtered_lax_reads = filter_psi(trapnell_PSI, trapnell_int_exons, mrna_per_event_trapnell, trapnell_coverage_tab['SJ_coverage'], 
#                           trapnell_read_counts, mrna_min=0, reads_min=10, cell_min=0.05)

#lescroart_int_genes, lescroart_int_exons = spu.get_int_events(lescroart_PSI, lescroart_mrna_counts, 0.05)
#lescroart_int_exons = [x for x in lescroart_int_exons if x in mrna_per_event_lescroart.index]
#lescroart_filtered_lax = filter_psi(lescroart_PSI, lescroart_int_exons, mrna_per_event_lescroart, lescroart_coverage_tab['SJ_coverage'], 
#                           lescroart_read_counts, mrna_min=10, reads_min=0, cell_min=0.05)
#
#lescroart_filtered_lax_reads = filter_psi(lescroart_PSI, lescroart_int_exons, mrna_per_event_lescroart, lescroart_coverage_tab['SJ_coverage'], 
#                           lescroart_read_counts, mrna_min=0, reads_min=10, cell_min=0.05)


# In[7]:


# Ws = get_distance_matrix(chen_pca_clust, 50)
# figsize(15, 15)
# sns.heatmap(Ws.loc[chen_pca_clust.pseudotime.sort_values().index, 
#                       chen_pca_clust.pseudotime.sort_values().index],cmap=cm.bone_r)
# plt.show()


# In[2]:


Ws = get_distance_matrix(chen_pca_clust, 50)
# # figsize(15, 15)
# # sns.heatmap(Ws.loc[chen_pca_clust.pseudotime.sort_values().index, 
# #                       chen_pca_clust.pseudotime.sort_values().index],cmap=cm.bone_r)
# # plt.show()


# In[ ]:


# Ws = get_distance_matrix(chen_pca_clust, 488)
# import time as t
# figsize(15, 15)
# sns.heatmap(Ws.loc[chen_pca_clust.pseudotime.sort_values().index, 
#                       chen_pca_clust.pseudotime.sort_values().index],cmap=cm.bone_r)
# plt.show()
# chen_iqr = chen_PSI.quantile(0.75, axis=1) - chen_PSI.quantile(0.25, axis=1)
chen_int_genes, chen_int_exons = spu.get_int_events(chen_PSI, chen_mrna_counts, 0.05)
# chen_int_exons = [x for x in chen_iqr.index[chen_iqr >= 0.25] if x in mrna_per_event_chen.index]
observed_exons = chen_PSI.index[chen_PSI.isna().mean(axis=1) <= 0.5]
test_exons = [x for x in observed_exons if x in chen_int_exons]

exon_list = []
C_scores = []
for exon in tqdm(test_exons):
    exon_score = get_C(chen_PSI, Ws, exon)
    if exon_score >= 0:
        C_scores.append(exon_score)
        exon_list.append(exon)
        for i in range(3):
            scramble_cells = r.choice(chen_PSI.columns, 488, replace=False)
            mock_PSI = chen_PSI[scramble_cells]
            mock_PSI.columns = chen_PSI.columns
            mock_score = get_C(mock_PSI, Ws, exon)
            if mock_score >= 0:
                C_scores.append(mock_PSI)
                exon_list.append('mock_'+exon+'_'+str(i))
    
pvals = pd.DataFrame()
pvals['C_score'] = C_scores
pvals.index = exon_list

pvals.to_csv('chen_autocorrelation_pvalues.tab', sep='\t', header=True, index=True)



# figsize(6, 5)
# selected_mrna = [x for x in chen_filtered_lax[0].index[chen_filtered_lax[0].isna().mean(axis=1) <= 0.5] if x in pvals.index]
# # for exon in pvals.index[pvals.C_score >= pvals.C_score.quantile(0.99)]:
# #     plt.scatter(chen_pca_clust.PC1, chen_pca_clust.PC2, c=chen_PSI.loc[exon], cmap=cm.viridis)
# #     plt.title(exon)
# #     plt.show()
    
# print('bad')

# # for exon in pvals.index[pvals.C_score <= pvals.C_score.quantile(0.01)]:
# #     plt.scatter(chen_pca_clust.PC1, chen_pca_clust.PC2, c=chen_PSI.loc[exon], vmin=0, vmax=1, cmap=cm.viridis)
# #     plt.title(exon)
# #     plt.show()
    
    
# # plt.hist(pvals.loc[selected_mrna, 'C_score'], alpha=0.5, density=True)
# # plt.hist(pvals.C_score, alpha=0.5, density=True)


# In[1]:


# figsize(6, 5)
# plt.scatter(chen_pca_clust.PC1, chen_pca_clust.PC2, c=chen_PSI.loc['Zfp511_2'], cmap=cm.viridis)
# plt.show()


# In[96]:


# exon='2700097O09Rik_1'
# corrected_score = get_signature_score(chen_PSI, exon)
# obs_cells = corrected_score.index
# x = (corrected_score.values.reshape(-1, 1) - corrected_score.values.reshape(1, -1))
# w = Ws.loc[obs_cells, obs_cells]
# num = (len(obs_cells)-1)*((w*(x**2)).sum().sum())
# den = (2*(w.sum().sum())*np.sum((corrected_score - corrected_score.mean())**2))
# C = num/den
# score = 1 - C

