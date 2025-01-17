
# n: number of discs
# source: source rod
# destination: destination rod
# auxiliary: auxiliary rod
def TowerOfHanoi(n , source, destination, auxiliary):
    # stop case
    if n==1:
        print ("Move disk 1 from ",source,"to ",destination)
        return

    #recursive cases: from source to auxiliary
    TowerOfHanoi(n-1, source, auxiliary, destination)
    #print current status/movement
    print ("Move disk",n,"from ",source,"to ",destination)
    #recursive cases: from auxiliary to destination
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 2
TowerOfHanoi(n,'A','B','C')
