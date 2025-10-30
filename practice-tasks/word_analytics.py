
def analyze_text(text):
    # Your solution here
    
    # 1. Split the text into words and normalize them
    # (make lowercase and remove punctuation)
    clean_text = [word.strip('.,!?:;"()') for word in text.lower().split()]

    # 2. Count the occurrences of each word
    words = {}
    for item in clean_text:
        if item  in words:
            words[item] += 1
        else: 
            words[item] = 1
    # 3. Find the number of unique words
    unique_count = len(words)
    # 4. Identify repeated words (appearing more than once)
    repeated_words = [word for word in words if words[word] > 1]
    
    
    # 5. Find palindrome words
    palindromes = [word for word in words if word == word[::-1] ]
    
    # 6. Return the results in a dictionary with sorted lists
    return {"unique_count": unique_count , "repeated_words" : sorted(repeated_words) , "palindromes": sorted(palindromes)}