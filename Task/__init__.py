from otree.api import *
import numpy as np
from numpy import random 
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'MouselabTemplate'
    PLAYERS_PER_GROUP = None
    mTrials = np.genfromtxt(f"_static/global/trials.csv", delimiter=',', dtype= 'unicode')
    NUM_PROUNDS = 0
    NUM_ROUNDS = len(mTrials)
    # Visual tracing vars
    sActivation = 'mouseover'
    sDisplayMode = 'self'
    # options
    bShuffleAttributes = True # Between-subjects (Every participants sees one order)
    bShuffleOptions = True # Within-subjects (every trial)
    # Constant info about your experiment 
    lAttributes = [
            {"name": "Wage (on basis of full time)", "id": "a1", "lValues": [1,2]},
            {"name": "Hours", "id": "a2", "lValues": [3,4]},
            {"name": "Distance (in minutes)", "id": "a3", "lValues": [5,6]},
            {"name": "Useful for society", "id": "a4", "lValues": [7,8]},
            {"name": "Advance opportunity", "id": "a5", "lValues": [9,10]}, 
        ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables
    dRT             = models.FloatField()
    sButtonClick    = models.LongStringField()
    sTimeClick      = models.LongStringField()
    iDec            = models.StringField()

# FUNCTIONS 

def creating_session(subsession):
    if subsession.round_number == 1:
            for player in subsession.get_players():
                p = player.participant
                lOrder = [0,1,2]
                random.shuffle(lOrder)
                p.lAttOrder = lOrder              

                mTrials = C.mTrials[:]

                mPTrials = mTrials[random.choice(mTrials.shape[0], C.NUM_PROUNDS, replace=False), :]
                mTrials = np.concatenate((mPTrials,mTrials),axis=0)
                p.mTrials = mTrials


# PAGES

class Task(Page):
    
    form_model = "player"
    form_fields = ["sButtonClick","sTimeClick","dRT","iDec"]

    @staticmethod
    def vars_for_template(player: Player):
        p = player.participant
        print(p.mTrials)
        vTrials = p.mTrials[player.round_number-1,:].tolist()
        lAttributes = C.lAttributes[:]
        for i in range(len(lAttributes)):
            lAttributes[i]["lValues"] = vTrials[2*i:(2*i+2)]
        print(lAttributes)
        lOptions = [
            'Option A',
            'Option B'
        ]
        return dict(
            lAttributes = lAttributes,
            lOptions = lOptions,
        )
    
    @staticmethod
    def js_vars(player: Player):

        return dict(
            sActivation = C.sActivation,
            sDisplayMode = C.sDisplayMode,
        )


page_sequence = [Task]