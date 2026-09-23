# Statement-only packet: Round 192 unimodular covector count

Let \(Q\ge1\), let \(U=mq>4Q\) be odd, and let \(U\mid u\). Fix
\(Y>Qm\). A literal set of positive integers \(v\) lies in a fixed finite
union of intervals of total length \(O(u)\), and every retained row has
\((v,U)=1\). Further row restrictions may only delete rows.

For \(v_0=[v]_U\in\{1,\ldots,U-1\}\), define the signed least inverse and
canonical quotient by

\[
\rho v_0-\beta U=1,
\qquad -\frac{U-1}{2}\le\rho\le\frac{U-1}{2}.
\]

Put

\[
T=\min\!\left(\frac{U-1}{2},
\left\lfloor\frac{QmU}{Y}\right\rfloor\right).
\]

Only rows with \(|\rho|>T\) remain. For a fixed constant \(C_0\ge2\), let

\[
A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\quad
\mathcal F_A=\{(c,d):1\le c\le A,\ 0\le d\le c,\ (c,d)=1\},
\]

and define \(\ell_{c,d}=c\beta-d\rho\). If \(T\ge1\), let

\[
\mathcal E_A={v:\min_{(c,d)\in\mathcal F_A}|\ell_{c,d}|\le T\};
\]

if \(T=0\), set \(\mathcal E_A=\varnothing\).

Each retained row has \(O(Y\kappa X^\eta)\) positive atom capacity. The
desired fixed-packet scale is \(Qm\kappa uX^\varepsilon\). A later linear
outer ledger has an exact weight \(m^{-1}c_q(a)\), logarithmic coefficient
mass, power-of-two bands, and divisor multiplicity; no positive power of
\(Y\) may be absorbed.

Independently determine:

1. the exact factorization for fixed \((c,d,\ell)\) and the sharpest uniform
   residue-class count obtainable from the elementary divisor bound;
2. the literal-row multiplicity and whether \(\mathcal E_A\) is target-safe
   up to fixed polylogarithms;
3. every exceptional case: signs, \(T=0\), \(\ell=0\), floors, \(c\ge U\),
   overlaps, and empty or saturated sets;
4. the strongest exact complement and any genuinely proved coverage
   corollary; and
5. whether the complement condition alone implies cancellation for arbitrary
   bounded row arrays, or whether a new literal coefficient theorem is still
   necessary.

Do not assume that the canonical quotient \(\beta\) equals the transport
quotient formed from the actual representative \(v\). Do not use computation
as proof. Return the required seven-section research report and stop.
