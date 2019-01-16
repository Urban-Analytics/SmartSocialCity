'''Main class for executing'''
from random import randint, random, choice
from copy import deepcopy
from math import log
import tree_01

addw = tree_01.fwrapper(lambda l:l[0]+l[1],2,'add')
subw = tree_01.fwrapper(lambda l: l[0] - l[1], 2, 'subtract')
mulw = tree_01.fwrapper(lambda l:l[0]*l[1],2,'multiply')

class humanplayer:
    def evaluate(self, board):
        # Get my location and the location of the other player
        me = tuple(board[0:2])
        others = [tuple(board[x:x+2]) for x in range(2, len(board)-1, 2)]

        #Display the Board
        for i in range(4):
            for j in range(4):
                if (i, j) == me:
                    print('0', end="")
                elif (i, j) in others:
                    print('X', end="")
                else:
                    print('.', end="")
            print("")
        #Show moves, for reference
        print('Your last move was %d' % board[len(board)-1])
        print(' 0')
        print('2 3')
        print(' 1')
        print('Enter move: ', end="")

        #Return whatever the user enters
        move = int(input())
        return move

def iffunc(l):
    if l[0]>0:
        return l[1]
    else:
        return l[2]


ifw = tree_01.fwrapper(iffunc, 3, 'if')
def isgreater(l):
    if l[0]>l[1]:
        return 1
    else:
        return 0


gtw = tree_01.fwrapper(isgreater, 2, 'isgreater')
flist=[addw, mulw, ifw, gtw, subw]


def makerandomtree(pc, maxdepth = 4, fpr = 0.5, ppr = 0.6):
    if random() < fpr and maxdepth > 0:
        f = choice(flist)
        children = [makerandomtree(pc, maxdepth-1, fpr, ppr)
                    for i in range(f.childcount)]
        return tree_01.node(f, children)
    elif random() < ppr:
        return tree_01.paramnode(randint(0, pc-1))
    else:
        return tree_01.constnode(randint(0, 10))


def exampletree():
    #A tree with 3 nodes and 4 functions, root is IF statement
    return tree_01.node(ifw,[
        tree_01.node(gtw,[tree_01.paramnode(0),tree_01.constnode(3)]),
        tree_01.node(addw,[tree_01.paramnode(1),tree_01.constnode(5)]),
        tree_01.node(subw,[tree_01.paramnode(1),tree_01.constnode(2)]),
                    ]
                )


def hiddenfunction(x, y):
    return x**2+2*y+3*x+5


def buildhiddenset():
    rows = [] #Empty list
    for i in range(200):
        x = randint(0, 40) #x is a random integer between 0 and 40
         #200 iterations
        y = randint(0, 40) #y is a random integer between 0 and 40
        rows.append([x, y, hiddenfunction(x, y)])
    return rows


def scorefunction(tree, s):
    dif = 0
    for data in buildhiddenset():
        v = tree.evaluate([data[0], data[1]])
        dif += abs(v - data[2])
    return dif


'''We check to see if the root is to be mutated, if not then we traverse
    to the children nodes and try again. Either: a node will be mutated, no node
    will be mutated from top to bottom or some nodes will be mutated. this
    all depends on the random() functions output.'''
def mutate(t, pc, probchange=0.5):
    if random() < probchange:
        return makerandomtree(pc)
    else:
        result = deepcopy(t)
        if isinstance(t, tree_01.node):
            result.children = [mutate(c, pc, probchange) for c in t.children]
        return result

'''The crossover function takes in two trees, given a probability if satisfied
    a new tree called result is produced which is a copy of the first tree but
    with the children of tree 2 added to it, so we create a hybrid tree.'''
def crossover(t1, t2, probswap = 0.7, top = 1):
    if random() < probswap and not top:
        return deepcopy(t2)
    else:
        result = deepcopy(t1)
        if isinstance(t1, tree_01.node) and isinstance(t2, tree_01.node):
            result.children = [crossover(c, choice(t2.children), probswap, 0) for
            c in t1.children]
        return result


'''Building the environment'''
def evolve(pc, popsize, rankfunction, maxgen = 500, mutation_rate = 0.1,
    breeding_rate = 0.4, pexp = 0.7, pnew = 0.05):


    def selectindex():
        return int(log(random())/log(pexp))


    population = [makerandomtree(pc) for i in range(popsize)]


    for i in range(maxgen):
        scores = rankfunction(population)
        print(scores[0][0])
        if scores[0][0] == 0:
            break
        newpop = [scores[0][1], scores[1][1]]
        while len(newpop) < popsize:
            if random() > pnew:
                newpop.append(mutate(crossover(scores[selectindex()][1],
                                                scores[selectindex()][1],
                                                probswap = breeding_rate),
                                                pc, probchange = mutation_rate))
            else:
                newpop.append(makerandomtree(pc))
        population = newpop
        scores[0][1].display()
        return scores[0][1]


