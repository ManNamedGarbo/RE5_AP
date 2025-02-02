Official page on Nexus: https://www.nexusmods.com/residentevil5goldedition/mods/2

Go to https://www.microsoft.com/en-us/download/details.aspx?id=52685 and download "vc_redist.x86.exe" then install it(VC++ 2017 might also work).

LTD Effect Patch: https://drive.google.com/open?id=1FShJXRnDvpaLd2JnjZYR9w1zI167hkfO
Dodge No Hit Sound Patch(Removes the sound when hit by enemies): https://drive.google.com/open?id=1NTw96zw6pF-tWZmxW4bMSX10C3j-3EOX
Core dodge patch(removes blood effects): https://drive.google.com/open?id=16iF4RXWridsNVqpZKHOLYWi_Y6ck5TS0
Animation swap patch(needed to completely swap player animations): https://drive.google.com/open?id=1NE0xMuVzLSRif7fRCrw85rsfiV8njMti

Options, enabled by default:
 - Multiplayer model swap fix: Finally, you can play online with your favorite characters. Every door, elevator, lever will work. 
   ( Fixes the bug when 2nd Player can't complete any partner actions (Doors,levers,elevators, everywhere you need to press "V") )
 - Improved pause menu for Versus mode: Now the host gets to restart, quit or end local coop (in this case, it will pause the game. 
   Other players will still be able to move around, but that’s about it. Select again to unpause.)
 - Camera Fix: Forces the game to load your camera values. (Notice: rarely fails to apply aim values, if it happens, use “Use Normal Camera Values for Aiming” option)
 - Pathfindig fix: Fixes jumping down majinis, crane majini
 - Region lock fix: This should allow you to play with more people
 - End of mission timer soft lock fix: Capcom fixed this in 1.2.0, so this fix is disabled


Characters Tab
 - Check “Freeze x Player” to actually change character
 - Character Swap: Swap default characters to characters you want. (Notice: Female to male or vice-versa swap has game breaking bugs)
 - Ignore Missing Files: Ignore any missing file, necessary for patchless character swap.
 - Fix Cutscenes: Static heads for characters during cutscenes.
 - Character properties:
 - Invincible: Makes your character invincible
 - Freeze Health: Does just that, freezes health.
 - Handedness: Changes your char’s handedness (Check “Freeze” to make it work)
 - Weapon: Changes your char’s weapon animation (Check “Freeze” to make it work)
 - Size/Speed: Change your char’s size or speed, check “Px Freeze Size/Speed” to change. 
   (Notice: Changing size to anything but 100 for a player not controlled by you will cause severe lags, restarting the level and changing the value back to 100 will fix this)
 - Move PLx to PLx: Copy and paste player x cords to another player.
 - Vehicle Health: Freeze or unfreeze your vehicle’s health
 - Gun Turrets: Never overheat
 - Mission 3-2 Timer: Freeze timer in 3-2.
 - Crosshair: Hide or show
 - Laser: Hide or show
 - One Hit Kill: Kill enemies with just one hit (doesn’t work for giant in 2-3, works for your vehicle in 2-3)
 - No Collision: Disable collision (will pull your char back as soon as you’ve disabled it, use “Freeze Z” instead)
 - Hide HUD: Hide it for good
 - Hide map: Hide it (only visible part is hidden, it can still be opened)
 - Hide Inventory: Hide it (only visible part is hidden, it can still be opened)
 - Friendly fire: Kill each other anytime
 - Ammo: Infinite Ammo (Use infinite ammo in “Inventory” section instead)
 - Eggs: Infinite eggs (Use infinite ammo in “Inventory” section instead)
 - Freeze stage: Freeze stage (If you need additional files, extract them using ArcTool)
 - Freeze Checkpoint: Set checkpoint to your liking. Unpredictable when used online
 - Skip cutscenes: Skips most cutscenes, both players should enable it
 - Money: Add or subtract money for story mode
 - DEC/LIN Points: Add or subtract points
 - Exchange Points: Add or subtract points
 - Developer menu: Contains a few advanced features(restarting/pausing/quitting the game by clicking corresponding buttons, changing game speed, disabling auto pause when not focused on the window etc)


Dodge|Melee Tab
 - Melee Swap: Swap default animations to the ones you want
 - Melee Moves Swap: Swap default animations for melee prompts to the ones you want

Dodge:
 - Basic: Only strikes and bullets will be dodged. Install this patch to fix blood effects: https://drive.google.com/open?id=16iF4RXWridsNVqpZKHOLYWi_Y6ck5TS0
 - Full: Everything above, plus grapple attacks. 
 - Dash fire/explosions: Only useful for Wesker or if you’re using “Character Anim Swap”
 - Directional dodge: Dodge in the last direction your character was moving when attacked
 - Successive dodge: Wesker-style dodge, this one has bugs, but stable (male majini sparks, metal sound, boss Wesker can’t be killed). Use “Improved Successive Dodge” 
   instead (Settings Tab).

 - Swap Character Anims: swap default animations for the character of your choice to something different. (Notice: Freezing characters on “Characters Tab” is required) 
   DO NOT USE without the patch: https://drive.google.com/open?id=1NE0xMuVzLSRif7fRCrw85rsfiV8njMti
 - Weapon on back: Removed – completely remove; Placement 1, Placement 2 – change weapon placement
 - Remove handgun: Wesker only – removes handguns from the holster only for Wesker. Everyone – for everyone.
 - Always Show Weapon: Will always show weapons during melee attacks.
 - Infinite Dash: Dash ad infinitum
 - Wesker sunglasses fix: Never lose them
 - Hand tremors fix: No shaky hands anymore
 - Reunion Moves: Unlocks “Mercenaries reunion” moves in any mode. (Note: Use “Swap Character Animations” and set Chris to Reunion, Sheva to Reunion or Josh to Reunion, 
   or swap to a proper character)
 - Fix sound: Silences sounds of enemy attacks, as well as LTD sound effects (if proper patch has been installed) 
   DO NOT USE without this patch: https://drive.google.com/open?id=1NTw96zw6pF-tWZmxW4bMSX10C3j-3EOX
   Works ONLY if applied before level begins or after a restart.
 - Save/Load INI: Save and load melee settings. “Melee Swap” and “Swap Character Anims” must be checked in order to save/load settings.


Speech Tab
 - Use speech anytime. 
 - Speech settings are saved for each character individually, use hotkeys when in game to alternate phrases. 
 - Fast speech: No pauses between phrases.


Camera Tab
 - “Freeze” checkboxes must be checked in order to change values. 
 - Freeze cam 1, Freeze cam 2: Will freeze the camera, suitable for taking screenshots. Option 1 completely freezes the camera, while option 2 still allows for adjustments.
 - Freeze melee camera: Freezes camera during melee, will be automatically disabled on some levels. (Notice: During short in-game cutscenes camera might behave erratically.)
 - Advanced camera: Different camera values for different types of weapons.
 - Use Normal Camera Values for Aiming: The game will ignore aim camera values and use normal camera values instead.
 - Save/Load INI: Save and load camera settings. “Freeze” checkboxes must be checked in order to save/load settings


Inventory Tab
 - Due to the fact that Story/Mercenaries slots and RTE slots differ, Rapid Fire/Infinite Ammo can only be set in “Real Time Editor” mode.
 - Item Box Editor mode: Edit weapons and treasures in story item box. For treasure slots only Mag.Capacity actually works, everything else is ignored, 
   setting anything but treasure to these slots is not recommended.
 - Swap Knife according to character: Knife will be swapped according to your current character (Notice: Changing Slot 10 knife to anything else, 
   even another knife causes the knife to always stay in the sheath, cannot be undone. Also, if swapped to a wrong knife (e.g. Wesker’s knife is given to Chris – 
   knife goes through Chris)
 - Enhanced RPG, Give RPG: give improved RPG with laser sight to a certain player, will occupy Slot 1 or Slot 2.
 - Enhanced LTD, Give LTD: If only “Enhanced LTD” is enabled, you need to set LTD to any slot yourself. If “Give LTD” is also set, selected player will have LTD 
   in the first slot with laser sight. Install this patch to remove the annoying effect: https://drive.google.com/open?id=1FShJXRnDvpaLd2JnjZYR9w1zI167hkfO
 - Save/Load INI: Save and load inventory loadouts. “Freeze” checkboxes must be checked in order to save loadouts. ONLY frozen slots will be saved.
 - Story Items: Set keys, emblems, slates, in other words, story-related items. “Freeze” checkbox needs to be set to actually edit these slots.

Mercenaries | Versus Tab
 - Player x Freeze must be checked to enable editing of any slots.
 - Slots status: X Player current slot status (host, closed)
 - Player Status: X Player current status (ready, not ready)
 - Player Team: Here you can change your or other player’s team.
 - Character: Select a character you want (Notice: Freezing characters on “Characters Tab” will override this)
 - Is AI: Spawn AI controlled player (Notice: Only works if slot status is Closed and “Player x Freeze” is checked)
 - Enable slot: enable slot in case it’s not enabled
 - Single player versus mode: Play the original Versus mode with AI in SP (Notice: At least two players are required (“is AI” checkbox))
 - Versus to 4 Player no mercy: Converts Versus to 4 Player No Mercy Mercenaries, AI can also be spawned.
 - Exchange all items in Story/Mercenaries: Exchange any items between you and your teammate/partner in Story, DLC, Mercenaries or Versus modes. 
   Doesn’t work for AI controlled teammates in Versus mode, hence will be disabled if your teammate is AI.
 - (Warning: If you exchange items with your partner online, you will lose all your upgrades.)
 - Freeze Screen Mode: Edit screen parameters to the ones you like. Auto Picture-in-Picture enables specific fixes to allow the use of sniper rifles, pause screen, 
   inventory and to automagically switch screen section to your current partner. (Notice: Changing screen parameters will lead to instability, use with caution)
 - Unlock all characters: Use if characters in Mercenaries/Versus modes are locked. Should be enabled all the time if that’s the case.
 - No mercy mode: Enables “No Mercy” mode for Mercenaries in Duo mode.
 - Enhanced No Mercy: A hybrid of Reunion, No Mercy Mercenaries and Versus modes. Players can kill up to 700 enemies.
 - Reunion Enhanced No Mercy: A hybrid of Reunion, No Mercy Mercenaries and Versus modes. Players can kill up to 700 enemies.
 - Versus Enhanced No Mercy: A hybrid of Reunion, No Mercy Mercenaries and Versus modes. Players can kill up to 700 enemies.
 - Freeze combo bonus time: Infinite combo bonus 
 - Freeze combo time: Infinite combo time
 - Freeze Timer: freezes timer
 - Freeze Kill Counter: Kill counter will never change
 - Change Mercenaries Time: Add or subtract time
 - Change Kill Counter: Add or subtract count
 - Change Mercenaries Score: Add or subtract score


Enemy Tab
 - Filter: Can be used to target specific enemies. If all 5 boxes are set to “Disable”, this particular filter will be disabled.
 - Set size: Change the size of enemies. Values can be constant or random. (Notice: Some enemies will have trouble jumping over fences 
   if they are too small, use filtering to solve this issue)
 - Set speed: Change the speed of enemies. Values can be constant or random. Settings to 0 will freeze most enemies. (Notice: some enemies – 
   spiders, dogs, lickers won’t be stopped if speed is set to 0, use “Stall enemies” in this case)
 - Kill enemies: Will set the health of enemies to 0. (Notice: Some enemies - bosses, dogs, spiders etc. won’t die if their health is at 0 points. 
   In this case It works similarly to one hit kill, only less buggy.)
 - Freeze health: Will freeze the health of enemies. (Notice: Headshots and explosions will still kill enemies)
 - Move Enemies: Will move enemies to the character who’s currently under your control.
 - Set Health: “Heal” will heal enemies, and “Set” will change min and max health (e.g. the health is 1000/1000, you’ve set it to 100, the health 
   has changed to 100/100). Values can be constant or random.
 - Jill’s device: Displays device’s current health. The health can be set or frozen.
 - Madness: Will trigger berserk state for some enemies.
 - Stall enemies: Will stall selected enemies (change their animations)
 - Do Not Attack: Enemies will not attack selected players, they’ll be gathering around instead.
 - Wesker Boss No Time Limit: Fight Wesker until he runs out of health.
 - Wesker never Gives up: Use it with Enemies never die to prevent him from running away.
 - Enemies never die: Nothing can kill enemies, even headshots.


Settings Tab
 - Don’t freeze magazine ammo for RTE slots: If you wish for the ammo to stay unfrozen, check this.
 - Extended enemy trainer: For mods with increased enemy count (e.g. Nightmare mod). This mode can process up to 150 enemies simultaneously (50 by default). 
   (Notice: enemy display section does not support more than 50 enemies, only cheats (Set health, Kill enemies, Move enemies, Filters, etc) is supported by this mode)
 - Disable Rapid Fire: Will temporarily disable rapid fire for all weapons if you can’t disable it otherwise.
 - Disable Infinite Ammo: Will temporarily disable infinite ammo for all weapons if you can’t disable it otherwise.
 - Never Change Player Size: Use this in conjunction with player size modifier to force the game show the same size when your character is jumping, climbing ladders etc.
 - Freeze Z Coordinate: Will freeze Z coordinate (altitude) for the character controlled by you and/or another Ai controlled character. 
 - Rapid Fire for Turrets: Enable rapid fire for stationary machine guns. (Notice: Use this when your inventory is full, or enable and forget)
 - Excella First Aid Fix: Your game won’t crash if you use her first aid. (Notice: Without this option, this move can only be used in Mercenaries/Reunion/Versus 
   if proper patch has been installed. 
 - Warning: This option changes enemy behavior, making them more prone to attack you.)
 - Improved Successive Dodge: Is an improved version of successive dodge, doesn’t cause any sparks or metal sounds like the original successive dodge 
   implementation and can be enabled for a particular player. (Notice: Even though it’s generally better to use this version, 
   it’s not without drawbacks – when used with “Friendly fire” sometimes produces a bug of its own. If you come very close to another character (touch him), 
   your character might or might not dodge. To fix this, either use the original successive dodge or just reenable dodge and this version of successive dodge. 
   Also might lead to random crashes)
 - RTE Slots: Enable rapid fire and/or infinite ammo for RTE slots 11 and 12. 
 - Not-So-Dying State: Your character won’t die on his own after getting critically injured. In addition, the use of weapons is enabled.
 - TPS (third person shooter) Mode: When this mode is enabled, your character can pick up items, place mines, shoot, reload, heal almost instantly.
 - (Notice: Might lead to random crashes, your character can become stuck(frozen) in cases undefined in the code. If that ever happens, let enemies attack you or restart.)
 - Reset Enh.Merc/Ver Score: The score will be reset as soon as 700 enemies have been killed or time has run out. 
   ONLY Enhanced Mercenaries/Reunion/Versus and Versus No Mercy modes are supported.

 - Dodge Anim Swap: Replace dodge anims with the anims of your choice. WESK(WESKER) checkbox will enable anim swap only for Wesker, other characters will continue to dodge normally.
 - Different Coords: Makes the coordinates more precise, useful for modders. 
 - Pathfinding fix: Improves enemy pathfinding (running in circles, jumping down). 
 - Disable CRC/Steam_ID checks: Allows you to use any save file you find on the internet.
 - Random Finishers: Random finishers in Versus mode.
 - Uncap FPS: Sets max fps to 240, useful for getting more bugs)
 - Dual wielding: Dual wielding capability for characters, see dualwielding.cfg for details
 - Mouse/Mouse Wheel: Allows you to use your mouse wheel to change weapons.
 - Versus unlock: Go to mercenaries to access versus menu...
 - No color filter: Removes green overlay. 2 modes, 2nd mode is preferred over 1st mode)
 - HD-Shadows: Sets the resolution to 4x of the original
 - G to cancel animations: Cancels some animations like reloading, melees etc.)
 - Physics feature: DoA is the preferred option, improves Wesker's coat and other good stuff
 - Hide button prompts: Hide most of the button prompts. Cutscenes are not affected.
 - Saving/Loading Settings: When you’re done playing around, you should save the changes you’ve made. Settings are loaded during trainer startup.