#!/usr/bin/env python

import tkinter as tk
from tkinter.filedialog import askopenfilename
import glob
 
finder_params = {
        'model': {
            'msg': 'find & click on <your modelname>/model_metadata.json file',
            'ftype_msg': 'json file',
            'ftype': '*json',
            'idx': 19},
        'training': {
            'msg': 'find & click on <your modelname>/logs/training/training...robomaker.log file',
            'ftype_msg': 'log file',
            'ftype': '*.log',
            'idx': 74},
        'evaluation': {
            'msg': 'find & click on <your modelname>/logs/evaluation/evaluation...robomaker.log file',
            'ftype_msg': 'log file',
            'ftype': '*.log',
            'idx': 78},
        'leaderboard': {
            'msg': 'find & click on <your modelname>/logs/leaderboard/leaderboard...robomaker.log file',
            'ftype_msg': 'log file',
            'ftype': '*.log',
            'idx': 80}
}

def finder(f):
    msg = finder_params[f]['msg']
    ftype = finder_params[f]['ftype']
    ftype_msg = finder_params[f]['ftype_msg']
    idx = finder_params[f]['idx']
    root = tk.Tk()
    root.withdraw()
    file_path_1 = 'sagemaker'
    while 'sagemaker' in file_path_1 or f not in file_path_1[-idx:]:
        file_path_1 = askopenfilename(title=msg, filetypes=((ftype_msg, ftype),))
    #root.quit()
    if f in ['training', 'evaluation']:
        file_path_2 = file_path_1[:-idx] + 'metrics/' + f + '/*.json'
        file_path_2 = glob.glob(file_path_2)[0]
        return file_path_1, file_path_2
    return file_path_1
