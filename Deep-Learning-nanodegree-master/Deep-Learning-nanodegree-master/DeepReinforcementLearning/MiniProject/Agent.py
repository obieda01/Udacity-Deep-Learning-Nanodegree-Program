# This program is intended to define the behavior of the reinforcement agent in the environment.
#
# implementation with Q-learning
# avg_score - 9.152
#
# by Hiroaki Hamada, oist, 2018/

import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.epsilon = 0.0005;
        
    def get_probs(self, Qs):
      policy_s = np.ones(self.nA)*self.epsilon/self.nA;
      b_action = np.argmax(Qs);
      policy_s[b_action] += 1 - self.epsilon;
      return policy_s
    
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        # get policy-based on epsilon-greedy method
        policy_s = self.get_probs(self.Q[state]);
        return np.random.choice(self.nA, p=policy_s)

    def step(self, state, action, reward, next_state, done):
      
      best_action = np.argmax(self.Q[next_state]);
      self.Q[state][action] += (reward + self.Q[next_state][best_action]- self.Q[state][action]);
              
              