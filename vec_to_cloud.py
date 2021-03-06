'''
vec_to_cloud.py
Created by Diya Das on 28 Jul 2016

This script contains functions for generating word clouds.
'''

from wordcloud import WordCloud
import numpy as np
import pickle 
import cluster_tree
import matplotlib.pyplot as plt
import os
from functools import reduce
from fractions import gcd
from cluster_tree import TreeNode

def vec2cloud(pkltf = 'Tfidf_Matrix.pkl',clabpkl = "c_labels.pkl", docpkl = "docs_in_cluster.pkl", treepkl = "ward_tree.pkl", labpkl='features_rev.pkl',prefix='' ):
    word_array = vec2words(pkltf, labpkl, clabpkl, docpkl, treepkl)
#    word_array = word_array[0:20] #for testing
    for i in range(len(word_array)):
        wc = WordCloud(background_color='black', width = 800, height = 400)
        wc = wc.generate(word_array[i])
        wc.to_file(prefix+'cloud'+str(i)+'.png')
        del wc

def vec2words(pkltf,labpkl,clabpkl, docpkl, treepkl):
    tree= pickle.load(open(treepkl,"rb"))
    labs = pickle.load(open(labpkl,'rb'))
    tf = np.empty((len(tree.iter_nodes()),len(labs)))
    clabels = pickle.load(open(clabpkl,'rb'))
    tf_idf = pickle.load(open(pkltf,'rb')).toarray()
    counter = 0;
    clustermeans,docsincluster = cluster_tree.get_means(clabels,tf_idf[:len(clabels),:])
    for node in tree.iter_nodes():
        tf[counter,:],ndocs = cluster_tree.get_branch_mean(node, clustermeans, docsincluster)
        counter += 1
    freqInt = np.array(tf*1e5 , dtype='int')
    freqInt = np.apply_along_axis(lambda counts: counts/reduce(gcd,counts.tolist()) if reduce(gcd,counts.tolist()) else counts,1,freqInt).astype('int')
    word_array = np.apply_along_axis(lambda counts: ' '.join(item for sublist in 
                                                          ([lab]*count for lab,count in zip(labs,counts)) 
                                                          for item in sublist),1,freqInt)
    return word_array
