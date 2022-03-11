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
    result_data=file_path.split('\n')

    
    return result_data

file_path=open('data\weight-height.csv').read()
print(read_csv_data(file_path))

    