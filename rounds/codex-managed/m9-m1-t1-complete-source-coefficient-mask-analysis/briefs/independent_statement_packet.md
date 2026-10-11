# Round 200 independent statement packet

Campaign: m9-m1-t1-complete-source-coefficient-mask-analysis.
Graph hash: 2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5.
Generated: 2026-09-23. Role: statement-only rederivation input.
This packet states candidate claims, not accepted conclusions.

Let K be a finite complex matrix with row set I and columns 1,...,N.
Assume |sum a_m b_n K(m,n)| <= B ||a||_2 ||b||_2 for all complex a,b.
For arbitrary f:I->{0,...,N}, independently prove or refute that the
prefix mask n<=f(m) has bound (1+ceil(log_2 N)) B ||a||_2 ||b||_2.
Derive the cost for at most J row-dependent intervals. Check empty rows,
non-power-of-two lengths, endpoints, arbitrary row order, complex vectors,
and zero extension. Do not assume f monotone.

For an arbitrary mixed amplitude A, define ||A||_pi as the infimum of
sum_j ||u_j||_2 ||v_j||_2 over A(m,n)=sum_j u_j(m)v_j(n).
Give the exact conditional masked bound and the correct meaning of this
norm over complex matrices; distinguish it from Frobenius norm and from
counting terms of a decomposition. Give an explicit control demonstrating
that bounded entries alone do not imply a cheap product decomposition.

Also check these finite identities independently. A single linear
transport U and a finite partition of unity sum_j M_j=I satisfy
sum_j [M_j,U]=0 on one common zero-extended domain. State the restrictions
when maps or domains differ. Given a finitely supported sequence z on Z,
define D=sum |z_n|^2, E_R=R^(-1)sum_s |sum_(j=0)^(R-1)z_(s+j)|^2,
C_even=sum_(0<r<R, r even)(1-r/R)sum_n z_(n+r)conj(z_n).
Prove or refute E_R<=2D+4 Re C_even, and
|sum z_n|^2 <= (M+R-1)/R E_R when support lies in M consecutive sites.
No result here supplies an unmasked arithmetic estimate B.

Do not read claimant reports, the strategy review, proof graph, best proof,
or previous round derivations. Protocol and this packet suffice.
