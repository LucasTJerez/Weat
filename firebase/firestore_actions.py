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
# firebase_admin.initialize_app(cred)
db = firestore.client()


def getRestaurants():

    rst_ref = db.collection(u'root/restaurants/rstList')

    docs = rst_ref.stream()

    rst_list = []

    for doc in docs:
        rst_list.append(doc.id)
        # print(f'{doc.id} => {doc.to_dict()}')

    return rst_list




