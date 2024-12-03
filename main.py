import random  

class State:
  def __init__(self, accept):
    self.vowel_path = ""
    self.consonant = ""
    self.accept = accept
  def set_noun(self, state)-> str:
    self.noun_path= state
    return self.noun_path
  def set_verb(self, state) -> str: 
    self.verb = state
    return self.verb
  def set_adjective(self, state) -> str:
    self.adjective = state 
    return self.adjective 
  def set_article(self, state) -> str: 
    self.article = state
    return self.article
  def set_preposition(self, state) -> str: 
    self.preposition = state
    return self.preposition
  def get_noun(self): 
    return self.noun_path
  def get_verb(self):
    return self.verb
  def get_adjective(self): 
    return self.adjective
  def get_article(self): 
    return self.article
  def get_preposition(self): 
    return self.preposition
  def is_accept(self): 
    return self.accept 
    
class Fsa:
    def __init__(self, start_state, states): 
       self.start_state = start_state 
       self.states = [] 
       self.consonants = ["z", "t", "n", "h", "d", "sh", "th", "ch", "b", "w", "x"]
       self.vowels = ["a", "e", "i", "o", "u", "y", ""]
       #nouns
       #verbs
       #adjectives
       #articles 
       #prepositions
       #auxiliary verbs 


    def get_start(self):
        return self.start_state 
    

def gen(fsa):
    
    word = []
    stop = False
    
    current_state = fsa.get_start()

    while not stop:
        print("at next state")


        choices = []

        #print(str(current_state.get_consonant()))
        #print(str(current_state.get_vowel()))

        #look at state and add possible options to choices array 
        if current_state.is_accept():
            choices.append("stop")
            print("choices accept:" , choices)
        if current_state.get_vowel() != "":
            choices.append("add vowel")
            #print("choices vowel:" , choices)
        if current_state.get_consonant()!= "":
            choices.append("add consonant")
            #print("choices consonant:" , choices)
        #print("choices:" , choices)
        
        #choose an option randomly
        choice = random.choice(choices)
        #print("choosing:", choice )

        # if adding a value
        if choice == "add vowel":
             i = random.choice(fsa.vowels)
             word.append(i)
             current_state = current_state.get_vowel()
        #if adding a consonant
        elif choice == "add consonant":
            i = random.choice(fsa.consonants)
            word.append(i)
            current_state = current_state.get_consonant()
        #if stopping 
        else:  # choice == 2, stop
            stop = True

    return ''.join(word)


def main():

    # create automata called fsa 

    #initalize states
    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(True)
    
    # set paths 
    # s1.set_consonant(s2)
    # s1.set_vowel(s2)
    # s2.set_vowel(s3)
    # s3.set_consonant(s4)
    # s4.set_vowel(s3)

    # store states in a list 
    states = [s1, s2, s3, s4]

    #create fsa 
    fsa = Fsa(s1, states)

    #generate 10 workds 
    words = []
    for i in range(10): 
      word = gen(fsa)
      words.append(word)
    print(words)



main()