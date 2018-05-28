# The project 6: Quadcopter
This is the final project of deep learning nanodegree to manipulate a quadcopter.
What you have to do is three-fold
1. define an algorithm to manipulate a quadcopter
2. define a task to guide the quadcopter such as takeoff,guiding, hovering, and landing.
3. define a reward function

I tried to do landing. Guide a quadcopeter to [0,0,0] from [0,0,10].
I thought three penalizing factors in the task.
1. penalizing distance between the target and the current position
2. penalizing orientation of the quadcopter in the x,y axes
3. penalizing velocity of the quadcopter in velocies of x and y velocities.

No. Episodes: 500

Best landing: 

- First 50 mean reward = -0.137262002995
- Mid 50 mean reward = 1.83526543088
- Last 50 mean reward = 2.6936476944


- First 50 mean distance = 53.7832225683
- Mid 50 mean distance = 2.38841290356
- Last 50 mean distance = 0.772107723791

I also used Deep Deterministic Policy Gradient (DDPG) as suggested from the project.
[Introduction to Various Reinforcement Learning Algorithms. Part I (Q-Learning, SARSA, DQN, DDPG)](https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-i-q-learning-sarsa-dqn-ddpg-72a5e0cb6287)

I hope you can give me any comments.
