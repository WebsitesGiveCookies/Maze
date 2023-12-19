#if you have a problem activating the Virtual environment:
#run the following comment: 
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#used to activate the VMaze:
#.\VMaze\Scripts\activate
from mazepy import mazepy

grid = mazepy.Grid(10,10)
grid = mazepy.getRandomMaze(grid)
file = open("./maze.txt", "w")
file.write("Madalina \n" + (str(grid)))
file.close()
#edit with git
