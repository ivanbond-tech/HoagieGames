# Hoagie Games

A python simulation script to simulate a "Hunger Games" style battle for every neighborhood in Pittsburgh to determine a winner. Data pulled from <a href="https://data.wprdc.org/dataset">WRPDC</a> and more information found in <code>info/rules.txt</code>. This simulation was made for a final project for CMPINF0010 Big Ideas in Computing and Information.

## TODO:
- [x] Movement
- [x] Player and map generation
- [x] Attributes and rules
- [x] Command line arguments
- [ ] Data analysis (still missing information about neighborhood schools, clubs, churches, etc.)
- [ ] Determine player attributes based on data from analysis
- [ ] Attacking - player with higher attributes wins
- [ ] Simulation - currently just picks random neighborhood as winner
- [ ] Run statistical tests to determine if result is conclusive

## Requirements
- <code>pip3 install pandas</code>
- <code>pip3 install numpy</code>

## How to Run
- Actual Simulation: <code>python3 run_sim.py</code>
- Test (Player movement in action): <code>python3 test.py</code>

## Files
- Map class: <code>Map.py</code>
- Players class: <code>Players.py</code>
- Tribute (individual player) class: <code>Tributes.py</code>
- Analysis Data: <code>data/</code>
- Info: <code>info/</code>
  - Rules: <code>info/rules.txt</code>
  - Bonuses: <code>info/bonuses.txt</code>
  - Traps: <code>info/traps.txt</code>
- Map Generated per Simulation: <code>info/map.txt</code>

## Contact
If you are interested in helping work on this project, please email me at ivanbonddev@gmail.com!
