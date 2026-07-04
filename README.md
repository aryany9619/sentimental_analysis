# SENTIMENT ANALYSIS - SUPER SIMPLE GUIDE

## What Does This Do?

It reads reviews and says if they are:
- **GOOD** = Customer is happy
- **BAD** = Customer is unhappy
- **OKAY** = Customer is neutral

## How to Run It?

### Step 1: Install Python
https://www.python.org/

### Step 2: Install Libraries
```
pip install -r requirements.txt
```

### Step 3: Run Program
```
python main.py
```

**That's it!**

---

## What's Included?

| File | What it does |
|------|-------------|
| `main.py` | **RUN THIS** - The main program |
| `analyzer.py` | Checks if reviews are good/bad/okay |
| `reviews.py` | Sample reviews to test with |
| `charts.py` | Makes charts |
| `requirements.txt` | Libraries needed |

---

## How It Works

### Example 1: GOOD Review
```
Review: "I love this product!"
                    ↓
           Analyzer checks
                    ↓
Score: 0.8 (positive)
                    ↓
          Result: GOOD ✓
```

### Example 2: BAD Review
```
Review: "This is terrible!"
                    ↓
           Analyzer checks
                    ↓
Score: -0.8 (negative)
                    ↓
          Result: BAD ✗
```

### Example 3: OKAY Review
```
Review: "It's okay."
                    ↓
           Analyzer checks
                    ↓
Score: 0.0 (neutral)
                    ↓
          Result: OKAY ~
```

---

## Sample Data

### 5 GOOD Reviews:
- "This is amazing!"
- "I love it!"
- "Perfect product!"
- "Best ever!"
- "Excellent!"

### 5 BAD Reviews:
- "This is terrible!"
- "I hate it!"
- "Worst product!"
- "Broken!"
- "Awful!"

### 5 OKAY Reviews:
- "It's okay."
- "Average."
- "Normal product."
- "It works."
- "Not bad, not great."

---

## Output

When you run `python main.py`, you get:

### In Terminal:
```
==================================================
SENTIMENT ANALYSIS FOR REVIEWS
==================================================

Analyzing reviews...
Done! Analyzed 15 reviews

Counting results...
Done!

==================================================
RESULTS
==================================================
Total Reviews: 15
GOOD Reviews: 5
BAD Reviews: 5
OKAY Reviews: 5

...

Results saved to: results.csv
```

### In results.csv File:
```
review,sentiment,score
This is amazing!,GOOD,0.67
I love it!,GOOD,0.6
This is terrible!,BAD,-0.67
...
```

### Charts:
- Bar chart showing counts
- Pie chart showing percentages

---

## How to Add Your Own Reviews

Edit `reviews.py`:

```python
good_reviews = [
    "Your review here",
    "Another good review",
]

bad_reviews = [
    "Bad review here",
]

okay_reviews = [
    "Okay review here",
]
```

Then run:
```
python main.py
```

---

## Score Explanation

Score ranges from -1 to 1:

```
-1.0 ← More Negative
-0.5 ← Somewhat Negative
 0.0 ← Neutral (okay)
 0.5 ← Somewhat Positive
 1.0 ← Very Positive
```

### How Decision is Made:
```
Score > 0.1   → GOOD
Score < -0.1  → BAD
Score -0.1 to 0.1 → OKAY
```

---

## Errors & Solutions

### Error: "No module named 'textblob'"
**Fix:** Run `pip install textblob`

### Error: "No such file or directory: 'main.py'"
**Fix:** Open terminal in the project folder first

### Charts won't show?
**This is normal on some systems. Check results.csv instead.**

---

## Try This!

### Analyze One Review:

```python
from analyzer import check_review

review = "This is awesome!"
sentiment, score = check_review(review)

print(f"Review: {review}")
print(f"Sentiment: {sentiment}")
print(f"Score: {score}")
```

### Analyze Your Reviews:

```python
from analyzer import check_many_reviews, count_sentiments

my_reviews = [
    "Love it!",
    "Hate it!",
    "It's ok"
]

results = check_many_reviews(my_reviews)
print(results)
```

---

## Files Explained

### main.py (The Main Program)
- Loads reviews
- Analyzes them
- Shows results
- Makes charts
- Saves to CSV

### analyzer.py (The Brain)
- `check_review()` - Analyzes one review
- `check_many_reviews()` - Analyzes multiple reviews
- `count_sentiments()` - Counts results

### reviews.py (The Data)
- 15 sample reviews
- 5 good
- 5 bad
- 5 okay

### charts.py (The Pictures)
- `show_chart()` - Bar chart
- `show_pie()` - Pie chart

---

## What You Learn

✓ Python basics  
✓ How sentiment analysis works  
✓ Using libraries (TextBlob, Pandas, Matplotlib)  
✓ Reading & writing files  
✓ Making charts  
✓ Data analysis  

---

## Next Steps

1. Run the program
2. Add your own reviews
3. Read the code
4. Try modifying it
5. Learn more about TextBlob

---

## Have Fun! 🎉

This is a great starting point for learning about:
- Sentiment analysis
- Python programming
- Data visualization
- Machine learning basics

**Happy coding!**
