"""
Analyze reviews - Check if they are GOOD, BAD, or OKAY
"""

from textblob import TextBlob


def check_review(review_text):
    """
    Check one review - Super simple!
    Returns: 'GOOD', 'BAD', or 'OKAY'
    """
    # Analyze the review
    blob = TextBlob(review_text)
    score = blob.sentiment.polarity  # -1 to 1
    
    # Decide: is it good, bad, or okay?
    if score > 0.1:
        return "GOOD", score
    elif score < -0.1:
        return "BAD", score
    else:
        return "OKAY", score


def check_many_reviews(reviews_list):
    """
    Check multiple reviews at once
    """
    results = []
    
    for review in reviews_list:
        sentiment, score = check_review(review)
        results.append({
            'review': review,
            'sentiment': sentiment,
            'score': round(score, 2)
        })
    
    return results


def count_sentiments(results):
    """
    Count how many are GOOD, BAD, and OKAY
    """
    good = len([r for r in results if r['sentiment'] == 'GOOD'])
    bad = len([r for r in results if r['sentiment'] == 'BAD'])
    okay = len([r for r in results if r['sentiment'] == 'OKAY'])
    total = len(results)
    
    return {
        'total': total,
        'good': good,
        'bad': bad,
        'okay': okay
    }
