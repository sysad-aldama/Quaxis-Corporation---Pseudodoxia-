# FILENAME: pseudosales.py 
# AUTHOR: Jp Aldama 
# DATE: 2/20/2020
# DESCRIPTION: TODO TODO TODO TODO FEST TODO CON
#

# NOTE BUG FIX TODO NOW 
# If products[product][0] <= 1.00
# Then numpy.random.geometric(p,size) returns value error
# so if p <= 0 or p 
import pandas as pd
import random
import datetime
import calendar
import numpy as np
import os
import time
import sys
"""
# For testing..
is_verbose = False
start_time = time.time()
processed_done = False
start_process = False
month_done = False
def verbose():
    if is_verbose == True:
        if start_process == True:
            print(f'______PROCESSING_DATA_____')
            if month_done == True:  
                print(f'___{month_}___Done!!___RUNTIME_{time.time()-start_time}')
                if processed_done == True:
                    print(f'__PROCESSING_COMPLETE!!_RUNTIME_{time.time()-start_time}__')     
    else: 
        print(f'_{month_}_{order_size}CURRENT_PROCESS__')                
"""
products = {
     # TODO Add weighted values for each product in this set {DONE]
     # {product : [price, weight]}
     # The higher the weight value, the more likely a customer will it.
     # Cheaper items would mean a higher weight value
     # play around with these values or go crazy and assign random values
     # all the values and have fun!
     # NOTE FIX Weights!! [NO!]
     'Sony Playstation 4 Pro': [399.99, 17],
     'Sony Playstation 4 Controller': [59.99, 10],
     'Microsoft XBox One Controller': [59.99, 9],
     'Nintendo Switch Joycon Pair': [89.99, 11],
     'Microsoft XBox One X': [399.99, 12],
     'Microsoft Surprise Game': [59.99, 9],
     'Sony Playstation 4 Surprise Game': [59.99, 10],
     'Nintendo Switch Surprise Game': [59.99, 10],
     'Nintendo Switch': [249.99, 20],
     'JBL Bluetooth Wireless Speaker': [199.99, 15],
     'Beats Wireless Headphones': [249.99, 1],
     'LG 65 Inch 4k Smart TV': [399.99, 8],
     'Apple iPhone 11 Pro': [1100, 14],
     'Lenovo Thinkpad': [799.00, 14],
     'Samsung Galaxy S10 Plus': [999.99, 15],
     'Apple TV': [99.99, 30],
     'Whirlpool Washer and Dryer': [699.00, 4],
     'Epson printer': [99.99, 13],
     'Apple Watch': [499.99, 10],
     'Apple Air Pods': [149.00, 13],
     'Apple Lightning USB Charger': [20.00, 12],
     'USB C Android Charger': [11.99, 11],
     'Duracell 9 Volt Batteries': [4.99, 40],
     'Light Bulbs 3 PK': [2.49, 37],
     'IooT Refrigerator': [1500.00, 2],
     'Apple Macbook Pro': [2700.00, 13],
     'Wired Headset for gaming': [49.99, 12],
     'Wireless Headset for gaming': [69.99, 15],
     'Sony wired Headset for MP3 and Movies': [12.99, 17],
     'Candy': [1.99, 60],
     'Soda': [2.00, 50],
     'Hot Dog': [10.00, 30],
     'Extended Warranty 3 Years': [49.00, 10]
}

columns = ['OrderID','Product','QuantityOrdered','Price','OrderDate','PurchaseAddress']
"""
def export_product_inventory():
    inventory = products
    product_index = pd.DataFrame(columns=[inventory])
    sorted_product_index = product_index.sort_values()
    sorted_product_index.to_csv('product_inventory.csv', index=None)
"""
def generate_random_datetime(month):
    day = generate_random_day(month)
    if random.random() < 0.5:
        date = datetime.datetime(2019, month, day, 12,00)
    else:
        date = datetime.datetime(2019, month, day, 20, 00)
    offset_time = np.random.normal(loc=0.0, scale=180)
    datetime_result = date + datetime.timedelta(minutes=offset_time)
    return datetime_result.strftime('%m-%d-%y %H:%M')

def generate_random_day(month):
    days_span = calendar.monthrange(2019,month)[1]
    return random.randint(1,days_span)

