#!/bin/bash

echo "...Instaling OpenAI Gym Atari Environment..."

pip install stable-baselines3
pip install gym
pip install gym[atari]
pip install pyglet
pip install pygame
pip install matplotlib

if [ ! -d "./ROMS/" ]; then
  wget http://www.atarimania.com/roms/Roms.rar
  unrar x Roms.rar
  unzip ROMS.zip
  rm Roms.rar
  rm 'HC ROMS.zip'
  rm ROMS.zip
fi

mkdir "training"
mkdir "./training/saved_models"

/home/"$USER"/.local/bin/ale-import-roms .



