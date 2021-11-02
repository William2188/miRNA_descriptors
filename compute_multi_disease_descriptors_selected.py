#!/usr/bin/env python
import pandas as pd
import os
cancer_type = ['lungcancer']
        


# In[12]:


#miRNA_sequence = 'ACUGUACGUACUACGUCCC'
listofmotifs = [
"AC",
"AU",
"AG",
"CA",
"CU",
"CG",
"UA",
"UC",
"UG",
"GA",
"GC",
"GU",
"AAC",
"AAU",
"AAG",
"ACA",
"ACC",
"ACU",
"ACG",
"AUA",
"AUC",
"AUU",
"AUG",
"AGA",
"AGC",
"AGU",
"AGG",
"CAA",
"CAC",
"CAU",
"CAG",
"CCA",
"CCU",
"CCG",
"CUA",
"CUC",
"CUU",
"CUG",
"CGA",
"CGC",
"CGU",
"CGG",
"UAA",
"UAC",
"UAU",
"UAG",
"UCA",
"UCC",
"UCU",
"UCG",
"UUA",
"UUC",
"UUG",
"UGA",
"UGC",
"UGU",
"UGG",
"GAA",
"GAC",
"GAU",
"GAG",
"GCA",
"GCC",
"GCU",
"GCG",
"GUA",
"GUC",
"GUU",
"GUG",
"GGA",
"GGC",
"GGU",
"AAAC",
"AAAU",
"AAAG",
"AACA",
"AACC",
"AACU",
"AACG",
"AAUA",
"AAUC",
"AAUU",
"AAUG",
"AAGA",
"AAGC",
"AAGU",
"AAGG",
"ACAA",
"ACAC",
"ACAU",
"ACAG",
"ACCA",
"ACCC",
"ACCU",
"ACCG",
"ACUA",
"ACUC",
"ACUU",
"ACUG",
"ACGA",
"ACGC",
"ACGU",
"ACGG",
"AUAA",
"AUAC",
"AUAU",
"AUAG",
"AUCA",
"AUCC",
"AUCU",
"AUCG",
"AUUA",
"AUUC",
"AUUU",
"AUUG",
"AUGA",
"AUGC",
"AUGU",
"AUGG",
"AGAA",
"AGAC",
"AGAU",
"AGAG",
"AGCA",
"AGCC",
"AGCU",
"AGCG",
"AGUA",
"AGUC",
"AGUU",
"AGUG",
"AGGA",
"AGGC",
"AGGU",
"AGGG",
"CAAA",
"CAAC",
"CAAU",
"CAAG",
"CACA",
"CACC",
"CACU",
"CACG",
"CAUA",
"CAUC",
"CAUU",
"CAUG",
"CAGA",
"CAGC",
"CAGU",
"CAGG",
"CCAA",
"CCAC",
"CCAU",
"CCAG",
"CCCA",
"CCCU",
"CCCG",
"CCUA",
"CCUC",
"CCUU",
"CCUG",
"CCGA",
"CCGC",
"CCGU",
"CCGG",
"CUAA",
"CUAC",
"CUAU",
"CUAG",
"CUCA",
"CUCC",
"CUCU",
"CUCG",
"CUUA",
"CUUC",
"CUUU",
"CUUG",
"CUGA",
"CUGC",
"CUGU",
"CUGG",
"CGAA",
"CGAC",
"CGAU",
"CGAG",
"CGCA",
"CGCC",
"CGCU",
"CGCG",
"CGUA",
"CGUC",
"CGUU",
"CGUG",
"CGGA",
"CGGC",
"CGGU",
"CGGG",
"UAAA",
"UAAC",
"UAAU",
"UAAG",
"UACA",
"UACC",
"UACU",
"UACG",
"UAUA",
"UAUC",
"UAUU",
"UAUG",
"UAGA",
"UAGC",
"UAGU",
"UAGG",
"UCAA",
"UCAC",
"UCAU",
"UCAG",
"UCCA",
"UCCC",
"UCCU",
"UCCG",
"UCUA",
"UCUC",
"UCUU",
"UCUG",
"UCGA",
"UCGC",
"UCGU",
"UCGG",
"UUAA",
"UUAC",
"UUAU",
"UUAG",
"UUCA",
"UUCC",
"UUCU",
"UUCG",
"UUUA",
"UUUC",
"UUUG",
"UUGA",
"UUGC",
"UUGU",
"UUGG",
"UGAA",
"UGAC",
"UGAU",
"UGAG",
"UGCA",
"UGCC",
"UGCU",
"UGCG",
"UGUA",
"UGUC",
"UGUU",
"UGUG",
"UGGA",
"UGGC",
"UGGU",
"UGGG",
"GAAA",
"GAAC",
"GAAU",
"GAAG",
"GACA",
"GACC",
"GACU",
"GACG",
"GAUA",
"GAUC",
"GAUU",
"GAUG",
"GAGA",
"GAGC",
"GAGU",
"GAGG",
"GCAA",
"GCAC",
"GCAU",
"GCAG",
"GCCA",
"GCCC",
"GCCU",
"GCCG",
"GCUA",
"GCUC",
"GCUU",
"GCUG",
"GCGA",
"GCGC",
"GCGU",
"GCGG",
"GUAA",
"GUAC",
"GUAU",
"GUAG",
"GUCA",
"GUCC",
"GUCU",
"GUCG",
"GUUA",
"GUUC",
"GUUU",
"GUUG",
"GUGA",
"GUGC",
"GUGU",
"GUGG",
"GGAA",
"GGAC",
"GGAU",
"GGAG",
"GGCA",
"GGCC",
"GGCU",
"GGCG",
"GGUA",
"GGUC",
"GGUU",
"GGUG",
"GGGA",
"GGGC",
"GGGU"]
listofrepetitions = ["AA","CC","UU","GG","AAA","CCC","UUU","GGG", "AAAA","CCCC","UUUU","GGGG"]

