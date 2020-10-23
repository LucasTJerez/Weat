import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
import pandas as pd
import numpy as np
import random

cred = credentials.Certificate("./keys/firebaseAdminAuth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def getData():
    mock_data = pd.read_csv('./mock_data/mock_database.csv')
    # print(rst_csv[0])

    rstNames = np.unique(mock_data['name'])
    # print(rstNames)

    data = []

    # print(type(mock_data))

    for name in rstNames:
        rst_data = mock_data.loc[mock_data['name'] == name]

        rst_loc = np.unique(rst_data['address'].values)[0]
        # print(rst_loc)
        
        rst = {
            'name' : name,
            'loc' : rst_loc
        }


        menu_list = []
        rst_menu = np.unique(rst_data['menuItem'].values)

    #     rst_menu = []
        
        for item in rst_menu:
            rst_item = {
                'name' : item,
                'price' : random.randint(7,20)
            }

            
            menu_list.append(rst_item)

        rst['menu'] = menu_list

        data.append(rst)

    return data
def init():
    rst_Ref = db.collection(u'root').document(u'restaurants')
    #build restaurants document

    rst_Ref.set({
        u'id' : u'restaurants'
    })

    data = getData()

    for idx, rst in enumerate(data):
        new_rst_ref = rst_Ref.collection('rstList').document(rst['name'])

        print(rst['loc'])

        new_rst_ref.set({
            'id' : idx + 2, #set id in ascending from 0-n
            'name' : rst['name'],
            'location' : rst['loc'],
        })

        for item in rst['menu']:
            menu_ref = new_rst_ref.collection('menu').document(item['name'])
            menu_ref.set({
                u'name' : item['name'],
                u'price' : item['price']
            })

def getItem():
    rst_list = db.collection('root').document('restaurants').collection('rstList')

    # rand_rst = rst_list[0]

    # menu = rand_rst.collection('menu')

    # rand_item = menu[0]

    # print(rand_item.get().to_dict())


    # /root/restaurants/rstList/Thai Villa/menu/Massaman Curry

def addTestOrders():
    item = getItem()

if __name__ == "__main__":
    arguments = ['test']

    if len(sys.argv) != 2 or sys.argv[1] not in arguments:
        print("You must input one of the following options:")
        for arg in arguments:
            print('\t'+arg)
        sys.exit()

    if sys.argv[1] == "test":
        init()

        addTestOrders()




