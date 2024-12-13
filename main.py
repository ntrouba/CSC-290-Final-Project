import random  
from typing import Self 


class State:
    def __init__(self, accept:bool):
        self.accept:bool = accept
        self.transitions:dict[str, list[State]] | None = None 

    def choose(self) -> tuple[str, Self|None]:
        
        # if self.accept and there are no transitions, have to accept. otherwise, choose randomly
        #whether or not to be done generating 
        if self.accept: 
            if len(list(self.transitions.keys()))== 0:
                stop = True 
            else: #
                stop = random.randint(0,1)
            if stop: 
                return "stop", None 
            else:
                transition:str = random.choice(list(self.transitions.keys()))
                #print(transition)
                next_state:State = random.choice(self.transitions[transition])
                return transition, next_state

        else:
            transition:str = random.choice(list(self.transitions.keys()))
           # print(transition)
            next_state:State = random.choice(self.transitions[transition])
            return transition, next_state

    def __str__(self):
        return str(self.accept)
    # def choose 
        # returns transition str, and next state 

    

    
class Fsa:
    def __init__(self, start_state:State, states:list[State]): 
       self.start_state:State = start_state 
       self.states:list[State] = [] 

       self.word_bank:dict[str, list[str] |State] = { 
       "noun": ["reindeer", "misteltoe", "stockings", "chimney", "elf"], 
       "adj": ["warm", "cold", "happy", "festive", "christmassy"], 
       "article" : ["a", "the"], 
       "prep": ["above", "with", "on", "between", "at"], 
       "det" : ["can", "might", "will"],
       "e" : [""], # epsiolon jump 
       "aux" : ["can", "may", "might", "will", "would"],
       "wp": ["who", "which", "that", "whose"],
       "punc" : [".", "!", "?"],
       "comma" : [","]

       }

       # transitions dictionary 


       #nouns
       #verbs
       #adjectives
       #articles 
       #prepositions
       #auxiliary verbs 



    #    self.nouns = ["reindeer", "misteltoe", "stockings", "chimney", "elf"]
    #    self.verbs = ["caroling", "sipping", "gifting", "opening", "kissing"]
    #    self.adjectives = ["warm", "cold", "happy", "festive", "christmassy"]
    #    self.articles = ["a", "the"]
    #    self.prepositions = ["above", "with", "on", "between", "at"]
    #    self.determiners = ["can", "might", "will"]


    

    

def gen(fsa:Fsa, fsa_dict:dict[str, Fsa])-> str:
    
    poem:str= ""
    stop = False
    
    current_state:State|None = fsa.start_state 

    while not stop:
       # print("current state:", current_state)
        if current_state == None: 
            stop = True 
        else:
            ret = current_state.choose()
            print(ret)
            print("type of ret: ", type(ret))
            transition:str = ret[0]
            
            if transition == "stop":
                stop = True
                #print("break")
                break
            next_state:State|None = ret[1]

           # print("transition: ", transition, "next state:" , next_state)
            # if transition is terminal, add word from list 
         

            if fsa_dict.get(transition) != None: 
                print("reciursive call to:", transition)
                poem += gen(fsa_dict[transition], fsa_dict)
            elif fsa.word_bank.get(transition) != None:
                word:str = random.choice(list(fsa.word_bank.get(transition)))
               # print("word:", word)
                poem += word
            else: 
                print("error, bad transition")
            poem+= ' '
            current_state:State = next_state 

    return poem 


def generate_np_automata()->Fsa: 

    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(True)

    s1.transitions = {"det": [s2]}
    s2.transitions = {"adj": [s2, s3], "e" : [s3]}
    s3.transitions = {"noun" : [s4]} 
    s4.transitions = {}

    # store states in a list 
    np_states = [s1, s2, s3, s4]
    #create fsa 
    np:Fsa = Fsa(s1, np_states)

    return np

def generate_sentence_automata()-> Fsa: 
   
    s5 = State(False)
    s6 = State(True)

    s_states = [s5, s6]

    s5.transitions = {"np":[s6]} 
    s6.transitions = {}

    s:Fsa = Fsa(s5, s_states)
    return s 


def generate_line_automata()-> Fsa:
    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(True)

    states = [s1, s2, s3, s4]

    s1.transitions = {"article": [s2]}
    s2.transitions = {"adj" : [s3]}
    s3.transitions = {"adj" : [s3], "noun" : [s4]}
    s4.transitions = {"prep": [s1, s2], "verb" : [s1, s2]}

    fsa =  Fsa(s1, states)

    return fsa




def main():
    fsa_dict:dict[str, Fsa] = {"np": generate_np_automata(), "s": generate_sentence_automata(), "line" : generate_line_automata()}

    l = gen(fsa_dict.get("line"), fsa_dict)
    print(l)


    #generate 10 workds 
   # sentence = gen(fsa_dict["s"], fsa_dict)
   # print(sentence)
  
   


##TODO fix spacing w/ episolon jumps 




main()