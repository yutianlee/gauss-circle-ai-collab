# Round 161 barrier packet: hard-TOP radical-frequency coupling

## Frozen owner

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
\]

and fix one half-open polynomial intermediate hard-TOP block
\(1\ll L\ll H\). For odd positive \(h\), define

\[
 a_{\rm end}(h,m)=\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right)
\]

on \(\lceil h/4\rceil\le m\le h\), with literal zero extension.
After removing \(hm=\square\) only through its accepted target-safe norm
owner, the scalar is

\[
 \mathcal T_L^{\rm ns}=
 \sum_{h\ {\rm odd}}\chi_4(h)
 \sum_{\substack{\lceil h/4\rceil\le m\le h\\hm\ne\square}}
 a_{\rm end}(h,m)e(J\sqrt{hm}).
\tag{161.B1}
\]

Its required bound is

\[
 \boxed{|\mathcal T_L^{\rm ns}|\ll_\varepsilon
 L^{3/2}X^\varepsilon.}
\tag{161.B2}
\]

## Accepted product-fibre facts

With

\[
 C_L(n)=\sum_{\substack{h\mid n,\ h\ {\rm odd}\\
 \sqrt n\le h\le2\sqrt n}}
 \chi_4(h)\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right),
\tag{161.B3}
\]

one has the exact identity

\[
 \mathcal T_L^{\rm ns}=L^{3/2}
 \sum_{\substack{n\asymp L^2\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n).
\tag{161.B4}
\]

The accepted structural bounds are

\[
 \sum_n|C_L(n)|^2\ll L^2\log(2L),
\tag{161.B5}
\]

and, for every squarefree \(D>1\),

\[
 \sum_{\operatorname{sf}(n)=D}
 |L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}|
 \ll_\varepsilon(1+L/\sqrt D)L^\varepsilon.
\tag{161.B6}
\]

Both positive closures have total \(L^{2+o(1)}\) capacity. The target
needs a new factor \(L^{1/2-o(1)}\).

## New exact radical interface

Every active nonsquare is uniquely \(n=Dt^2\), with \(D>1\)
squarefree. Define

\[
 B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2)
 1_{Dt^2\asymp L^2}.
\tag{161.B7}
\]

Then

\[
 \mathcal T_L^{\rm ns}
 =\sum_{D>1\ {\rm sf}}\sum_{t\ge1}
 B_D(t)e(tJ\sqrt D).
\tag{161.B8}
\]

For every incidence \(hm=Dt^2\), the unique coprime decomposition is

\[
 h=gd_1u^2,\qquad m=gd_2v^2,\qquad
 d_1d_2=D,\qquad t=guv,
\tag{161.B9}
\]

where \(d_1,d_2\) are squarefree, the cone is
\(d_2v^2\le d_1u^2\le4d_2v^2\), and odd \(h\) forces
\(g,d_1,u\) odd. A successful theorem must use this literal incidence or
another proved property of \(B_D(t)\); arbitrary channel coefficients
can absorb all displayed phases.

## Resonance and collision controls

The whole \(D\)-channel is phase one exactly when
\(J\sqrt D\in\mathbb Z\). At a fixed real center this can happen for at
most one squarefree \(D\), and (161.B6) makes it target-safe. This does
not estimate near resonances.

Any square-root-frequency or large-sieve route must retain wraparound and
price

\[
 \left\|J(\sqrt{D_1}-\sqrt{D_2})\right\|_{\mathbb R/\mathbb Z}
\tag{161.B10}
\]

on the actual unequal and moving \(t\)-ranges. A theorem for one common
test sequence is not automatically a theorem for the matrix
\(B_D(t)\). Any tensor or projective reduction must state and bound its
literal decomposition norm before using frequency spacing.

## Inherited no-go controls

- Fibrewise modulus and positive product energy miss (161.B2) by
  \(L^{1/2-o(1)}\).
- Summing (161.B6) over \(D\) restores \(L^{2+o(1)}\).
- Smooth first/second derivative estimates do not apply to \(C_L(n)\).
- Lawful divisibility completion and the B-process return the original
  reciprocal hard-TOP principal family.
- Complementary-divisor switching is involutive.
- Full-divisor completion has an uncontrolled complement and a circular
  localized radial term.
- Center averages and phase-aligned artificial coefficients are controls,
  not fixed-center physical estimates.

## Mandatory hostile strata

- \(t=1\) squarefree products, including close semiprime singleton fibres;
- small \(D\) long channels and large \(D\) one- or few-point channels;
- the unique exact-resonance channel and all near-resonant collars;
- even \(D\), odd-height parity, hard entries and exits, and zero
  extension;
- every projective, tensor, Bessel, and Sobolev norm introduced;
- arbitrary real \(J\), without metric or Diophantine assumptions; and
- all source hypotheses and the restored \(L,J,H,X\) powers.

## Exit gate

Prove (161.B2), prove an owner-complete strict polynomial range, or prove
the first exact route-scoped coefficient/collision/source/capacity
obstruction. Close under exactly one of
`hard_top_radical_frequency_target`,
`strict_hard_top_radical_frequency_range`, or
`hard_top_radical_frequency_coupling_no_go`.
