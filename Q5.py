import os

def create_dir(name, address):
    new_path = address + '\\' + name
    if not os.path.exists(new_path):
        os.mkdir(new_path)

def create_file(name, address):
    new_path = address + '\\' + name
    if not os.path.exists(new_path):
        open(new_path, 'a').close()

def delete(name, address):
    new_path = address + '\\' + name
    if os.path.exists(new_path):
        os.remove(new_path)

def find(name, address):
        file_list = os.listdir(address)
        print([address + "\\" + i for i in file_list if str(i).find(name + ".") == 0])
                

find('a', 'E:\\Class files\\AP\\HW5')
