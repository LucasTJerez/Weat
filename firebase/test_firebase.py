import sys
import firestore_init
import firestore_actions

def test_init():
    firestore_init.init()

def test_restaurantList():
    validation = ['Milanos Market', 'Saravana Bhavan', 'Thai Villa']

    rst_list = firestore_actions.getRestaurants()

    section = list(set(validation).intersection(rst_list))

    assert len(section) == len(validation)


# test_init()
test_restaurantList()
