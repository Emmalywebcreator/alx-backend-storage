#!/usr/bin/env python3
'''
A module that list and document in database
and return empty list when n0 document in 
a collection
'''


def list_all(mongo_collection):
    '''Lists all documents in a collection.
    '''
    return [doc for doc in mongo_collection.find()]
