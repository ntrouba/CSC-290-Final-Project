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
            else:
                stop = random.randint(0,1)
            if stop: 
                return "stop", None 
          
        else:
            transition:str = random.choice(list(self.transitions.keys()))
            print(transition)
            next_state:State = random.choice(self.transitions[transition])
            return transition, next_state

    def __str__(self):
        return str(self.accept) + str(self.transitions)
    # def choose 
        # returns transition str, and next state 

    

    
class Fsa:
    def __init__(self, start_state:State, states:list[State]): 
       self.start_state:State = start_state 
       self.states:list[State] = [] 

       self.word_bank:dict[str, list[str] |State] = { "noun": ["reindeer", "misteltoe", "stockings", "chimney", "elf"], 
       "adj": ["warm", "cold", "happy", "festive", "christmassy"], 
       "articles" : ["a", "the"], 
       "prep": ["above", "with", "on", "between", "at"], 
       "det" : ["can", "might", "will"],
       # epsiolon jump 
       "e" : [""]
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
    
    sentence:str= ""
    stop = False
    
    current_state:State|None = fsa.start_state 

    while not stop:
        print("current state:", current_state)

        if current_state == None: 
            stop = True 
        
        else:

            ret = current_state.choose()
            #print(ret)
            #print("type of ret: ", type(ret))
            transition:str = ret[0]
            if transition == "stop":
                stop = True
                #print("break")
                break

            next_state:State|None = ret[1]

           # print("transition: ", transition, "next state:" , next_state)

            # if transition is terminal, add word from list 

            # if transition is an fsa (nonterminal)
                #sentence += gen(transition)
            if fsa_dict.get(transition) != None: 
                print("reciursive call to:", transition)
                sentence += gen(fsa_dict[transition], fsa_dict)
            elif fsa.word_bank.get(transition) != None:
                word:str = random.choice(list(fsa.word_bank.get(transition)))
                print("word:", word)
                sentence += word
            else: 
                print("error, bad transition")
            
            sentence += ' '

            current_state:State = next_state 



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

    # store states in a list 
    np_states = [s1, s2, s3, s4]
    #create fsa 
    np:Fsa = Fsa(s1, np_states)

    s5 = State(False)
    s6 = State(True)

    s_states = [s5, s6]

    s5.transitions = {"np":[s6]} 
    s6.transitions = {}

    s:Fsa = Fsa(s5, s_states)

    fsa_dict:dict[str, Fsa] = {"np": np, "s": s}




    #generate 10 workds 
    sentence = gen(s, fsa_dict)
    print(sentence)





main()