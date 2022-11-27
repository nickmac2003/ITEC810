# Import the needed packages
import os


# Function to add data to the text file
def append_data(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Function to create the directory if it does not already exist
def create_directory(directory):
    if not os.path.exists(directory):
        print('Creating Directory ' + directory)
        os.makedirs(directory)


# Function to create the text file if it doesn't exist
def create_file(directory_name, fileName, data):
    f = directory_name + fileName
    if not os.path.isfile(f):
        write_file(f, data)


# Function to delete the text file
def delete_file(path):
    with open(path, 'w'):
        pass


# Function to read the text file
def read_file(path):
    content = []
    with open(path, 'r') as f:
        data = f.read()
        content.append(data)
    return content


# Function to write data to the text file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

