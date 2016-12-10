WIN_TITLE = "ConnectCztery"
COL = 7
ROW = 6
WIN_X = 700
WIN_Y = 700 * ROW/COL
RADIUS = 3/4 * WIN_X / (2*COL)
BASE = WIN_Y/18 # Height of the part with numbers
background_color = "white"
TL = 4 # Target Length
debug = True
player1 = 0
player2 = 2
v = [0,1,5,20,1000000000]
control=(
    {"manual":True},                            #0
    {"manual":False,"ev":1,"AI":"2dminimax"},   #1
    {"manual":False,"ev":2,"AI":"2dminimax"},   #2
    {"manual":False,"AI":"debug"},              #3
)