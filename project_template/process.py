"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv
from collections import defaultdict


def load_data(filename):
    #Load the data from CSV file
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def reviews_by_park(data, park_name):
    # Iterate through reviews in the data list and print reviews matching the specified park name.
    for review in data:
        if review['Branch'].lower() == park_name.lower():
            print(review)

def reviews_by_location(data, park_name, location):
    # Count the number of reviews that match the specified park name and reviewer location.
    count = sum(1 for review in data if review['Branch'].lower() == park_name.lower() and review[
        'Reviewer_Location'].lower() == location.lower())
    return count


def rating_by_year(data, park_name, year):
    # Filter reviews by park and year
    ratings = [
        int(review['Rating'])
        for review in data
        if review['Branch'].lower() == park_name.lower() and review['Year_Month'].startswith(year)
    ]
    # Return average rating or 0 if no reviews
    return sum(ratings) / len(ratings) if ratings else 0


def score_by_location(data):
    # Calculates and prints the average rating for each branch and reviewer location.
    scores = defaultdict(list)
    for review in data:
        scores[review['Branch'], review['Reviewer_Location']].append(int(review['Rating']))
    for (park, location), ratings in scores.items():
        print(f"{park} - {location}: {sum(ratings) / len(ratings)}")


def export_data(data, filename):
    if not data:
        print("No data to export.")
        return
    # Get the headers from the keys of the first dictionary
    headers = data[0].keys()
    try:
        with open(filename) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            # Write the header row
            writer.writeheader()
            # Write the data rows
            writer.writerows(data)
        print(f"Data successfully exported to {filename}")

    except Exception as e:
        print(f"An error occurred while exporting data: {e}")