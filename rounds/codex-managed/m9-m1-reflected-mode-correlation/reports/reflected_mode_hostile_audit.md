# 1. Result

There is no automatic cancellation between the actual Mellin sector and its
functional-equation reflection.  The completed root number is (+1); the map
(z\mapsto-z) leaves the positive-real-part Mellin chamber; and returning the
reflected contours crosses the two hard-cutoff poles (u=0) and (v=0).
Their joint residue is the (z=0) Hardy--Voronoi mode.  The reflected angular
sector is not M1 and only resembles, without equalling, M2.  Thus reflection
does not isolate a smaller already-controlled kernel.

# 2. Exact statement and hypotheses

Assume the exact Round-15 representation with
(z=u+v), (Re u=a>0), (Re v=b>0),

\[
 F_z(s)=\zeta(s+z/2)L(s-z/2,\chi_4),\qquad
 \Lambda_z(s)=\Lambda_{-z}(1-s),
\]

and retain all scale factors, floors, product cutoffs, and endpoint stars.
Then no identity obtained solely from the functional equation makes the
signed (z)- and (-z)-integrals cancel.  Any comparison on common contours
contains the (u=0), (v=0), and zeta-pole residues (plus any radial Perron
residue introduced for (n\le N_X)).  In particular the top (1/u) pieces
complete complementary Perron sectors rather than sum to zero.

# 3. Proof or derivation

For the primitive odd character $\chi_4$, its Gauss sum satisfies
$\tau(\chi_4)=2i$ and $\tau(\chi_4)/(i\sqrt4)=1$.  Zeta also has root
number $+1$.
Consequently the displayed functional equation has no cancelling minus sign.

On the actual contours, (Re z=a+b>0).  Replacing (z) by (-z) sends it to
(Re z<0); it cannot be realized while keeping both Mellin lines in their
original positive chambers.  Moving the reflected lines back crosses

\[
 \widehat W_+(u)=1/u+\text{rapid},\qquad
 \widehat\phi(v)=1/v+\text{holomorphic near }0,
\]

and hence their single and double residues.  A radial functional-equation
contour also crosses the pole of (zeta(s+z/2)) at
(s=1-z/2).  These terms cannot be discarded.

The apparent oddness of (1/u) is misleading: after contour reversal and
restoration, Perron inversion gives, off the boundary,
(H(x)+H(x^{-1})=1), and gives two half weights at (x=1).  It is completion,
not cancellation.  At (u=v=0), (a_0(n)=r_2(n)/4), so the double residue is
precisely the known Hardy return.

Finally, (a_{-z}) reverses the divisor ratio but retains (chi_4(q)).
Reindexing (h\leftrightarrow q) moves the character and parity condition,
while actual M2 also has a factor-four lattice map, a different Vaaler
variable, and different cone support.  Round 9 proves its leading stationary
constant has the same sign as M1.  The reflected object is therefore an
absent/complementary sector, not an opposite copy of either actual kernel.

# 4. First doubtful or unproved step

A uniform vector-valued Voronoi estimate could conceivably control the
outside-integral correlation after all residues are subtracted.  No such
estimate is presently proved, especially at large (|\Im z|) and for the
hard top Perron limit.

# 5. Required control test and outcome

Take (n=5).  Exactly

\[
 a_z(5)=5^{z/2}+5^{-z/2}=a_{-z}(5),
\]

so reflection reinforces this coefficient; it cannot cancel it by root
number or divisor algebra.  In the actual M1 angular sector the incidence
((h,q)=(1,5)) is active while its swapped incidence is absent.  This is an
exact, nonnumerical falsifier of automatic reflected-sector cancellation.

# 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, Round-15 Mellin synthesis, Round-9 combined-cone
synthesis, Round-8 endpoint synthesis, and this brief.  No Round-16 report,
web source, or numerical experiment was used.

# 7. Recommended state effect

Promote the no-go result and retain the reflected correlation as open.
Pointwise fixed-mode bounds have insufficient uniformity and do not integrate
the (1/u) top.  Ordinary (L^2)/Cauchy--Schwarz may treat the rapid interior
remainder but loses the required signed reflection and leaves the Hardy
residue.  A maximal-Perron, vector-valued correlation theorem is necessary
for the top route, but is not sufficient unless it also controls every
crossed residue at target scale.  No change to M9-M1 or the Gauss target.
