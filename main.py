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
        
        # if not stopping, pick random transition and random destination from that transition 
        transition:str = random.choice(list(self.transitions.keys()))
        # print(transition)
        next_state:State = random.choice(self.transitions[transition])
        return transition, next_state

    def __str__(self):
        return str(self.accept)


class Fsa:
    def __init__(self, start_state:State, states:list[State]): 
       self.start_state:State = start_state 
       self.states:list[State] = [] 

       self.word_bank:dict[str, list[str] |State] = { 
       "noun": ["girl", "boy", "santa", "reindeer", "misteltoe", "stockings", "chimney", "elf"], 
       "adj": ["warm", "cold", "happy", "festive", "christmassy"], 
       "article" : ["a", "the"], 
       "prep": ["above", "with", "on", "between", "at"], 
       "det" : ["can", "might", "will"],
       "e" : [""], # epsiolon jump 
       "aux" : ["can", "may", "might", "will", "would"],
       "wp": ["who", "which", "that", "whose"],
       "punc" : [".", "!", "?"],
       "comma" : [","],
       "verb" : ["caroling", "drinking", "dancing", "opening", "laughing", "smiling", "crying" ]

       }


def gen(fsa:Fsa, fsa_dict:dict[str, Fsa])-> str:

    print("gen", fsa)
    
    poem:str= ""
    stop = False
    
    current_state:State|None = fsa.start_state 

    while not stop:
       # print("current state:", current_state)
        if current_state == None: 
            stop = True 
        else:
            ret = current_state.choose()
           # print(ret)
           # print("type of ret: ", type(ret))
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
                print("error, transiton is:", transition)
            poem+= ' '
            current_state:State = next_state 

    return poem 


def generate_np_automata()->Fsa: 

    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(False)
    s5 = State(False)
    s6 = State(True)

    s1.transitions = {"det": [s2]}
    s2.transitions = {"adj": [s2, s3], "e" : [s3]}
    s3.transitions = {"noun" : [s4]} 
    s4.transitions = {"prep" :[s5], "e" : [s5]}
    s5.transitions = {"whnp" : [s6], "e" : [s6]}
    s6.transitions = {}

    # store states in a list 
    np_states = [s1, s2, s3, s4, s5, s6]
    #create fsa 
    np:Fsa = Fsa(s1, np_states)

    return np

def generate_whnp_autamata() -> Fsa: 
    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(False)
    s5 = State(True)
    s6 = State(True)
    s7 = State(False)

    s1.transitions = {"comma": [s2]}
    s2.transitions = {"wp": [s3]}
    s3.transitions = {"noun": [s4], "e" : [s4]}
    s4.transitions = {"aux" : [s5]}
    s5.transitions = {"verb_phrase": [s6]}
    s6.transitions = {"comma" : [s7]}
    s7.transitions = {}


    whnp_states = [s1, s2, s3, s4, s5, s6, s7]
    #create fsa 
    whnp:Fsa = Fsa(s1, whnp_states)

    return whnp


#TODO make verb_phrase automaata 

def generate_verb_phrase_automata()-> Fsa: 
    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(False)
    s5 = State(True)
    
    s6 = State(False)
    s7 = State(False)
    s8 = State(True)

    s1.transitions = {"e" : [s2, s6] }

    s2.transitions = {"verb" : [s3]}
    s3.transitions = {"np" : [s4], "e" : [s4]}
    s4.transitions = {"prep": [s4, s5], "e": [s5]}
    s5.transitions = {}

    s6.transitions = {"verb" : [s7]}
    s7.transitions = {"adj" : [s8]}
    s8.transitions = {}

    verb_phrase_states = [s1, s2, s3, s4, s5, s6, s7, s8]
    verb_phrase_fsa = Fsa(s1, verb_phrase_states)
    return verb_phrase_fsa




    


def generate_sentence_automata()-> Fsa: 
    s1 = State(False)
    s2 = State(False)
    s3 = State(False)
    s4 = State(False)
    s5 = State(True)

    s6 = State(False)
    s7 = State(False)
    s8 = State(False)
    s9 = State(True)

    s1.transitions = {"e": [s2, s6]}
    s2.transitions = {"np" : [s3]}
    s3.transitions = {"aux" : [s4], "e" : [s4]}
    s4.transitions = {"vp": [s5]}
    s5.transitions= {}
    
    s6.transitions = {"aux": [s7], "adj": [s7]}
    s7.transitions = {"np" : [s8]}
    s8.transitions = {"vp" : [s9]}
    s9.transitions = {}


    s_states = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

    
    s:Fsa = Fsa(s1, s_states)
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
    fsa_dict:dict[str, Fsa] = {"np": generate_np_automata(), "s": generate_sentence_automata(), "line" : generate_line_automata(), "vp" : generate_verb_phrase_automata(), "whnp" : generate_whnp_autamata()}

    #l = gen(fsa_dict.get("line"), fsa_dict)
     # print(l)
    s = gen(fsa_dict.get("s"), fsa_dict) 
    print(s)


    #generate 10 workds 
   # sentence = gen(fsa_dict["s"], fsa_dict)
   # print(sentence)
  
   


##TODO fix spacing w/ episolon jumps 




main()