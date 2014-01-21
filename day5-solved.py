def add_2_numbers(x, y):
    return x + y

def divide_2_numbers(x, y):
    return float(x) / float(y)

def get_3rd_value(x):
    return x.split(',')[2]

def get_4th_comma_plus(x):
    return x.split(',', 4)[4]

def get_lines_4_5(x):
    return x.splitlines()[3:5]

def get_cleaned_values_3_4(x):
    y = x.split(',')
    
    a = y[3]
    a = a[1:]
    
    b = y[4]
    b = b[1:]
    
    return [a,b]