def getrankfunction(dataset):


    def rankfunction(population):


        scores = [(scorefunction(t, dataset), t) for t in population]
        return scores


    return rankfunction


'''A mini grid game, of a 4 by 4 plane, each player can move in one of four directions
    but is constrained from moving outside the plane, if it does then it loses a point
    to win a game player A must enter the square player B currently occupies or vice versa
    both players a random trees of makerandomtree(i) where i is the depth we want our tree
    to have. The output of the game can be of any 3 outcomes, these are 1, 0 or -1
    if 0 -> player A won, 1 -> player B won or -1 -> tie.'''
def gridgame(p):
    #board size
    max = (3, 3)

    #Remember the last move for each player
    lastmove=[-1, -1]

    #Remember the player's locations
    location = [[randint(0, max[0]), randint(0, max[1])]]

    #Put the second player a sufficient distance from the first
    location.append([(location[0][0] + 2) % 4, (location[0][1] + 2) % 4])

    #Maximum of 50 moves before a tie
    for o in range(50):

        #For each player
        for i in range(2):
            locs = location[i][:] + location[1-i][:]
            locs.append(lastmove[i])
            move = p[i].evaluate(locs) % 4

            #You lose if you mnove the same direction twice in a row
            if lastmove[i] == move: return 1 - i
            lastmove[i] = move
            if move == 0:
                location[i][0] -= 1
                #Board limits
                if location[i][0] < 0: location[i][0] = 0
            if move == 1:
                location[i][0] += 1
                if location[i][0] > max[0]: location[i][0] = max[0]
            if move == 2:
                location[i][1] -= 1
                if location[i][1] < 0: location[i][1] = 0
            if move == 3:
                location[i][1] += 1
                if location[i][1] > max[1]: location[i][1] = max[1]

            #If you have captured the other player, you win
            if location[i] == location[1-i]: return i
    return -1


def tournament(pl):
    #count losses
    losses = [0 for p in pl]

    #Every player plays every other player
    for i in range(len(pl)):
        for j in range(len(pl)):
            if i == j:
                continue

            #Who is the winner?
            winner = gridgame([pl[i], pl[j]])
            #Two points for a loss, one point for a tie
            if winner == 0:
                losses[j] += 2
            elif winner == 1:
                losses[i] += 2
            elif winner == -1:
                losses[i] += 1
                losses[i] += 1
                pass

    #sort and return the results
    z = list(zip(losses, pl))
    for i in range(len(z)):
        print(z[i])
    return z

print("Test tree 1")
test_tree = makerandomtree(2)
test_tree.evaluate([2, 1])
print (test_tree.display())
print("Test tree 2")
test_tree_02 = makerandomtree(2)
test_tree_02.evaluate([5, 3])
print (test_tree_02.display())


print("Mutated tree 2")
mutated_tree_02 = mutate(test_tree_02, 2)
print(mutated_tree_02.display())


print("Crossover of tree 1 and tree 2")
cross = crossover(test_tree, test_tree_02)
print (cross.display())


#Note: if our scorefunction returns 0 then our program is absolutely correct, this is an extremely rare outcome.
print("Result for test_tree_01: " + str(scorefunction(test_tree, buildhiddenset())))
print("Result for test_tree_02: " + str(scorefunction(test_tree_02, buildhiddenset())))


print("Evolved tree:")
rf = getrankfunction(buildhiddenset)
x = evolve(2, 500, rf, mutation_rate = 0.2, breeding_rate = 0.1, pexp = 0.7, pnew = 0.1)
x
print("Competitive grid game between players 1 and 2, two random programs with depth 5")
player_1 = makerandomtree(5)
player_2 = makerandomtree(5)
'''The game will return 0 if player 1 wins, 1 if player 2 wins and finally -1
    in the event of a tie.'''
print(gridgame([player_1, player_2]))

print("Tournament:")

''' You lose the game if you:
        1. Move off the grid or
        2. Move in the same dirction twice.'''

winner = evolve(5, 100, tournament, maxgen=50)
gridgame([winner, tree_01.humanplayer()])
