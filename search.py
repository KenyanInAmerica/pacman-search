# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Randy Osoti

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    fringe = util.Stack()
    fringe.push((problem.getStartState(), []))
    explored = []

    while True:
        if fringe.isEmpty():
            return []
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        explored.append(node[0])
        for successor in problem.getSuccessors(node[0]):
            coordinate = successor[0]
            if coordinate not in explored and coordinate not in fringe.list:
                path = node[1] + [successor[1]]
                fringe.push((coordinate, path))

    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))
    explored = []

    while True:
        if fringe.isEmpty():
            return []
        node = fringe.pop()
        explored.append(node[0])
        for successor in problem.getSuccessors(node[0]):
            inFringe = False
            for element in fringe.list:
                if successor[0][0] is element[0][0] and successor[0][1] is element[0][1]:
                    inFringe = True
            coordinates = successor[0]
            if coordinates not in explored and not inFringe:
                if problem.isGoalState(coordinates):
                    return node[1] + [successor[1]]
                path = node[1] + [successor[1]]
                fringe.push((coordinates, path))

    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    start_node = (problem.getStartState(), 0)
    coordinates = start_node[0]
    cost = start_node[1]
    path = []

    fringe = util.PriorityQueue()
    fringe.push((coordinates, path, 0), 0)
    explored = []

    while True:
        if fringe.isEmpty():
            return []
        node = fringe.pop()
        coordinates = node[0]
        path = node[1]
        cost = node[2]
        if problem.isGoalState(coordinates):
            return path
        explored.append(coordinates)
        for successor in problem.getSuccessors(coordinates):
            successorCoordinates = successor[0]
            successorPath = successor[1]
            successorCost = successor[2]
            if successorCoordinates not in explored and successorCoordinates not in fringe.heap:
                fringe.push((successorCoordinates, path + [successorPath], cost + successorCost), cost + successorCost)

    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    start_node = (problem.getStartState(), 0)
    coordinates = start_node[0]
    cost = start_node[1]
    path = []

    fringe = util.PriorityQueue()
    fringe.push((coordinates, path, 0), 0)
    explored = []

    while True:
        if fringe.isEmpty():
            return []
        node = fringe.pop()
        coordinates = node[0]
        path = node[1]
        cost = node[2]
        if problem.isGoalState(coordinates):
            return path
        explored.append(coordinates)
        for successor in problem.getSuccessors(coordinates):
            successorCoordinates = successor[0]
            successorPath = successor[1]
            successorCost = successor[2]
            if successorCoordinates not in explored and successorCoordinates not in fringe.heap:
                fringe.push((successorCoordinates, path + [successorPath], cost + successorCost), cost + successorCost + heuristic(successorCoordinates, problem))

    return None

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
