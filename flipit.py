import random
import search

class FlipIt(search.Problem):
    """
    A class to represent a flipit problem. Key parameters to init are:
     SIZE: the number of rows and columns in the grid.
     STATE: we represent a state as a string of size**2 characters
      where each chacater is either a 0 or a 1.  The first character
      holds the value of upper left cell of the grid, the second
      character the cell to its right, etc.
     INITIAL: an arbitrary start state.
     GOAL: a state with all bits equal to 0
    """

    def __init__(self, size=3, initial=None, goal=None):
        self.size = size
        self.goal = goal or ''.join('0' for _ in range(size**2))
        self.initial = initial if initial else ''.join(random.choice(['0','1']) for _ in range(size**2))
        # add any additional variables or code you need here
        pass        

    def __repr__(self):
        """ Returns a string representing the class """
        #add your code here
        pass

    def goal_test(self, state):
        """ Returns true if state is a goal state """
        #add your code here
        pass

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        # No need to change this, we won't instaniate the base FlipIt directly
        return 1
    
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

class FlipIt_optimal(FlipIt):
    name = "optimal"
    def h(self, node):
        """ Returns an admissable estimate of cost of shortest path
        from node to a goal """
        #add your code here
        pass

class FlipIt_aggressive(FlipIt):
    name = "aggressive"
    def h(self, node):
        """ a more aggressive, non-admissable estimate of cost of
        shortest path from node to a goal """
        #add your code here
        pass
        
# add other functins or data you need below
