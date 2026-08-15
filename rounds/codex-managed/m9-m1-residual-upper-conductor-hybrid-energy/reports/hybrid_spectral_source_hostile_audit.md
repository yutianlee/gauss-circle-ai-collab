## Result

**No-go for the frozen Round-73 target; retain the residual range open.**  The
exact diagonal in the row energy is already below the target, but none of the
audited hybrid, reciprocal-fraction, or phase-matched spectral inputs controls
the actual-symbol off-diagonal.  The smallest direct survivor is the exact
off-diagonal correlation

\[
 \mathfrak H_{C,k}^{(\kappa)}=
 \sum_{b\asymp C/T}\ \sum_{\substack{z,z'\in\mathcal Z_b\\z\ne z'}}
 a_{b,z}\overline{a_{b,z'}}
 e\!\left(\pm A_{\kappa,b}
       \left(\frac1{c_{b,z}}-\frac1{c_{b,z'}}\right)\right),       \tag{1.1}
\]

where \(z=(r,\nu,\ell)\), \(c_{b,z}=r+4b\ell\), and
\(a_{b,z}=u_{b,r,k}^{(\kappa)}w_{b,r,\nu,k}^{(\kappa)}(\ell)\)
with the exact half-open one-count ownership.  Round 73 would require
\(\mathfrak H_{C,k}^{(\kappa)}\ll_\varepsilon
X^\varepsilon J^2/T\).  No source checked below proves that estimate from
(73.2)--(73.5).

The proposed exponent-pair upgrade has one lawful and one unlawful part.
Bourgain's primary Theorem 6 proves the epsilon-shifted exponent pair
\((13/84+\varepsilon,55/84+\varepsilon)\), and it applies uniformly to the
pure reciprocal phase on any one residue progression or any one of its
subintervals.  It gives the ambient-scale cap

\[
 H_{\rm Bou}:=Q^{13/42}T^{55/84}=J^{31/60}.                    \tag{1.2}
\]

Abel summation lawfully inserts one cell weight satisfying (73.4).  It does
not, however, glue the \(O(Q)\) independently weighted Farey cells into
\(O(b)\) weights of bounded total variation.  The packet therefore gives only

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \min\{C,QH_{\rm Bou}\}
 =X^\varepsilon\min\{C,J^{11/12}\},                            \tag{1.3}
\]

not \(C Q^{-5/24}\).  Combined with the accepted third-derivative bound,
(1.3) is better only for \(C>J^{59/60}\), where it remains far above the
energy target.  If a new gluing lemma proved total variation
\(O_\varepsilon(BX^\varepsilon)\), one per residue progression rather than
one per Farey cell, then Bourgain would conditionally replace \(Q^{1/3}\) in
(73.7) by \(Q^{5/12}\) and extend the derivative-safe range to
\(C\le J^{13/18}\).  That gluing lemma is absent, so this extension is not
promotable.

The alternate small-modulus route also fails after an exact source audit.
In its ideal smooth odd model, \(c\)-Poisson with \(q=4b\) has stationary
index \(n\asymp Q^2\).  The positive Kuznetsov branch cancels the secondary
phase exactly and leaves a spectral coefficient sum

\[
 V_f=\sum_{n\asymp Q^2}
 \lambda_{f,\mathfrak a}(n)V_f(n/Q^2)e(-J\sqrt n),             \tag{1.4}
\]

for which the lossless normalization requires \(|V_f|\ll
Q^{3/2+\varepsilon}\).  Exact level-four GL(2) Voronoi summation switches
cusps and sends (1.4) to coefficients with

\[
 |m-X|\ll T,qquad
 V_f=\frac{Q^{3/2}}{J^{1/2}}
 \sum_{|m-X|\ll T}\lambda_{f,\mathfrak b}(m)
 \Psi_{f,C}\!\left(\frac{m-X}{T}\right)+\text{tails}.         \tag{1.5}
\]

Thus the required input is the pointwise short-coefficient bound
\(\sum_{|m-X|\ll T}\lambda_{f,\mathfrak b}(m)\Psi_{f,C}
\ll J^{1/2+\varepsilon}=X^{1/4+\varepsilon}\).  Even granting the
optimistic length bound \(T X^\varepsilon\), (1.5) is
\(Q^{1/2}J^{1/2}\), missing \(Q^{3/2}\) by
\(J^{1/10}=X^{1/20}\).  The primary square-root resonance asymptotic has
exactly the same error.  This is not the forbidden scalar
\(c\)-Poisson/\(B\)-process loop, but it is a genuine GL(2) resonance return
to the original product-wavelet deficit.

Finally, both spectral reductions are only odd, positive-index model
reductions until the periodic local unit, level-four cusp and scaling data,
transition transforms, continuous spectrum, and opposite orientation are
proved.  The two even local classes do not follow by a sign change.  The
accepted axis bound \(C^2/J\) is independently target-safe only through
\(C\le J^{3/4}\); axes remain open above that point.  No perfect-square or
fourth-power counterexample was found: the obstruction is the whole
\(T\)-wide near-resonant window, not its possible exact center.

## Exact statement and hypotheses

Put

\[
 J=X^{1/2},\qquad Q=X^{1/5}=J^{2/5},\qquad
 T=J/Q=J^{3/5},\qquad B=C/T,                                  \tag{2.1}
\]

and assume the frozen residual range
\(J^{32/45}<C\le J\), \(b\asymp B\), fixed compatible nonaxial
\(k=\rho\sigma>0\), and
\(\kappa\in\{1/4,1/2,1\}\).  Assume exactly the row identity (73.3), the
cellwise sup-plus-variation estimate (73.4), and the one-count capacity
(73.5).  No differentiability or factorization in \(b\), \(r\), or across
distinct \(\nu\)-cells is assumed.  The two axes are excluded from the
positive nonaxial row and retained separately.

Under only these hypotheses the following assertions are proved here.

1.  The literal diagonal of the energy satisfies

\[
 \mathcal D_{C,k}^{(\kappa)}
 :=\sum_{b\asymp B}\sum_{z\in\mathcal Z_b}|a_{b,z}|^2
 \ll_\varepsilon X^\varepsilon BC
 =X^\varepsilon\frac{C^2}{T}
 \le X^\varepsilon\frac{J^2}{T}.                              \tag{2.2}
\]

For any fixed nonzero denominator offset \(d\), the raw number of pairs
\(c'-c=d\) has the same capacity \(O(BC)\); a single offset layer is safe.
What is not controlled is the coherent accumulation of all nonzero offsets,
which is exactly (1.1).

2.  On one cell, write

\[
 \alpha=\frac r{4b},\qquad K_{\kappa,b}=\frac{A_{\kappa,b}}{4b},
 \qquad
 \frac{A_{\kappa,b}}{r+4b\ell}
 =\frac{K_{\kappa,b}}{\ell+\alpha}.                           \tag{2.3}
\]

Uniformly for all three \(\kappa\), \(K_{\kappa,b}\asymp X\) and
\(\ell+\alpha\asymp T\).  Bourgain's exponent pair, with its epsilon loss
absorbed into \(X^\varepsilon\), gives for every subinterval \(I\) of that
ambient progression

\[
 \left|\sum_{\ell\in I}e\!\left(\pm
       \frac{K_{\kappa,b}}{\ell+\alpha}\right)\right|
 \ll_\varepsilon X^\varepsilon
 \min\{|I|,H_{\rm Bou}\}.                                    \tag{2.4}
\]

The same estimate holds with one weight having the (73.4) norm.  Summing
(2.4) over the packet's cells proves (1.3), but no stronger row estimate.

3.  The Bettin--Chandee theorem may be mapped to the odd inverse fraction
with \(m=c\asymp C\), \(n=4b\asymp B\), and fixed \(a=k\), only after the
actual amplitude is separated.  Its permitted coupled phase perturbation
forces complexity \(\mathcal X\gg XB^2\), and therefore inserts the factor

\[
 \left(1+\frac{\mathcal X}{BC}\right)^{1/2}
 \gg (1+X/T)^{1/2}\asymp J^{7/10}.                            \tag{2.5}
\]

The source is consequently inapplicable at the target scale even before
the nonseparated Farey amplitude is restored.

4.  For the small-modulus spectral calculation, additionally assume an
ideal smooth odd row for which the periodic local unit has been identified
with the correct level-four character/cusp data and the cells have been
glued into common smooth tests with summable transform norms.  Under those
extra hypotheses, Poisson, Kuznetsov, and Voronoi give (1.4)--(1.5).  These
are exact transform reductions, not a bound.  The needed bound is

\[
 \boxed{\quad
 \sum_{|m-X|\ll T}\lambda_{f,\mathfrak b}(m)
 \Psi_{f,C}\!\left(\frac{m-X}{T}\right)
 \ll_\varepsilon J^{1/2+\varepsilon},
 \quad}                                                       \tag{2.6}
\]

uniformly over the Maass, holomorphic, and Eisenstein data produced by the
level-four trace formula, including the relevant cusps, oldforms, local
factors, and spectral width \(t_f^2\ll J/C\).  No audited source proves
(2.6).

5.  Assertions (1.4)--(2.6) do not include \(\kappa=1/2,1\), either zero
index, or a lift-dependent local unit.  Any theorem claiming the full row
must separately establish those local cases and the finite transform tails.

## Proof or derivation

**The exact energy decomposition.**  The one-count cells make
\(\mathcal Z_b\) a genuine disjoint index set.  Expanding the square gives

\[
 \mathcal E_{C,k}^{(\kappa)}
 =\mathcal D_{C,k}^{(\kappa)}+\mathfrak H_{C,k}^{(\kappa)}.     \tag{3.1}
\]

By (73.4)--(73.5),
\(\sum_{z\in\mathcal Z_b}|a_{b,z}|^2\ll X^\varepsilon C\).
There are \(O(B)\) values of \(b\), proving (2.2).  For a fixed offset
\(d\), each \(c\) has at most one partner \(c+d\), so that layer also has
at most \(O(BC)\) terms.  This calculation neither assumes nor creates
cancellation.  It shows that the target obstruction must involve many
off-diagonal layers or an alias family, not the literal diagonal or one
fixed near-diagonal layer.

For \(c'=c+d\), the phase separation at fixed \(b\) has scale

\[
 A_{\kappa,b}\left(\frac1c-\frac1{c+d}\right)
 \asymp \frac{bX}{C^2}d=\frac{JQ}{C}d.                        \tag{3.2}
\]

This is large for \(d\ne0\), but its distance to an integer is not
uniformly bounded below.  More importantly, the packet supplies no
bounded variation in \(b\) for the multiplier multiplying (3.2).
Consequently a continuous Hessian calculation or a first-derivative slogan
does not bound (1.1).  The Poisson indices derived below are precisely the
discrete aliases hidden by such a slogan.

**Exponent-pair audit.**  From (73.2),

\[
 K_{\kappa,b}
 =\frac X4+\frac{\sqrt{\kappa kX}}{2b}
   +\frac{\kappa k}{4b^2}\asymp X.                            \tag{3.3}
\]

For every fixed \(p\ge0\),

\[
 \frac{d^{p+1}}{d\ell^{p+1}}
 \frac{K_{\kappa,b}}{\ell+\alpha}
 =(-1)^{p+1}(p+1)!K_{\kappa,b}(\ell+\alpha)^{-p-2}.           \tag{3.4}
\]

Thus this is exactly the reciprocal \(\sigma=2\) exponent-pair model on
ambient scale \(N\asymp T\), with derivative parameter

\[
 Y=K_{\kappa,b}/T^2\asymp X/T^2=Q^2,
 \qquad \mathcal T=K_{\kappa,b}/T\asymp JQ.                  \tag{3.5}
\]

The direct Bourgain range also checks numerically:
\(\log T/\log(JQ)=3/7\), which lies between \(17/42\) and \(1/2\).
Bourgain's Theorem 6 and its proper-subinterval discussion therefore give

\[
 Y^{13/84}T^{55/84}
 =Q^{13/42}T^{55/84}=J^{31/60}.                               \tag{3.6}
\]

Discrete Abel summation multiplies the uniform partial-sum bound only by
\(\|w\|_\infty+\operatorname{Var}(w)\), so (73.4) proves (2.4) for one
cell.  Half-open endpoints add only \(O(\|w\|_\infty)\).

The hostile seam is the ambient scale.  If a cell has length \(L\ll T\),
then \(f'\asymp Q^2\) but
\(f^{(j)}\asymp Q^2T^{1-j}\); after rescaling by \(L\), these are not the
fixed reciprocal derivative relations with \(T\) replaced by \(L\).  The
source therefore gives \(\min(L,H_{\rm Bou})\), not
\(Q^{13/42}L^{55/84}\).  With at most \(QX^\varepsilon\) separately
weighted cells and total length \(O(C)\),

\[
 \sum_{r,\nu}\min\{|I_{b,r,\nu}|,H_{\rm Bou}\}
 \le \min\{C,QH_{\rm Bou}\},                                 \tag{3.7}
\]

which is (1.3).  No multiplication-free summation over neighbor pieces is
present in the source.

For comparison, a general exponent pair \((\eta,\lambda)\) on one full
progression would give

\[
 Q^{2\eta}T^\lambda
 =Q^{2\eta+3\lambda/2}
 =TQ^{-s},\qquad
 s=\frac32-2\eta-\frac{3\lambda}{2}.                          \tag{3.8}
\]

The classical \((1/6,2/3)\) has \(s=1/6\); its A-transform
\((1/14,11/14)\) has \(s=5/28\); Bourgain has
\(s=5/24\).  If, and only if, all cells on each fixed residue progression
could be glued with total variation \(O(X^\varepsilon)\), summing over the
\(O(B)\) residues would give

\[
 |S_b|\ll X^\varepsilon C Q^{-5/24},\qquad
 \mathcal E_C\ll X^\varepsilon
 \frac{C^3}{TQ^{5/12}}.                                      \tag{3.9}
\]

Then \(C^3\le J^2Q^{5/12}\) would be
\(C\le J^{13/18}\).  The A-transformed classical pair would similarly
give \(C\le J^{5/7}\).  These are conditional ledgers, not consequences
of (73.4), whose variation is per cell.  At \(C=J\), (3.7) gives a row of
size \(J^{11/12}\), while the energy target requires average row size
\(J^{1/2}\); the squared miss is \(J^{5/6}\).

**Reciprocal-fraction theorem.**  Bettin--Chandee treats separated
coefficients in

\[
 \sum_{a,m,n}\alpha_m\beta_n\nu_a
 e\!\left(\vartheta a\overline m/n\right).                   \tag{3.10}
\]

Map \(a=k\), \(m=c\asymp C\), and \(n=4b\asymp B\).  For
\(g(c,b)=-A_{\kappa,b}/c\), the leading derivatives are
\(|\partial_b g|\asymp X/C\) and
\(|\partial_c g|\asymp BX/C^2\).  Remark 1 requires
\(|\partial_n g|\ll\mathcal X/(B^2C)\) and
\(|\partial_m g|\ll\mathcal X/(BC^2)\), hence
\(\mathcal X\gg XB^2\).  Since \(BC=C^2/T\), the theorem's complexity
factor is (2.5).  Its displayed
\((AMN)^{7/20}(M+N)^{1/4}\) and
\((AMN)^{3/8}(AN+AM)^{1/8}\) terms therefore cannot compensate for this
loss.  Moreover, Remark 1 permits a coupled differentiable phase, not the
jointly varying transition amplitude and local unit in (73.3).

**Small-modulus Poisson and Kuznetsov.**  First suppress the preceding
actual-symbol seam.  For a smooth odd row with \(q=4b\), Poisson summation
has the form

\[
 \sum_c W_b(c)e_q(k\overline c)e(-A_{1/4,b}/c)
 =\frac1q\sum_n S(n,k;q)I_b(n),                               \tag{3.11}
\]

where

\[
 I_b(n)=\int W_b(x)e\!\left(-\frac{A_{1/4,b}}x-\frac{nx}{q}\right)dx.
                                                                    \tag{3.12}
\]

The stationary equation and critical phase are

\[
 n=\frac{qA_{1/4,b}}{x^2}\asymp\frac{B^2X}{C^2}=Q^2,         \tag{3.13}
\]

\[
 -2\sqrt{A_{1/4,b}n/q}
 =-\left(J+\frac{\sqrt k}{2b}\right)\sqrt n,                \tag{3.14}
\]

because
\(A_{1/4,b}/(4b)=(J/2+\sqrt k/(4b))^2\).  The same-sign
Kuznetsov argument is \(4\pi\sqrt{kn}/q\).  Its positive large-argument
branch is \(e(+2\sqrt{kn}/q)=e(+\sqrt{kn}/(2b))\), cancelling the second
term of (3.14) exactly.  The argument has scale

\[
 \frac{\sqrt n}{b}\asymp\frac QB=\frac JC=:R,                \tag{3.15}
\]

so the phase-matched transform has spectral width \(t_f^2\ll R\).  With
the standard \(S/q\) Kuznetsov normalization, the stationary integral at
\(b\asymp B\) has size

\[
 |I_b(n)|\asymp \frac{C^{3/2}}{\sqrt{BX}}
 =\frac{C}{\sqrt{JQ}}.                                      \tag{3.15a}
\]

This is the amplitude of the Kuznetsov test because the factor \(1/q\)
in (3.11) is already the geometric \(S/q\) normalization.  Phase matching
adds \(R^{-1/2}\), and Weyl capacity gives \(O(RX^\varepsilon)\) fixed-level
spectral modes with \(t_f^2\ll R\).  Thus the lossless absolute spectral
ledger outside (1.4) is

\[
 R\frac{C}{\sqrt{JQ}}R^{-1/2}
 =\sqrt{\frac CQ}.                                           \tag{3.15b}
\]

Since the first-moment target is
\(J\sqrt C/T=Q\sqrt C\), the corresponding coefficient-sum target is
exactly \(|V_f|\ll Q^{3/2+\varepsilon}\).  This calculation assumes
harmless fixed-index Fourier normalizations; their actual cusp/local
identification is one of the seams stated below.

For the actual row, (3.11) is already not established.  The residue sum is
in general

\[
 \mathcal K_b(n,k)=
 \sum_{r\bmod4b}^{*}u_{b,r,k}^{(1/4)}
 e_{4b}(k\overline r+nr),                                    \tag{3.16}
\]

not the standard \(S(n,k;4b)\), unless the periodic unit is identified
with exact character/cusp data.  Cellwise bounded variation also does not
give the smooth common \(W_b\) needed to truncate (3.12) and then use one
Kuznetsov test.  The even lifts produce different local sums again.

**Exact GL(2) Voronoi resonance.**  In Assing--Corbett's Corollary 6.3,
the dual Hankel argument for level \(N_0\), character conductor \(M\), and
additive denominator \(q_0\) is
\(m/[q_0^2,Mq_0,N_0]\), and the coefficients occur at the switched cusp.
Here \(N_0=4\) and the nonlinear sum has no rational additive twist, so
\(q_0=1\) and the argument is \(m/4\).  The positive Bessel branch in the
Hankel integral is therefore

\[
 e\!\left(+2\sqrt{(m/4)n}\right)=e(+\sqrt{mn}).               \tag{3.17}
\]

It cancels \(e(-J\sqrt n)\) exactly at \(m=X=J^2\).  Since
\(n\asymp Q^2\), integration by parts confines the dual index to

\[
 |\sqrt m-J|\,Q\ll1,qquad |m-X|\ll J/Q=T.                   \tag{3.18}
\]

The Bessel amplitude is \((mn)^{-1/4}\); integrating over a primal interval
of length \(Q^2\) gives

\[
 Q^2(J^2Q^2)^{-1/4}=Q^{3/2}J^{-1/2},                         \tag{3.19}
\]

which proves the scale in (1.5).  Granting a length bound \(T\) for the
dual coefficient sum gives

\[
 |V_f|\ll X^\varepsilon\frac{Q^{3/2}}{J^{1/2}}T
 =X^\varepsilon Q^{1/2}J^{1/2}
 =X^\varepsilon Q^{3/2}J^{1/10}.                             \tag{3.20}
\]

Thus exact Voronoi does not remove the deficit; it identifies it.

The primary resonance formula quoted by Ye (from Iwaniec--Luo--Sarnak,
Appendix C) states for a fixed full-level holomorphic cusp form, a fixed
smooth \(\phi\), and integer \(q_0>0\),

\[
 \sum_n\lambda_f(n)e(-2\sqrt{nq_0})\phi(n/N)
 =q_0^{-1/4}\lambda_f(q_0)N^{3/4}\widehat B(0)
  +O_\varepsilon((q_0N)^{1/4+\varepsilon}).                  \tag{3.21}
\]

Taking \(q_0=X/4\) when this is an integer and \(N=Q^2\), the main term
has size \(J^{-1/2}Q^{3/2}=J^{1/10}\), while the error is

\[
 (XQ^2)^{1/4}=J^{1/2}Q^{1/2}
 =Q^{3/2}J^{1/10}.                                           \tag{3.22}
\]

The best directly relevant primary resonance asymptotic therefore has the
same \(X^{1/20}\) miss.  It also does not cover the level-four moving
Maass, holomorphic, and Eisenstein family or the transition-dependent
profiles in (2.6).

An exact center contributes only one term of (1.5), of size
\(Q^{3/2}J^{-1/2}=J^{1/10}\) up to coefficient factors, well below
\(Q^{3/2}\).  Since consecutive squares near \(X\) are spaced by
\(\asymp J>T\), the window contains \(O(1)\) squares; fourth powers are
still sparser.  Perfect powers are therefore not the obstruction.  The
generic \(T\)-term near-resonant window is.

**Other source capacities.**  Blomer--Risager--Shparlinski prove

\[
 \sum_{N\le|n|<2N}\left|\sum_{c\le Z}S(n,1;c)\right|^2
 \ll (NZ^2+N^{1/3}Z^{7/3})(NZ)^{o(1)}.                       \tag{3.23}
\]

At \(N=Q^2\), \(Z=B\), the leading diagonal is sharp.  After the
modulus normalization and Cauchy over the \(Q^2\) primal indices, it gives
the scale \(Q^2\), missing the required \(Q^{3/2}\) by \(Q^{1/2}\).
It also lacks modulus \(4b\), fixed \(k\), the phase-matched test, and the
actual coefficient matrix.

Blomer--Pascadi's Theorems 1.1 and 5.5 are fixed-modulus bilinear bounds
with arbitrary separated sequences and save \(c^{-1/32}\) in the balanced
critical range \(M=N\asymp\sqrt c\).  Here the modulus varies, one
arithmetic index is fixed, \(n\asymp Q^2\) need not lie below the modulus,
and the transition amplitude is coupled.  Even the fantasy saving
\(Q^{-1/32}\) is much smaller than the \(Q^{-1/2}\) missing before Voronoi
or the \(J^{-1/10}=Q^{-1/4}\) missing after it.

Pascadi's regular spectral large sieve has cost
\(K^2+\mu(\mathfrak a)N^{1+\varepsilon}\) for coefficients supported at
index magnitude \(N\).  Applied after (1.5), this pays \(N\asymp X\), not
the span \(T\).  His frequency-concentrated improvement concerns the
exceptional spectrum and does not remove the regular Maass, holomorphic,
or Eisenstein parts.  His generic Bessel-transform lemma assumes a slowly
varying test and does not accept the phase-matched oscillation as a black
box.  Hence neither the standard nor exceptional large sieve proves
(2.6).

## First doubtful or unproved step

For the direct hybrid route, the first missing mathematical input is a
bound for the actual-symbol correlation (1.1).  The packet has enough
information to identify and bound its diagonal, but it has no regularity
or factorization in \(b\) or \(r\) with which to apply a two-variable
large sieve.  Replacing the local units by arbitrary coefficients would
discard the only possible arithmetic cancellation; replacing them by a
separated product is not an identity.

For the exponent-pair proposal, the first false step would be either
rescaling a short cell of length \(L\) as though the reciprocal ambient
scale were \(L\), or applying the full-progression estimate once per
residue without paying the jumps between the \(O(Q)\) Farey cells.  The
source lawfully proves (2.4), and Abel lawfully handles each BV cell.  What
is unproved is the gluing estimate

\[
 \sum_{r\bmod4b}
 \big(\|W_{b,r}\|_\infty+\operatorname{Var}W_{b,r}\big)
 \ll_\varepsilon BX^\varepsilon,                             \tag{4.1}
\]

for globally glued progression weights \(W_{b,r}\).  The packet gives the
corresponding sum only at cell count \(O(QX^\varepsilon)\).

For either spectral route, the first actual-row seam comes even earlier:
the local residue unit and the Farey entry/exit cells must be transformed
into the precise level-four cusp/character Kloosterman family with common
smooth tests and summable Fourier/Bessel norms.  Bounded variation is
sufficient for Abel summation but not, by itself, for arbitrary repeated
Poisson, stationary-phase, and Kuznetsov integrations by parts.  The exact
even lifts and the zero indices must be derived separately.

Even after granting that ideal decomposition, the first missing analytic
theorem is (2.6).  Exact Voronoi and the primary resonance formula show
that this gap is not a normalization accident: they reproduce the
\(X^{1/20}\) deficit.  A cusp-form-only assertion would still leave the
Eisenstein integral and possible residues untreated.

## Required control test and outcome

| Control | Outcome |
|---|---|
| Inherited row normalization | **Pass.** All comparisons use \(\mathcal E\ll J^2/T\) and the first-moment scale \(J\sqrt C/T\), with \(B=C/T\).  The model small-modulus ledger needs \(V_f\ll Q^{3/2}\), not \(Q\) or \(T^{1/2}\). |
| Residue-progression one-count | **Pass.** The diagonal uses the exact half-open \(z=(r,\nu,\ell)\) ownership.  No boundary is duplicated. |
| Transition BV | **Pass per cell; fail for gluing.** Equation (73.4) supports Abel on one cell.  It does not prove (4.1), and multiplying a full-progression saving by no piece cost is forbidden. |
| Energy deficit | **Fail to close.** The accepted deficit is \(C^3/(J^2Q^{1/3})\).  Bourgain gives no packet-level replacement.  The spectral resonance misses by \(J^{1/10}=X^{1/20}\). |
| Diagonal and near diagonal | **Diagonal pass; off-diagonal open.** The diagonal and each fixed offset layer have capacity \(BC=C^2/T\le J^2/T\).  Coherent accumulation over offsets is (1.1).  Phase scale \((JQ/C)d\) alone does not control integer aliases. |
| Analytic rank and aliases | **No extra saving found.** The continuous leading \((b,c)\)-phase is nondegenerate, but the discrete multiplier has no \(b\)-regularity.  Exact \(c\)-Poisson exposes \(n\asymp Q^2\); Kuznetsov plus Voronoi sends the phase-matched aliases to \(m=X+O(T)\), so there is only one unresolved resonant direction. |
| Inverse local unit | **Open for spectral use.** The actual Poisson sum is (3.16), not automatically \(S(n,k;4b)\).  Bettin--Chandee also does not accept the coupled amplitude. |
| Even local classes | **Derivative phase passes; spectral transfer fails.** Bourgain applies to (73.3) after the exact even unit is frozen on a residue.  The \(c\equiv2\pmod4\) and \(4\mid c\) lifts do not become the odd Kuznetsov cusp by changing a sign. |
| Axes and gcds | **Open above \(J^{3/4}\).** The accepted axis contribution \(C^2/J\) is at most the fixed-block target \(J^{1/2}\) only for \(C\le J^{3/4}\).  Positive fixed \(k\) has only divisor-size gcd losses; at zero index Ramanujan/twisted Gauss sums can have gcd of size \(c\). |
| Perfect squares and fourth powers | **Pass as a counterexample test.** At most \(O(1)\) such centers lie in the \(T\)-window, and one exact resonant term has scale \(J^{1/10}\), below \(Q^{3/2}\).  They furnish no lower-bound obstruction and no saving. |
| Finite dual and error sums | **Pass only for the inherited derivative method.** New Poisson/Voronoi routes require fresh smooth truncation, stationary transition, Bessel-tail, opposite-sign, oldform, and Eisenstein error estimates.  They are not inherited from (73.4). |
| Source applicability | **Fail for closure.** Bourgain is lawful only at ambient scale and per BV cell; Bettin--Chandee pays (2.5); the Kloosterman moments give \(Q^2\); fixed-modulus bilinear saving is too small; the regular spectral large sieve pays index magnitude; no short-Hecke theorem gives (2.6). |
| Self-return avoidance | **Pass with qualification.** The direct off-diagonal and odd completion routes do not repeat the forbidden scalar loop.  The small-modulus diagnostic is allowed, but exact GL(2) Voronoi returns to the same \(X^{1/20}\) resonance deficit and cannot be counted as a second independent saving. |
| Downstream scope | **Pass.** Nothing here concerns cone edges or proves full \(M9\!-M1\), \(M9\), or the Gauss-circle exponent.  The conditional \(J^{13/18}\) range is not an accepted extension. |

## Dependencies and exact artifacts/sources used

The repository artifacts used were exactly:

* protocol.md;
* state/proof_obligations.yml;
* state/active_campaign.yml;
* rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/briefs/hybrid_spectral_source_hostile_audit.md;
* rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/derivation_packet.md;
* rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/synthesis.md;
* rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_reciprocal_source_hostile_audit.md.

No sibling Round-73 report was read.

The primary-source audit was as follows.

* **Exponent pair and proper subintervals.**  Jean Bourgain,
  [*Decoupling, exponential sums and the Riemann zeta function*, J. Amer.
  Math. Soc. 30 (2017), 205--224](https://arxiv.org/pdf/1408.5794),
  DOI 10.1090/jams/860, Theorem 4 and Section 5, Theorem 6.  The literal
  result is \((13/84+\varepsilon,55/84+\varepsilon)\), so the endpoint
  notation used above is only in the repository's \(X^\varepsilon\)
  convention.  Section 5 explicitly treats a proper subinterval by a phase
  extension and an \(O(\log M)\) partial-sum loss.  The cited primary
  subinterval device is P. Sargos,
  [*Points entiers au voisinage d'une courbe, sommes trigonométriques
  courtes et paires d'exposants*, Proc. London Math. Soc. (3) 70 (1995),
  285--312](https://doi.org/10.1112/plms/s3-70.2.285), Lemma 2.1.
  Neither source licenses replacing the ambient reciprocal scale \(T\) by
  a much shorter neighbor-cell length.

* **Trilinear inverse fractions.**  Sandro Bettin and Vorrapan Chandee,
  [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/html/1502.00769),
  Theorem 1 and Remark 1.  The exact derivative hypotheses in Remark 1
  yield \(\mathcal X\gg XB^2\) and hence (2.5); its coefficient sequences
  remain separated.

* **General-level Voronoi.**  Edgar Assing and Andrew Corbett,
  [*Voronoï summation via switching cusps*, Monatsh. Math. 194 (2021),
  657--685](https://arxiv.org/pdf/1904.02025), DOI
  10.1007/s00605-021-01537-5, Theorem 6.2, Corollary 6.3, and Hankel
  formulae (38)--(39).  Corollary 6.3 has dual argument
  \(m/[q^2,Mq,N]\) and coefficients at the switched cusp.  For level four
  and \(q=1\), this is \(m/4\), giving exactly (3.17)--(3.19), not a
  full-level \(m\)-normalization.

* **Square-root resonance.**  Yangbo Ye,
  [*Bounds toward Hypothesis S for cusp forms*, J. Number Theory 236
  (2022), 128--143](https://doi.org/10.1016/j.jnt.2021.07.012), equation
  (1.2), records (3.21) and attributes the underlying formula to Henryk
  Iwaniec, Wenzhi Luo, and Peter Sarnak,
  [*Low lying zeros of families of L-functions*, Publ. Math. IHÉS 91
  (2000), 55--131](https://www.numdam.org/article/PMIHES_2000__91__55_0.pdf),
  Appendix C.  Its error gives (3.22); its hypotheses are narrower than
  the level-four family here.

* **Kuznetsov and spectral large sieve.**  Alexandru Pascadi,
  [*Large sieve inequalities for exceptional Maass forms and the greatest
  prime factor of \(n^2+1\)*, Forum Math. Pi 14 (2026), e8](https://doi.org/10.1017/fmp.2026.10025),
  Proposition 3.5, Lemmas 3.4 and 3.9, and Theorem 5.2.  Proposition 3.5
  requires specified cusps and positive indices; Lemma 3.9 pays the index
  magnitude; Lemma 3.4 is a slowly-varying-test statement; Theorem 5.2 is
  exceptional-spectrum frequency concentration, not a replacement for all
  regular and continuous terms.

* **Modulus second moment.**  Valentin Blomer, Morten S. Risager, and
  Igor E. Shparlinski,
  [*Triple sums of Kloosterman sums and the discrepancy of modular
  inverses*, arXiv:2411.17823v3](https://arxiv.org/abs/2411.17823),
  Theorem 1.3.  Its exact leading term yields (3.23) and the \(Q^2\)
  capacity at the present parameters.

* **Fixed-modulus phase-specific bilinear estimate.**  Valentin Blomer
  and Alexandru Pascadi,
  [*Bilinear forms with Kloosterman sums via quadratic characters*,
  arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311), Theorems 1.1 and
  5.5.  Its \(c^{-1/32}\) critical saving is for one fixed modulus and
  separated intervals near \(\sqrt c\), not (3.16) or (1.4).

* **Level, cusp, character, and zero-index warning.**  Andrew Knightly and
  Charles Li,
  [*Kuznetsov's trace formula and the Hecke eigenvalues of Maass forms*,
  Mem. Amer. Math. Soc. 224 (2013)](https://arxiv.org/abs/1202.0189),
  Theorems 7.14, 8.1, and 9.2.  The generalized sums depend on exact
  scaling matrices, level, nebentypus, cusps, and gcd data; the source does
  not identify the two even lifts or dispose of zero indices automatically.

* **Pointwise short-coefficient status.**  J. L. Hafner and A. Ivić,
  [*On sums of Fourier coefficients of cusp forms*, Enseign. Math. 35
  (1989), 375--382](https://www.e-periodica.ch/cntmng?pid=ens-001%3A1989%3A35%3A%3A150),
  gives the classical pointwise scale and discusses the conjectural
  \(X^{1/4+\varepsilon}\) barrier.  Hulse, Kuan, Lowry-Duda, and Walker,
  [*The Second Moment of Sums of Coefficients of Cusp Forms*](https://arxiv.org/abs/1512.01299),
  proves averaged second-moment statements, not (2.6) uniformly over the
  required level-four spectrum.

Every imported theorem was checked at the actual summation variable,
ambient scale, index magnitude and span, modulus, level, cusp, character,
coefficient dependence, smoothing, zero indices, and spectral family.

## Recommended state effect

**Retain (73.8) open and reject all claimed full residual closures.**
Promote no new conductor range from the exponent-pair calculation.  Record
as source-verified evidence that Bourgain applies to each exact reciprocal
cell at ambient scale \(T\), giving (2.4), and record the sharp no-go that
(73.4)--(73.5) aggregate it only to (1.3).  Retain (4.1) as the smallest
additional transition lemma which would make the conditional energy
\(C^3/(TQ^{5/12})\) and the conditional range \(C\le J^{13/18}\) valid.

Retain (2.2) and (1.1) as the exact diagonal/off-diagonal split.  The direct
hybrid problem should be formulated against \(\mathfrak H\) with the actual
local units and cell symbols; Bettin--Chandee is rejected as a closing
import at these parameters.

Retain the small-modulus Poisson--Kuznetsov--Voronoi chain only as a
conditional exact model reduction.  Record its smallest analytic survivor
as (2.6), together with the exact center \(m=X+O(T)\), switched level-four
cusp, and unavoidable \(X^{1/20}\) deficit.  Do not promote it until the
actual unit/transition decomposition, all spectral components, and a
uniform short-coefficient theorem are proved.

Keep the even spectral families, both axes, and zero-index gcd terms open.
The accepted axis estimate may be used through \(C\le J^{3/4}\) only; it
does not settle \(J^{3/4}<C\le J\).  Make no downstream change to cone
edges, full \(M9\!-M1\), \(M9\), or the Gauss-circle exponent.
