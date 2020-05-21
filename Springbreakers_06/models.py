
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Springbreakers_06'
    players_per_group = 2
    num_rounds = 1
    my_constant = ()
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    def live_slider(self, id_in_group, package):
        broadcast = {"slider_value": package["slider_value"], "disable": package["disable"]}
        return {0: broadcast}
class Player(BasePlayer):
    PartnerAgreement = models.StringField(choices=[['Strongly disagree', 'Strongly disagree'], ['Somewhat disagree ', 'Somewhat disagree '], ['Disagree ', 'Disagree '], ['Neither agree nor disagree', 'Neither agree nor disagree'], ['Somewhat agree', 'Somewhat agree'], ['Agree', 'Agree']], label='I think that my partner and I are on the same wavelength with regard to our judgments of the video', widget=widgets.RadioSelectHorizontal)
    judgement1 = models.FloatField()
    certainty1 = models.FloatField()
    judgement2 = models.FloatField()
    certainty2 = models.FloatField()
    judgement3 = models.FloatField()
    certainty3 = models.FloatField()