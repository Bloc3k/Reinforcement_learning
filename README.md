# Instalation

Successfull instalation can be tested by runing `python3 random_agent.py`. Pop-up window should 
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