def descriptorsall(mirId, miRNA_sequence, listofmotifs, listofrepetitions, df):
    listofdescriptornames = []
    result = []
    N = len(miRNA_sequence)
    NA = 0
    NU = 0
    NC = 0
    NG = 0
    for x in miRNA_sequence:
        if x == 'A':  
            NA = NA + 1
        if x == 'U':  
            NU = NU + 1
        if x == 'C':  
            NC = NC + 1
        if x == 'G':  
            NG = NG + 1
    percentA = NA/N
    percentU = NU/N
    percentC = NC/N
    percentG = NG/N
    result.append(N)
    listofdescriptornames.append('N')
    result.append(NA)
    listofdescriptornames.append('NA')
    result.append(NU)
    listofdescriptornames.append('NU')
    result.append(NC)
    listofdescriptornames.append('NC')
    result.append(NG)
    listofdescriptornames.append('NG')
    result.append(percentA)
    listofdescriptornames.append('freqA')
    result.append(percentU)
    listofdescriptornames.append('freqU')
    result.append(percentC)
    listofdescriptornames.append('freqC')
    result.append(percentG)
    listofdescriptornames.append('freqG')
    
    for x in listofmotifs:
        listofdescriptornames.append('motif_'+x+'_inall')
        if x in miRNA_sequence:
            result.append(1)
        else: 
            result.append(0)

    for x in listofmotifs:
        subsequence = miRNA_sequence[0:4]
        listofdescriptornames.append('motif_'+x+'_infirst5')
        if x in subsequence:
            result.append(1)
        else: 
            result.append(0)

    for x in listofmotifs:
        subsequence = miRNA_sequence[-5:-1]
        listofdescriptornames.append('motif_'+x+'_inlast5')
        if x in subsequence:
            result.append(1)
        else: 
            result.append(0)
    result2 = 0
    for x in miRNA_sequence:
        if x == 'A':
            result2 = result2+135.1
        elif x == 'G':
            result2 = result2+151.1
        elif x == 'U':
            result2 = result2+112.1
        elif x == 'C':
            result2 = result2+111.1
        result3=result2/(len(miRNA_sequence))
    listofdescriptornames.append('norm_h_bond')
    result.append(result3)
        
    result4=0
    for x in miRNA_sequence:
        if x == 'A':
            result4 = result4+2
        elif x == 'U':
            result4 = result4+2
        elif x == 'G':
            result4 = result4+3
        elif x == 'C':
            result4 = result4+3
    result5 = (result4/(len(miRNA_sequence)))
    listofdescriptornames.append('mean_mass')
    result.append(result5)

    for x in listofrepetitions:
        listofdescriptornames.append('repitition_'+x)
        if x in miRNA_sequence:
            result.append(1)
        else: 
            result.append(0)
    half_len = int(N/2)
    symm_score = 0
    for i in range(half_len):
        if miRNA_sequence[i] == miRNA_sequence[N-i-1]:
            symm_score=symm_score+1
    symm_score = symm_score/half_len
    result.append(symm_score)
    listofdescriptornames.append('symm_score')
    #df=pd.read_csv('miRDB_v6.0_prediction_result_hsa.csv')
    mirId = mirId.lower()
    df1=df[df['mirId']==mirId]
    if df1.empty:
        df1=df[df['mirId']==mirId+'-3p']
        if df1.empty:
            df1=df[df['mirId'] == mirId+'-5p']
    #print(mirId)
    list_name = list(df1.columns)
    list_value = list(df1.iloc[0])
    result = result + list_value[2:]
    #print(len(result))

    listofdescriptornames = listofdescriptornames + list_name[2:]
    #print(len(listofdescriptornames))
    return result, listofdescriptornames

    
       


