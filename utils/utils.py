import sys
import pyperclip

def read_data():
    """Reads the input file, deletes the final empty line if necessary and returns a list of lines"""
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    if data[-1] == '':
        del data[-1]
    return data

def copy_result(result):
    """Copies the argument to the clipboard"""
    pyperclip.copy(str(result)) 
