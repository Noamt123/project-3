
from sample_players import DataPlayer
from isolation import DebugState

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
        if state.ply_count < 4:
            A = random.choice(state.actions())
            self.queue.put(A) #used as opening book for run match.py but not part of project
            #self.queue.put(A) #used for unittest

        else:
            if self.context == None:
                print(state.locs[0],", 1 | 2 ,", state.locs[1])
                self.context = 0
            Action = None
            depth_l = 7
            """for depth in range(1, depth_l+1):
                Action = self.alpha_beta_algorithm(state, depth, self.player_id)"""
            """print('In get_action(), state received:')
            debug_board = DebugState.from_state(state)
            print(debug_board)"""
            sc = float("-inf")
            for depth in range(1, depth_l+1):
                for a in state.actions():
                    ba = self.principle_v(state.result(a), depth, float("-inf"), float("inf"), 1, self.player_id)
                    if sc <= ba:
                        sc = ba
                        Action = a
            self.queue.put(Action)
        return 0



    def alpha_beta_algorithm(self, state, depth, player):
        alpha = float("-inf")
        beta = float("inf")
        best =  float("-inf")
        besta = None
        v = 1
        #print(state.actions(),"acts")
        for a in state.actions():
            #print("HRO")
            v  = self.min_v(state.result(a), depth, alpha, beta, player)
            alpha = max(alpha, v)
            """print(v,"v")
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
            print("____________________")"""
            if v >= best:
                best = v
                besta = a
        #print(besta,"besta")
        return besta

    def min_v(self, state, depth, alpha, beta, player):
        if state.terminal_test():           
            #print(state.utility(player),"ia"):
            return state.utility(player)
        elif depth == 0:
            #print(len(state.liberties(state.locs[player])),"di")
            i = 0
            if player == 0:
                i = 1
            #nex =0
            #p1 = state.liberties(state.locs[player])
            #p2 = state.liberties(state.locs[i])
            """for a in p1:
                nex += len(state.liberties(a))
            for b in p2:
                nex -= len(state.liberties(b))"""
            return len(state.liberties(state.locs[player]))**2 - len(state.liberties(state.locs[i]))**1.5
        v = float("inf")
        for a in state.actions():
            v = min(v, self.max_v(state.result(a), depth-1, alpha, beta, player))
            if v <= alpha:
                #print(v,"MOOOM")
                return v
            beta = min(beta, v)
        #print(v,"ji")
        return v

    def max_v(self, state, depth, alpha, beta, player):
        if state.terminal_test():
            #print(state.utility(player), "aa")
            return state.utility(player)
        elif depth == 0:
            #print(len(state.liberties(state.locs[player])),"da")
            i = 0
            if player == 0:
                i = 1
            #p1 = state.liberties(state.locs[player])
            #p2 = state.liberties(state.locs[i])
            #nex = 0
            """for a in p1:
                nex += len(state.liberties(a))
            for b in p2:
                nex -= len(state.liberties(b))"""
            return (len(state.liberties(state.locs[player]))) - (len(state.liberties(state.locs[i])))
        v = float("-inf")
        for a in state.actions():
            v = max(v, self.min_v(state.result(a), depth-1, alpha,  beta, player))
            if v >= beta:
                #print(v,"WOOOOW")
                return v
            alpha = max(alpha, v)
        #print(v,"ja")
        return v

    def principle_v(self, state, depth, alpha, beta, mult, player):
        if state.terminal_test():
            return state.utility(player)
        elif depth == 0:
            i = 0
            if player == 0:
                i = 1
            return mult * len(state.liberties(state.locs[player])) - len(state.liberties(state.locs[i]))
        x = 0
        score = 0
        for a in state.actions():
            if x == 1:
                score = -self.principle_v(state.result(a), depth-1, -alpha-1, -alpha,-mult, player)
                if alpha < score and score < beta:
                    score = -self.principle_v(state.result(a), depth-1, -beta, -score, -mult, player)
            else:
                score = -self.principle_v(state.result(a), depth-1, -beta, -alpha, -mult, player)
                x += 1
            alpha = max(a, score)
            if alpha >= beta:
                break
        return alpha








