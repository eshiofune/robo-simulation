class State:
    '''
    Possible states
    '''
    WITH_BALL = 0
    LOOKING_FOR_BALL = 1
    LOOKING_FOR_POST = 2
    POST_FOUND = 3
    BALL_FOUND = 4

    @staticmethod
    def has_state(state_arr, state):
        '''
        Returns True if the state array has value 1 for the specified state, otherwise False.
        '''
        return state_arr[state] == 1


class Environment:
    '''
    Simulation environment.
    '''
    INITIAL = [0, 0, 0, 0, 0]

    def reset(self):
        '''
        Resets the environment to its default state and returns this state.
        '''
        return Environment.INITIAL

    def select_action(self, current_state_arr):
        '''
        Acts on the current state and decides on which state should be next.
        '''
        return next_state_arr, reward, done
