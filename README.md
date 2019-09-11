# Classic Reinforcement Learning Exercises

My interest in **Reinforcement Learning** started around  2016 with an [Andrej Karpathy blog](https://karpathy.github.io/2016/05/31/rl/) from which I did not understand a line further past the title and from the announcement of Deepmind that they were going to [start working on StarCraft](https://deepmind.com/blog/article/alphastar-mastering-real-time-strategy-game-starcraft-ii) as a environment after defeating the Go champion. It looked exciting because you **didn't need training data**, you could **see agents actually learning** and it was being **used on video games** (something much closer to me than industrial processes).


It was nice seeing that they worked, but I had no idea why. So I went for the theory behind it, and it turns out **Reinforcement Learning was something much older than I thought it was.** There was some previous work in the areas of **optimal control, game theory and economics**, but the novelty of the recent interest in RL was that they used **Neural Networks to solve some dimensionality problems** that RL always faced. Before using NN's it was studied with tabular function approximations or linear approximations, and there were a lot of important concepts upon which the theory is building nowadays.


First I tried to follow the [David Silver video course](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-) in which he talked about *Markov Decision Processes, Dynamic Programming, Bellman Equations, Bootstraping...* But I still didn't get it. And as that omnipresent Feynman quote ***"What I cannot create, I do not understand"*** , so I had to work on it to understand it.  At that time I had the subject of Reinforcement Learning in the master and it had Matlab assignments for the different chapters but I agreed with the teacher that I could do them in Python. To do them I followed the theory of the course, which is the same as in the [book by Sutton and Barto](http://incompleteideas.net/book/bookdraft2017nov5.pdf) and to get some intuition on the implementation I followed this [blog by M. Pattachiola](https://mpatacchiola.github.io/blog/2016/12/09/dissecting-reinforcement-learning.html). One great use case of these tabular techniques is a [SARSA-bot](https://www.youtube.com/watch?v=pRjAfs4bJDI) used for Starcraft minigames (a usual testbed for RL algorithms) where the machine learned to defeat enemy units.


**Exercises**

- [2.1 Multiarmed Bandits](https://github.com/itsTAMART/ClassicRL/blob/master/2.1%20Multiarmed%20Bandits.ipynb) 
- [3.2 Markov Processes](https://github.com/itsTAMART/ClassicRL/blob/master/3.2%20Markov%20Processes.ipynb) 
- [3.3 Markov Decision Processes - V and q](https://github.com/itsTAMART/ClassicRL/blob/master/3.3%20Markov%20Decision%20Processes%20-%20V%20and%20q.ipynb)
- [3.4 Markov Decision Processes - V](https://github.com/itsTAMART/ClassicRL/blob/master/3.4%20Markov%20Decision%20Processes%20-%20V.ipynb)
- [3.5 Markov Decision Processes - evaluating policies](https://github.com/itsTAMART/ClassicRL/blob/master/3.5%20Markov%20Decision%20Processes%20-%20evaluating%20policies.ipynb)
- [4.1 Policy Evaluation](https://github.com/itsTAMART/ClassicRL/blob/master/4.1%20Policy%20Evaluation%20.ipynb)
- [4.2 Policy Iteration from V and q](https://github.com/itsTAMART/ClassicRL/blob/master/4.1%20Policy%20Evaluation%20.ipynb)
- [4.3 Value Iteration for V and q](https://github.com/itsTAMART/ClassicRL/blob/master/4.3%20Value%20Iteration%20for%20V%20and%20q.ipynb)
- [4.4 GridWorld Problem](https://github.com/itsTAMART/ClassicRL/blob/master/4.4%20GridWorld%20Problem.ipynb)
- [5.1 Monte Carlo Policy Evaluation - Every Visit](https://github.com/itsTAMART/ClassicRL/blob/master/5.1%20Monte%20Carlo%20Policy%20Evaluation%20-%20Every%20Visit.ipynb)
- [5.2 MonteCarlo policy evaluation - First Visit and Importance Sampling](https://github.com/itsTAMART/ClassicRL/blob/master/5.2%20MonteCarlo%20policy%20evaluation%20-%20First%20Visit%20and%20Importance%20Sampling.ipynb)
- [5.3 Temporal Difference vs MC](https://github.com/itsTAMART/ClassicRL/blob/master/5.3%20Temporal%20Difference%20vs%20MC.ipynb)
- [5.4 SARSA and Q-Learning](https://github.com/itsTAMART/ClassicRL/blob/master/5.4%20SARSA%20and%20Q-Learning.ipynb)
- [5.5 Cliff Walking Problem with SARSA](https://github.com/itsTAMART/ClassicRL/blob/master/5.5%20Cliff%20Walking%20Problem%20with%20SARSA.ipynb)
- [7.1 Cartpole](https://github.com/itsTAMART/ClassicRL/blob/master/7.1%20Cartpole.ipynb)
- [7.2 Mountain Cart](https://github.com/itsTAMART/ClassicRL/blob/master/7.2%20Mountain%20Cart.ipynb)


**Helper Scripts**

- set_up_cliff.py
- set_up_grid_world.py
- set_up_random_walk.py
