import hashlib
import argparse
from termcolor import colored
import os
def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("-P"  , '--path' , dest="path" , help="Specify The Path ")
    #parse.add_argument("-A"  , '--Algorithms' , dest="Algo" , help="Specify The Path ")
    options = parse.parse_args()

    if not options.path :
        parse.error(" Path has not been specified ")
    #if not options.Algo :
      #  parse.error(" Algorithm Type has not been specified ")
    return options

def AHASH(bfile) :
    hasher = hashlib.sha256()
    with open(bfile , 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(colored("Hash Value : " , 'cyan' , attrs=["bold"]) + hasher.hexdigest())

options = parser()
os.system("cls")
AHASH(options.path)