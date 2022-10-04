import os.path
import subprocess
import argparse

from helpers.helper_base import Helperbase

if __name__ == '__main__':

    list = [
        # 'D:\\ImpressicoProjects\\BehavePlaywrightDemo\\features\\loginfeature.feature'
        'D:\\ImpressicoProjects\\BehavePlaywrightDemo\\features\\amazonearbuds.feature'
    ]
    p = argparse.ArgumentParser()
    p.add_argument('--testdir', required=False, help="Path of feature file")
    a = p.parse_args()
    featurefld = 'features'
    testdir = a.testdir
    c = f'behave --no-capture {testdir}'
    for i in list:
        s = subprocess.run('behave --no-capture --junit --junit-directory '
                           'D:\\ImpressicoProjects\\BehavePlaywrightDemo\\Reports' + " " + i, shell=True, check=True)

