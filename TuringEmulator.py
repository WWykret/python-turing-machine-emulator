import json
import os
from typing import Tuple, List, Union
from sys import argv
import re


def print_machine_state(tape: str, index: int, state: str) -> None:
    cls()
    print(tape)
    print(' ' * index + '^' + ' ' * (len(tape) - index - 1))
    print(f'current state: {state}')


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def load_data_from_machine(machine_data: dict) -> Tuple[str, str, str, int, List[str]]:
    state = machine_data.get('initial')
    empty = machine_data.get('empty')
    tape = empty * 2 + machine_data.get('start') + empty * 2
    index = 2
    final_states = machine_data.get('final')
    return state, empty, tape, index, final_states


def replace_substring(original: str, new_str: str, beg: int, end: Union[int, None]) -> str:
    if end is None:
        end = beg
    return original[:beg] + new_str + original[end + 1:]


def move_left(index: int, tape: str, empty_symbol: str) -> Tuple[int, str]:
    index -= 1
    if index < 0:
        index = 0
        tape = empty_symbol + tape
    return index, tape


def move_right(index: int, tape: str, empty_symbol: str) -> Tuple[int, str]:
    index += 1
    if index >= len(tape):
        tape = tape + empty_symbol
    return index, tape


def loop(machine_data: dict) -> None:
    state, empty, tape, index, final_states = load_data_from_machine(machine_data)

    print_machine_state(tape=tape, index=index, state=state)

    while state not in final_states:
        input()

        move_func = machine_data.get(state).get(tape[index])
        state = move_func[0]
        tape = replace_substring(original=tape, new_str=move_func[1], beg=index, end=index)
        move = move_func[2]
        if move == '<':
            index, tape = move_left(index, tape, empty)
        elif move == '>':
            index, tape = move_right(index, tape, empty)

        print_machine_state(tape=tape, index=index, state=state)


def main():
    try:
        machine_json_path = argv[1]
        if re.search('.*\\.json', machine_json_path) is None:
            print(f'{machine_json_path} is not a valid turing machine path')
            raise IndexError
        with open('machine.json') as machine_file:
            machine = json.load(machine_file)
            loop(machine)
    except IndexError:
        print('Path to turing machine in json form required!')
        print(f'try: py {__file__} turing_machine_path.json')


if __name__ == '__main__':
    main()
