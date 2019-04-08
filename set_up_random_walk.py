import numpy as np


class Random_Walk():
    def __init__(self):
        self.gamma = .9
        self.N_states = 7
        self.N_actions = 2
        self.terminal_states = np.array([0,6])
        self.alpha = .02
        self.v_ini = np.zeros(self.N_states)
        self.q_ini = np.zeros(self.N_states * self.N_actions)

        self.R = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]).T

        self.P = np.matrix(   [[1, 0, 0, 0, 0, 0, 0],#0
                               [1, 0, 0, 0, 0, 0, 0],#0
                               [0, 0, 1, 0, 0, 0, 0],#1
                               [1, 0, 0, 0, 0, 0, 0],#1
                               [0, 0, 0, 1, 0, 0, 0],#2
                               [0, 1, 0, 0, 0, 0, 0],#2
                               [0, 0, 0, 0, 1, 0, 0],#3
                               [0, 0, 1, 0, 0, 0, 0],#3
                               [0, 0, 0, 0, 0, 1, 0],#4
                               [0, 0, 0, 1, 0, 0, 0],#4
                               [0, 0, 0, 0, 0, 0, 1],#5
                               [0, 0, 0, 0, 1, 0, 0],#5
                               [0, 0, 0, 0, 0, 0, 1],#6
                               [0, 0, 0, 0, 0, 0, 1]])#6

        self.pi_rp = np.matrix([[.5, .5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5]])
        self.pi_opt = np.matrix([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

        self.pi_off = np.matrix([[2 / 3, 1 / 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 2 / 3, 1 / 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 2 / 3, 1 / 3, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 2 / 3, 1 / 3, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 2 / 3, 1 / 3, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 / 3, 1 / 3, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 / 3, 1 / 3]])


    def plot_policy(self,policy):
        symbols = ['⬅️', '➡️']
        plot = [''] * self.N_states
        for s in range(self.N_states):
            plot[s] = symbols[np.argmax(policy[s, s * self.N_actions:s * self.N_actions + self.N_actions])]
        print(plot)

if __name__ == "__main__":

    env = Random_Walk()
    # initial parameters
    gamma = env.gamma
    R = env.R
    P = env.P
    v_ini = env.v_ini
    q_ini = env.q_ini

    N_states = env.N_states
    N_actions = env.N_actions
    pi_rp = env.pi_rp
    pi_opt = env.pi_opt
    pi_off = env.pi_off

    print(R)
    print(P)
    env.plot_policy(pi_rp)
    env.plot_policy(pi_opt)
    env.plot_policy(pi_off)