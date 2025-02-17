import random as rand
import time
import streamlit as st
import datetime 


ALL_PROBLEM_TYPES = ["Multiplication 2x2","Multiplication 3x3","Find Day of Week"]
DATE_DICT = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
ALL_VOICE_TESTS = ["How much wood would a woodchuck chuck if a woodchuck would chuck wood?",
                   "Peter Piper picked a peck of pickled peppers.",
                   "What do you call a hippie’s wife? ... Mississippi.",
                   "You know what they say about nomadic life: it's in - tents.",
                   "I wonder what percentage of people have sat in the back seat of their own car.",
                   "A perfectly straight road would go into space.",
                   "If there's one thing that makes me throw up, it's a dart board on a ceiling.",
                   "I was gonna tell a time-traveling joke but you didn't like it."]

def logout(*s): print("[LOG]: ", ' '.join([str(k) for k in s]))

class TimeKeeper(object):
    def __init__(self):
        self.mode = None
        self.mode_settings = dict()
    

class ProblemEngine(object):
    def __init__(self,ptype,pdisp,time_keeper):
        self.problem_type = ptype
        self.problem_display_setting = pdisp
        self.timer_keeper = time_keeper
        self.answer = None
        self.out = None
    
    def __str__(self):
        return f"{self.out}, Answer: {self.answer}"
    
    def isValid(self):
        return self.problem_type in ALL_PROBLEM_TYPES and all([self.problem_display_setting,self.timer_keeper.mode])
    
    def getOptions(self):
        return [self.problem_type,self.problem_display_setting,self.timer_keeper.mode]
        
    def generateProblem(self):
        # returns a either disp/tts, answer output
        match self.problem_type:
            case "Multiplication 2x2":
                a = rand.randint(11,99)
                b = rand.randint(11,99)
                answer = a*b
                if self.problem_display_setting == "Read Aloud":
                    out = f"{a} times {b}"
                else:
                    out = f"{a} \\times {b}"
                
            case "Multiplication 3x3":
                a = rand.randint(101,999)
                b = rand.randint(101,999)
                answer = a*b
                if self.problem_display_setting == "Read Aloud":
                    out = f"{a} times {b}"
                else:
                    out = f"{a} \\times {b}"
            case "Find Day of Week":
                start_date = datetime.date(1776,1,1)
                end_date = datetime.date(2099,12,31)
                dates_range = (end_date-start_date).days
                rand_date = datetime.timedelta(days = rand.randint(0,dates_range)) + start_date
                
                
                answer = DATE_DICT[rand_date.weekday()].lower() # monday is 0 and sunday is 6
                if self.problem_display_setting == "Read Aloud":
                    out = f"What day of the week is {rand_date.isoformat()}"
                else:
                    out = "\\text{" + rand_date.strftime("%B %d, %Y") + "}"
            case _:
                out = None
                answer = None
        
        self.out = out
        self.answer = answer
        logout("GENERATING NEW PROBLEM", self)
    
    def showProblem(self, sound_engine):
        
        if self.problem_display_setting == "Read Aloud":
            sound_engine.playVoice(self.out)
        else:
            st.latex(self.out)
            
        