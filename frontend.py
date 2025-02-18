import streamlit as st
#import pyttsx3
import numpy as np
from NumberSense import TimeKeeper,ProblemEngine, logout, ALL_PROBLEM_TYPES, ALL_VOICE_TESTS
# from pygame import mixer
import random as rand


# class SoundEngine(object):
#     def __init__(self):
#         self.soundfiles = ["incorrect.mp3", "correct.mp3","alarm.mp3"]
#         #self.loadTTS()
#         self.loadSFXEngine()
    
#     # def loadTTS(self):
#     #     engine = pyttsx3.init('espeak')
        
#     #     voices = engine.getProperty('voices')
#     #     #engine.setProperty('voice',voices[7].id)
#     #     rate = engine.getProperty('rate')   # getting details of current speaking rate
#     #     engine.setProperty('rate',200)     # setting up new voice rate
        
#     #     self.tts_engine = engine
        
        

#     # def playVoice(self,s): # all voices are through this command
#     #     assert type(s) is str
#     #     self.tts_engine.stop()
#     #     try:
#     #         self.tts_engine.endLoop()
#     #     except RuntimeError:
#     #         pass
#     #     self.tts_engine.say(s)
#     #     self.tts_engine.runAndWait()
        

#     def loadSFXEngine(self):
#         mixer.init()
#         mixer.music.set_volume(0.7)
        
#     def playSound(self,fname):
#         if fname not in self.soundfiles:
#             raise LookupError
#         mixer.music.load(fname)
#         mixer.music.play()
        
#     def reset(self):
#         #self.tts_engine.stop()
#         mixer.music.stop()
    

def main():
    st.set_page_config(layout='centered')
    
    ### Initialize session state variables
    if "current_answer" not in st.session_state: # tracks the current correct answer
        st.session_state.current_answer = "" 
    if "inSession" not in st.session_state: # true if currently in a number sense session
        st.session_state.inSession= False
    if "prevDispOption" not in st.session_state: # true if currently in a number sense session
        st.session_state.prevDispOption = ""
    if "prevOut" not in st.session_state:
        st.session_state.prevOut = ""
    if "userInput" not in st.session_state:
        st.session_state.userInput = ""
    if "prevProblem" not in st.session_state:
        st.session_state.prevProblem = None
        
    ## timer state vars
    if "prevTime" not in st.session_state:
        st.session_state.prevTime = TimeKeeper()
    
    time_keeper = st.session_state.prevTime
    #####
    
    st.title("Numberino Sensorino!")
    st.text("Practice allat mental maths!")
    st.text("Created by Jack Qiao")
    st.markdown("""
    **Email:** [jackqiao2002@gmail.com](mailto:jackqiao2002@gmail.com)
    """)
    
    
    # sound_engine = SoundEngine()
    
    # pills to select mode like: addition, multiplication, find day of week
    # another set of pills for settings: voice only, display
    # another set for timing: stopwatch or timer
    
    if not st.session_state.inSession:
        st.subheader("Settings")
        
        problem_type = st.pills("Select Problem Type", ALL_PROBLEM_TYPES)
        problem_display_mode = st.segmented_control("Problem Display", ["Show on Screen"])
        if problem_display_mode == "Read Aloud" and st.session_state.prevDispOption != "Read Aloud":
            #sound_engine.playVoice(rand.choice(ALL_VOICE_TESTS))
            st.session_state.prevDispOption = problem_display_mode
        elif problem_display_mode != "Read Aloud":
            st.session_state.prevDispOption = ""
        else:
            st.session_state.prevDispOption = "Read Aloud"
            
        col1,col2,col3 = st.columns(3)
        with col1:
            time_keeper.mode = st.segmented_control("Timekeeping", ["Stopwatch", "Timer"])
        
        if time_keeper.mode == "Timer":
            with col2:
                minutes = st.number_input("Minutes", 0, value= 10)
            with col3:
                secs = st.number_input("Seconds",0,59)
            time_keeper.setTimer(minutes*60 + secs)
        else: # stopwatch mode
            time_keeper.setStopwatch()
    
    
        problem_engine = ProblemEngine(problem_type,problem_display_mode,time_keeper)
    else:
        problem_engine = st.session_state.prevProblem
    
    if not problem_engine.isValid():
            
        st.warning("Please select all settings options.")
        st.session_state.inSession = False


    
    if st.button("Start!") and problem_engine.isValid():
        logout("Starting session...")
        
        st.session_state.inSession = True
        #sound_engine.reset()
        time_keeper.reset()
        
        problem_engine.generateProblem()
        st.session_state.prevProblem = problem_engine
        
        
        st.rerun() # refresh so the settings don't pop up
        
        
    
    ###########
    def handle_submit():
        
        uin = st.session_state.userInput.strip().lower()
        correct_answer = str(st.session_state.prevProblem.answer)
        if uin == correct_answer:
            logout("CORRECT!")
            #sound_engine.playSound("correct.mp3")
            problem_engine.count += 1
            st.session_state.prevProblem = problem_engine
            problem_engine.generateProblem()
            
            
        elif len(uin) > 0 and uin != correct_answer: # wrong answer
            logout("WRONG!")
            #sound_engine.playSound("incorrect.mp3")
        else:
            st.warning("Please type an answer.")
        
        
        
        # reset
        st.session_state.userInput = ""
        return

    # Get user input
    if st.session_state.inSession:
        
        #st.session_state.prevProblem.showProblem(sound_engine)
        st.session_state.prevProblem.showProblem()
        
        st.text_input(f"Problem {problem_engine.count}.", key = "userInput", on_change=handle_submit)
        if st.session_state.prevTime.isValid():
            st.session_state.prevTime.showTime()
        else:
            #sound_engine.playSound("alarm.mp3")
            st.session_state.inSession = False
            st.rerun()
        
    
    
if __name__ == "__main__":
    main()
