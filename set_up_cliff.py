import numpy as np


class Cliff():
    def __init__(self):
        self.N_states = 48
        self.N_actions = 4
        self.gamma = .95
        self.alpha = .02
        self.terminal_states = np.arange(1,12,dtype='int8')
        # We split the states in blocss
        B1 = 1
        B2 = 12
        B3 = 37
        B4 = 48
        B5 = np.array([25, 13])
        B6 = np.arange(38,48)
        B7 = np.array([36, 24])
        B8 = np.arange(2,12)
        B9 = np.arange(26,36)
        B10 = np.arange(14,24)
        
        # We build all variables
        self.P = np.zeros((self.N_states * self.N_actions, self.N_states))
        self.R = np.zeros((self.N_states * self.N_actions, 1))
        self.pi_rp = np.zeros((self.N_states, self.N_states * self.N_actions))
        self.pi_opt = np.zeros((self.N_states, self.N_states * self.N_actions))
        
        for s in range(self.N_states):
            s
            if (s + 1) == 1:
                self.P[s * self.N_actions - 1 + 1, 13] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, 2] = 1
                self.R[s * self.N_actions - 1 + 2] = -100
                self.P[s * self.N_actions - 1 + 3, 1] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, 1] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([1, 0, 0, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif (s + 1) == 12:
                self.P[s * self.N_actions - 1 + 1, 12] = 1
                self.P[s * self.N_actions - 1 + 2, 12] = 1
                self.P[s * self.N_actions - 1 + 3, 12] = 1
                self.P[s * self.N_actions - 1 + 4, 12] = 1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 0, 1, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif (s + 1) == 37:
                self.P[s * self.N_actions - 1 + 1, s] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s + 1] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, s] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 1, 0, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif (s + 1) == 48:
                self.P[s * self.N_actions - 1 + 1, s] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, s - 1] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 0, 1, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif ((s + 1) in B5):
                self.P[s * self.N_actions - 1 + 1, s + 12] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s + 1] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, s] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 1, 0, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif ((s + 1) in B6):
                self.P[s * self.N_actions - 1 + 1, s] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s + 1] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, s - 1] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 1, 0, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif ((s + 1) in B7):
                self.P[s * self.N_actions - 1 + 1, s + 12] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, s - 1] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 0, 1, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])


            elif ((s + 1) in B8):
                self.P[s * self.N_actions - 1 + 1, s] = 1
                self.R[s * self.N_actions - 1 + 1] = 0
                self.P[s * self.N_actions - 1 + 2, s] = 1
                self.R[s * self.N_actions - 1 + 2] = 0
                self.P[s * self.N_actions - 1 + 3, s] = 1
                self.R[s * self.N_actions - 1 + 3] = 0
                self.P[s * self.N_actions - 1 + 4, s] = 1
                self.R[s * self.N_actions - 1 + 4] = 0
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif ((s + 1) in B9):
                self.P[s * self.N_actions - 1 + 1, s + 12] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s + 1] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -1
                self.P[s * self.N_actions - 1 + 4, s - 1] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 1, 0, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])

            elif ((s + 1) in B10):
                self.P[s * self.N_actions - 1 + 1, s + 12] = 1
                self.R[s * self.N_actions - 1 + 1] = -1
                self.P[s * self.N_actions - 1 + 2, s + 1] = 1
                self.R[s * self.N_actions - 1 + 2] = -1
                self.P[s * self.N_actions - 1 + 3, s - 12] = 1
                self.R[s * self.N_actions - 1 + 3] = -100
                self.P[s * self.N_actions - 1 + 4, s - 1] = 1
                self.R[s * self.N_actions - 1 + 4] = -1
                self.pi_opt[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([0, 1, 0, 0])
                self.pi_rp[s, s * self.N_actions : (s + 1) * self.N_actions] = np.array([.25, .25, .25, .25])
        
        #   self.pi_rp[s,(s-1)*self.N_actions+1:s*self.N_actions]=[.25, .25, .25, .25])
        
        self.v_ini = np.zeros(self.N_states)
        self.q_ini = np.zeros(self.N_states * self.N_actions)



    def plot_policy(self,policy):
        symbols = ['⬆️', '➡️', '⬇️', '⬅️']
        plot = [''] * self.N_states
        for s in range(self.N_states):
            plot[s] = symbols[np.argmax(policy[s, s * self.N_actions : (s+1) * self.N_actions])]

        print(np.reshape(plot, (4, 12))[[3,2,1,0], :])


if __name__ == "__main__":

    env = Cliff()
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


    #print(R)
    #print(P)
    print('pi_rp \n')
    env.plot_policy(pi_rp)
    print('\n pi_opt \n')
    env.plot_policy(pi_opt)
