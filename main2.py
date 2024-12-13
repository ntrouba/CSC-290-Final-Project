import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import random

# Download NLTK resources (only needed the first time)
nltk.download('punkt_tab', force=True)
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')

def parse_text(filename):
    with open(filename, 'r') as file:
        text = file.read()


    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]


    tagged_tokens = pos_tag(filtered_tokens)


    nouns = [word for word, tag in tagged_tokens if tag.startswith('NN')]
    verbs = [word for word, tag in tagged_tokens if tag.startswith('VB')]
    adjectives = [word for word, tag in tagged_tokens if tag.startswith('JJ')]

    return list(set(nouns)), list(set(verbs)), list(set(adjectives))


class State:
    def __init__(self, name, accept=False):
        self.name = name
        self.transitions = {}
        self.accept = accept

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def get_next_state(self, symbol):
        return self.transitions.get(symbol, None)

    def is_accept(self):
        return self.accept


def generate_poem_line(state, fsa, sentence=[]):
    # Base case: If the state is accepting, return the sentence
    if state.is_accept():
        return ' '.join(sentence).capitalize()

    # Randomly select the next transition
    possible_transitions = list(state.transitions.keys())
    if not possible_transitions:
        raise ValueError(f"No transitions available from state: {state.name}")

    transition = random.choice(possible_transitions)


    if transition == "article":
        sentence.append(random.choice(fsa["articles"]))
    elif transition == "adjective":
        sentence.append(random.choice(fsa["adjectives"]))
    elif transition == "noun":
        sentence.append(random.choice(fsa["nouns"]))
    elif transition == "verb":
        sentence.append(random.choice(fsa["verbs"]))
    elif transition == "preposition":
        sentence.append(random.choice(fsa["prepositions"]))


    next_state = state.get_next_state(transition)
    return generate_poem_line(next_state, fsa, sentence)


def main():
    # Parse text from A Christmas Carol
    nouns, verbs, adjectives = parse_text("christmas_carol.txt")


    articles = ["a", "the"]
    prepositions = ["with", "at", "above", "on", "beside", "near"]

    fsa = {
        "nouns": nouns,
        "verbs": verbs,
        "adjectives": adjectives,
        "articles": articles,
        "prepositions": prepositions,
    }


    s1 = State("start")
    s2 = State("article")
    s3 = State("adjective")
    s4 = State("noun")
    s5 = State("verb", accept=True)

    s1.add_transition("article", s2)
    s2.add_transition("adjective", s3)
    s3.add_transition("noun", s4)
    s4.add_transition("verb", s5)


    print("A Recursive Dickensian Holiday Poem:")
    for _ in range(5):
        line = generate_poem_line(s1, fsa)
        print(line)

if __name__ == "__main__":
    main()
