#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
cancer_type = cancer_type = ['lungcancer']
for item in cancer_type:
    df1 = pd.read_csv(item+'.csv')
    mirna_cancer = df1['mirId'].to_list()
    #print(mirna_cancer)
    df2 = pd.read_csv(item+'_non_associated_hsa.csv')
    mirna_nocancer = df2['mirId'].to_list()
    #print(mirna_nocancer)
    mirna_combined = mirna_cancer+ mirna_nocancer
    print(mirna_combined[0:10])
    for i in range(len(mirna_combined)):
        temp=str(mirna_combined[i])

        temp = temp.replace('-3p', '')
        temp = temp.replace('-5p', '')
        temp = temp.replace('-??', '')

        temp = temp.lower()
        x = temp.find('mir')
        if x>0:
            #print(temp[x+3])
            if(temp[x+3] != '-'):
                temp2=temp[:x+3] + '-' + temp[x+4:]
                temp = temp2
        x = temp.find('let')
        if x>0:
            #print(temp[x+3])
            if(temp[x+3] != '-'):
                temp2=temp[:x+3] + '-' + temp[x+4:]
                temp = temp2

        mirna_combined[i] = temp

    #print(mirna_combined)


    # In[ ]:


    miRDB = open('miRDB_v6.0_prediction_result_hsa.txt')
    mirna_list = []
    target_list = []
    miRDB_pd = []
    miRDB_dict = {}
    counter = 0
    num_sample = 0
    for line in miRDB:

        temp = line.split('\t')
        if float(temp[2]) > 0:
        #print(temp[2])
            temp_base = temp[0].lower()
            if temp[1] not in target_list and float(temp[2]) > 90 and num_sample < 1000:
                target_list.append(temp[1])
            if temp[0] not in mirna_list:
                if miRDB_dict:
                    miRDB_pd.append(miRDB_dict)
                    miRDB_dict = {}
                    num_sample = 0
                mirna_list.append(temp[0])
                miRDB_dict['mirId'] = temp_base
            temp2={}

            if float(temp[2]) > 99 and num_sample < 1000:
                temp2[temp[1]]='1'
                miRDB_dict.update(temp2)
                num_sample = num_sample+1
        counter = counter + 1

        if counter % 100000 == 0:
            print (counter)
    if miRDB_dict:
        miRDB_pd.append(miRDB_dict)
    pd_mirDB = pd.DataFrame(miRDB_pd)
    pd_mirDB.fillna('0', inplace=True)
    pd_mirDB.to_csv(item+'_miRDB_v6.0_prediction_result_hsa.csv')
    print(item)
    miRDB.close()
    #print('done')
    #print(mirna_list)
    #print(target_list)


    # In[ ]:


    #print(len(mirna_list), len(target_list))


# In[ ]:




