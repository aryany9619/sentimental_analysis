# 10+ WAYS TO RUN THE SENTIMENT ANALYSIS PROGRAM

## 🌐 ONLINE (No Installation Needed!)

### 1. **Google Colab** ⭐ EASIEST
- https://colab.research.google.com/
- Just sign in with Google
- Paste code and click Run
- **No setup needed!**

Steps:
1. Open https://colab.research.google.com/
2. New notebook
3. Paste this code:

```python
!pip install textblob pandas matplotlib

from textblob import TextBlob
import pandas as pd

def check_review(review_text):
    blob = TextBlob(review_text)
    score = blob.sentiment.polarity
    if score > 0.1:
        return "GOOD", score
    elif score < -0.1:
        return "BAD", score
    else:
        return "OKAY", score

good_reviews = ["This is amazing!", "I love it!", "Perfect product!", "Best ever!", "Excellent!"]
bad_reviews = ["This is terrible!", "I hate it!", "Worst product!", "Broken!", "Awful!"]
okay_reviews = ["It's okay.", "Average.", "Normal product.", "It works.", "Not bad, not great."]
all_reviews = good_reviews + bad_reviews + okay_reviews

results = []
for review in all_reviews:
    sentiment, score = check_review(review)
    results.append({'review': review, 'sentiment': sentiment, 'score': round(score, 2)})

good = len([r for r in results if r['sentiment'] == 'GOOD'])
bad = len([r for r in results if r['sentiment'] == 'BAD'])
okay = len([r for r in results if r['sentiment'] == 'OKAY'])

print("\n" + "="*50)
print("SENTIMENT ANALYSIS FOR REVIEWS")
print("="*50)
print(f"Total Reviews: {len(all_reviews)}")
print(f"GOOD Reviews: {good}")
print(f"BAD Reviews: {bad}")
print(f"OKAY Reviews: {okay}")

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

df = pd.DataFrame(results)
print("\n" + "="*50)
print("Results saved (can download as CSV)")
print("="*50)
```

4. Click Run ▶
5. Done!

---

### 2. **Replit** ⭐ EASY
- https://replit.com
- Free account
- All files in one place

Steps:
1. Go to https://replit.com
2. Click "+ Create"
3. Choose Python
4. Paste the same code as above
5. Click Run

---

### 3. **GitHub Codespaces** (FREE 60 hrs/month)
- https://github.com/features/codespaces
- Based on VS Code (online)
- Same as your repo

Steps:
1. Go to: https://github.com/aryany9619/sentimental_analysis
2. Click **Code** (green button)
3. Click **Codespaces** tab
4. Click **Create codespace on main**
5. Wait 1-2 minutes
6. In terminal:
   ```bash
   pip install -r requirements.txt
   python main.py
   ```

---

### 4. **Glitch**
- https://glitch.com
- Free hosting

Steps:
1. Go to https://glitch.com
2. New project → Python
3. Paste code
4. Click Run

---

### 5. **PythonAnywhere**
- https://www.pythonanywhere.com
- Free tier available

Steps:
1. Create account
2. New console → Python
3. Paste code
4. Press Enter

---

## 💻 DESKTOP (Easier than Git)

### 6. **Download ZIP + Extract**
Steps:
1. Go to: https://github.com/aryany9619/sentimental_analysis
2. Click **Code** (green button)
3. Click **Download ZIP**
4. Extract/unzip the folder
5. Open in VS Code: File → Open Folder
6. Terminal: `python main.py`

---

### 7. **Python IDLE** (Built-in Python)
No installation needed if Python is installed!

Steps:
1. Create a text file: `sentiment.py`
2. Paste the code below:

```python
from textblob import TextBlob
import pandas as pd

def check_review(review_text):
    blob = TextBlob(review_text)
    score = blob.sentiment.polarity
    if score > 0.1:
        return "GOOD", score
    elif score < -0.1:
        return "BAD", score
    else:
        return "OKAY", score

good_reviews = ["This is amazing!", "I love it!", "Perfect product!", "Best ever!", "Excellent!"]
bad_reviews = ["This is terrible!", "I hate it!", "Worst product!", "Broken!", "Awful!"]
okay_reviews = ["It's okay.", "Average.", "Normal product.", "It works.", "Not bad, not great."]
all_reviews = good_reviews + bad_reviews + okay_reviews

results = []
for review in all_reviews:
    sentiment, score = check_review(review)
    results.append({'review': review, 'sentiment': sentiment, 'score': round(score, 2)})

good = len([r for r in results if r['sentiment'] == 'GOOD'])
bad = len([r for r in results if r['sentiment'] == 'BAD'])
okay = len([r for r in results if r['sentiment'] == 'OKAY'])

print("\n" + "="*50)
print("SENTIMENT ANALYSIS FOR REVIEWS")
print("="*50)
print(f"Total Reviews: {len(all_reviews)}")
print(f"GOOD Reviews: {good}")
print(f"BAD Reviews: {bad}")
print(f"OKAY Reviews: {okay}")

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
```

3. Right-click file → Open with → Python
4. Done!

---

### 8. **Sublime Text** + Python
Steps:
1. Download Sublime: https://www.sublimetext.com/
2. Create file → Save as `sentiment.py`
3. Paste code from above
4. Tools → Build (or Ctrl+B)

---

### 9. **PyCharm Community** (Free IDE)
- https://www.jetbrains.com/pycharm/
- Full Python IDE

Steps:
1. Download & Install
2. Open the project folder
3. Install requirements: Terminal → `pip install -r requirements.txt`
4. Run: Right-click main.py → Run

---

### 10. **Command Prompt (Windows)** - Simple Way
No Git needed!

Steps:
1. Create folder: `C:\Users\Lenovo\sentiment_project`
2. Create file: `run.py`
3. Paste code from above
4. Open Command Prompt
5. Type:
   ```
   cd C:\Users\Lenovo\sentiment_project
   pip install textblob pandas matplotlib
   python run.py
   ```

---

### 11. **PowerShell (Windows)**
```powershell
cd C:\Users\Lenovo\sentiment_project
pip install textblob pandas matplotlib
python run.py
```

---

### 12. **Terminal (Mac/Linux)**
```bash
cd ~/Desktop/sentiment_project
pip install textblob pandas matplotlib
python main.py
```

---

## 🏆 RECOMMENDED BY DIFFICULTY

| Difficulty | Method | Time |
|-----------|--------|------|
| **Easiest** | Google Colab | 2 min |
| **Very Easy** | Replit | 3 min |
| **Easy** | Download ZIP | 3 min |
| **Easy** | GitHub Codespaces | 5 min |
| **Medium** | Python IDLE | 5 min |
| **Medium** | Sublime Text | 5 min |
| **Medium** | Command Prompt | 5 min |
| **Advanced** | PyCharm | 10 min |
| **Advanced** | VS Code (with Git) | 10 min |

---

## 🎯 MY TOP 3 PICKS

### For Beginners:
**1. Google Colab** - No setup, just go!
- https://colab.research.google.com/

### For Learning:
**2. Download ZIP + VS Code** - See folder structure
- Download ZIP → Open in VS Code → Run

### For Building Projects:
**3. GitHub Codespaces** - Like VS Code, online
- https://github.com/aryany9619/sentimental_analysis
- Click Code → Codespaces

---

## 🚀 QUICK START

**My recommendation for you:**

Since you're having Git issues, use **Google Colab**:
1. Open: https://colab.research.google.com/
2. Sign in with Google
3. New notebook
4. Paste the code from Method 1 above
5. Click Run ▶
6. **Done in 2 minutes!**

**Ready? Go!** 🎉
