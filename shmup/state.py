#
# State Machine and State functions
# Structure - Make State
from typing import List


class State:
    """
    General State class to utilize in a state machine
    has constructor, __repr__, and run
    run will hide looping functions, and when finished will return value of state, **kwargs
    Put Code implimentation in Run!
    """

    def __init__(self, **kwargs):
        """Creates the intitial state"""
        pass

    def run(self) -> list:
        """
        :return: dictionary of next state and args
        """
        pass


class StateMachine:
    """
    Semi StateMachine
    Contains States: String dict, start_state str and final state *str
    Unlike a normal state machine, uses states internal logic to get next input; cannot imput command str in advance
    Only runs ONE final state object - Use only for ending game, error collection, fatal handling
    """

    def __init__(self, states: dict, start_state: str, finals: List[str]):
        """
        Creates new StateMachine object at starting element start_state
        Will start at start_state, and loop through states internal code until executing one final state

        :param states: dict of str: State type objects
        :param start_state: str of initial starting state
        :param finals: set of final states - when reached will be executed and exit
        :param kwargs: optional key word args to be passed to first state
        """
        self.states: dict = states
        self.finals: list = finals
        self.start_state = start_state
        self.current_state: State = None
        self.new_state_id: str = None
        return

    def run(self, **init_kwargs):
        """
        Starts with first state
        :param init_kwargs: Initial Kwargs to be passed to first state
        :return:
        """
        self.current_state = self.states[self.start_state](**init_kwargs)  # Makes new State Object
        while True:
            self.new_state_id, new_kwargs = self.current_state.run()  # Returns (Str, Dict)
            if self.new_state_id in self.finals:
                self.current_state = self.states[self.new_state_id](**new_kwargs)
                self.current_state.run()
                return
            else:
                self.current_state = self.states[self.new_state_id](**new_kwargs)


# Test code
if __name__ == "__main__":
    class GenieState(State):
        def __init__(self, name):
            self.name = name

        def run(self):
            print("New State! Magic Name is " + self.name)
            new_name = input("Enter name for end state: ")
            if new_name == self.name:
                return "End", dict()
            else:
                print("Wrong name, but you have set the magic name for my next incarnation")
                return "Genie", {"name": new_name}


    class EndState(State):
        def run(self):
            print("The End is Upon us!")
            return


    machine = StateMachine(
        {"Genie": GenieState,
         "End": EndState},
        start_state="Genie",
        finals=["End"],
    )
    machine.run(
        name="Ajraaneh")
