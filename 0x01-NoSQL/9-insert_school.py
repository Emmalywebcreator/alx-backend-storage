#!/usr/bin/env python3
'''
A module that insert a document into a collection
'''


def insert_school(mongo_collection, **kwargs):
    '''A function that Inserts a new document in a collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
