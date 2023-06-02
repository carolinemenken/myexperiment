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
    D2 = models.IntegerField()
    D3 = models.StringField()
    D4 = models.IntegerField()
    D5 = models.IntegerField()
    D6 = models.StringField(blank=True)
    D7 = models.IntegerField()

    E8 = models.IntegerField()
    E9 = models.IntegerField()
    E10 = models.IntegerField()
    E11 = models.IntegerField()
    E12 = models.IntegerField()

    # ET1 = models.StringField()
    # ET2 = models.StringField()
    # ET3 = models.StringField(blank=True)
    # EQ1 = models.StringField()
    # EQ2 = models.IntegerField()
    # EQ3 = models.IntegerField()
    # EQ4 = models.IntegerField()
    # EQ5 = models.IntegerField()
    # Final Checks for Prolific
    dPayoff     = models.FloatField()
    iOutFocus   = models.IntegerField()
    iFullscreenChanges = models.IntegerField()
    dTimeOutFocus = models.FloatField()
    bCheckQ = models.BooleanField()
    sProlificID = models.StringField()

# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']

class Questionnaire2(Page):
    form_model = 'player'
    form_fields = ['E8', 'E9', 'E10', 'E11', 'E12']
    # 'E9', 'E10', 'E11', 'E12']

class Endpage(Page):    
    form_model = 'player' 

page_sequence = [Questionnaire, Questionnaire2, Endpage]