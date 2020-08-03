# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:08:00 2019

@author: David
"""

#import collections

import numpy as np
import pandas as pd
from sklearn import metrics
#from sklearn.preprocessing import label_binarize


#def get_y_true(task_name):
def get_y_true(true_data_file):
    """ 
    Read file to obtain y_true.
    
    """
    
    df = pd.read_csv(true_data_file,sep='\t')
    y_true = []
    for i in range(len(df)):
        label = df['sentiment'][i]
        assert label in [1, 2, 0], "error!"
        if label == 0:
            n = 0
        elif label == 1:
            n = 1
        else:
            n = 2
        y_true.append(n)
    return y_true
        
true_data_file = "data/test_data.tsv"
pred_data_file = "y_pred.txt"

#print(len(get_y_true(true_data_file)))

def get_y_pred(pred_data_file):
    """ 
    Read file to obtain y_pred.
    
    """
    
    pred=[]
    
    nameHandle = open(pred_data_file, 'r')
    for line in nameHandle:
        pred.append(int(line[:-1]))
    nameHandle.close()
    
    return pred


def sentitel_strict_acc(y_true, y_pred):
    """
    Calculate "strict Acc" of aspect detection task of Sentitel.
    """
    total_cases=int(len(y_true))
    true_cases=0
    for i in range(total_cases):
        if y_true[i]!=y_pred[i]:continue
        true_cases+=1
    aspect_strict_Acc = true_cases/total_cases

    return aspect_strict_Acc


def sentitel_macro_F1(y_true, y_pred):
    """
    Calculate "Macro-F1" of aspect detection task of Sentitel.
    """
    p_all=0
    r_all=0
    count=0
    for i in range(len(y_pred)):
        a=set()
        b=set()
        if y_pred[i]!=1:
            a.add(i)
        if y_true[i]!=1:
            b.add(i)
                
        if len(b)==0:continue
        a_b=a.intersection(b)
        if len(a_b)>0:
            p=len(a_b)/len(a)
            r=len(a_b)/len(b)
        else:
            p=0
            r=0
        count+=1
        p_all+=p
        r_all+=r
    Ma_p=p_all/count
    Ma_r=r_all/count
    aspect_Macro_F1 = 2*Ma_p*Ma_r/(Ma_p+Ma_r)

    return aspect_Macro_F1



def sentitel_Acc(sentiment_y_true, sentiment_y_pred):
    # sentiment Acc
    sentiment_y_true = np.array(sentiment_y_true)
    sentiment_y_pred = np.array(sentiment_y_pred)
    sentiment_Acc = metrics.accuracy_score(sentiment_y_true,sentiment_y_pred)

    return  sentiment_Acc


#print(get_y_pred())
    
y_true = get_y_true(true_data_file)
y_pred = get_y_pred(pred_data_file)


print("\n\naspect_strict_Acc:\t",sentitel_strict_acc(y_true, y_pred))    
print("\n\nsentiment_Acc:\t",sentitel_Acc(y_true, y_pred))
print("\n\naspect_Macro_F1:\t",sentitel_macro_F1(y_true, y_pred))


nameHandle = open('results.txt', 'w')

nameHandle.write('\naspect_strict_Acc:\t'+ str(sentitel_strict_acc(y_true, y_pred)))
nameHandle.write('\nsentiment_Acc:\t' + str(sentitel_Acc(y_true, y_pred)))
nameHandle.write('\naspect_Macro_F1:\t' + str(sentitel_macro_F1(y_true, y_pred)))

nameHandle.close()