# In[13]:


import pandas as pd
import math


# In[ ]:





# In[15]:
for item in cancer_type:

    df_target=pd.read_csv(item+'_miRDB_v6.0_prediction_result_hsa.csv')
    fname2 = item+'_selected.csv'
    print('process ' + fname2)
    data = pd.read_csv(fname2)
    list_descriptors = [[]]
    for i, row in data.iterrows():
        if(row['sequence']!='NO_EXIST'):
            miRNA_sequence = row['sequence']
            mirId = row['mirId']
            #print(miRNA_sequence)
            descriptor, listofdescriptornames = descriptorsall(mirId, miRNA_sequence, listofmotifs, listofrepetitions,df_target)
            #row['Cancer'] = 'cancer'
            descriptor.append(row['disease'])
            #descriptor.append(row['Profile'])
            list_descriptors.append(descriptor)
            #print(descriptor)
        else:
               pass

    column_header = listofdescriptornames
    column_header.append('disease')
    #column_header.append('Profile')
    df_descriptor = pd.DataFrame(list_descriptors, columns=column_header)
    df = df_descriptor[1:]
    num_rows=df.shape[0]
    df.to_csv(item+'_selected_descriptor_output.csv', index=False)

    data = pd.read_csv(fname2)
    list_descriptors = [[]]
    for i, row in data.iterrows():
        if(row['sequence']!='NO_EXIST'):
            miRNA_sequence = row['sequence']
            mirId = row['mirId']
            #print(miRNA_sequence)
            descriptor, listofdescriptornames = descriptorsall(mirId, miRNA_sequence, listofmotifs, listofrepetitions,df_target)
            #row['Cancer'] = 'cancer'
            descriptor.append(row['disease'])
            #descriptor.append(row['Profile'].strip())
            list_descriptors.append(descriptor)
            #print(descriptor)
        else:
               pass

    #column_header = listofdescriptornames
    ##column_header.append('CancerLabel')
    ##column_header.append('Profile')
    #df_descriptor = pd.DataFrame(list_descriptors, columns=column_header)
    #df = df_descriptor[1:]
    #df.to_csv(item+'_updown_descriptor_output.csv', index=False)
    #print('output file: ' + item + '_cancer_updown_descriptor_output.csv')
    if not (item == 'multi_disease'):
        data = pd.read_csv(item+'_non_associated_hsa.csv')

        list_descriptors = [[]]
        mirna_list = [[]]

        for i, row in data.iterrows():
            if(row['sequence']!='NO_EXIST'):
                miRNA_sequence = row['sequence']
                mirna_id = []
                mirna_id.append(row['mirId'])
                mirna_list.append(mirna_id)
                #print(miRNA_sequence)
                descriptor, listofdescriptornames = descriptorsall(row['mirId'], miRNA_sequence, listofmotifs, listofrepetitions, df_target)
                descriptor.append(row['disease'])
                #descriptor.append(row['Profile'])
                list_descriptors.append(descriptor)
                #print(descriptor)
            else:
                pass
        column_header2 = ['mirId']
        #print(mirna_list)
        column_header = listofdescriptornames
        column_header.append('disease')
        #column_header.append('Profile')
        df_descriptor = pd.DataFrame(list_descriptors, columns=column_header)
        df_id = pd.DataFrame(mirna_list , columns=column_header2)
        df = df_descriptor.loc[range(1000, 1000+num_rows)]
        df = df.loc[1:]
        df2 = df_id.loc[range(1000, 1000+num_rows)]
        df2 = df2.loc[1:]
        #print(df)
        df.to_csv(item+'_selected_descriptor_output.csv', mode ='a', index=False, header=False)
        df2.to_csv(item+'_selected_non_associated_mirna_id.csv', index=False, header=True)
        print('output file: ' + item+'_selected_descriptor_output.csv')

# In[ ]:





# In[ ]:




