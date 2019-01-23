from typing import Tuple, List, Union
import numpy as np
from spacetimerl.base_environment import BaseEnvironment


class TestGame(BaseEnvironment):

    @property
    def min_players(self) -> int:
        return 2

    @property
    def max_players(self) -> int:
        return 2

    @property
    def state_shape(self) -> tuple:
        return 1,

    @property
    def observation_shape(self):
        return 1,

    def new_state(self, num_players: int = 1):
        return np.random.randint(0, 100, (1,)), [0]

    def next_state(self, state: np.ndarray, players: [int], actions: [str]) \
            -> Tuple[np.ndarray, List[int], List[float], bool, Union[List[int], None]]:
        action = int(actions[0])
        distance = -np.abs(action - state[0])
        print("action: {} state: {} distance: {}".format(action, state, distance))
        if action == state[0]:
            return state, [(players[0] + 1) % self.max_players], [distance], True, players
        return state, [(players[0] + 1) % self.max_players], [distance], False, None

    def valid_actions(self, state: np.ndarray) -> [str]:
        return map(lambda x: str(x), np.arange(100))

    def is_valid_action(self, state: np.ndarray, action: str) -> bool:
        return action in self.valid_actions(state)

    def state_to_observation(self, state: np.ndarray, player: int) -> np.ndarray:
        return state