import numpy as np
from badger import environment
from badger.interface import Interface


class Environment(environment.Environment):

    name = 'silly'
    var_channel_map = {
        'q1': 'c1',
        'q2': 'c2',
        'q3': 'c3',
        'q4': 'c4',
        'q5': 'c5',
        'q6': 'c6',
        'q7': 'c7',
        'q8': 'c8',
        'q9': 'c9',
        'q10': 'c10',
        'q11': 'c11',
        'q12': 'c12',
        'q13': 'c13',
        'q14': 'c14',
        'q15': 'c15',
        'q16': 'c16',
    }

    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)

    @staticmethod
    def list_vars():
        return ['q1', 'q2', 'q3', 'q4',
                'q5', 'q6', 'q7', 'q8',
                'q9', 'q10', 'q11', 'q12']

    @staticmethod
    def list_obses():
        return ['l1', 'l2']

    @staticmethod
    def get_default_params():
        return None

    def _get_var(self, var):
        return self.interface.get_value(self.var_channel_map[var])

    def _set_var(self, var, x):
        self.interface.set_value(self.var_channel_map[var], x)

    def _get_obs(self, obs):
        if obs == 'l1':
            values = self.interface.get_values(
                ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'])
            return np.sum(np.abs(values))
        elif obs == 'l2':
            return self.interface.get_value('norm')
