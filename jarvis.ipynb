import os
import re
import time
import schedule
import yagmail
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ----------------------------
# TRAIN A SIMPLE INTENT CLASSIFIER
# ----------------------------
training_sentences = [
    "send email to John",
    "compose an email",
    "mail my teacher",
    "create a shopping list",
    "make a to do list",
    "add bread and milk to my list",
    "set reminder for tomorrow 8 am",
    "remind me at 6 pm",
    "reminder for meeting at 10",
    "open calculator",
    "start notepad",
]

training_labels = [
    "email", "email", "email",
    "list", "list", "list",
    "reminder", "reminder", "reminder",
    "system", "system"
]

# Vectorizer + classifier
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_sentences)
clf = LogisticRegression()
clf.fit(X_train, training_labels)

# Load spaCy model for entity extraction
nlp = spacy.load("en_core_web_sm")

# ----------------------------
# HELPER FUNCTIONS
# ----------------------------
def classify_intent(text):
    X = vectorizer.transform([text])
    return clf.predict(X)[0]

def extract_entities(text, intent):
    doc = nlp(text)
    if intent == "email":
        # crude: take proper nouns as recipient
        names = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG"]]
        return {"recipient": names[0] if names else "unknown@example.com"}
    elif intent == "reminder":
        return {"time": text}
    elif intent == "list":
        # crude: nouns as list items
        items = [token.text for token in doc if token.pos_ == "NOUN"]
        return {"items": items}
    else:
        return {}

def send_email(recipient, body="This is a test from JARVIS!"):
    # requires Gmail setup beforehand
    try:
        yag = yagmail.SMTP("your_email@gmail.com", "your_app_password")
        yag.send(recipient, "JARVIS says hi!", body)
        print(f"[+] Email sent to {recipient}")
    except Exception as e:
        print("[-] Email failed:", e)

def set_reminder(text):
    def job():
        print(f"[Reminder 🔔]: {text}")
        # Mac notification
        os.system(f'''osascript -e 'display notification "{text}" with title "JARVIS Reminder"' ''')
    # schedule after 1 minute for demo
    schedule.every(1).minutes.do(job)
    print("[+] Reminder scheduled (demo: triggers every 1 minute)")

def create_list(items):
    if not items:
        print("[!] No items detected to add to list")
        return
    with open("shopping_list.txt", "a") as f:
        f.write(", ".join(items) + "\n")
    print("[+] Items added to shopping_list.txt:", items)

def run_system_command(text):
    if "calc" in text or "calculator" in text:
        os.system("open -a Calculator")  # Mac Calculator
    elif "notepad" in text:
        os.system("open -a TextEdit")    # Mac Text Editor
    else:
        print("[!] No matching system command")

# ----------------------------
# MAIN LOOP
# ----------------------------
print("🤖 J.A.R.V.I.S ready! Type 'exit' to quit.\n")

while True:
    command = input(">>> ")
    if command.lower() in ["exit", "quit"]:
        print("Shutting down JARVIS...")
        break

    intent = classify_intent(command)
    print(f"[DEBUG] Intent detected: {intent}")

    entities = extract_entities(command, intent)
    print(f"[DEBUG] Entities: {entities}")

    if intent == "email":
        send_email(entities.get("recipient", "someone@example.com"))
    elif intent == "reminder":
        set_reminder(command)
    elif intent == "list":
        create_list(entities.get("items", []))
    elif intent == "system":
        run_system_command(command)
    else:
        print("[!] I didn’t understand that command.")

    # run scheduled reminders
    schedule.run_pending()
    time.sleep(1)

    

