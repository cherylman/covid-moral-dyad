
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Coughing_woman_03'
    players_per_group = 2
    num_rounds = 1
    my_constant = 0
    my_constant2 = 0
    my_constant3 = ()
    List = ()
    my_constant4 = ''
class Subsession(BaseSubsession):
    my_field = models.CurrencyField()
class Group(BaseGroup):
    discussion1 = models.FloatField()
    my_field = models.FloatField()
    my_field2 = models.StringField(initial='')
    my_field3 = models.StringField()

    def live_slider(self, id_in_group, package):
        broadcast = {"slider_value": package["slider_value"], "disable": package["disable"]}
        return {0: broadcast}
              
              
class Player(BasePlayer):
    Name = models.StringField(label='What is your name?')
    Age = models.IntegerField(label='What is your age?')
    PartnerAgreement = models.StringField(choices=[['Strongly disagree', 'Strongly disagree'], ['Disagree', 'Disagree'], ['Somewhat disagree', 'Somewhat disagree'], ['Neither agree nor disagree', 'Neither agree nor disagree'], ['Somewhat agree', 'Somewhat agree'], ['Agree', 'Agree']], label='I think that my partner and I are on the same wavelength with regard to our judgments of the video', widget=widgets.RadioSelectHorizontal)
    judgement1 = models.FloatField()
    certainty1 = models.FloatField()
    judgement2 = models.FloatField()
    certainty2 = models.FloatField()
    judgement3 = models.FloatField()
    certainty3 = models.FloatField()
    mutual_judgment = models.IntegerField()
    def my_method(self):
        "live_slider"