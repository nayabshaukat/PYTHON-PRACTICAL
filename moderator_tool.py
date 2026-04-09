message = "This special offer gives you are free access to an amazing deal, but be careful because it might be a scam. Some messages look free and exciting, yet they hide real danger and are actually spam designed to trick people."
spam_words = ["spam", "free","danger","scam","offer"]

for word in spam_words:
    if word in message:
       message = message.replace(word, "****")

print(message)
print(f"Total character count of the message{len(message)}: ")

