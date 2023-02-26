import csv
import json
import nltk
from nltk.tokenize import word_tokenize

# Load existing data from dataset.json if it exists
try:
    with open("dataset.json", "r") as infile:
        data = json.load(infile)
except FileNotFoundError:
    data = {"intents": []}

def add_intent(tag, pattern, response):
    for intent in data["intents"]:
        if intent["tag"] == tag and pattern in intent["patterns"] and response in intent["responses"]:
            print("This intent already exists!")
            return
        elif intent["tag"] == tag:
            intent["patterns"].append(pattern)
            intent["responses"].append(response)
            print(f"Intent added to existing tag {tag}")
            return
    data["intents"].append({
        "tag": tag,
        "patterns": [pattern],
        "responses": [response]
    })
    print(f"New intent added to dataset with tag {tag}")


def TagSelector(question, answer):
    
        # Tokenize the question and answer
    tokens = word_tokenize(question.lower())
    tokens.extend(word_tokenize(answer.lower()))

    # Determine the tag name by checking for keywords in the tokens
    if any(word in tokens for word in ["hi", "hello", "hey", "yo", "greetings"]):
        tag = "greeting"
    elif any(word in tokens for word in ["goodbye", "bye", "see you", "ttyl", "talk to you later"]):
        tag = "goodbye"
    elif any(word in tokens for word in ["help", "support", "assistance", "faq", "question"]):
        tag = "help"
    elif any(word in tokens for word in ["menu", "order", "food", "drink", "hungry"]):
        tag = "ordering"
    elif any(word in tokens for word in ["reservation", "book", "table", "time", "schedule"]):
        tag = "reservation"
    elif any(word in tokens for word in ["price", "cost", "discount", "offer", "sale"]):
        tag = "pricing"
    elif any(word in tokens for word in ["hours", "open", "close", "schedule"]):
        tag = "hours"
    elif any(word in tokens for word in ["location", "address", "directions", "where", "map"]):
        tag = "location"
    elif any(word in tokens for word in ["feedback", "suggestion", "complaint", "improvement"]):
        tag = "feedback"
    elif any(word in tokens for word in ["yes", "no", "okay", "ok", "got it"]):
        tag = "confirmation"
    elif any(word in tokens for word in ["thanks", "thank you", "thx", "appreciate"]):
        tag = "thanks"
    elif any(word in tokens for word in ["news", "updates", "info", "announcement"]):
        tag = "news"
    elif any(word in tokens for word in ["weather", "temperature", "forecast"]):
        tag = "weather"
    elif any(word in tokens for word in ["joke", "funny", "laugh", "humor"]):
        tag = "joke"
    elif any(word in tokens for word in ["movie", "show", "entertainment", "watch"]):
        tag = "entertainment"
    elif any(word in tokens for word in ["music", "song", "playlist", "genre", "band"]):
        tag = "music"
    elif any(word in tokens for word in ["book", "author", "genre", "reading", "recommendation"]):
        tag = "books"
    elif any(word in tokens for word in ["sports", "game", "score", "team", "athlete"]):
        tag = "sports"
    elif any(word in tokens for word in ["history", "fact", "date", "timeline"]):
        tag = "history"
    elif any(word in tokens for word in ["language", "translate", "dictionary", "learn"]):
        tag = "language"
    elif any(word in tokens for word in ["calculator", "compute", "math", "equation"]):
        tag = "calculator"
    elif any(word in tokens for word in ["news", "updates", "article", "headline"]):
        tag = "news"
    elif any(word in tokens for word in ["traffic", "direction", "commute", "route"]):
        tag = "traffic"
    elif any(word in tokens for word in ["health", "nutrition", "fitness", "wellness", "medical"]):
        tag = "health"
    elif any(word in tokens for word in ["shopping", "buy", "store", "discount", "sale"]):
        tag = "shopping"
    elif any(word in tokens for word in ["chat", "conversation", "talk", "discuss", "speak"]):
        tag = "chat"
    elif any(word in tokens for word in ["birthday", "celebration", "party", "gift"]):
        tag = "celebration"
    elif any(word in tokens for word in ["password", "account", "login", "username", "registration"]):
        tag = "account"
    elif any(word in tokens for word in ["travel", "destination", "vacation", "tourism"]):
        tag = "travel"
    elif any(word in tokens for word in ["pet", "animal", "dog", "cat", "fish"]):
        tag = "pets"
    elif any(word in tokens for word in ["food", "recipe", "restaurant", "cuisine"]):
        tag = "food"
    elif any(word in tokens for word in ["movie", "cinema", "showtime", "trailer"]):
        tag = "movie"
    elif any(word in tokens for word in ["job", "career", "resume", "interview", "salary"]):
        tag = "job"
    elif any(word in tokens for word in ["relationship", "dating", "love", "breakup", "marriage"]):
        tag = "relationship"
    elif any(word in tokens for word in ["technology", "software", "hardware", "device", "internet"]):
        tag = "technology"
    elif any(word in tokens for word in ["fashion", "style", "clothing", "accessories", "beauty"]):
        tag = "fashion"
    elif any(word in tokens for word in ["education", "school", "college", "course", "degree"]):
        tag = "education"
    elif any(word in tokens for word in ["finance", "investment", "budget", "savings", "tax"]):
        tag = "finance"
    elif any(word in tokens for word in ["how are you", "how's it going", "how have you been", "how's your day", "what's up"]):
        tag = "how_are_you"
    elif any(word in tokens for word in ["sad", "happy", "angry", "frustrated", "anxious", "excited", "nervous", "stressed", "overwhelmed", "confused", "disappointed", "content", "grateful", "hopeful", "proud", "embarrassed", "surprised", "jealous", "scared"]):
        tag = "feelings"
    elif any(word in tokens for word in ["what is", "who is", "where is", "why", "when", "how", "which", "can you", "do you", "tell me", "explain", "define", "clarify", "elaborate", "could you", "would you"]):
        tag = "question_and_answer"
    else:
        print("the input does not match any previously defined tags. So give the tag name manually")
        tag = input()

    # If a tag name was found, add the intent to the data dictionary
    if tag:
        add_intent(tag, question, answer)

    # Write the updated data back to dataset.json
    with open("dataset.json", "w") as outfile:
        json.dump(data, outfile, indent=4, separators=(',', ': '))
    
    print("Data written to dataset.json")


def process_csv_file(file_path):
    with open(file_path, encoding='iso-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) # skip header row if exists
        for row in csv_reader:
            question, answer = row[0], row[1]
            TagSelector(question, answer)

    
def Main():
    print("do you want to \n1) process a csv file \n2)give questions and answers manually to generate the JSON File (1 or 2): ")
    choice = int(input())
    if choice == 1:
        file_path = input("Enter the location of csv file: ")
        process_csv_file(file_path)
        return "process finished"
    
    elif choice == 2:
        while True:
            question = input("enter question(type exit to quit): ")
            if question == "exit":
                break
            else:
                answer = input("Enter the answer: ")
                TagSelector(question, answer)
        return "process finished"
    
    else:
        print("Enter a valid value")
        Main()


print(Main())
