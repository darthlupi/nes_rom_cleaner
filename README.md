# nes_rom_cleaner
Python script to clean up my nes rom collection.

This assumes your roms are in the /pi/home/RetroPi/roms/nes directory and that there is a /pi/home/RetroPi/roms/nes/good_roms
directory to dump to.

The idea is to generate a dictionary based on the games name ( everything before the first '(' in the filename ), and then
only get US or European copies if available. Remove any Hacks or Pirate copies to make the total game list more approachable.
