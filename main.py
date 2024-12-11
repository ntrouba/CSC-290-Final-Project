import random  
from typing import Self 


class State:
    def __init__(self, accept:bool):
        self.accept:bool = accept
        self.transitions:dict[str, list[State]] | None = None 

    def choose(self) -> tuple[str, Self|None]:
        if self.accept: 
            stop = random.randint(0,1)
            if stop: 
                return "stop", None 
        else:
            transition:str = random.choice(list(self.transitions.keys()))
            print(transition)
            next_state:State = random.choice(self.transitions[transition])
            return transition, next_state

    # def choose 
        # returns transition str, and next state 

    

    
class Fsa:
    def __init__(self, start_state:State, states:list[State]): 
       self.start_state = start_state 
       self.states = [] 

       # transitions dictionary 


       #nouns
       #verbs
       #adjectives
       #articles 
       #prepositions
       #auxiliary verbs 




       self.nouns = ["reindeer", "misteltoe", "stockings", "chimney", "elf"]
       self.verbs = ["caroling", "sipping", "gifting", "opening", "kissing"]
       self.adjectives = ["warm", "cold", "happy", "festive", "christmassy"]
       self.articles = ["a", "the"]
       self.prepositions = ["above", "with", "on", "between", "at"]
       self.determiners = ["can", "might", "will"]


    

    

def gen(fsa:Fsa)-> str:
    
    sentence:str= ""
    stop = False
    
    current_state:State|None = fsa.start_state 

    while not stop:
        print("current state:", current_state)

        if current_state == None: 
            stop = True 
        
        else:

            ret = current_state.choose()
            transition:str = ret[0]
            if transition == "stop":
                stop = True

            next_state:State|None = ret[1]

            print("transition: ", transition, "next state:" , next_state)

            sentence += transition 
            sentence += ' '
            current_state = next_state 







    #temp for testing 
        

        # ret = state.choose  
        # transition = ret[0]
        # next_state = ret[1]


            #if transition = accept, stop  = True 

            # if transition terminal, 
            # words = fsa.transition 
                 # add random word to sentence 

            # if choice not terminal 
                # gen(transition) 

            #current_state = next_state 








        




        




        #print(str(current_state.get_consonant()))
        #print(str(current_state.get_vowel()))

        #look at state and add possible options to choices array 

        # make choice 

        


        # if nonterminal 
    

    return sentence


def main():

    # create automata called fsa 

    #initalize states
    s1:State
    s2:State
    s3:State
    s4:State

    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(True)

    s1.transitions = {"det": [s2]}
    s2.transitions = {"adj": [s2, s3], "e" : [s3]}
    s3.transitions = {"noun" : [s4]} 
    s4.transitions = {}





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
    sentence = gen(fsa)
    print(sentence)





main()