# Conductor candidate: blockwise owner completion

Campaign: m9-m2-blockwise-owner-completion

Starting graph SHA-256:
f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d

## Candidate interface

For the canonical hard top block, write

\[
 \mathcal E_L^\top
 =\mathcal E_{\mathrm{owned},L}
  +2\Re\sum_{B\in\mathcal B_L}\mathfrak Q_B^{\mathrm{res}},
\qquad
 \mathcal E_{\mathrm{owned},L}
 \ll_\varepsilon L^2X^\varepsilon.
\tag{C109.1}
\]

The block index contains the dyadic physical scales
\(B=(A,D,K,G,R,\sigma)\), with orientations and support transitions
included.  The proposed fixed-\(K\) completion is

\[
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}
  -\sum_{\nu\in\mathcal O}\mathfrak O_{B,\nu}.
\tag{C109.2}
\]

The owner list must include, once only:

1. the Round-77 full-lattice endpoint samples, fixed physical collars,
   original Poisson zero and positive modes, equality modes, wrong-sign
   modes, entry/exit terms, and negative nonstationary tails;
2. the signed primitive-square/common-squarefree family;
3. exact nonsquare centres and the positive-safe \(\rho\ll1\) blocks;
4. the singleton and prescribed polylogarithmic fixed-\(q\) rows when
   they occur inside the chosen block decomposition;
5. every conjugate orientation and zero-extension boundary.

The desired missing estimate is not (C109.1).  It is

\[
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{C109.3}
\]

If (C109.2)--(C109.3) hold, then

\[
 \sum_B|\mathfrak Q_B^{\mathrm{res}}|
 \leq \sum_B|\mathfrak Q_B^{\mathrm{comp}}|
      +O_\varepsilon(L^2X^\varepsilon).
\tag{C109.4}
\]

This is a scalar pair-sum statement before a second positive Gram lift.
It does not assert commutation with a Fejér operator.

## Algebra that is already exact

At fixed \(k\), a compact smooth difference cutoff separates by

\[
 \psi((b-a)/D)
 =\int\widehat\psi(\xi)e(-\xi a/D)e(\xi b/D)\,d\xi,
\qquad \|\widehat\psi\|_1\ll_\psi1.
\tag{C109.5}
\]

Primitivity separates as

\[
 1_{(a,b)=1}=\sum_{d\mid a,\ d\mid b}\mu(d),
\tag{C109.6}
\]

and the actual \(a^{-3/4}b^{-3/4}\) factors give the absolutely
summable cost \(\sum_d d^{-3/2}\).  A fixed finite number of
orientations and \(X^\varepsilon\)-many dyadic blocks cost no power.

Completing the moving reciprocal interval to a fixed dyadic lattice is
therefore algebraically lawful if its complement is exactly the owner
sum in (C109.2).  Extending the physical integration range through
flat collars is lawful under the same condition.  Neither step proves
(C109.3).

## The decisive classification

Each accepted owner must be classified as one of:

- a scalar owner theorem already proving the absolute block sum needed
  in (C109.3);
- a positive row-energy theorem that implies such a scalar estimate
  after an explicit Cauchy normalization;
- a signed aggregate theorem whose cancellation may run across blocks
  and therefore does not imply (C109.3);
- a genuinely pair-dependent mask whose separation/projective norm is
  not controlled.

The words owner, safe, and already bounded are insufficient.  The
literal formula, normalization, range, sign, and block placement must
be displayed.

## Promotion fork

Promote a blockwise completion lemma only if every owner family passes
the same scalar absolute ledger with no duplicate ownership.  Otherwise
promote only the exact partial completion for the passing families and
name the first failing owner as the smaller survivor.

Even a full positive result would not estimate
\(\mathfrak Q_B^{\mathrm{comp}}\).  Round 108 proves that Gaussian
functional calculus, separate character transforms, and Plancherel
have equal capacity.  The actual directional theorem and the global
quarter target remain open.
