import gym

environment_name = 'MsPacman-v0'
env = gym.make(environment_name)
observation = env.reset()

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0
    while not done:
        env.render()
        # ------ Take random action  --------
        action = env.action_space.sample()
        # -----------------------------------

        observation, reward, done, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))
env.close()


