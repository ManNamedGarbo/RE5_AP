# Resident Evil 5 Guide

## Required Software

- A copy of Resident Evil 5 on Steam
- [The Arc_Rando program](https://github.com/ManNamedGarbo/RE5_Arc_Rando)
- The latest [Resident Evil 5 APWorld](https://github.com/ManNamedGarbo/RE5_AP/releases)
- The latets version of [Archipelago Multiworld Randomizer program](https://archipelago.gg/tutorial/Archipelago/setup/en)

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a YAML file?

You can customize your options by visiting [Resident Evil 5 Options Page](/games/Resident%20Evil%205/player-options). or locally by installing the apworld in your archipelago install, then opening the launcher, and clicking generate templates.

### Connect to the MultiServer

1. Once a game is generated, ask your host for the output json file named after your slot.
2. Place the json file in the same directory as the arc rando program.
3. Place all your arc files from your resident evil 5 install (.\Resident Evil 5\nativePC_MT\Image\Archive) next to the arc rando tool. You can also do the opposite and place the arc rando in that same folder, however it may get very cluttered in that folder.
4. Run arc_rando.py through powershell, give it some time to randomize your files.
5. When complted, it will spit out all the randomized files into the same folder as your arc_rando.py script. Place these back into the RE% install (.\Resident Evil 5\nativePC_MT\Image\Archive)
6. Launch the game!

This is all the steps for now until we have a client to connect to AP itself. I want this to happen as much you however I lack the coding knowledge to make the client AND have it watch and write to dynamic memory. Sorry, maybe in the future someone can help with that.