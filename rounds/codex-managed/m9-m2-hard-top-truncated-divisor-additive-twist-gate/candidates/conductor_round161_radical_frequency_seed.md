# Conductor Round-161 radical-frequency seed

## 1. Result: exact candidate reduction, not a target estimate

The nonsquare hard-TOP scalar has an exact unique squarefree-radical
linearization

\[
 \mathcal T_L^{\rm ns}
 =\sum_{\substack{D>1\\D\ {\rm squarefree}}}
  \sum_{t\ge1}B_D(t)e(tJ\sqrt D),
\tag{161.C1}
\]

where

\[
 B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2)
 1_{Dt^2\asymp L^2}.
\tag{161.C2}
\]

This is a candidate interface only. It makes the phase linear inside each
\(D\)-channel, but the coefficient varies with both \(D\) and \(t\).
Consequently a standard large sieve for many frequencies acting on one
common coefficient vector is not yet applicable. The round must either
derive and price a literal low-cost decomposition of \(B_D(t)\), prove a
more general actual-coefficient theorem, or certify the first exact
capacity obstruction.

## 2. Exact statement and hypotheses

Retain the definitions and literal profiles of the Round-161 barrier
packet. For each incidence \(hm=Dt^2\), put \(g=(h,m)\),
\(h=ga\), and \(m=gb\). Since \((a,b)=1\) and
\(\operatorname{sf}(ab)=D\), there are unique positive \(u,v\) and
unique coprime squarefree \(d_1,d_2\) such that

\[
 a=d_1u^2,\qquad b=d_2v^2,\qquad d_1d_2=D.
\tag{161.C3}
\]

Then

\[
 t=guv,\qquad d_2v^2\le d_1u^2\le4d_2v^2,
\tag{161.C4}
\]

and odd \(h\) is equivalent to \(g,d_1,u\) all odd. Coprimality may be
written \((d_1u,d_2v)=1\). No sign, positivity, lower-envelope,
smoothness-in-\(n\), or common-vector hypothesis is assumed for the
literal coefficient.

## 3. Proof or derivation

The representation \(n=Dt^2\) is the unique squarefree-kernel
factorization of a nonsquare integer. Substituting it into the accepted
product-fibre identity proves (161.C1)--(161.C2).

For the finer incidence formula, division by \(g=(h,m)\) gives coprime
\(a,b\). Every prime occurs to odd exponent in exactly one of them or to
even exponent in one of them, so splitting the odd-exponent primes gives
the unique disjoint squarefree factors \(d_1,d_2\), and the remaining
parts are \(u^2,v^2\). Hence (161.C3) is bijective. Moreover

\[
 hm=g^2d_1d_2u^2v^2=D(guv)^2,
\]

which proves \(t=guv\). The integer cone
\(\lceil h/4\rceil\le m\le h\) is exactly
\(m\le h\le4m\), giving (161.C4).

Thus (161.C2) can be unmasked exactly as

\[
\begin{aligned}
 B_D(t)=
 \sum_{\substack{d_1d_2=D\\d_1,d_2\ {\rm squarefree}}}
 \sum_{\substack{guv=t\\(d_1u,d_2v)=1\\
 g,d_1,u\ {\rm odd}\\d_2v^2\le d_1u^2\le4d_2v^2}}
 &\chi_4(gd_1)\eta_L(gd_1u^2)
 \Phi\!\left(\frac{gd_1u^2}{H+1}\right)\\
 &\times\left(\frac{L^2}{Dt^2}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xd_1u^2}{4d_2v^2}}\right),
\end{aligned}
\tag{161.C5}
\]

with the literal support and zero extension understood. Conversely every
tuple in (161.C5) gives one original \((h,m)\), so no multiplicity is
hidden.

The accepted Round-137 estimates imply

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L)
\tag{161.C6}
\]

and

\[
 \sum_t|B_D(t)|\ll_\varepsilon
 (1+L/\sqrt D)L^\varepsilon.
\tag{161.C7}
\]

Global Cauchy in (161.C6), or absolute summation in (161.C7), gives only
\(L^{2+o(1)}\). The deficit is still \(L^{1/2-o(1)}\).

For a whole channel to have phase one one needs
\(J\sqrt D\in\mathbb Z\). If this holds for two squarefree
\(D_1,D_2\), then \(\sqrt{D_1/D_2}\in\mathbb Q\), forcing
\(D_1=D_2\). Thus the exact whole-channel resonance is unique and is
target-safe by (161.C7). This does not control the modulo-one near
collisions between unequal \(D\)'s.

Finally, frequency spacing alone cannot estimate (161.C1) for all arrays
having only the displayed support and magnitude constraints: replacing
an arbitrary array by its magnitude times
\(e(-tJ\sqrt D)\) aligns every term. This is a method control only; it is
not the literal (161.C5) and is not a lower bound for the physical scalar.
A valid argument must identify an exact property of (161.C5) that the
aligned array lacks.

## 4. First doubtful or unproved step

The first missing step is a cancellation-preserving reduction from the
literal matrix \(B_D(t)\) to a theorem that can exploit the frequency
family \(J\sqrt D\bmod1\). A classical large-sieve operator typically
tests one vector \((c_t)\) at many frequencies. Here each row has its own
vector \((B_D(t))\). Writing

\[
 B_D(t)=\sum_r x_r(D)c_r(t)
\tag{161.C8}
\]

would make common-test estimates relevant only after the complete
projective or Hilbert factorization cost of (161.C8) is bounded. No such
bound follows from (161.C6)--(161.C7), and expanding (161.C5) term by term
can restore the original product cone.

## 5. Control tests and outcomes

| Control | Seed outcome |
|---|---|
| unique radical factorization | Pass: (161.C1)--(161.C4) are bijective. |
| literal coefficient incidence | Pass as identity: (161.C5) retains character, parity, profiles, cone, and zero extension. |
| accepted energy | Pass but no closure: (161.C6) gives global capacity \(L^{2+o(1)}\). |
| fixed-channel bound | Pass but no closure: (161.C7) makes one exact channel safe; absolute summation restores \(L^{2+o(1)}\). |
| exact resonance | Pass: at most one whole channel at a fixed center. Near resonance remains open. |
| common-test applicability | Open: the physical coefficient is a varying matrix, not one common vector. |
| projective/tensor cost | Open: (161.C8) requires a literal norm theorem. |
| phase-aligned array | Hostile control only; it rules out coefficient-uniform reasoning, not the physical target. |
| owner scope | No target, strict range, downstream owner, or exponent follows from this seed. |

## 6. Dependencies and exact artifacts used

This seed uses `protocol.md`, `state/proof_obligations.yml`, the Round-137
blind statement, candidate, adjudication, and synthesis, the Round-161
strategy, and the Round-161 barrier packet. It uses no external theorem,
numerical experiment, or symbolic experiment.

## 7. Recommended state effect

No graph mutation is recommended at round opening. Retain (161.C1)--
(161.C5) as the candidate kernel to be independently rederived and
hostilely audited. Promote only if post-unmask seam review verifies a new
literal theorem or a sharply scoped obstruction not already contained in
Round 137.
