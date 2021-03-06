import abce
from abce.agents import Household


class Killer(abce.Agent, Household):
    def init(self):
        # your agent initialization goes here, not in __init__
        pass

    def kill_silent(self):
        return ('victim', self.round)

    def kill_loud(self):
        return ('loudvictim', self.round)
