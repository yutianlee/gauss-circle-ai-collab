# Statement-only packet for Round 173 (repaired)

## Setting

Let (J=\sqrt X), (1\ll L\ll H\le J^{1/2}), (M\asymp L^2), and
(R_0=\lceil L\rceil). A finite literal sequence is supported on an
(M)-site interval and has energy

\[
 D_L=\sum_N|c_N|^2\ll_\varepsilon L^2X^\varepsilon.
\]

Every coefficient has the exact finite near-square divisor opening

\[
 c_N=\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)\lambda_N(d).
\]

On every nonzero opened incidence,

\[
 N=dm\asymp L^2,\qquad d\asymp L,\qquad m\asymp L,
 \qquad |\lambda_N(d)|\ll X^\eta,
\]

for arbitrarily small fixed (eta>0), and each product has at most
(X^\eta) active opened divisors after epsilon rebudgeting. The literal
weight may otherwise jump: it contains specified selectors, squarefree and
coprimality deletion masks, both two-adic branches, profiles, hard endpoints,
point values, and zero-extension conventions. No regularity across adjacent
products or divisors may be assumed unless proved. In particular, the
weighted absolute double opening over (O(MT)) physical ordered pairs of gap
(<T) is at most (MTX^{O(\eta)}).

For (R<T\le2R), define

\[
 \beta_{R,T}(r)=
 \begin{cases}
 r(T-R)/(RT),&0<r<R,\\
 1-r/T,&R\le r<T,\\
 0,&r\le0\text{ or }r\ge T.
 \end{cases}
\]

The physical even-gap link is

\[
 \Delta_{R,T}=2\Re\sum_{\substack{N'-N>0\\2\mid N'-N}}
 \beta_{R,T}(N'-N)c_{N'}\overline{c_N}
 e(J(\sqrt{N'}-\sqrt N)).
\]

## Tangent chart

After opening both coefficients, write uniquely

\[
 N=dm,\quad d'=d+2s,\quad m'=m+v,
\]

so (v) is even and

\[
 r_s=N'-N=dv+2s(m+v),\qquad
 \chi_4(d+2s)\chi_4(d)=(-1)^s.
\]

Define (G_{d,m,v}(s)) to be the complete opened weight and phase when both
atoms are on positive literal support, and zero otherwise. Thus

\[
 \Delta_{R,T}=2\Re\sum_{d,m,v,s}(-1)^s
 \beta_{R,T}(r_s)G_{d,m,v}(s).
\]

For every finitely supported (H),

\[
 2\sum_s(-1)^sH(s)=\sum_s(-1)^s\{H(s)-H(s+1)\}.
\]

Consequently

\[
 \Delta_{R,T}=\mathcal C_{R,T}+\mathcal R_{R,T},
\]

with

\[
 \begin{aligned}
 \mathcal C_{R,T}
 &=\Re\sum(-1)^s
 \{\beta_{R,T}(r_s)-\beta_{R,T}(r_{s+1})\}G(s),\\
 \mathcal R_{R,T}
 &=\Re\sum(-1)^s\beta_{R,T}(r_{s+1})
 \{G(s)-G(s+1)\}.
 \end{aligned}
\]

All support births, deaths, selector changes, and endpoint jumps are part of
the displayed difference.

## Frozen question

Let (R_{j+1}=\min(2R_j,M)), with repetitions removed and the exact final
non-doubling link retained. Prove

\[
 \sum_j\mathcal R_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon
\]

one-sided, while retaining one outer real part, or locate the first exact
identity, multiplicity, endpoint, support-jump, phase, restored-power, or
tautology obstruction. Independently verify the complete commutator using
(r_{s+1}-r_s=2m'\asymp L), the exact bandpass slopes, and the stated
opened-incidence ledger.

No modulus may be inserted by link, fibre, row, selector class, cell, or mode
before a saving is proved. The repaired near-square and opened-weight
hypotheses exclude arbitrary single-divisor (d=N,m=1) arrays and arbitrarily
large cancelling divisor openings; those remain useful false controls but are
not members of the literal coefficient class.
