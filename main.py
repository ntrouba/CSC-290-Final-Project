import random

class State:
    def __init__(self, accept):
        self.noun_path = None
        self.verb_path = None
        self.adjective_path = None
        self.article_path = None
        self.preposition_path = None
        self.accept = accept

    def set_noun(self, state):
        self.noun_path = state

    def set_verb(self, state):
        self.verb_path = state

    def set_adjective(self, state):
        self.adjective_path = state

    def set_article(self, state):
        self.article_path = state

    def set_preposition(self, state):
        self.preposition_path = state

    def get_noun(self):
        return self.noun_path

    def get_verb(self):
        return self.verb_path

    def get_adjective(self):
        return self.adjective_path

    def get_article(self):
        return self.article_path

    def get_preposition(self):
        return self.preposition_path

    def is_accept(self):
        return self.accept


class Fsa:
    def __init__(self, start_state):
        self.start_state = start_state
        self.nouns = ["reindeer", "mistletoe", "stockings", "chimney", "elf", "tree", "gift", "sleigh"]
        self.verbs = ["caroling", "sipping", "gifting", "opening", "kissing", "dancing", "gliding"]
        self.adjectives = ["warm", "cold", "happy", "festive", "christmassy", "sparkling", "jolly"]
        self.articles = ["a", "the"]
        self.prepositions = ["above", "with", "on", "between", "at", "near", "beside"]

    def get_start(self):
        return self.start_state


def gen_poem_line(fsa):
    sentence = []
    stop = False
    current_state = fsa.get_start()

    while not stop:
        choices = []

        if current_state.get_article() is not None:
            choices.append("add article")
        if current_state.get_adjective() is not None:
            choices.append("add adjective")
        if current_state.get_noun() is not None:
            choices.append("add noun")
        if current_state.get_verb() is not None:
            choices.append("add verb")
        if current_state.get_preposition() is not None:
            choices.append("add preposition")
        if current_state.is_accept():
            choices.append("stop")

        if not choices:
            raise ValueError("No valid transitions available")

        choice = random.choice(choices)

        if choice == "add article":
            sentence.append(random.choice(fsa.articles))
            current_state = current_state.get_article()
        elif choice == "add adjective":
            sentence.append(random.choice(fsa.adjectives))
            current_state = current_state.get_adjective()
        elif choice == "add noun":
            sentence.append(random.choice(fsa.nouns))
            current_state = current_state.get_noun()
        elif choice == "add verb":
            sentence.append(random.choice(fsa.verbs))
            current_state = current_state.get_verb()
        elif choice == "add preposition":
            sentence.append(random.choice(fsa.prepositions))
            current_state = current_state.get_preposition()
        elif choice == "stop":
            stop = True

    return ' '.join(sentence).capitalize()


def main():
    # Create states for the automaton
    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(True)

    # Define transitions
    s1.set_article(s2)
    s2.set_adjective(s3)
    s3.set_noun(s4)
    s4.set_verb(s1)

    # Initialize FSA
    fsa = Fsa(s1)

    # Generate a holiday poem with 5 lines
    print("Your Holiday Poem:")
    for _ in range(5):
        line = gen_poem_line(fsa)
        print(line)


if __name__ == "__main__":
    main()