def generate_pseudo_address():
    streets_avenues= [
                          '1st',
                          '2nd',
                          '3rd',
                          '4th',
                          '5th',
                          '6th',
                          '7th',
                          '8th',
                          '9th',
                          'Park',
                          'Madison',
                          'Lexington',
                          'Broadway',
                          'Amsterdam',
                          'St Nicholas', 
                          'Wadsworth', 
                          'Audobon' ]
                     
    cities = ['Bronx', 'New York City', 'Queens', 'Brooklyn', 'Staten Island']
    weights = [6,9,5,4,6]
    zipcodes = ['10032','10033','10473','12116','10023']
    states = ['NY','NY','NY','NY','NY']
    
    street = random.choice(streets_avenues)
    index = random.choices(range(len(cities)), weights=weights)[0]
    return (f"{random.randint(1,999)} {street} Avenue, {cities[index]}, {states[index]} {zipcodes[index]}")


# TODO take the data and create csv files 

def data_to_csv():
    pass

#  Maybe json for API?
def data_to_json():
    pass

# TODO WRITE ROWS FOR EXTRA PURCHASES
	
def write_row(order_number,product, thedate, address):
    price_product = products[product][0]
    
    quantity = np.random.geometric(p=1.0-(1.0/price_product), size=1)[0]
    
    output = [order_number,product,quantity,price_product,thedate,address]
      
    return output




# TODO wrap this up and test already!
# TODO create conditions to control what gets bought and what is added
# EX-> if its november, add purchases on certain days 
# EX-> time of day of order. This is very important!
# NOTE Think it through! 
if __name__ == '__main__':
    #if is_verbose == True:
    #    verbose()
    #    start_process = True
        
    order_number = 112358
    for months in range(1,13):       
       # Normal distribution example
        if months <= 9:
            order_size = int(np.random.normal(loc=13500, scale=4000))
        elif months == 10:
            order_size = int(np.random.normal(loc=23750, scale=3000))
        elif months == 11:
            order_size = int(np.random.normal(loc=25000, scale=2500))
        else: #december
            order_size = int(np.random.normal(loc=30000, scale=2000))
            
        product_all = [product for product in products]
        weights = [products[product][1] for product in products]

        df = pd.DataFrame(columns=columns)
    
        i = 0
        while order_size > 0:
        #for i in range(order_size):
                
            address = generate_pseudo_address()
            thedate = generate_random_datetime(months)
            product = random.choices(product_all, weights=weights)[0]
            df.loc[i] = write_row(order_number, product,thedate,address)
            i += 1
                
            # Add more items with random chance
            # If Iphone
            if product == 'Apple iPhone 11 Pro':
                if random.random() < 0.15:
                   # add related accesories
                    df.loc[i] = write_row(order_number, 
                                    'Apple Lightning USB Charger', 
                                    thedate,address)
                    i += 1
                if random.random() < 0.05:
                            
                    df.loc[i] = write_row(order_number, 
                                    'Apple Air Pods',
                                    thedate, address) 
                    i += 1
            elif product == 'Sony Playstation 4 Pro':
                if random.random() < 0.15:
                    df.loc[i] = write_row(order_number,
                                    'Sony Playstation 4 Surprise Game',
                                    thedate, address)
                        
                    i += 1
                if random.random() < 0.13:
                    df.loc[i] = write_row(order_number,
                                    'Sony Playstation 4 Surprise Game',
                                    thedate, address)
                    i += 1
                if random.random() < 0.10: 
                    df.loc[i]  = write_row(order_number,
                                    'Sony Playstation 4 Controller',
                                    thedate, address)
                    i += 1
            elif product == 'Microsoft XBox One X':
                if random.random() < 0.15:
                    df.loc[i] = write_row(order_number,
                                    'Microsoft Surprise Game',
                                    thedate, address)
                        
                    i += 1
                if random.random() < 0.13:
                    df.loc[i] = write_row(order_number,
                                    'Microsoft Surprise Game',
                                    thedate, address)
            
    
                    i += 1

                if random.random() < 0.10: 
                    df.loc[i]  = write_row(order_number,
                                    'Microsoft XBox One Controller',
                                    thedate, address)
                    i += 1
            if random.random() <= 0.02:
                product = random.choices(product_all,weights)[0]
                df.loc[i] = write_row(order_number,product,thedate,address)
                i += 1 
      


                
                
                    
            order_number += 1       
            order_size -= 1
        month_ = calendar.month_name[months]
        df.to_csv(f"pseudocorp_{month_}_2019.csv", index=False)
        print(f"{month_} Done!")    
#            month_done = True
#            if month_done == True and months == 13 and order_size == 0:
#                processed_done == True
                
         


