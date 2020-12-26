# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:55:33 2020

@author: Freedom
"""
import numpy as np 
import matplotlib.pyplot as plt
import time
from sklearn.metrics import mean_squared_error
import pandas as pd

#Time of simulation
vreme_simulacije = 259200 # len of  test in min ( 6 month period )

#Load datasets from simulation
vremena_otkaza = np.load('lista_vremena_otkz_1000_BTD.npy', allow_pickle=True)
vremena_popravke = np.load('lista_vremena_pop_1000_BTD.npy', allow_pickle=True)
vrsta_otkaza = np.load('lista_vrsta_pop_1000_BTD.npy', allow_pickle=True)

#Load Real data
Real_data_fail = np.load('lista_vremena_otkz_1000_BTD.npy', allow_pickle=True)
Real_data_fail = np.load('lista_vremena_pop_1000_BTD.npy', allow_pickle=True)
Real_data_class = np.load('lista_vrsta_pop_1000_BTD.npy', allow_pickle=True)

for i in range(2):
    ls_ = []
    podatci1 = vremena_otkaza[i].reshape(-1)
    podatci2 = vremena_popravke[i].reshape(-1)
    podatci3 = vrsta_otkaza[i].reshape(-1)

    #drop if the last value is larger then len_of_simulation
    if vreme_simulacije < podatci1[-1]:
        podatci1[:-1]
    if vreme_simulacije < podatci2[-1]:
        podatci2[:-1]

    #make list vector with cosistant(same) len
    #sometimes one vector is longer than another for single value
    len_1 = len(podatci1)
    len_2 = len(podatci2)
    len_3 = len(podatci3)
    ls_.extend((len_1, len_2, len_3))
    min_len = min(ls_)
    podatci1 = podatci1[:min_len]
    podatci2 = podatci2[:min_len]
    podatci3 = podatci3[:min_len]

    def gen_lambda_and_mi(podatci1,podatci2, podatci3, seq_len, t):
        '''
        This Funcion consist of 3 parts:
        1. We generate 3 matrix with len(len_of_simulation(in minutes))
        2.a) We put 1 in moment (minut) in which the event happend 
             and 0 otherwise (for repair and failure rates)
        2.b) We put class (1,2,3) of falilure in moment (minut) in which the event happend 
             and 0 otherwise (for class of failures)
        3. We go through Matrixes with sliding_window (window size, and step) 
        '''

        #1. step: Generate matrix for each list
        matrix = np.zeros(vreme_simulacije)
        matrix1 = np.zeros(vreme_simulacije)
        matrix2 = np.zeros(vreme_simulacije)

        #2. step: Fill the each Matrix with mooments 
        #(in which minute) event happend (or what type of event happend in that moment (matrix2))
        for index, value in enumerate(podatci1):
            matrix[int(value)] = 1
            matrix2[int(value)] = podatci3[index] + 1      
        for i in podatci2:
            matrix1[int(i)] = 1 

        #3. step: Evaluate for window_size(seq_len) and step(dt)         
        lambd = []
        mi = [] 
        fail_distribution = []   
        start = 0
        end = seq_len
        one_day = (24*60) / seq_len #when multiplied with window_size(seq_len) returns values scaled to 1 day
        for i in range(int((len(matrix)-seq_len)/t)):
            #Generate fail number per window and step
            ls = matrix[start:end]
            lambd.append(sum(ls)*one_day) #Number of Failures per 1 day for current window and step
            #Generate repair number per window and step
            ls1 = matrix1[start:end]
            mi.append(sum(ls1)*one_day) #Number of Repairs per 1 day for current window and step
            #Generate fail_distribution per window and step
            types_of_fail_ = []
            types_of_fail_.extend(matrix2[start:end])
            Mechanical_fail = types_of_fail_.count(1)
            Electro_fail = types_of_fail_.count(2) 
            Other_fail = types_of_fail_.count(3) 
            total_fail = Mechanical_fail + Electro_fail + Other_fail
            ls_ = [Mechanical_fail/total_fail, Electro_fail/total_fail, Other_fail/total_fail]
            fail_distribution.append(ls_) 
             
            start += t #update for step(dt)
            end += t #update for step(dt)
        return lambd, mi, fail_distribution
            
    seq_leng = [7*24*60, 15*24*60, 30*24*60] #windows of 7, 15 and 30 days
    dt = [8*60] #step of 60 minutes
    Results = []
    for seq_len in seq_leng:
        for t in dt:
            lamb, mi, fail_distribution =  gen_lambda_and_mi(podatci1,podatci2,podatci3, int(seq_len), t)
            mi_gen = np.array(mi).reshape(-1, 1)
            lamb_gen = np.array(lamb).reshape(-1, 1)
            fail_distribution = np.array(fail_distribution).reshape(-1, 3)

            #Optinal: Save into lists
            np.save('fail_window{}_dt{}_sim{}.npy'.format(seq_len/(24*60), t, i), lamb_gen)
            np.save('repair_window{}_dt{}_sim{}.npy'.format(seq_len/(24*60), t, i), lamb_gen)
            np.save('class_window{}_dt{}_sim{}.npy'.format(seq_len/(24*60), t, i), lamb_gen)

            lis_ = []
            #MSE/Evaluation of real vs predicted failure rate
            len_tst_st = int(len(Real_data_fail)*0.8)
            Test_data_fail = Real_data_fail[len_tst_st:len_tst_st + len(lamb_gen)].reshape(-1,1)
            MSE_sim_f = mean_squared_error(Test_data_fail, Sim_data)
            #MSE/Evaluation of real vs predicted repair rate
            len_tst_st = int(len(Real_data_fail)*0.8)
            Test_data_repair = Real_data_fail[len_tst_st:len_tst_st + len(mi_gen)].reshape(-1,1)
            MSE_sim_r = mean_squared_error(Test_data_repair, Sim_data)
            #KL_divergance/Evaluation KL_divergance for probability distribution
            len_tst_st = int(len(Real_data_class)*0.8)
            Test_data_class = Real_data_class[len_tst_st:len_tst_st + len(fail_distribution)]
            res =[] 
            for i in  range(len(p)):
                kl_ = kl_div(p[i], q[i])
                res.append(sum(kl_))
            KL_div = np.mean(res)
            #Append results in order 1. Failure_rate 2. Repair_rate 3. Class
            Results.extend(MSE_sim_f, MSE_sim_r, KL_div)


# sim_name_lam = 'Failure_rates_' + str(t) + 'dt_' + str(seq_len) + 'min_simulacija' + '.npy'
# sim_name_mi = 'Repair_rates' + str(t) + 'dt' + str(seq_len) + 'min_simulacija' + '.npy'
# np.save(sim_name_lam, lamb_gen_simulacija)
# np.save(sim_name_mi +str(t), mi_gen_simulacija)
    