# Python script to give player control over OpenAI Gym Atari environment.

def play():
    import gym
    from gym.utils.play import play

    env = gym.make("MsPacmanNoFrameskip-v0")
    play(env, zoom=4)


if __name__ == "__main__":
    play()
