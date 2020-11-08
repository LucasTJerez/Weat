import sys
import firestore_init
import firestore_actions
import pandas as pd
import numpy as np

rst_list = ['Milanos Market', 'Saravana Bhavan', 'Thai Villa']
mock_data = pd.read_csv('./mock_data/mock_database.csv')
itemNames = np.unique(mock_data['menuItem'])

def test_documents_exists():
    # firestore_init.init()

    

    tests = ['root/restaurants', 'root/items']

    for item in itemNames:
        tests.append('root/items/itemList/' + item)
    for rst in rst_list:
        tests.append('root/restaurants/rstList/' + rst)


    for test in tests:
        assert firestore_actions.checkDocument(test)

def test_restaurantList():
    validation = rst_list

    firestore_rst_list = firestore_actions.getRestaurants()

    section = list(set(validation).intersection(firestore_rst_list))

    assert len(section) == len(validation) 


# test_init()
# test_restaurantList()
# test_documents_exists()

