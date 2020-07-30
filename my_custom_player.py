
from sample_players import DataPlayer


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        import time
        #I am using the alpha beta algorithm to calculate the best move
        alpha = float("-inf")
        beta = float("inf")
        best =  float("-inf")
        besta = None
        depth = 3
        v = 1
        print(state.actions(),"acts")
        for a in state.actions():
            print("HRO")
            v  = self.min_v(state.result(a), depth, alpha, beta)
            alpha = max(alpha, v)
            print(v,"v")
            print(a,"a")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            print("____________________")
            if v > best:
                best = v
                besta = a
        print(besta,"besta")
        self.queue.put(besta)
        print("OOOT")

    def min_v(self, state, depth, alpha, beta):
        if state.terminal_test():
            print(state.utility(0),"ia")
            return state.utility(0)
        if depth == 0:
            print(len(state.liberties(state.locs[0])),"di")
            return len(state.liberties(state.locs[0]))
        v = float("inf")
        for a in state.actions():
            v = min(v, self.max_v(state.result(a), depth-1, alpha, beta))
            if v <= alpha:
                print(v,"MOOOM")
                return v
            beta = min(beta, v)
        print(v,"ji")
        return v

    def max_v(self, state, depth, alpha, beta):
        if state.terminal_test():
            print(state.utility(0), "aa")
            return state.utility(0)
        if depth == 0:
            print(len(state.liberties(state.locs[0])),"da")
            return len(state.liberties(state.locs[0]))
        v = float("-inf")
        for a in state.actions():
            v = max(v, self.min_v(state.result(a), depth-1, alpha,  beta))
            if v >= beta:
                print(v,"WOOOOW")
                return v
            alpha = max(alpha, v)
        print(v,"ja")
        return v










