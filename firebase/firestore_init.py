import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
import pandas as pd
import numpy as np
import random
# import google_cloud_firestore 
from google.cloud import firestore as fs

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
    items_Ref = db.collection(u'root').document(u'items')

    rst_Ref.set({
        u'id' : u'restaurants',
        u'numRestaurants' : 0
    })

    items_Ref.set({
        u'id' : u'items',
        u'numItems' : 0
    })

    data = getData()

    for idx, rst in enumerate(data):
        rst_Ref.update({
            u'numRestaurants' : fs.Increment(1)
        })

        new_rst_ref = rst_Ref.collection('rstList').document(rst['name'])

        # print(rst['loc'])

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
            items_Ref.update({
                u'numItems' : fs.Increment(1)
            })
            items_Ref.set({
                u'name' : item['name'],
                u'price' : item['price']
            })

def getRandomItem():

    # restaurants_ref = db.document('root/restaurants')

    # num_rst = restaurants_ref.numRestaurants

    # rand_num = random.randint(0,num_rst)

    # rst_stream = restaurants_ref.collection('rstList').stream()

    # for idx, doc in enumerate(rst_stream):
    #     if(idx)


    rst_list = db.collection('root/restaurants/rstList').stream()



    




def getItem(mode):

    if mode == 'random':
        getRandomItem()
    else:
        # rst_list = db.collection('root/restaurants/rstList')
        print("random item")
        # s = rst_list.stream()
        # print(s[0])

        # docs = db.collection(u'cities').stream()

        # for doc in docs:
        #     print(f'{doc.id} => {doc.to_dict()}')

    # for doc in s:

def addTestOrders():
    item = getItem('random')

if __name__ == "__main__":
    print("hello")
    init()
    # addTestOrders()




