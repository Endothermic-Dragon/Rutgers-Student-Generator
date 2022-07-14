# How it works
Everything is run by `main.py`:
- Fetches the list of names and the groups
- Iterates random shuffles
  - For each shuffle, calculates "cost" - how many people in the new group know each other
- Returns minimal-cost group
  - Prints to console
  - Saves to `output_1.txt` or `output_2.txt` (as specified)

`output_1.txt` and `output_2.txt` contains outputs from the program

`student_list.txt` contains the list of all students
- Note the student `Placeholder Student`, which makes sure each group is "filled"

`groups.txt` contains the groups each student has been in
- Note the student `Placeholder Student`, which makes sure each group is "filled"