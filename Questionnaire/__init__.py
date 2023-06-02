from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables for Demographics
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField(blank=True)
    D7 = models.StringField()
    # E8 = models.StringField()
    # E9 = models.StringField()
    # E10 = models.StringField()
    # E11 = models.StringField()
    # E12 = models.StringField()

    # ET1 = models.StringField()
    # ET2 = models.StringField()
    # ET3 = models.StringField(blank=True)
    # EQ1 = models.StringField()
    # EQ2 = models.IntegerField()
    # EQ3 = models.IntegerField()
    # EQ4 = models.IntegerField()
    # EQ5 = models.IntegerField()
    # Final Checks for Prolific
    # dPayoff     = models.FloatField()
    # iOutFocus   = models.IntegerField()
    # iFullscreenChanges = models.IntegerField()
    # dTimeOutFocus = models.FloatField()
    # bCheckQ = models.BooleanField()
    # sProlificID = models.StringField()

# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
    # 'E8','E9','E10','E11','E12']

class Endpage(Page):    
    form_model = 'player' 

page_sequence = [Questionnaire, Endpage]