# Instalation

Suported only Ubuntu 20.04  
Successfull instalation can be tested by runing `python3 random_agent.py`. Pop-up window should 
appear with agent that takes random actions.

## Autoinstall

Make sure you have **pip**, **unrar** and **unzip** packages installed.  
If you want to play on your own. You also need **pygame** and **matplotlib** python modules.  
Than run `./install.sh` in your project folder to autoinstall.  

## Manual install

You can also do manual installation:

```

pip install gym gym[atari] pyglet
wget http://www.atarimania.com/roms/Roms.rar

```

Extract *Roms.rar* archive

`unrar x Roms.rar` - or any other way

than extract *ROMS.zip*

`unzip ROMS.zip`

and run following command to import ROMs

`/home/<your_user_name>/.local/bin/ale-import-roms .`

