from read_data import read_csv_data

def get_data(data):
    """
    Get data from list.
    Gender: Change Male to 0 and Female to 1
    Weight: Place the column in the Kg view given in Pound (1 kg = 2,205 pound).
    Height: Place the column on the list in the cm view given in inches (2.54 cm = 1 inch).
    Args:
        data(list): data split row
    Returns:
        tuple: gender, weight and height

    """

    

    old_gender=[]
    pound_weight=[]
    inch_height=[]
    gender = []
    weight = []
    height = []
    
    # WRITE YOUR CODE HERE

    #-----------------------------Gender ------------------------------------------
    
    coloumn=file_path.split('\n')
    for idx in range(len(coloumn)):
        coloumn2=coloumn[idx].split(',')
        a=coloumn2[0]
        old_gender.append(a)
    del old_gender[0]
    
    for i in range(len(old_gender)):
        if old_gender[i]=='"Male"':
            gender.append(0)
        if old_gender[i]=='"Female"':
            gender.append(1)
    #-----------------------------Weight ------------------------------------------

    for idx in range(len(coloumn)):
        coloumn2=coloumn[idx].split(',')
        b=coloumn2[2]
        pound_weight.append(b)
    del pound_weight[0]
    
    for idx2 in range(len(pound_weight)):
        kg=float(pound_weight[idx2])/2.205
        weight.append(kg)
    
    #-----------------------------Height ------------------------------------------

    for idx in range(len(coloumn)):
        coloumn2=coloumn[idx].split(',')
        c=coloumn2[1]
        inch_height.append(c)
    del inch_height[0]
    
    for idx3 in range(len(inch_height)):
        cm=float(inch_height[idx3])*2.54
        height.append(cm)

    
    
    return gender,weight,height
file_path=open('data/weight-height.csv').read()
data=read_csv_data('data/weight-height.csv')
print(get_data(data))


