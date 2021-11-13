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
        self.path: str = './training/'
        self.__saved_model_name = 'pacman'

    def train(self, n_timestep: int):
        """Train new model if none exists in 'training/saved_models/' directory.
        Otherwise train for aditional 'timesteps' already existing model.

        :param n_timestep: The number of timesteps to train
        """
        if os.path.exists(self.path + 'saved_models/' + self.__saved_model_name):
            env = make_atari_env(Model.env_name, n_envs=4, seed=0)
            env = VecFrameStack(env, n_stack=4)
            self.model.learn(total_timesteps=n_timestep)
            self.save(self.model)
            del model
            env.close()
        else:
            self._train_new_model(n_timestep)


    def _train_new_model(self, n_timesteps: int):
        """Train new model for 'n' timesteps in parallel and save it to 'training/saved_models/' directory.
                Will DELETE old one!!!

        :param n_timesteps: The number of timesteps to train
        """
        env = make_atari_env(Model.env_name, n_envs=4, seed=0)
        env = VecFrameStack(env, n_stack=4)
        new_model = A2C('CnnPolicy', env, verbose=1)
        new_model.learn(total_timesteps=n_timesteps)
        self.save(new_model)
        env.close()
        del new_model

    def evaluate(self, n_eval_episodes:int=5, render=True):
        """Evaluate trained 'pacman' model in 'training/saved_models/' directory on 'n' episodes.

        :param n_eval_episodes: The number of episodes to be evaluated on, default 5
        :param render: Render mode True (Default) or False
        """
        if self.model is None:
            self.model = self.load()
        env = make_atari_env(Model.env_name, n_envs=1, seed=0)
        env = VecFrameStack(env, n_stack=4)
        p = evaluate_policy(self.model, env, n_eval_episodes=n_eval_episodes, render=render,
                            return_episode_rewards=True)
        print(p)
        with open(self.path + "evaluated_scores.txt", "a") as f:
            f.write(str(p) + '\n')
        env.close()

    def test(self, n_episodes:int=5):
        """Test model on 'n'(default 5) episodes.

        :param n_episodes: The number of episodes used for testing
        """
        if self.model is None:
            self.model = self.load()
        env = make_atari_env(Model.env_name, n_envs=1, seed=0)
        env = VecFrameStack(env, n_stack=4)
        epizodes = n_episodes
        for epizode in range(1, epizodes + 1):
            obs = env.reset()
            done = False
            score = 0
            while not done:
                env.render()
                action, _ = self.model.predict(obs)
                obs, reward, done, info = env.step(action)
                score += reward
            print('Epizoda:{} Score:{}'.format(epizode, score))
        env.close()

    def load(self):
        """Try to load 'pacman' model in 'training/saved_models/' directory and store it in object atrtibute self.model."""
        env = make_atari_env(Model.env_name, n_envs=1, seed=0)
        env = VecFrameStack(env, n_stack=4)
        try:
            self.model = A2C.load(os.path.join(self.path, 'saved_models', self.__saved_model_name), env)
        except FileNotFoundError:
            raise FileNotFoundError(f'No such model or file exists: {self.__saved_model_name} in {self.path}saved_models/ directory'
                                    f'\n\tHave to have zip file with trained model in {self.path}saved_models/ directory.')
        finally:
            env.close()
        return self.model

    def save(self, model: A2C):
        """Save model to zip file in 'training/saved_models/' directory."""
        return model.save(os.path.join(self.path, 'saved_models', self.__saved_model_name))
