# Sujet 09 : Labyrinthe

Crée une fonction python `resolution` prenant en entrée une chaine de caractère encodant un labyrinthe de la façon suivante :
- La première ligne est composée de "-" (case pleine) et d'un " " (l'entrée du labyrinthe).
- La dernière ligne est composée de "-" (case pleine) et d'un " " (la sortie du labyrinthe).
- Chaque ligne intermédiaire est composée de "o" (case pleine) et " " (case vide).

la fonction resolution renverra la chaine de caractère avec le chemin le plus court reliant l'entrée et la sortie en passant par des cases vides (on ne peut avancer que de haut en bas et gauche à droite) ces cases seront remplis par des "x".

Ainsi si l'entrée est
```
--------------- ----------------
ooooooooooooooo oooooooooooooooo
ooooooooooooooo   oooooooooooooo
ooooooooooooooooo oooooooooooooo
ooooo             oooooooooooooo
ooooo ooooooooooo     oooooooooo
ooooo ooooooooooooooo oooooooooo
ooooo oooooooo        oooooooooo
ooooo      ooo oooooo oooooooooo
oooooooooooooo oooooo     oooooo
oooooo       oooooooooooo oooooo
oo ooo ooooo oooo      oo oooooo
oo ooo ooooo oooo oooo oo oooooo
oo ooo ooooo oooo oooo oo oooooo
oo ooo ooooo       ooo    oooooo
oo     ooooooo ooo ooooooooooooo
oooooooooooooo ooo     ooooooooo
ooooooooo oooo ooooooo ooooooooo
ooooooooo oooo ooooooo ooooooooo
ooooooooo      ooooooo ooooooooo
oooooooooooooooooooooo ooooooooo
---------------------- ---------
```


la sortie sera

```
---------------x----------------
oooooooooooooooxoooooooooooooooo
oooooooooooooooxxxoooooooooooooo
oooooooooooooooooxoooooooooooooo
ooooo            xoooooooooooooo
ooooo oooooooooooxxxxxoooooooooo
ooooo oooooooooooooooxoooooooooo
ooooo oooooooo       xoooooooooo
ooooo      ooo ooooooxoooooooooo
oooooooooooooo ooooooxxxxxoooooo
oooooo       ooooooooooooxoooooo
oo ooo ooooo ooooxxxxxxooxoooooo
oo ooo ooooo ooooxooooxooxoooooo
oo ooo ooooo ooooxooooxooxoooooo
oo ooo ooooo     xxoooxxxxoooooo
oo     ooooooo oooxooooooooooooo
oooooooooooooo oooxxxxxooooooooo
ooooooooo oooo oooooooxooooooooo
ooooooooo oooo oooooooxooooooooo
ooooooooo      oooooooxooooooooo
ooooooooooooooooooooooxooooooooo
----------------------x---------
```
