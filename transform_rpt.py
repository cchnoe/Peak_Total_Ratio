import pandas as pd 
import os
from tqdm import tqdm

def read_rpt():
    path_rpt = 'input_data/'
    list_rpt = os.listdir(path_rpt)
    rpt_file = []
    data_rpt = {}
    for file in list_rpt:
        if os.path.isfile(os.path.join(path_rpt, file)) and file.endswith('.RPT'):
            rpt_file.append(file)
    for rpt in rpt_file:
        f = open(path_rpt+rpt)
        data_rpt[str(rpt)] = list(f)
    return data_rpt, rpt_file


def n_corte(list_name):
    n_data = {}
    path = 'input_data/'
    for file in list_name:
        f = open(path+file)
        rpt= list(f)
        n_index = []
        for m in range(len(rpt)):
            try:
                int(rpt[m][4])
                if type(int(rpt[m][4])) == int:
                    n_index.append(m)
            except Exception:
                pass
        n_data[file] = n_index
    return n_data

def rpt_to_csv(data, n_data):
    dict_dfrpt = {} 
    dict_rpt = {}
    for key in tqdm(data.keys()):
        peak_n = []
        energy = []
        peak_area = []
        end_roi = []
        c_count = []
        rpt = data[key].copy()
        for j in n_data[key]:
            rpt[j] = rpt[j].replace('\n','')
            rpt[j] = rpt[j].replace('- ','-')                     
            peak_n.append(rpt[j][3:6])
            energy.append(rpt[j][27:34])
            peak_area.append(rpt[j][42:53])
            end_roi.append(rpt[j][12:18])
            c_count.append(rpt[j][62:74])

            dict_rpt[key] = {'n_peak':peak_n,'Energy (Kev)':energy,'Peak Net Area':peak_area, 'End_Roi': end_roi, 'continum_count':c_count}
            dict_dfrpt[key] = pd.DataFrame(dict_rpt[key]).set_index('n_peak')
            for i in dict_dfrpt[key]:
                dict_dfrpt[key][str(i)] = pd.to_numeric(dict_dfrpt[key][i])
            dict_dfrpt[key]['Energy (Kev)'] = dict_dfrpt[key]['Energy (Kev)'].astype(int)
            dict_dfrpt[key].to_csv('output_data/'+key+'.csv')  
    return dict_dfrpt