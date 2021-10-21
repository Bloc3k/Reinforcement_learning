import gym
from gym.utils.play import play

env = gym.make("MsPacmanNoFrameskip-v0")
play(env, zoom=4)
