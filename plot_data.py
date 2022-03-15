
from read_data import read_csv_data
from get_data import get_data
import matplotlib.pyplot as plt

def show(gender, weight, height):
    """
    Show data.
    Args:
        gender(list): 0 and 1
        weight(list): weight
        height(list): height
    Returns:
        None
    """
    w_male = []
    w_female = []
    h_male = []
    h_female = []
    
    #WRITE YOUR CODE HERE
    for i,j in zip(gender,weight):
        if i==0:
            w_male.append(j)
        else:
            w_female.append(j)

    for i,j in zip(gender,height):
        if i==0:
            h_male.append(j)
        else:
            h_female.append(j)
    

    plt.figure(figsize=(5,2.5),dpi=150)
    plt.scatter(h_male,w_male,c='black',label='male')
    plt.scatter(h_female,w_female,c='red',label='female')
    plt.legend()
    plt.show()

data = read_csv_data('data/weight-height.csv')
gender, weight, height = get_data(data)

show(gender, weight, height)