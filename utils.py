import os
import pathlib
from uuid import UUID
import sys

def get_file_path() -> str:
    return os.path.dirname(sys.executable)
    # return str(pathlib.Path(__file__).parent.resolve())

def get_all_htmls(directory, extension) -> list:
    f = []
    level = 0
    first_root = True
    for (root, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            if file.endswith('.' + extension):
                f.append((level, root, os.path.join(root,file)))                        
        if is_valid_uuid(restore_uuid(root[-32:])) or first_root:
            level = level + 1
            first_root = False        
    return f

def create_dir(dirname) -> str:
    path = get_file_path() + "\\" + dirname
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    return path

def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test

def restore_uuid(uuid_without_dash):
    return uuid_without_dash[:8] + "-" + uuid_without_dash[8:12] + "-" + uuid_without_dash[12:16] + '-' + uuid_without_dash[16:20] + '-' + uuid_without_dash[20:]
    #5f74048d-1846-4dab-b395-91c85c77b6c5

#print(restore_uuid('5f74048d18464dabb39591c85c77b6c5'))

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()