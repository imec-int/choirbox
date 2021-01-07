# import sys
# sys.path +=['.']
# from states import State, StateMachine
# # from StateMachine import StateMachine
# class pdSendBPM(State):
#     def run(self):
#         print("receiving")
        
#     def next(self, input):
#         print("next")
        
#         return BPMsetter.taptempo


# class taptempo(State):
#     def run(self):
#         print("reading tap tempo")
#     def next(self, input):
#         print("next")


# class ProgramBPM(State):
#     def run(self):
#         print("updating tap tempo")
#     def next(self, input):
#         print("next")


# class BPMsetter(StateMachine):
#     def __init__(self):
#         print("statemachine init")
#         StateMachine.__init__(self, BPMsetter.pdSendBPM)
#         # self.button = button
#         # self.led = led
from statemachine import StateMachine, State

class BPMStateMachine(StateMachine):
    pdSendsBPM = State('pdSendsBPM', initial=True)
    tapTempo = State('taptempo')
    programBPM = State('programBPM')

    tapped = pdSendsBPM.to(tapTempo)
    tapStopped = tapTempo.to(programBPM)
    go = programBPM.to(pdSendsBPM)