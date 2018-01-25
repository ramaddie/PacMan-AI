# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    openlist = Stack()

    #push tuple of state, action, and cost to openlist
    state = problem.getStartState()
    openlist.push((state, [], 0))

    #pop top off and add to closed list
    state, totalpath, totalcost = openlist.pop()
    closedlist = [state]
    isEmpty = False #set to false initially so that we can enter loop

    #While not at goal state and openlist is not empty
    while ((not problem.isGoalState(state)) & (not isEmpty)):
        #grab successors of current state
        successors = problem.getSuccessors(state)

        # for each successor of current
        for succ, action, cost in successors:
            # if we havent visted before, add to openlist with updated path and cost
            if (not succ in closedlist):
                openlist.push((succ, totalpath + [action], totalcost + cost))

        #if openlist is empty, we've exhausted search
        isEmpty = openlist.isEmpty()
        #pop off next top of stack, uodate variables
        state, totalpath, totalcost = openlist.pop()
        #visit top and repeat search
        closedlist.append(state)

    return totalpath


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    #same as DFS but implemented with Queue instead
    from util import Queue
    openlist = Queue()

    #push start state, action, and cost to openlist
    state = problem.getStartState()
    openlist.push((state, [], 0))

    #pop top off and add to closed list
    state, totalpath, totalcost = openlist.pop()
    closedlist = [state]
    isEmpty = False #set to false initially so that we can enter loop

    #While not at goal state & not empty, search
    while ((not problem.isGoalState(state)) & (not isEmpty)):
        #grab successors of current
        successors = problem.getSuccessors(state)

        #for each successor of current, if not visited,
        for succ, action, cost in successors:
            #add to open list and visit it immediately cause we visit by level in BFS
            if (not succ in closedlist):
                openlist.push((succ, totalpath + [action], totalcost + cost))
                closedlist.append(succ)

        isEmpty = openlist.isEmpty()
        state, totalpath, totalcost = openlist.pop()
        #repeat

    return totalpath


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    #Basic search with low cost as priority for deciding what to visit! Use PQ
    from util import PriorityQueue
    openlist = PriorityQueue()

    #push start state, action, and cost to openlist
    state = problem.getStartState()
    tup = (state, [], 0)
    openlist.push(tup, 0) #initially no cost

    state, totalpath, c = openlist.pop()
    closedlist = [(state, 0)] #has cost already factored in
    isEmpty = False

    #while not at goal state & not empty 
    while ((not problem.isGoalState(state)) & (not isEmpty)):
        successors = problem.getSuccessors(state)

        #for each successor 
        for succ, action, cost in successors:
            #set the boolean seen to false which will help decide
            #if we should visit it or not later
            seen = False

            #get total cost of path using the successor
            pathCost = problem.getCostOfActions(totalpath + [action])

            #iterate through closedlist 
            #this bascially updates path if we have shortcuts
            for i in range(len(closedlist)):
                
                tempState, tempCost = closedlist[i]
                
                if (pathCost >= tempCost) and (succ == tempState):
                    #if the max cost > tempCost, change boolean to seen!
                    seen = True
                    
            #if we have not already seen it, then we can visit
            if (not seen):
                openlist.push((succ, totalpath + [action], pathCost), pathCost)
                closedlist.append((succ, pathCost))

        #pop in order of least cost since it is a PQ
        isEmpty = openlist.isEmpty()
        state, totalpath, c = openlist.pop()

    return  totalpath


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    #Same as uniform cost search with a little difference f+h to consider
    from util import PriorityQueue
    openlist = PriorityQueue()

    #push start state, action, and cost to openlist
    state = problem.getStartState()
    tup = (state, [], 0)
    openlist.push(tup, 0) #f+h where h is initially 0

    state, totalpath, c = openlist.pop()
    closedlist = [(state, 0)] #has cost already factored (dont include h)
    isEmpty = False

    #while not at goal state, get successor list 
    while ((not problem.isGoalState(state)) & (not isEmpty)):
        successors = problem.getSuccessors(state)
        
        for succ, action, cost in successors:
            #set a boolean to false which will help decide
            #if we should visit it or not
            seen = False

            #get total cost of path using the successor
            pathCost = problem.getCostOfActions(totalpath + [action])

            #iterate through closedlist
            for i in range(len(closedlist)):

                #checking visited list
                tempState, tempCost = closedlist[i]

                #change to seen is pathC > what we have currently
                if (pathCost >= tempCost) and (succ == tempState):
                    seen = True
                    
            #if it is a good choice, then we can visit
            if (not seen):
               
                #factor in heuristic to help prioritize openlist
                h = pathCost + heuristic(succ, problem)

                #update openlist with succ 
                openlist.push((succ, totalpath + [action], pathCost), h)

                #visit the next least cost node
                closedlist.append((succ, pathCost))
                
        #pop in order of least cost and repeat while not empty
        isEmpty = openlist.isEmpty()
        state, totalpath, c = openlist.pop()
        
    return  totalpath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
