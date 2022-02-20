import os
import pandas as pd
def sorted_data():
    path_rpt = 'output_data/'
    list_rpt = os.listdir(path_rpt)
    g_185p= {}
    g_50p = {}
    t_185p = {}
    t_50p = {}
    q_100p = {}
    q_30p = {}
    data_rpt = {}
    for file in list_rpt:
        if os.path.isfile(os.path.join(path_rpt, file)) and file.startswith('g') and file.endswith('185p.RPT.csv'):
            df_file = pd.read_csv(path_rpt + file).set_index('n_peak')
            g_185p[file] = df_file
        elif os.path.isfile(os.path.join(path_rpt, file)) and file.startswith('g') and file.endswith('50p.RPT.csv'):
            df_file = pd.read_csv(path_rpt + file).set_index('n_peak')
            g_50p[file] = df_file
        elif os.path.isfile(os.path.join(path_rpt, file)) and file.startswith('q') and file.endswith('100p.RPT.csv'):
            df_file = pd.read_csv(path_rpt + file).set_index('n_peak')
            q_100p[file] = df_file  
        elif os.path.isfile(os.path.join(path_rpt, file)) and file.startswith('q') and file.endswith('30p.RPT.csv'):
            df_file = pd.read_csv(path_rpt + file).set_index('n_peak')
            q_30p[file] = df_file 
        elif os.path.isfile(os.path.join(path_rpt, file)) and file.startswith('t') and file.endswith('185p.RPT.csv'):
            df_file = pd.read_csv(path_rpt + file).set_index('n_peak')
            t_185p[file] = df_file
        elif os.path.isfile(os.path.join(path_rpt, file)) and file.startswith('t') and file.endswith('50p.RPT.csv'):
            df_file = pd.read_csv(path_rpt + file).set_index('n_peak')
            t_50p[file] = df_file
        data_rpt = {'g_185p':g_185p, 'g_50p':g_50p, 'q_100p':q_100p,'q_30p':q_30p ,'t_185p':t_185p,'t_50p':t_50p}
    return data_rpt