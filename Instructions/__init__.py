import numpy as np
from otree.api import *
import time 

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url         = 'Instructions'
    players_per_group = None
    num_rounds          = 1
    EvalTime           = 45
    AvgDur              = '15'
    iMaxScale           = '7'
    iBonus              = 1
    iPracticeRounds     = 3
    NumTrials           = 30
    # Friendly Checks
    bRequireFS          = True
    bCheckFocus         = True

    SlidesIntro         = [
        dict(
            Title = 'General Information',
            path='Introduction/slide0.html',
            ),
        dict(
            Title = 'Informed Consent',
            path='Introduction/slide1.html',
            ),      
    ]
    
    SlidesInstructions = [
        dict(
            Title='Instructions',
            path='Instructions/slide0.html',
        ),
        dict(
            Title='Instructions',
            path='Instructions/slide1.html',
        )
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dError              = models.FloatField()
    ValidPts            = models.IntegerField()
    Result              = models.StringField()
    NumCal              = models.IntegerField()
    iBlockOrder         = models.IntegerField()
    # Friendly Check vars and PixelRatio
    dPixelRatio         = models.FloatField()
    sSlideSequence      = models.StringField(blank=True)
    sSlideTime          = models.StringField(blank=True)
    # Prolific ID
    sProlific_ID        = models.StringField()


# FUNCTIONS

def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            part            = player.participant
            block = np.random.choice([0,1])
            # part.BlockOrder = block # if two blocks
            part.BlockOrder = 0
            player.iBlockOrder = int(block)
   


# PAGES
     
                

class Introduction(Page):
    

    @staticmethod
    def vars_for_template(player):
        return dict(
            Slides = Constants.SlidesIntro,
        )
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part = player.participant
        # Initialize Focus variables#        
        part.startTime          = time.time()
        part.iOutFocus          = 0
        part.iFullscreenChanges = 0
        part.dTimeOutFocus      = 0

class Instructions(Page):

    @staticmethod
    def vars_for_template(player):
        return dict(
            Slides          = Constants.SlidesInstructions,
        )
    # @staticmethod 
    # def js_vars(player: Player):
    #     return dict(      
    #         bRequireFS    = Constants.bRequireFS,
    #         bCheckFocus   = Constants.bCheckFocus,
    #         defaultPixel  = player.participant.dPixelRatio,
        # )
page_sequence = [Introduction, Instructions]