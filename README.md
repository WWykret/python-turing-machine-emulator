## Turing Machine Emulator
This console script can emulate any single tape turing machine given in JSON format (details below).

##Usage
To emulate machine given in JSON format
```
py TuringEmulator.py turing_machine_in_json_form.json
```
Installation of some packages via pip may be required
## Turing Machine JSON
Example machine that clears tape that has a sequence of 0s and 1s
```json
{
  "initial": "state_0",
  "final": ["final_state"],
  "empty": "#",
  "start": "10101010101010",
  "state_0": {
    "0": ["state_0", "#", ">"],
    "1": ["state_0", "#", ">"],
    "#": ["final_state", "#", "-"]
  }
}
```
where
* `initial` is the initial state of turing machine
* `final` is set of final states
* `empty` is a default empty tape symbol
* `start` is starting tape content (the machine begins at the start of this string)

Possible movements for machine are `<`, `>` and `-`.

For more complex turing machine example check `examples` directory.
