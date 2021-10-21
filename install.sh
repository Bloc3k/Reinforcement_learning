#!/bin/bash

echo "...Instaling OpenAI Gym Atari Environment..."

pip install gym
pip install gym[atari]
pip install pyglet

if [ ! -d "./ROMS/" ]; then
  wget http://www.atarimania.com/roms/Roms.rar
  unrar x Roms.rar
  unzip ROMS.zip
  rm Roms.rar
  rm 'HC ROMS.zip'
  rm ROMS.zip
fi

/home/"$USER"/.local/bin/ale-import-roms .



