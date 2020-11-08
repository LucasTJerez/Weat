import sys
import firestore_init
import firestore_actions

rst_list = ['Milanos Market', 'Saravana Bhavan', 'Thai Villa']


def test_documents_exists():
    # firestore_init.init()



    tests = ['root/restaurants']
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
