# Round 150 barrier packet

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Round: 150
- Starting graph SHA-256: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`

## Accepted input

Round 149 proves the exact compressed coefficient and row, uniformly in
the literal finite prefix:

$$
 B_{d,U}(L)=\sum_g\frac{C_d(gL)\kappa_{d,U}(gL)}g,
$$

$$
 G_U(d)=\sum_{\substack{(L,q)=1\\q\asymp LQ}}
 \chi_4(Lq)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q)e(NdL/q).
$$

It also proves

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}\ll_\varepsilon X^\varepsilon,
$$

the literal diagonal \(O_\varepsilon(DQX^\varepsilon)\), the distinct
exact off-diagonal \(O_\varepsilon(DX^\varepsilon)\), and all exact
phase classes \(O_\varepsilon(DQX^\varepsilon)\).  The stratum
\(q/(q,N)\leq R\) is also target-safe.

## Frozen unresolved term

For two nonexact cells, put

$$
 q_i=hr_i,\quad(r_1,r_2)=1,\quad
 \delta=L_1r_2-L_2r_1,\quad
 \rho=N\delta-khr_1r_2,
$$

with \(|\rho|\leq hr_1r_2/2\).  Round 150 owns only

$$
 0<|\rho|\leq hr_1r_2/D.
$$

The exact kernel contains

$$
 \mu^2(d)B_{d,U}(L_1)\overline{B_{d,U}(L_2)}
 \mathscr W_{d,U}(L_1/q_1)
 \overline{\mathscr W_{d,U}(L_2/q_2)}
 e\!\left(d\frac{N\delta}{hr_1r_2}\right)
$$

and the two mod-four factors.  Every component must remain literal.

## Rejected shortcuts

1. Cauchy before lcm and gcd-lift compression loses a factor \(R\).
2. Montgomery--Vaughan's primal and dual large sieves have one common
   coefficient vector; they do not accept the literal moving row.
3. Even an illegal fixed-vector unwrapped-spacing estimate has capacity
   \(Q(D+M)X^\varepsilon\) and loses \(\sqrt M\) in energy.
4. A bounded profile does not by itself have bounded variation.  The
   Round-149 second-derivative diagnostic is conditional and unused.
5. A termwise map from the cube-free \(L\)-coordinate to the powerful
   Round-147 \(H\)-coordinate is invalid.
6. Adverse absolute or operator capacities are not signed lower bounds.
7. An arbitrary-matrix counterexample says nothing about the special
   arithmetic coefficient unless it is realized inside the admissible
   family.

## Mandatory new checks

- Exact two-row divisor-incidence expansion of both \(B\)-coefficients.
- Exact dependence of the prefix and sampled profile on \(d\); no
  invented monotonicity or variation hypothesis.
- The shifted-factor identity
  \((NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh\rho\), with \(k=0\) separate.
- Complete summation over \(h,k,\rho,L_1,L_2\), not merely a divisor
  bound for fixed parameters.
- \(D=1,L_i=1\), balanced and extreme aspects, even \(d\), primes
  dividing \(d_{\mathrm o}\), common factors, imprimitive denominators,
  and short prefixes.
- Clear separation of raw tuple count, coefficient-weighted absolute
  mass, and the signed collar contribution.

## Scope boundary

The generic non-collar, all \(t\geq2\) layers, the Round-138 cross
owner, lower GAR, M9--M1, M9--M2, endpoint uniformity, M9, the bridge,
the quarter target, and both recorded exponents remain unchanged unless
proved by their own complete owners.
