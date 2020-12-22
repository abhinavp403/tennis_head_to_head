# tennis_head_to_head

Data provided courtesy of https://github.com/JeffSackmann/tennis_atp, https://github.com/JeffSackmann/tennis_wta

Script written in Python which determines head to head tennis stats between players involved in the ATP (men) and WTA circuits (women).

Stats include- matches won, sets won, games won, break points won, clean sets (without losing a single game ex. 6-0), straight sets (without losing a single set ex 6-1 6-2 for best of 3), aces, double faults.

Future plan is to make an Android app out of this script. The results of this script helps in betting and is designed to help players in drafting players in Draft King tennis tournaments. 
I personally would spend an hour doing tons of research to find head to head stats. But now I can get these stats within a minute.

Example of run:
Entry 1- Novak Djokovic
Entry 2- Rafael Nadal
Output-
Novak Djokovic {'matches-won': 29, 'sets-won': 77, 'games-won': 733, 'breakpts-won': 176, 'clean-sets': 0, 'straight-sets': 22, 'aces': 278, 'doublefaults': 87}
Rafael Nadal {'matches-won': 27, 'sets-won': 72, 'games-won': 709, 'breakpts-won': 161, 'clean-sets': 2, 'straight-sets': 15, 'aces': 157, 'doublefaults': 88}

If the year is provided then,
Entry 1- Novak Djokovic
Entry 2- Rafael Nadal
Year = 2019
Output-
Novak Djokovic {'matches-won': 1, 'sets-won': 4, 'games-won': 25, 'breakpts-won': 6, 'clean-sets': 0, 'straight-sets': 1, 'aces': 15, 'doublefaults': 1}
Rafael Nadal {'matches-won': 1, 'sets-won': 2, 'games-won': 24, 'breakpts-won': 6, 'clean-sets': 1, 'straight-sets': 0, 'aces': 3, 'doublefaults': 2}
