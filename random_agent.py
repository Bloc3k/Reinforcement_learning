# Python script to run random agent in OpenAI Gym Atari environment.


def random_agent():
    import gym
    from model import Model

    #env = gym.make(environment_name, render_mode='human')
    env = gym.make(Model.env_name)
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
            score += reward
        print('Episode:{} Score:{}'.format(episode, score))
    # print(env.action_space)
    # print(env.observation_space)
    env.close()


if __name__ == "__main__":
    random_agent()
