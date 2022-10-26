* Getting all information from Eagle Library .lbr File

This script is written to see how many symbols, footprints and devices 
are present in an eagle library without the need to open it. I personaly 
am a PCB designer, and to open a library situated else where was a very 
slow task (slow pc) so I decided to automate the task.

** Step 1. 
Parsing xml in eagle library for SYMBOLS and their pins.

** Step 2.
Parsing xml in eagle library for FOOTPRINTS and their THruHoles/SMD.

** Step 3.
Parsing xml in eagle library for DEVICES and their Respective Symbols and Footprints.

** Step 4.
Counted Number of Sym,Foot and dev and Printed it neatly on terminal

** Step 5.
Added Tkinter for Open, Save as, and Prompt

** Step 6.
Processing Many files now available

** Pending.
-Saving in excel still pending
-Getting structured output still pending.



