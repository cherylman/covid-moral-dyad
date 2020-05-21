
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Stimuli(Page):
    form_model = 'group'
class Judgement_1(Page):
    form_model = 'player'
    form_fields = ['judgement1']
class Certainty_1(Page):
    form_model = 'player'
    form_fields = ['certainty1']
class MyWaitPage_2(WaitPage):
    pass
class Discussion_1(Page):
    form_model = 'player'
    live_method = "live_slider"
class Wavelength(Page):
    form_model = 'player'
    form_fields = ['PartnerAgreement']
class Judgement_2(Page):
    form_model = 'player'
    form_fields = ['judgement2']
class Certainty_2(Page):
    form_model = 'player'
    form_fields = ['certainty2']
class MyWaitPage_3(WaitPage):
    pass
class Stimuli_Rewatch(Page):
    form_model = 'player'
class Judgement_3(Page):
    form_model = 'player'
    form_fields = ['judgement3']
class Certainty_3(Page):
    form_model = 'player'
    form_fields = ['certainty3']
class MyWaitPage_4(WaitPage):
    pass
page_sequence = [Stimuli, Judgement_1, Certainty_1, MyWaitPage_2, Discussion_1, Wavelength, Judgement_2, Certainty_2, MyWaitPage_3, Stimuli_Rewatch, Judgement_3, Certainty_3, MyWaitPage_4]