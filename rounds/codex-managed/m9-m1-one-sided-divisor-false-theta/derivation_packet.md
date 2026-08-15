# Round 63 derivation packet: one-sided divisor false-theta kernel

## Accepted input

For every fixed subcritical block \(n\asymp N=X^\nu\),
\(0<\nu<1/2\), Round 62 proves the exact coefficient

\[
 \mathcal D(n)=
 \sum_{\substack{hq=n\\q\ {m odd}\\q>4h}}\chi_4(q).
\tag{63.1}
\]

Through \(\nu=2/5\), replacing the full angular coefficient by
\(\mathcal D\) costs only \(X^\varepsilon\).  The remaining target is

\[
 \mathcal L_{X,V}(N)=
 \sum_nV(n/N)\mathcal D(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{63.2}
\]

No signed estimate in (63.2) is accepted.

## Exact generating identity to verify

For \(|z|<1\), write odd \(q\) by residue class.  The cone condition
gives, in both cases, \(m\ge h\):

\[
 q=4m+1\quad(\chi_4(q)=1),\qquad
 q=4m+3\quad(\chi_4(q)=-1).
\]

The candidate identity is

\[
 \begin{aligned}
 \mathscr F(z)
 &:=\sum_{n\ge1}\mathcal D(n)z^n\\
 &=\sum_{h\ge1}\sum_{m\ge h}
 \left(z^{h(4m+1)}-z^{h(4m+3)}\right)\\
 &=\boxed{\sum_{h\ge1}\frac{z^{4h^2+h}}{1+z^{2h}}}.
 \end{aligned}
\tag{63.3}
\]

The last step uses
\((1-z^{2h})/(1-z^{4h})=1/(1+z^{2h})\).

There is also an exact bilateral Appell candidate.  Put
\(z=e^{\pi i\tau}\), so \(Q=z^2=e^{2\pi i\tau}\), and use the
Semikhatov--Taormina--Tipunin level-four convention

\[
 \mathscr K_4(\tau,\nu,\mu)=
 \sum_{r\in\mathbb Z}
 \frac{e^{4\pi i r^2\tau+8\pi i r\nu}}
 {1-e^{2\pi i(\nu+\mu+r\tau)}}.
\tag{63.4}
\]

At \(\nu=0\), \(\mu=1/2\), its summand is
\(z^{4r^2}/(1+z^{2r})\).  Pairing \(r=h\) and \(r=-h\) gives

\[
 \frac{z^{4h^2}}{1+z^{2h}}
 +\frac{z^{4h^2}}{1+z^{-2h}}=z^{4h^2}.
\]

This specialization therefore yields an ordinary theta series, not
(63.3); it is a control against a tempting but false direct Appell
identification.

A different common level-four convention

\[
 A_4(u,v;\tau)=e^{4\pi i u}
 \sum_{r\in\mathbb Z}
 \frac{Q^{2r(r+1)}e^{2\pi i rv}}
 {1-e^{2\pi i u}Q^r}
\tag{63.5}
\]

gives the desired bilateral summand at
\(u=1/2\), \(v=-3\tau/2\).  In the Semikhatov convention (63.4), the
same candidate corresponds, by direct numerator and denominator
comparison, to

\[
 \mathscr K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right).
\tag{63.6}
\]

Indeed the numerator is
\(e^{4\pi i r^2\tau+\pi i r\tau}=z^{4r^2+r}\), while the denominator
is \(1+z^{2r}\).  Pairing \(r=h\) and \(r=-h\) gives equal terms and
\(r=0\) contributes \(1/2\), so the candidate exact relation is

\[
 \mathscr K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)
 =\frac12+2\mathscr F(z).
\tag{63.7}
\]

This algebra is included as an authorized lead, but its modular orbit,
all correction terms, and usefulness for the radial phase still require
the Round-63 audits.  In particular it must not be confused with the
false \(\mathscr K_4(\tau,0,1/2)\) specialization above.

## Frozen objective

Determine whether (63.3) yields a coefficient-preserving partial-theta,
false-theta, Appell--Lerch, indefinite-theta, or sector-Poisson
transformation that proves (63.2) on a nonempty fixed interval of
\(0<\nu\le2/5\), or rigorously show why known transformations return to
an equally hard cone.

Any useful transform must retain:

1. the exact coefficient \(\mathcal D(n)\), including \(\chi_4\);
2. the one-sided boundary \(q>4h\);
3. the smooth radial weight \(V(n/N)n^{-3/4}\);
4. the phase \(e(\sqrt{Xn})\), not an additive phase \(e(\alpha n)\);
5. uniformity in \(X\) and \(N=X^\nu\);
6. all boundary or Mordell-integral correction terms.

## Allowed analytic routes

- Directly complete (63.3) to an indefinite theta series and derive its
  exact correction terms.
- Use a coefficient-preserving Laplace/Fourier integral representation
  of the smooth radial phase and apply a modular transformation.
- Apply Poisson or Voronoi summation in \(m\) or \(h\), retaining the
  cone boundary and character difference.
- Derive an exact sector-lattice interpretation and apply a proven
  sector theta theorem after auditing its hypotheses.
- Prove a sharp no-go showing that the transformed main term is the
  original M1/Hardy kernel or has unchanged \(N^{1/4}\) capacity.

## Forbidden shortcuts and controls

- Do not call (63.3) modular merely from its appearance.
- Do not replace \(\mathcal D\) by \(r_2/4\).
- Do not infer a square-root phase estimate from bounds for
  \(\sum\mathcal D(n)e(\alpha n)\) without a uniform integral transform.
- Keep Abel/radial-transform losses explicit.
- Test cusps and rational phases, especially perfect-fourth-power
  coherence.
- A primary theorem is importable only after exact source and hypothesis
  audit.
- Numerical work is optional and diagnostic only, capped below 20%; the
  round is intended to be analytic.

## Promotion gate

A new exponent or lower-radial closure requires a rigorous bound for
(63.2) on a stated nonempty radial interval, with the Round-62 error
recombined.  An exact transform or a no-go may be promoted as a scoped
reduction, but neither alone changes M9-M1, M9, or the final exponent.
