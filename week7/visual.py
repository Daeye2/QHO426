import datetime
from collections import Counter, defaultdict
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
    # Calculate average rating per location for a specific park
    location_ratings = defaultdict(list)
    for review in data:
        if review['Branch'].lower() == park_name.lower():
            location_ratings[review['Reviewer_Location']].append(int(review['Rating']))

    # Calculate averages
    avg_ratings = {}
    for loc, ratings in location_ratings.items():
        avg_ratings[loc] = sum(ratings) / len(ratings)

    # Define a custom sorting function
    def sort_by_rating(item):
        return item[1]  # Sort by the average rating

    # Convert dictionary to a list of tuples and sort
    sorted_avg_ratings = list(avg_ratings.items())
    sorted_avg_ratings.sort(key=sort_by_rating, reverse=True)

    # Extract the top 10 locations
    top_10_locations = sorted_avg_ratings[:10]

    # Prepare data for the bar chart
    labels = [item[0] for item in top_10_locations]
    ratings = [item[1] for item in top_10_locations]

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(labels, ratings, color='orange')
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.title(f"Top 10 Locations by Rating for {park_name}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()



def monthly_avg_rating(data, park_name):
    # Calculate average rating for each month for a specific park
    month_ratings = defaultdict(list)
    for review in data:
        if review['Branch'].lower() == park_name.lower():
            # Extract month from 'Year_Month' column
            month = datetime.datetime.strptime(review['Year_Month'], '%Y-%m').month
            month_ratings[month].append(int(review['Rating']))

    # Calculate averages for each month
    months = range(1, 13)
    avg_ratings = [sum(month_ratings[month]) / len(month_ratings[month]) if month in month_ratings else 0 for month in
                   months]

    # Plot the bar chart
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.figure(figsize=(10, 6))
    plt.bar(month_names, avg_ratings, color='green')
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title(f"Monthly Average Ratings for {park_name}")
    plt.show()
