# DFTB+ Charges from MD.out
**Extract charges from electron density population of DFTB+ trajectory file**

DFTB+ produce a trajectory output file 
```
62
MD iter: 0
    C      8.45917579     -5.34844091      3.46693181      4.09198740      1.35876635     -1.98824484     -4.82334369
    C      9.57109640     -5.88403274      2.84331597      4.06738192     -4.65870613      9.27153852     -5.35064945
    N      9.22151415     -7.12802686      2.38235178      4.88962112     -2.41282543      0.86551045     -1.86380622
    H     10.56851547     -5.48528334      2.72952837      0.85694754     34.10827415     26.54011982      0.46293533
    C      7.92868580     -7.36091084      2.70857527      3.94542548     -1.34575468     -1.43965913     -7.20829039
    N      7.45609259     -6.28212285      3.37515549      4.88964874      3.61848836      0.76214022      2.74678416
    H      7.38088347     -8.27254779      2.50861236      0.84935140     -1.77067330     12.61366615     -8.32431691
    H      8.30390224     -4.39795008      3.96255201      0.83145246    -55.42221846    -30.40060313    -17.42691506
```
for every step saved the first line is the number of atoms of the box

then a comment line with the timestep `MD iter: 0`

after the first 2 lines there  are all coordinates and other properties of atoms in the simulation.

**We need to know what is the total charge of defined molecules in every step**

the 5th coloumn of the output is the quantity of electrons on that specific atom (extrapolated from system eletron density)

given the index of the molecule is simple to extract all the frame and sum up all the electron deficiency/excess. by comparing of isolated atom is trivial to end up with the charge per atom
