from cmath import inf
import random
import math
#from turtle import setundobuffer

#from connect383 import streaks


BOT_NAME = "co-lateral" # INSERT NAME FOR YOUR BOT HERE OR IT WILL THROW AN EXCEPTION



class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
  
    rseed = None  # change this to a value if you want consistent random choices

    def __init__(self):
        if self.rseed is None:
            self.rstate = None
        else:
            random.seed(self.rseed)
            self.rstate = random.getstate()

    def get_move(self, state):
        if self.rstate is not None:
            random.setstate(self.rstate)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move.  Very slow and not always smart."""

    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, nstate in state.successors():
            util = self.minimax(nstate)
                    
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, nstate
        return best_move, best_state

    def minimax(self, state):
        if(state.is_full()):         
            return state.utility()           
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf   
        for move, nState in state.successors(): 
                        
            currUtil = self.minimax(nState)
            if ((nextp == 1) and (currUtil > best_util)) or ((nextp == -1) and (currUtil < best_util)):
                best_util = currUtil   
        return best_util

    
        """Determine the minimax utility value of the given state.
        recursively call it self until an end state is reached.
        get the value of that end state
        bubble back up
        Gets called by get_move() to determine the value of each successor state.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the exact minimax utility value of the state
        """
        #
        # Fill this in!
        #
         # Change this line!


class MinimaxLookaheadAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move.
 
    Hint: Consider what you did for MinimaxAgent. What do you need to change to get what you want? 
    """

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        if(self.depth_limit == 0):
            return self.evaluation(state)
        if(self.depth_limit == None):
            self.depth_limit = inf #handle this
        return self.minimax_depth(state, self.depth_limit)


        """Determine the heuristically estimated minimax utility value of the given state.

        Gets called by get_move() to determine the value of successor states.

        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the (possibly estimated) minimax utility value of the state
        """
        #
        # Fill this in!
        #
        return 9  # Change this line!

    def minimax_depth(self, state, depth):
        if(state.is_full()):         
            return state.utility()
        if(depth==0):            
            return self.evaluation(state)           
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf   
        for move, nState in state.successors():           
            currUtil = self.minimax_depth(nState,depth-1)
            if ((nextp == 1) and (currUtil > best_util)) or ((nextp == -1) and (currUtil < best_util)):
                best_util = currUtil   
        return best_util
        

    def evaluation(self, state):
        #the value should be p1-p2 (from the perspective of p1)
        value = state.utility()
        for r in state.get_rows():
            for s in r:
                if(s==0):
                    if(s>=0 and s<len(r)-1):
                        if(r[s+1]==1):
                            value+=1
                        if(r[s+1]==-1):
                            value-=1
                    if(s>0 and s<len(r)):
                        if(r[s+1]==1):
                            value+=1
                        if(r[s+1]==-1):
                            value-=1
        for c in state.get_cols():
            for s in c:
                if(s==0):
                    if(s>=0 and s<len(c)-1):
                        if(r[s+1]==1):
                            value+=1
                        if(r[s+1]==-1):
                            value-=1
                    if(s>0 and s<len(c)):
                        if(r[s+1]==1):
                            value+=1
                        if(r[s+1]==-1):
                            value-=1
        """Estimate the utility value of the game state based on features.

        Gets called by minimax() once the depth limit has been reached.  
        N.B.: This method must run in "constant" time for all states!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heuristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #

        # Note: This cannot be "return state.utility() + c", where c is a constant. 
        return value  # Change this line!


class AltMinimaxLookaheadAgent(MinimaxAgent):
    """Alternative heursitic agent used for testing."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        if(self.depth_limit == 0):
            return self.evaluation(state)
        if(self.depth_limit == None):
            return 0 #handle this
        return self.minimax_depth(state, self.depth_limit)

        """Determine the heuristically estimated minimax utility value of the given state.

        Gets called by get_move() to determine the value of successor states.

        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the (possibly estimated) minimax utility value of the state
        """
    def minimax_depth(self, state, depth):
        if(state.is_full()):         
            return state.utility()
        if(depth==0):            
            return self.evaluation(state)           
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf   
        for move, nState in state.successors():           
            currUtil = self.minimax_depth(nState,depth-1)
            if ((nextp == 1) and (currUtil > best_util)) or ((nextp == -1) and (currUtil < best_util)):
                best_util = currUtil   
        return best_util
        

    def evaluation(self, state):
        #the value should be p1-p2 (from the perspective of p1)
        value = state.utility()
        for r in state.get_rows():
            for s in r:
                if(s==0):
                    if(s>=0 and s<len(r)-1):
                        if(r[s+1]==1):
                            value+=1
                        if(r[s+1]==-1):
                            value-=1
                    if(s>0 and s<len(r)):
                        if(r[s+1]==1):
                            value+=1
                        if(r[s+1]==-1):
                            value-=1
    
        """Estimate the utility value of the game state based on features.

        Gets called by minimax() once the depth limit has been reached.  
        N.B.: This method must run in "constant" time for all states!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heuristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #

        # Note: This cannot be "return state.utility() + c", where c is a constant. 
        return value  # Change this line

class MinimaxPruneAgent(MinimaxAgent):
    """Computer agent that uses minimax with alpha-beta pruning to select the best move.
    
    Hint: Consider what you did for MinimaxAgent.  What do you need to change to prune a
    branch of the state space? 
    """
    def minimax(self, state):
        return self.alphabeta(state, -inf,inf)
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the 
        algorithm should do less work.  You can check this by inspecting the value of the class 
        variable GameState.state_count, which keeps track of how many GameState objects have been 
        created over time.  This agent does not have a depth limit.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to column 1 (we're trading optimality for gradeability here).

        Args: 
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
 

    def alphabeta(self, state,alpha, beta):
        """This is just a helper method for minimax(). Feel free to use it or not."""
        if(state.is_full()):
            return state.utility()
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf  
        a = alpha
        b = beta
        for move, nState in state.successors(): 
            currUtil = self.alphabeta(nState, alpha, beta)
            if(nextp == 1) and (currUtil > alpha):
                alpha = currUtil
            if(nextp == -1) and (currUtil < beta):
                beta = currUtil
            if ((nextp == 1) and (currUtil > best_util)) or ((nextp == -1) and (currUtil < best_util)):
                best_util = currUtil
            if(nextp == 1) and (currUtil > beta):
               #print("pruned beta")
                break
            if(nextp == -1) and (currUtil < alpha):
                #print("pruned alpha")
                break
        return best_util



def get_agent(tag):
    if tag == 'random':
        return RandomAgent()
    elif tag == 'human':
        return HumanAgent()
    elif tag == 'mini':
        return MinimaxAgent()
    elif tag == 'prune':
        return MinimaxPruneAgent()
    elif tag.startswith('look'):
        depth = int(tag[4:])
        return MinimaxLookaheadAgent(depth)
    elif tag.startswith('alt'):
        depth = int(tag[3:])
        return AltMinimaxLookaheadAgent(depth)
    else:
        raise ValueError("bad agent tag: '{}'".format(tag))       
