# MEPsearcher
author: ponychen

## usage
+ preparing a PES.data, containing the 2D potential surface. The 1st, 2nd and 3rd columns indicate X, Y axis and energy value, respectively
+ runing sort.py, then the PES.data being sorted will be applicale for matplotlib
+ editing guess.data. 1st row: number of beads in initial path. 2nd row: start point of the initial guess path, containg X and Y aixs. 3rd row: end point of 
the initial guess path.
+ running MEPSearcher.py. some default parameters in this py file can be adjusted by yourself. After convergence reached, the minimum energy path (MEP) will be 
stored in out.data.
+ running draw.py. see results.
