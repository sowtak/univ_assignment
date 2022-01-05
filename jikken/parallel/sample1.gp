reset
set nokey
set xrange [0:1]
set yrange [0:100]
set size square

set terminal gif animate delay 50
set output "test.gif"

n0=0
nmax=1000
dn=20

load "sample1.plt"

set terminal x11
unset output