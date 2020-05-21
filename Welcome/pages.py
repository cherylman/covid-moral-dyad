
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent(Page):
    form_model = 'player'
class Welcome(Page):
    form_model = 'player'
class Skype_link(Page):
    form_model = 'player'
page_sequence = [Consent, Welcome, Skype_link]