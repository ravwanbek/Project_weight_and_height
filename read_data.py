import csv

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    
    result_data = []

    # WRITE YOUR CODE HERE
    f=file_path.split('\n')
    for j in f:
        result_data.append(j)
    
    return result_data

file_path=open('data\weight-height.csv').read()
print(read_csv_data(file_path))

    