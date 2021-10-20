from genericpath import exists
import os
from os import path

def main():
    filePath = ''

    if(os.path.exists(filePath) == 0):
        print('error no file provided')
    else:
        print('file provided, continuning')

    fileInput = 'hello there my name is riki'

    for token in range(fileInput):
        print(token)

main()