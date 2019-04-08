import numpy as np


class Grid_World():
    def __init__(self):
        # Grid world problem
        self.N_states = 25
        self.N_actions = 4
        self.gamma = .9
        # We split the states in blocks
        B1 = 1
        B2 = 5
        B3 = 21
        B4 = 25
        B5 = 6
        B6 = 16
        B7 = 11
        B8 = np.array([22, 23, 24])-1
        B9 = np.array([10, 15, 20])-1
        B10 = np.array([2, 3, 4])-1
        B11 = np.array([7, 8, 9, 12, 13, 14, 17, 18, 19])-1
        self.P = np.zeros(shape=(self.N_states * self.N_actions, self.N_states))
        self.R = np.zeros(shape=(self.N_states * self.N_actions , 1))
        self.pi_m = np.zeros(shape=(self.N_states, self.N_states * self.N_actions))
        for k in range(self.N_states):
            k
            if k == 1-1:
                self.P[k * self.N_actions , 1-1] = 1
                
                self.R[k * self.N_actions ] = -1
                
                self.P[k * self.N_actions  + 1, 6-1] = 1
                self.P[k * self.N_actions  + 2, 2-1] = 1
                self.P[k * self.N_actions  + 3, 1-1] = 1
                
                self.R[k * self.N_actions  + 3] = -1
            elif k == 5-1:
                self.P[k * self.N_actions , 4-1] = 1
                self.P[k * self.N_actions  + 1, 10-1] = 1
                self.P[k * self.N_actions  + 2, 5-1] = 1
                
                self.R[k * self.N_actions  + 2] = -1
                
                self.P[k * self.N_actions  + 3, 5-1] = 1
                
                self.R[k * self.N_actions  + 3] = -1
            elif k == 21-1:
                self.P[k * self.N_actions , 21-1] = 1
                
                self.R[k * self.N_actions ] = -1
                
                self.P[k * self.N_actions  + 1, 21-1] = 1
                
                self.R[k * self.N_actions  + 1] = -1
                
                self.P[k * self.N_actions  + 2, 22-1] = 1
                self.P[k * self.N_actions  + 3, 16-1] = 1
            elif k == 25-1:
                self.P[k * self.N_actions , 24-1] = 1
                self.P[k * self.N_actions  + 1, 25-1] = 1
                
                self.R[k * self.N_actions  + 1] = -1
                
                self.P[k * self.N_actions  + 2, 25-1] = 1
                
                self.R[k * self.N_actions  + 2] = -1
                
                self.P[k * self.N_actions  + 3, 20-1] = 1
            elif k == 6-1:
                self.P[k * self.N_actions , 10-1] = 1
                
                self.R[k * self.N_actions ] = 10
                
                self.P[k * self.N_actions  + 1, 10-1] = 1
                
                self.R[k * self.N_actions  + 1] = 10
                
                self.P[k * self.N_actions  + 2, 10-1] = 1
                
                self.R[k * self.N_actions  + 2] = 10
                
                self.P[k * self.N_actions  + 3, 10-1] = 1
                
                self.R[k * self.N_actions  + 3] = 10
            elif k == 16-1:
                self.P[k * self.N_actions , 18-1] = 1
                
                self.R[k * self.N_actions ] = 5
                
                self.P[k * self.N_actions  + 1, 18-1] = 1
                
                self.R[k * self.N_actions  + 1] = 5
                
                self.P[k * self.N_actions  + 2, 18-1] = 1
                
                self.R[k * self.N_actions  + 2] = 5
                
                self.P[k * self.N_actions  + 3, 18-1] = 1
                
                self.R[k * self.N_actions  + 3] = 5
            elif k == 11-1:
                self.P[k * self.N_actions , 11-1] = 1
                
                self.R[k * self.N_actions ] = -1
                
                self.P[k * self.N_actions  + 1, 16-1] = 1
                self.P[k * self.N_actions  + 2, 12-1] = 1
                self.P[k * self.N_actions  + 3, 6-1] = 1
            elif (k in B8):
                self.P[k * self.N_actions , k - 1] = 1
                self.P[k * self.N_actions  + 1, k] = 1
                
                self.R[k * self.N_actions  + 1] = -1
                
                self.P[k * self.N_actions  + 2, k + 1] = 1
                self.P[k * self.N_actions  + 3, k - 5] = 1
            elif (k in B9):
                self.P[k * self.N_actions , k - 1] = 1
                self.P[k * self.N_actions  + 1, k + 5] = 1
                self.P[k * self.N_actions  + 2, k] = 1
                
                self.R[k * self.N_actions  + 2] = -1
                
                self.P[k * self.N_actions  + 3, k - 5] = 1
            elif (k in B10):
                self.P[k * self.N_actions , k - 1] = 1
                self.P[k * self.N_actions  + 1, k + 5] = 1
                self.P[k * self.N_actions  + 2, k + 1] = 1
                self.P[k * self.N_actions  + 3, k] = 1
                
                self.R[k * self.N_actions  + 3] = -1
            elif (k in B11):
                self.P[k * self.N_actions , k - 1] = 1
                self.P[k * self.N_actions  + 1, k + 5] = 1
                self.P[k * self.N_actions  + 2, k + 1] = 1
                self.P[k * self.N_actions  + 3, k - 5] = 1

            self.pi_m[k, k * self.N_actions : (k + 1) * self.N_actions] = [.25, .25, .25, .25]


def plot_policy(policy):
    symbols = ['⬆️', '➡️', '⬇️', '⬅️']
    plot = [''] * N_states
    for s in range(N_states):
        plot[s] = symbols[np.argmax(policy[s, s * N_actions:s * N_actions + N_actions])]

    print(np.reshape(plot, (5, 5)).T)


if __name__ == "__main__":

    env = Grid_World()
    # initial parameters
    gamma = env.gamma
    R = env.R
    P = env.P

    N_states = env.N_states
    N_actions = env.N_actions
    pi_m = env.pi_m

    print(R)
    print(P)
    plot_policy(pi_m)