# Contents

1. [Theory](#reinforcement_learning)
2. [Installation](#installation)
3. [References](#references)

---

# Reinforcement Learning

We have **Policy Network** (PN) that translate *input frames* to *output actions*. Simplest method to train PN is called **Policy Gradients**. The output is set of probabilities for every possible action. By learning, based on reward from environment, probability distribution changes so that model gets bigger reward. So we define what model should do by giving it a reward or penalty based on its actions. 

![Reinforcement Learning, Agent and Environment. | Download ...](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FRoohollah_Amiri%2Fpublication%2F323867253%2Ffigure%2Fdownload%2Ffig2%2FAS%3A606095550738432%401521515848671%2FReinforcement-Learning-Agent-and-Environment.png&f=1&nofb=1)


One of the biggest problem in Reinforcement Learning (RL) is **Credit Assignment Problem** - problem of giving reward. For example in **Sparse Reward Setting/Environments** the reward is given after long period of time or at the end of the episode. Model than has to figure out what action led to the reward. If we give reward after a many actions were taken, model could have difficulties with understanding what exactly let to the reward. For example in balancing games model could balance the stick pretty well but if it make mistake at the end and it get penalty for it, model will think that the entire sequence of actions were bad so it will lower the probability for occurring it again even if the most of the actions were good. The result of this is that the training will take a long time or fail completely in cases where the model has to do a long sequence of actions to get reward. Or model can face the situations of never getting reward if the task to complete is too hard and reward given at completion.

> Stacking the blocks on top of each other with a robotic hand is a pretty hard task (because of sparse reward setting, it wont get any reward if it use random action at beginning and gets reward only for successful stacked block) compare to some tasks with the computer vision. It is because in computer vision we have target label for every *input frame* which let us do very efficient **Gradient Descent** with backpropagation, whereas in RL we have to deal with **Sparse Reward Setting**

Here the **Reward Shaping** comes in. It is the process of manually designing a reward function that guides the policy (model) to desired behavior. One downside is that we now have to create reward function for every new environment in which we want our policy to be trained (that's expensive). It also leads to the **Alignment Problem** where the agent find surprising way to get a lot rewards but not doing at all what we want. And in other cases we don't want to constrain the policy to our perception of the right way of doing things. We might want to give freedom to our policy to explore new possibilities of getting the job done.

In conclusion we could say that it is really hard to train a policy in **sparse rewards** setting so we can use **reward shaping** to resolve it. But we have to be extremely conscious as it is really tricky to design such a reward function.

# Installation

Successful installation can be tested by running `python3 random_agent.py`. Pop-up window should 
appear with agent that takes random actions.

> **Note:** We support only Ubuntu 20.04

## Auto-install

Run `./install.sh` in your project folder.  

> **Note:** Make sure you have **pip**, **unrar**, **unzip** and **cmake** packages installed.   

---
## Manual install

You can also do manual installation:

```
pip install stable-baselines3 gym gym[atari] pyglet
wget http://www.atarimania.com/roms/Roms.rar
```

Extract *Roms.rar* archive

`unrar x Roms.rar` - or any other way

than extract *ROMS.zip*

`unzip ROMS.zip`

and run following command to import ROMs

`/home/<your_user_name>/.local/bin/ale-import-roms .`

# References

[ ]	OpenAI Gym Atari environments, URL: https://gym.openai.com/envs/#atari

[]	OpenAI Gym Documentation, URL: https://gym.openai.com/docs/

[]	Stable-Baselines 3 Documentation, URL: https://stable-baselines3.readthedocs.io/en/master/

[]	Playing Atari with Deep Reinforcement Learning, DeepMinds. URL: https://arxiv.org/pdf/1312.5602v1.pdf

[]	Break-out RL Implementation, GitHub, URL: https://github.com/JackFurby/Breakout

[]	An introduction to Reinforcement Learning, YouTube, URL: https://www.youtube.com/watch?v=JgvyzIkgxF0

[]	PacMan with DQN, URL: https://medium.com/analytics-vidhya/how-to-train-ms-pacman-with-reinforcement-learning-dea714a2365e

[]	Building DQN on Breakout, URL: https://www.datahubbs.com/deepmind-dqn/



