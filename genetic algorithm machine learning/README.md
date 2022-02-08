## Details
The vectors are assigned unique ids to improve readability. To search what the index corresponds to, please run

> $ python3 view_vector.py index

Replace index by the index you want to search. It will show the ordered representation of the vector, its fitness and also its unordered representation. The unordered representation was required to implement the inversion operation. It is just a permutation of the indices and has the form 

(a1, P1), (a1, P2), ..., (a11, P11)

where a_i are the values in [-10, 10] and P_i's the indices.


The generations_i.txt has this format for every generation

,Genotype <br>
0, v1,<br>
1, v2, <br>
.        <br>  
.<br>
.<br>
29, v29<br>
,Generation,Parent1,Parent2,Child1,Child2,Mutated Child1,Mutated Child2<br>
0,g_index, p1, p2, c1, c2, m1, m2
...<br>


The starting zero is present because saving a single row in pandas required 
an index so we chose it as 0. Generation corresponds to the number of generations that elapsed since the running of program. It is **not** the actual generation index. The actual generation index can be found by searching for Genotype and finding its index in the search bar.   


This pattern repeats for all the generations.