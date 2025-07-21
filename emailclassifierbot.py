# Email classifier bot without using ML to classify into work-rleated, promotional, personal, spam category

# Defining 4 categories and related keywords lists

work_keywords = ["project", "meeting", "deadline", "update"]
spam_keywords = ["free", "win", "urgent", "lottery", "claim"]
promo_keywords = ["offer", "sale", "discount", "deal", "coupon"]
personal_keywords = ["party", "dinner", "lunch", "call", "hangout", "family"]

# function to classify email
def classify_email(text):
    text = text.lower()

    # counting the number of words in the text with the list defined and comparing to specify exact match
    work_count = sum(1 for word in work_keywords if word in text)
    # updated the code for returning the number of words matched in the text
    work_matched = [word for word in work_keywords if word in text]
    spam_count = sum(1 for word in spam_keywords if word in text)
    spam_matched = [word for word in spam_keywords if word in text]
    promo_count = sum(1 for word in promo_keywords if word in text)
    promo_matched = [word for word in promo_keywords if word in text]
    personal_count = sum(1 for word in personal_keywords if word in text)
    personal_matched = [word for word in personal_keywords if word in text]

    if spam_count >= 2 :
        return f"Category: Spam 🚫\nMatched Words: {spam_matched}"
    elif work_count >= promo_count and work_count >= personal_count:
        return f"Category: Work ✅\nMatched Words: {work_matched}"
    elif promo_count >= work_count and promo_count >= personal_count:
        return f"Category: Promotional 🛍️\nMatched Words: {promo_matched}"
    elif personal_count > 0:
        return f"Category: Personal 🤝\nMatched Words: {personal_matched}"
    else:
        return "Unclassified ❓"
    

# printing the output
email1 = "Hey, don’t forget the project deadline for our client meeting."
email2 = "Congratulations! You’ve won a free vacation. Claim now!"
email3 = "Wanna hangout for dinner with the family?"
email4 = "Congratulations! You got an offer of 20LPA."
email5 = "Urgent Meeting! is there are you free now will you be able to join now?"

print(classify_email(email1))  
print(classify_email(email2))  
print(classify_email(email3))
print(classify_email(email4))
print(classify_email(email5))