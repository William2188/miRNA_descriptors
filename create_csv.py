
import pandas as pd
import os

def read_mir_base():
    f = open("maturerna.txt", "r")
    mirna={}
    while True:
        mirna_term = f.readline()
        mirna_sequence = f.readline()
        if not mirna_sequence:
            break  # EOF
        else:
            name = mirna_term.split(' ')[0][1:].lower()
            mirna[name] = mirna_sequence.replace('\n','').upper()

    f.close()
    return mirna
mirna_db = read_mir_base()
disease_type = ['lungcancer']
multi_disease_data = pd.DataFrame()
mrnaid_list_multi = list(mirna_db.keys())

for item in disease_type:
    print(item)
    fname1 = item+'.txt'
    fname2 = item+'.csv'
    data1 = pd.read_csv(fname1, sep="\t", engine='python')
    #data = data1.drop(['PubMed Article'], axis=1)
    mrnaid_list = list(mirna_db.keys())
    data = data1.filter(['mirId'], axis=1)
    remove_list = []
    #int(mirna_db)
    for i, row in data.iterrows():

        seq = 'NO_EXIST'
        #print(row['mirId'])
        if(row['mirId'][-3:] != '-5p' and row['mirId'][-3:] != '-3p'):
            x=row['mirId']
            x=x.lower()
            x1=row['mirId']+'-5p'
            x1=x1.lower()
            x2 = row['mirId'] + '-3p'
            x2=x2.lower()
            if x in mirna_db:
                seq = mirna_db[x]
            elif x1 in mirna_db:
                seq = mirna_db[x1]
            elif x2 in mirna_db:
                seq = mirna_db[x2]
        else:
            x2=row['mirId'].lower()
            if x2 in mirna_db:
                seq = mirna_db[x2]
        data.at[i, 'sequence']=seq
        data.at[i, 'disease'] = "cancer"
        x = row['mirId'].lower()
        if (row['mirId'][-3:] == '-5p' or row['mirId'][-3:] == '-3p'):
            x = row['mirId'][:-3]
            x = x.lower()
        #print(x)
        for key in mrnaid_list:
            if x in key.lower():
                if len(key) > len(x) and (key[len(x)].isdigit()):
                    #print("key", key)
                    pass
                else:
                    #mrnaid_list.remove(key)
                    remove_list.append(key)

                    #print('append', key)
        for key in remove_list:
            print('removed', key)
            if key in mrnaid_list:
                mrnaid_list.remove(key)
        remove_list = []
        for key in mrnaid_list_multi:

            if x in key.lower():

                if len(key) > len(x) and (key[len(x)].isdigit()):
                    pass
                else:
                    remove_list.append(key)
        for key in remove_list:
            if key in mrnaid_list_multi:
                mrnaid_list_multi.remove(key)

                    #print('removed multi', key)
    data = data.drop_duplicates(subset=['mirId'])
    data.to_csv(fname2, index=False, header=True)
    print(fname2)

    number_rows = data.shape[0]
    random_list = []
    import random
    for i in range(50):
        random_list.append(random.randrange(0,number_rows))
    res = []
    [res.append(x) for x in random_list if x not in res]
    df_selected = data.iloc[res,:]
    df_selected.to_csv(item+'_selected.csv', index=False, header=True)

    normal_mirna = {}
    mirId = []
    family = []
    association = []
    profile = []
    sequence = []
    for x in mrnaid_list:
        if 'hsa' in x.lower():
            mirId.append(x)
            family.append(' ')
            association.append('non_cancer')
            #profile.append('normal')
            sequence.append(mirna_db[x])
    normal_mirna['mirId'] = mirId
    #normal_mirna['Family/Cluster'] = family

    #normal_mirna['Profile'] = profile
    normal_mirna['sequence'] = sequence
    normal_mirna['disease'] = association
    df_normal = pd.DataFrame(normal_mirna)
    df_normal.to_csv(item+'_non_associated_hsa.csv', index=False)
    df_normal.to_csv(item+'_selected_non_associated_hsa.csv', index=False)


is_first = True
for item in disease_type:
    fname2 = item + '.csv'
    data = pd.read_csv(fname2)
    if is_first:
        multi_disease_data = data
        is_first = False
    else:
        for i, row in data.iterrows():
            if multi_disease_data[multi_disease_data['mirId'] == row['mirId']].empty:
                multi_disease_data = multi_disease_data.append(row)
            else:
                multi_disease_data.loc[multi_disease_data['mirId'] == row['mirId'],'disease'] += "_"+item
                #multi_disease_data.loc[multi_disease_data['mirId'] == row['mirId'], 'Profile'] = multi_disease_data[multi_disease_data['mirId'] == row['mirId']]['Profile'] + '|' + row['Profile']

multi_disease_data.to_csv('multi_disease.csv', index=False)
normal_mirna = {}
mirId = []
family = []
association = []
profile = []
sequence = []
for x in mrnaid_list_multi:
    if 'hsa' in x.lower():
        mirId.append(x)
        family.append(' ')
        association.append('not_associated')
        #profile.append('normal')
        sequence.append(mirna_db[x])
normal_mirna['mirId'] = mirId
#normal_mirna['Family/Cluster'] = family
normal_mirna['disease'] = association
#normal_mirna['Profile'] = profile
normal_mirna['sequence'] = sequence
df_normal = pd.DataFrame(normal_mirna)
df_normal.to_csv( 'multi_disease_non_associated_hsa.csv', index=False)


#os.system('python generate_miRDB_csv_order.py')
os.system('python compute_multi_disease_descriptors.py')
os.system('python compute_multi_disease_descriptors_selected.py')
