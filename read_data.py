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
    fayl=open(file_path).read()
    result_data=fayl.split('\n')
    
    return result_data
read_csv_data('data/weight-height.csv')

    