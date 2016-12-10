WIN_TITLE = "ConnectCztery"
COL = 7
ROW = 6
WIN_X = 700
WIN_Y = 700 * ROW/COL
RADIUS = 3/4 * WIN_X / (2*COL)
BASE = WIN_Y/18 # Height of the part with numbers
background_color = "white"
TL = 4 # Target Length
debug = False
player1 = 1
player2 = 1

v2 = [0.0, 0.8666797479867846, 5.260811256103154, 13.856940843222523, 859238947.6526098]
v1 = [0.0, 1.1618467048970542, 3.592102942571896, 11.897222125087286, 615327169.9169197]

#  evaluate1 leader -> [0.0, 0.8666797479867846, 5.260811256103154, 13.856940843222523, 859238947.6526098]
#  evaluate2 leader?-> [0.0, 1.1618467048970542, 3.592102942571896, 11.897222125087286, 615327169.9169197]
control=(
    {"manual":True},                            #0
    {"manual":False,"ev":1,"AI":"2dminimax"},   #1
    {"manual":False,"ev":2,"AI":"2dminimax"},   #2
    {"manual":False,"AI":"debug"},              #3
)