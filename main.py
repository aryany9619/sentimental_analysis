"""
MAIN PROGRAM - RUN THIS FILE
Command: python main.py
"""

from analyzer import check_many_reviews, count_sentiments
from reviews import all_reviews
from charts import show_chart, show_pie
import pandas as pd


print("\n" + "="*50)
print("SENTIMENT ANALYSIS FOR REVIEWS")
print("="*50 + "\n")

# STEP 1: Analyze all reviews
print("Analyzing reviews...")
results = check_many_reviews(all_reviews)
print(f"Done! Analyzed {len(all_reviews)} reviews\n")

# STEP 2: Count results
print("Counting results...")
counts = count_sentiments(results)
print("Done!\n")

# STEP 3: Show results
print("="*50)
print("RESULTS")
print("="*50)
print(f"Total Reviews: {counts['total']}")
print(f"GOOD Reviews: {counts['good']}")
print(f"BAD Reviews: {counts['bad']}")
print(f"OKAY Reviews: {counts['okay']}")
print()

# STEP 4: Show examples
print("="*50)
print("EXAMPLES")
print("="*50)

print("\nGOOD REVIEWS:")
for r in results:
    if r['sentiment'] == 'GOOD':
        print(f"  - {r['review']} (score: {r['score']})")

print("\nBAD REVIEWS:")
for r in results:
    if r['sentiment'] == 'BAD':
        print(f"  - {r['review']} (score: {r['score']})")

print("\nOKAY REVIEWS:")
for r in results:
    if r['sentiment'] == 'OKAY':
        print(f"  - {r['review']} (score: {r['score']})")

# STEP 5: Save to file
print("\n" + "="*50)
df = pd.DataFrame(results)
df.to_csv('results.csv', index=False)
print("Results saved to: results.csv")
print("="*50 + "\n")

# STEP 6: Show charts
print("Showing charts...\n")
show_chart(counts)
show_pie(counts)

print("Done! ✓")
