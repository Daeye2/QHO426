"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv

def load_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def display_reviews_by_park(data, park_name):
    for review in data:
        if review['Branch'].lower() == park_name.lower():
            print(review)

def count_reviews_by_location(data, park_name, location):
    count = sum(1 for review in data if review['Branch'].lower() == park_name.lower() and review[
        'Reviewer_Location'].lower() == location.lower())
    return count