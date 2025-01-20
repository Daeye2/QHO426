"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
from collections import Counter

from matplotlib import pyplot as plt


def pie_chart_review_counts(data):
    # Count reviews for each park
    park_counts = Counter(review['Branch'] for review in data)
    labels = list(park_counts.keys())
    sizes = list(park_counts.values())

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Review Counts by Park")
    plt.show()


def bar_chart_average_scores(data):
    return None


def top_locations_by_rating(data, park_name):
    return None


def monthly_avg_rating(data, park_name):
    return None