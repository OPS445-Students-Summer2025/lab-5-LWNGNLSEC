#!/usr/bin/env python3
# Author ID: clee259

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')    #opens file
    file_content = f.read()     #reads file
    f.close()                   #closes file
    return file_content

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    new_content = file_content.splitlines() #splits lines, not same as split('\n') -> also displays ''
    f.close()
    return new_content

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))