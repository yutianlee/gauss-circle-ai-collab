# Blind statement: actual reduced-determinant fibre at W=Y^(7/16)

This is a statement-only problem. Do not use the proof graph, strategy
files, Round-94/95 reports, the Round-117 derivation packet or candidate,
or any sibling report.

## 1. Fixed literal block

Let (Y) be large, (c\asymp Y), (W=Y^{7/16}), and fix one dyadic
block (d\asymp D), (|h|\asymp L), with

\[
 Y^{1/4}\le D\le Y^{1/2},\qquad 1\le L\le DY^{-1/4}.
\]

Fix one moving-symbol stratum, so every height, prefix, floor, hard-top
profile, and star is fixed. For (i=1,2), put
(kappa_1=1), (kappa_2=4). Reduce (h/d=a/b), with
(a\in\mathbb Z\setminus\{0}), (b>0), ((|a|,b)=1), and define the
complete lift coefficient

\[
 A_i(a,b)=\sum_{g\ge1}q_i(ga,gb).
\]

The literal coefficient identities supplied as hypotheses are

\[
 A_1(a,b)={2\chi_4(b)\over\pi i a}
 \sum_{g\ge1}{\chi_4(g)\over g}U_{1,a,b}(g),
\]

\[
 A_2(a,b)=-{4\chi_4(|a|)\over\pi |a|}
 \sum_{g\ge1}{\chi_4(g)\over g}U_{2,a,b}(g).
\]

Every literal support and endpoint convention is contained in the real
sampled-BV functions (U_{i,a,b}). The accepted lift estimates are

\[
 |A_i(a,b)|\ll_\varepsilon L^{-1}Y^\varepsilon,
 \qquad
 \sum_{(a,b)=1}|A_i(a,b)|^2
 \ll_\varepsilon {D\over L}Y^\varepsilon.
\tag{117.B1}
\]

M1 is supported on odd (b); M2 is supported on odd (a). Both signs of
(a) remain.

## 2. Exact open correlation

The complete equal-frequency contribution is already contained in
(117.B1). The unequal one-sided correlation is

\[
 \mathfrak O_i=2\Re
 \sum_{\substack{(a,b),(a',b')\\
 0<n=ab'-a'b<\kappa_i bb'/W}}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left({cn\over\kappa_i bb'}\right)
 \left(1-{Wn\over\kappa_i bb'}\right).
\tag{117.B2}
\]

All sums are over the literal reduced supports. No arithmetic absolute
value is present in (117.B2). The target is

\[
 |\mathfrak O_i|\ll_\varepsilon Y^{1/2+\varepsilon}
\tag{117.B3}
\]

uniformly on the hard region

\[
 D=Y^\delta,\quad L=Y^\ell,\quad
 {1\over4}\le\delta\le{1\over2},\quad
 0\le\ell\le\delta-{1\over4},\quad
 3\delta-\ell>{15\over16}.
\]

At ((D,L)=(Y^{1/2},Y^{1/6})), coefficient-blind spacing has capacity
(Y^{43/48+\varepsilon}), while the target is (Y^{24/48+\varepsilon}).

## 3. Required rederivation

Set

\[
 p=a'-a,\qquad q=b'-b.
\]

Derive, rather than assume, the determinant, phase, parity-character, and
both strip-width charts. It is useful to split reduced denominators
(b,b'\asymp B\le D); then (|a|,|a'|\asymp A:=LB/D) on a same-sign
interior ray shell. Every conclusion for this shell must be distinguished
from a conclusion for the whole block.

You must retain primitivity, the congruence (aq-bp=n), the triangular
boundary, opposite signs when present, and the possible nonsmooth
dependence of the lift transforms on ((a,b)).

## 4. Required decision

Prove (117.B3), a target-safe strict block subrange, a quantified saving,
or a rigorous no-go for a precisely named determinant-fibre/high-pass
proof class. State the smallest complete signed survivor and charge every
absolute value, Cauchy step, divisor expansion, progression, transform,
and boundary term.

The report must use the seven-section contract and must not infer M9, the
quarter theorem, or a global exponent without the complete all-block local
moment implication.
