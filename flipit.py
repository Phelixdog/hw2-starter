import random
import search

class FlipIt(search.Problem):
    """
    STATE: string of size**2 bits
    GOAL: a state with all bits = 0
    PROBLEM:  """

    def __init__(self, size=3, initial=None, goal=None):
        self.size = size
        self.goal = goal or ''.join('0' for _ in range(size**2))
        self.initial = initial if initial else ''.join(random.choice(['0','1']) for _ in range(size**2))
        # add any additional code you need here

    def __repr__(self):
        """ Returns a string representing the object """
        return "FlipIt({},{},{})".format(self.size, self.initial, self.goal)

    def goal_test(self, state):
        """ Returns true if state is a goal state """
        #add your code here
        pass

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        #add your code here
        pass
    
    def actions(self, state):
        """ generates legal actions for state """
        #add your code here
        pass

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        #add your code here
        pass
    
    def path_cost(self, c, state1, action, state2):
        """ Cost of path from start node to state1 assuming cost c to
        get to state1 and doing action to get to state2 """
        #add your code here
        pass
        
# add other functins or data you need below
