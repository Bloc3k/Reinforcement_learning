# This file consist of definition of Model used for playing Pac-Man game
# in OpenAI Gym Atari environment as a school project.

import os
import gym
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack


class Model:
    """Model for playing Pac-Man in OpenAI Gym Atari environment."""

    env_name = 'MsPacman-v0'

    def __init__(self):
        self.model: A2C = None
        self.env = DummyVecEnv([lambda: gym.make(Model.env_name)])
        self.path: str = './training/'
        self.__saved_model_name = 'pacman'

    def evaluate(self, n_eval_episodes:int=5, render=True):
        """Evaluate trained 'pacman' model in 'training/saved_models/' directory on 'n' episodes.

        :param n_eval_episodes: The number of episodes to be evaluated on, default 5
        :param render: Render mode True (Default) or False
        """
        if self.model is None:
            self.model = self.load()
        print(evaluate_policy(self.model, self.env, n_eval_episodes, render=render))

    def train_new_model(self, n_timesteps: int):
        """Train new model for 'n' timesteps and save it to 'training/saved_models/' directory.
                Will DELETE old one!!!"""
        new_model = A2C('CnnPolicy', self.env, verbose=1)
        new_model.learn(total_timesteps=n_timesteps)
        self.save(new_model)
        del new_model

    def test(self, n_episodes:int=5):
        """Test model on 'n'(default 5) episodes."""
        if self.model is None:
            self.model = self.load()
        env = gym.make(Model.env_name)
        epizodes = n_episodes
        for epizode in range(1, epizodes + 1):
            obs = env.reset()
            done = False
            score = 0
            while not done:
                env.render()
                action, _ = self.model.predict(obs) # Make a move
                obs, reward, done, info = env.step(action)
                score += reward
            print('Epizoda:{} Score:{}'.format(epizode, score))
        env.close()

    def load(self):
        """Try to load 'pacman' model in 'training/saved_models/' directory and store it in object atrtibute self.model."""
        try:
            self.model = A2C.load(os.path.join(self.path, 'saved_models', self.__saved_model_name), self.env)
        except FileNotFoundError:
            raise FileNotFoundError('No such model or file: "pacman" in "saved_models" directory'
                                    '\n\tHave to have zip file with trained model in "training/saved_models" directory')
        return self.model

    def save(self, model_to_save: A2C):
        """Save model to zip file in 'training/saved_models/' directory."""
        return model_to_save.save(os.path.join(self.path, 'saved_models', self.__saved_model_name))
