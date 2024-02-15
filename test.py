import random
import time
from tkinter import *
import tkinter as tk


def ancient():
    # Display each sentence's words
    phrase_example = "I am here"
    print("A*** There is", len(phrase_example.split()), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(phrase_example.split()):
        print(j + 1, "-", mot)

    # Display each sentence's words
    new_phrase_example = phrase_example.split()
    print("B*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Delete word with his name in list : table.remove("word")
    new_phrase_example.remove("am")
    print(new_phrase_example)
    print("C*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Delete word with his position in the list : table.pop(index)
    new_phrase_example.pop(0)
    print(new_phrase_example)
    print("D*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add word at the end of the list : table.append("word")
    new_phrase_example.append("Sandy")
    print(new_phrase_example)
    print("E*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add word at word with specific position : table.insert(index, "word")
    new_phrase_example.insert(0, "Who")
    print(new_phrase_example)
    print("F*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add word with specific position : table.insert(index, "word")
    new_phrase_example.insert(1, "is")
    print(new_phrase_example)
    print("G*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add all word characters at the list end : table.extend("word") --> [..., 'w', 'o', 'r', 'd']
    new_phrase_example.extend("Mo")
    print(new_phrase_example)
    print("H*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add more elements in the list : table = ['', '', '',...]; table.extend(['1', '2', '3',...]) --> ['1', '2', '3',..., '', '', '',...]
    new_phrase_example.extend(["Moriarty", "?"])
    print(new_phrase_example)
    print("I*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add more elements in the list
    new_list = ["Sandy", ",", "give", "me", "answer", "please", "."]
    new_phrase_example = new_phrase_example + new_list
    print(new_phrase_example)
    print("J*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    # Add more elements in the list
    new_list = ["Sandy", ",", "are", "you", "listen", "to", "me", "?"]
    new_phrase_example += new_list
    print(new_phrase_example)
    print("K*** There are", len(new_phrase_example), "words in this sentence.")
    print("The words are :")
    for j, mot in enumerate(new_phrase_example):
        print(j + 1, "-", mot)

    print("\n")


window = Tk()
window.geometry("500x300+1000+500")

all_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             " ", "-", "'", ]

all_min_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 " ", "-", "'", ]

all_min_cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', " ", "-", "'", ]

all_min_voy = ['a', 'e', 'i', 'o', 'u', 'y', " ", "-", "'", ]

words_table = ["able", "about", "absolutely", "accept", "accident", "accidentally", "accommodation", "acquaintance", "across", "act", "activity",
               "actual", "actually", "address", "admit", "adult", "advance", "advantage", "advertising", "advice", "advise", "aerobics", " a few",
               "affect", "afraid", "after", "afternoon", "again", "age", "agency", "ago", "agree", "ahead", "air-conditioning", "air mail", "airport",
               "all", "all right", "all the time", "a lot", "almost", "along", "already", "also", "altogether", "always", "amaze", "amazing", "America", "American",
               "amusing", "ancient", "ancient", "animal", "another", "announce", "annoying", "answer", "antibiotics", "anticlockwise", "anxious", "any",
               "anybody", "anymore", "anyone", "anything", "anytime", "anyway", "anywhere", "apologize", "apparently", "appeal", "appetite", "applause",
               "apple", "apply", "appointment", "appreciate", "approaching", "April", "area", "armistice", "around", "arrange", "arrival", "arrive", "art",
               "artificial", "artist", "as", "as well as", "ask", "aspirin", "assure", "attend", "attendant", "attitude", "attraction", "attractive", "August",
               "aunt", "automatic", "avoid", "away", "awful", "back", "back out", "bacon", "bad", "bag", "bake", "baker", "bald", "band", "banger", "bargain",
               "base", "basically", "bat", "bath", "bathroom", "battery", "battle", "be", "beach", "bean", "bean-stalk", "bear", "beard", "beat", "beaten",
               "beautiful", "because", "become", "bed", "bedroom", "bedsitter", "beef", "been", "beer", "before", "began", "beggar", "begin", "begun", "behead",
               "behind", "believe", "belong", "best", "best man", "bet", "better", "between", "beyond", "bicycle", "big", "bike", "bill", "bin", "bin men", "bird",
               "birthday", "birthplace", "biscuit", "bit", "bite", "bitten", "bitter", "black", "blackcurrent", "blanket", "blind" "block", "block of flats",
               "bloke", "blood", "bloody", "blow-dry", "blue", "board", "boat", "body", "bone", "bonfire", "bonus", "book", "boot", "border", "bore", "boring",
               "born", "borrow", "boss", "both", "bother", "bottle", "bought", "bouquet", "bowling", "box", "Boxing day", "boy", "brandy", "bread", "breadbin", "break",
               "breakfast", "break down", "break up", "breast", "bride", "bridegroom", "bridesmaid", "bridge", "bright", "bring", "Britain", "British", "British Rail",
               "brochure", "brogues", "broke", "broken", "brooch", "brother", "brought", "brown", "builder", "building", "built", "bulldog", "bulldozer", "burn", "bus",
               "bus-stop", "business", "busy", "butcher", "butter", "button", "buy", "by", "by any chance", "by the way", "bye", 'cab', 'cake', "calculate", "calculation",
               "calculator", 'call', 'caller', 'camcorder',
               'camera', 'camping', 'can', 'cancel', 'captain', 'car', 'car-boot', 'car-hire', "car keys", "card", "care", "Carol singer", "carriageway", "carrot", "carry",
               "carry away", "carry on", "case", "cases", "cash", "casserole", "cassette", "castle", "casual", "catch", "catching", "catch up on", "caterer", "caught", "cease",
               "ceiling", "celebrate", "celebration", "cellar", "centre", "century", "cereal", "certainly", "chair", "chance", "change", "channel", "the Channel", "charge",
               "charity", "charming", "chat", "cheap", "check", "cheek", "cheerful", "cheers", "cheese", "chemist", "cheque", "chess", "chew", "chicken", "child", "childhood",
               "chips", "chocolate", "choice", "choose", "chose", "chosen", "Christmas", "Christmas Eve", "church", "citizen", "city", "civil", "civilised", "class", "classical",
               "clean", "cleaner", "cleanliness", "clear", "clear up", "clever", "client", "clip", "clock", "clockwise", "close", "clothe", "clothes", "cloud", "cloudy", "club",
               "clue", "coal", "coat", "coat hanger", "code book", "coffee", "coin", "coke", "cold", "collar", "colonial", "colour", "combined", "comfortable", "come",
               "come along", "come back", "come home", "come in", "come on", "come over", "company", "compensation", "complain", "complete", "completely", "complexion", "composer",
               "computer", "conceited", "concern", "condemn", "condition", "conditioner", "condone", "conductor", "conference", "confirm", "congestion", "connect", "connection",
               "conscience", "conscious", "conspiracy", "contact", "contraflow", "control", "conversation", "convinced", "co-ordinated", "cook", "cool", "corner", "cost", "cough",
               "could", "councillor", "count", "country", "countryside", "couple", "course", "cousin", "cow", "cow-boy", "crack", "cram", "crazy", "cream", "credit card", "cricket",
               "crisps", "criticize", "cross", "cross off", "crossing", "crossroads", "crowd", "cruise", "cry", "cup", "cupboard", "cupboard space", "curb", "curly", "curry", "curtain",
               "custard", "customs", "cut", "cut off"]

greetings_words = ["Hi", "hi", "Hello", "hello", "Welcome", "Welcome back", ""]

print("I have a dictionary with **", len(words_table), "** words actually.")

word_count_lim = 10 ** 5
word_count = 1

print("\n")

essai_word = input("Write something: ")
random_word = essai_word.lower()
print(random_word, "; his length is:", len(random_word))


def word_by_word():
    def display_wbw(index):
        if index < len(random_word):
            random_word_found = random_word[index]
            bot_word_label.config(text=bot_word_label.cget("text") + random_word_found + "")
            index += 1
            window.after(100, display_wbw, index)

    display_wbw(0)


window.after(2000, word_by_word)

bot_word_label = tk.Label(master=window, activebackground="white", activeforeground="blue", font="SegoeUI 30", fg="black",
                          borderwidth=0, border=0, relief=FLAT, text="", wraplength=300, justify='left', anchor="w",
                          bg="#FFFFFF", bd=2, )
bot_word_label.pack(padx=0.5, pady=0.5)


def random_word_function(new_essai_word, rdm_word, new_word_rdm, new_words_rdm):
    rdm_word = random_word
    print(rdm_word, "; his length is:", len(random_word))
    new_essai_word = random.choices(population=all_min_table, k=len(rdm_word))

    new_word_rdm = ""
    new_words_rdm = ""

    for new_var in range(len(new_essai_word)):
        new_word_rdm = new_essai_word[new_var]
        new_words_rdm += new_word_rdm
    print("New word:", new_words_rdm, "; his length is:", len(new_words_rdm))


new_word = ""
new_words = ""
essai_word_two = random.choices(population=all_min_table, k=len(random_word))
print(essai_word_two, "; his length is:", len(essai_word_two))
for first_var in range(len(essai_word_two)):
    new_word = essai_word_two[first_var]
    new_words += new_word

change_word = ""
print(new_words, "; his length is:", len(new_words))

if new_words == random_word:
    print("I write it!")

new_table = []

for first_var in range(len(essai_word_two)):
    change_word = essai_word_two[first_var]
    new_table.extend([change_word])

if new_words != random_word:
    print("There are not the same!")

    print(essai_word_two)

    for second_var in range(len(new_words)):
        print("Number iteration: ***", second_var, "***")

        if new_words[second_var] != random_word[second_var]:
            print("***", new_words[second_var], "*** and ---", random_word[second_var], "--- are not the same.")

            """
            if random_word[second_var] in all_min_voy:
                print("It's a vowel.")
            elif random_word[second_var] in all_min_cons:
                print("It's a consonant.")
            """

        else:
            print("These letters are the same.")

print("\n")

print("BEFORE: ===", new_table, "=== ;", len(new_table))

print("\n")

new_word_form = ""
new_word = ""

start = time.time()

for new in range(len(new_table)):
    if random_word[new] in all_min_table:
        new_table[new] = random.choice(all_min_table)
        while new_table[new] != random_word[new]:
            new_table[new] = random.choice(all_min_table)
            word_count += 1

        if new_table[new] == random_word[new]:
            new_word = new_table[new]
            new_word_form += new_word

end = time.time()
duration = end - start

print("I found your word: ~~~", new_word_form, "~~~ after ", word_count, " try and", duration, "seconds!")


"""

    def word_by_word():
        def display_wbw(index):
            if index < len(new_word_form):
                word_word_found = new_word_form[index]
                bot_word_label.config(text=bot_word_label.cget("text") + word_word_found + "")
                index += 1
                window.after(100, display_wbw, index)

        display_wbw(0)


    window.after(5000, word_by_word)

    bot_word_label = tk.Label(master=window, activebackground="white", activeforeground="blue", font="SegoeUI 30", fg="black",
                              borderwidth=0, border=0, relief=FLAT, text="", wraplength=300, justify='left', anchor="w",
                              bg="#FFFFFF", bd=2, )
    bot_word_label.pack(padx=0.5, pady=0.5)
"""


for third_var in words_table:
    if new_word_form == third_var:
        print("I found it: ---", new_word_form, "--- and ***", third_var, "***")

print("\n")

print("AFTER: ===", new_table, "=== ;", len(new_table))

print("\n")
print("\n")

question_table = ["what", "when", "where", "who", "whom", "which", "whose", "why", "how"]
verb_conj_table = ["are", "is", "have", "has", "can", "could", "will", "would", "may", "might", "do"]
pronoun_table = ["i", "me", "you", "he", "him", "she", "her", "it", "we", "us", "they", "them", "who", "whom", "whose", "what", "which", "that", "your"]

question = ""
verb_conj = ""
pronoun = ""
questions = question + " " + verb_conj + " " + pronoun

word = new_word_form.split()
for j, mot in enumerate(new_word_form.split()):
    print(j + 1, "-", mot)
    for fourth_var in words_table:
        if mot == fourth_var:
            print("I found it: *--", mot, "--* and -**", fourth_var, "**-")

    for quest_var in question_table:
        if mot == quest_var:
            print("I found a question word")
            question = mot
            questions = question + " " + verb_conj + " " + pronoun

    for verb_conj_var in verb_conj_table:
        if mot == verb_conj_var:
            print("I found a conjugated verb.")
            verb_conj = mot
            questions = question + " " + verb_conj + " " + pronoun

    for pronoun_var in pronoun_table:
        if mot == pronoun_var:
            print("I found a pronoun.")
            if mot in ["who", "whom", "whose", "what"]:
                pronoun = new_word_form[2:]
                questions = question + " " + verb_conj + " " + pronoun
            else:
                pronoun = mot
                questions = question + " " + verb_conj + " " + pronoun

print("A question is : ***", questions, "***")

print("\n")


class SuperclassDetector:
    def __init__(self):
        self.question_table = {
            "what": "asking for information about something",
            "when": "asking about the time or date",
            "where": "asking about a place or location",
            "who": "asking about a person or people",
            "whom": "asking about a person or people (object of verb)",
            "which": "asking about a choice between options",
            "whose": "asking about possession",
            "why": "asking about the reason or cause",
            "how": "asking about the manner or process"
        }
        self.verb_table = {
            "be": "exist, occur, take place",
            "have": "possess, own, hold",
            "do": "perform, execute, carry out",
            "say": "speak, utter, express",
            "go": "move, travel, proceed",
            "get": "obtain, acquire, receive",
            "make": "create, produce, build",
            "know": "understand, comprehend, be aware of",
            "think": "believe, consider, judge",
            "take": "grab, seize, hold",
            "see": "perceive, observe, notice",
            "come": "arrive, approach, enter",
            "want": "desire, wish, crave",
            "look": "see, observe, watch",
            "use": "utilize, employ, make use of",
            "find": "discover, locate, uncover",
            "give": "offer, provide, donate",
            "tell": "inform, notify, instruct",
            "work": "labor, toil, exert oneself",
            "call": "telephone, phone, ring",
            "try": "attempt, endeavor, strive",
            "ask": "inquire, question, request",
            "need": "require, demand, necessitate",
            "feel": "sense, perceive, experience",
            "become": "develop into, grow into, turn into"
        }
        self.pronoun_table = {
            "i": "first person singular",
            "me": "first person singular (object)",
            "you": "second person singular or plural",
            "he": "third person singular (male)",
            "him": "third person singular (male, object)",
            "she": "third person singular (female)",
            "her": "third person singular (female, object)",
            "it": "third person singular (neutral)",
            "we": "first person plural",
            "us": "first person plural (object)",
            "they": "third person plural",
            "them": "third person plural (object)",
            "who": "refers to a person or people",
            "whom": "refers to a person or people (object of verb)",
            "whose": "refers to possession",
            "what": "refers to a thing or things",
            "which": "refers to a choice between options",
            "that": "refers to a specific thing or things"
        }
        self.verb_conj_table = {
            "are": "exist, occur, take place",
            "is": "exist, occur, take place",
            "have": "",
            "has": "",
            "can": "",
            "could": "",
            "will": "",
            "would": "",
            "may": "",
            "might": "",
            "do": "perform, execute, carry out",
        }

    def recognize_superclass(self, first_sentence: str) -> dict:
        """
        Recognize question words, verbs, and pronouns in a sentence based on a list of common English question words, verbs, and pronouns and their meanings.

        Args:
            first_sentence (str): The sentence to recognize question words, verbs, and pronouns in.

        Returns:
            dict: A dictionary of question words, verbs, and pronouns recognized in the sentence and their meanings.
        """
        words = first_sentence.lower().split()
        questions = {word: self.question_table[word] for word in words if word in self.question_table}
        verbs = {word: self.verb_table[word] for word in words if word in self.verb_table}
        pronouns = {word: self.pronoun_table[word] for word in words if word in self.pronoun_table}
        verbs_conj = {word: self.verb_conj_table[word] for word in words if word in self.verb_conj_table}
        return {"questions": questions, "verbs": verbs, "pronouns": pronouns, "verbs_conj": verbs_conj}


# Example usage
detector = SuperclassDetector()

superclass = detector.recognize_superclass(random_word)
if superclass["questions"]:
    print("The question words in the sentence are:")
    for question, meaning in superclass["questions"].items():
        print(f"***{question}: {meaning}")
else:
    print("No question words found in the sentence. So it's not a question.")

if superclass["verbs"]:
    print("The verbs in the sentence are:")
    for verb, meaning in superclass["verbs"].items():
        print(f"***{verb}: {meaning}")
else:
    print("No verbs found in the sentence.")

if superclass["verbs_conj"]:
    print("The conjugated verbs in the sentence are:")
    for verbs_conj, meaning in superclass["verbs_conj"].items():
        print(f"***{verbs_conj}: {meaning}")
else:
    print("No verbs found in the sentence.")

if superclass["pronouns"]:
    print("The pronoun(s) in the sentence are:")
    for pronouns, meaning in superclass["pronouns"].items():
        print(f"***{pronouns}: {meaning}")
else:
    print("No pronoun found in the sentence.")

print("\n")

bot_pronoun = ""
if pronoun == "your":
    bot_pronoun = "My"
else:
    bot_pronoun = "The"

bot_answer = bot_pronoun + " " + word[len(word) - 1] + " " + verb_conj + " " + random.choice(words_table)

last_word = bot_answer.split()[len(bot_answer.split()) - 1]
upper_first_letter = last_word[0].upper()
last_letter_table = []
new_last_word = ""
for last_var in range(len(last_word)):
    last_letter_table.extend([last_word[last_var]])
    last_letter_table.pop(0)
    last_letter_table.insert(0, f"{upper_first_letter}")

new_last_table = ''
for new_last_var in range(len(last_letter_table)):
    new_last_table = last_letter_table[new_last_var]
    new_last_word += new_last_table

print(new_last_word)

ai_name_var = ""
ai_name = ""
ai_new_last_word = ""
bot_answer = bot_pronoun + " " + word[len(word) - 1] + " " + verb_conj + " " + new_last_word + "."

# Write AI name lines code
if word[len(word) - 1] == "name":
    ai_new_last_word = random.choices(population=all_table, k=5)
    print(ai_new_last_word, "; his length is:", len(ai_new_last_word))
    for fifth_var in range(len(ai_new_last_word)):
        ai_name = ai_new_last_word[fifth_var]
        ai_name_var += ai_name

    change_word = ""
    print("---------------------------------------------", ai_name_var, "; his length is:", len(ai_name_var))

    ai_name_ai = "Sandy"
    new_ai_table = []

    for new_sixth_var in range(len(ai_new_last_word)):
        change_word = ai_new_last_word[new_sixth_var]
        new_ai_table.extend([change_word])

    new_ai_word_form = ""
    new_ai_word = ""
    word_count_ai = 1

    start_ai = time.time()

    for new_ai_var in range(len(new_ai_table)):
        if ai_name_ai[new_ai_var] in all_table:
            new_ai_table[new_ai_var] = random.choice(all_table)
            while new_ai_table[new_ai_var] != ai_name_ai[new_ai_var]:
                new_ai_table[new_ai_var] = random.choice(all_table)
                word_count_ai += 1

            if new_ai_table[new_ai_var] == ai_name_ai[new_ai_var]:
                new_ai_word = new_ai_table[new_ai_var]
                new_ai_word_form += new_ai_word

    end_ai = time.time()
    duration_ai = end_ai - start_ai

    if new_ai_word_form == ai_name_ai:
        print("I found your word: ~~~", new_ai_word_form, "~~~ after ", word_count_ai, " try and", duration_ai, "seconds!")
        new_last_word = new_ai_word_form

bot_answer = bot_pronoun + " " + word[len(word) - 1] + " " + verb_conj + " " + new_last_word + "."

print("Bot: ", bot_answer)


def wbw():
    def display_word_by_word(index):
        if index < len(bot_answer):
            word_word_found = bot_answer[index]
            bot_word_answer.config(text=bot_word_answer.cget("text") + word_word_found + "")
            index += 1
            window.after(100, display_word_by_word, index)

    display_word_by_word(0)


window.after(10000, wbw)

bot_word_answer = tk.Label(master=window, activebackground="white", activeforeground="blue", font="SegoeUI 30 bold", fg="black",
                           borderwidth=0, border=0, relief=FLAT, text="", wraplength=300, justify='left', anchor="w",
                           bg="#FFFFFF", bd=2, )
bot_word_answer.pack(padx=0.5, pady=20)

for i in range(len(word)):
    print(word[i])

window.mainloop()
