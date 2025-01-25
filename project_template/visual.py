"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
from collections import Counter, defaultdict

from matplotlib import pyplot as plt


def pie_chart(data):
    # Count reviews for each park
    park_counts = Counter(review['Branch'] for review in data)
    labels = list(park_counts.keys())
    sizes = list(park_counts.values())

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Review Counts by Park")
    plt.show()


def bar_chart(data):
    # Calculate average rating for each park
    park_ratings = defaultdict(list)
    for review in data:
        park_ratings[review['Branch']].append(int(review['Rating']))

    # Prepare data for the bar chart
    labels = list(park_ratings.keys())
    avg_ratings = [sum(ratings) / len(ratings) for ratings in park_ratings.values()]

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(labels, avg_ratings, color='skyblue')
    plt.xlabel("Park")
    plt.ylabel("Average Rating")
    plt.title("Average Review Scores by Park")
    plt.show()

def top_locations_by_rating(data, park_name):
    return None


def monthly_avg_rating(data, park_name):
    return None