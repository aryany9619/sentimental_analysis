"""
Make simple charts
"""

import matplotlib.pyplot as plt


def show_chart(counts):
    """
    Show a simple bar chart
    """
    sentiments = ['GOOD', 'BAD', 'OKAY']
    numbers = [counts['good'], counts['bad'], counts['okay']]
    colors = ['green', 'red', 'gray']
    
    plt.figure(figsize=(8, 5))
    plt.bar(sentiments, numbers, color=colors)
    plt.title('Customer Reviews')
    plt.ylabel('Number of Reviews')
    plt.xlabel('Type')
    
    # Add numbers on bars
    for i, n in enumerate(numbers):
        plt.text(i, n + 0.1, str(n), ha='center')
    
    plt.show()


def show_pie(counts):
    """
    Show a simple pie chart
    """
    sentiments = ['GOOD', 'BAD', 'OKAY']
    numbers = [counts['good'], counts['bad'], counts['okay']]
    colors = ['green', 'red', 'gray']
    
    plt.figure(figsize=(8, 6))
    plt.pie(numbers, labels=sentiments, autopct='%1.1f%%', colors=colors)
    plt.title('Review Breakdown')
    plt.show()
