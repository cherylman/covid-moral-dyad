from otree.api import Currency as c
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        yield pages.Stimuli, dict()
        yield pages.Judgement1, dict(judgement1=0.0)
        yield pages.Certainty_1, dict(certainty1=0.0)
        yield pages.Discussion_1, dict(discussion1=0.0)
        yield pages.Wavelength, dict(PartnerAgreement="Strongly disagree")
        yield pages.Judgement_2, dict(judgement2=0.0)
        yield pages.Certainty_2, dict(certainty2=0.0)
        yield pages.Stimuli_Rewatch
        yield pages.Judgement_3, dict(judgement3=0.0)
        yield pages.Certainty_3, dict(certainty3=0.0)