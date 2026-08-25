## 1. Result

Decision label: `strict_signed_farey_reduction`.

Write

\[
 c_{a,b}:=\lambda_bJ_{R,y}(a/b),\qquad
 \theta_{a,b}:=\frac{aN}{b}\pmod 1
\]

on the literal reduced support, and define the ordered, real, cross-denominator nonresonant survivor

\[
 \mathscr C_N^{\star}:=
 \sum_{\substack{b\ne b'\\bb'\nmid N(ab'-a'b)}}
 \ \sum_{a,a'}
 c_{a,b}\overline{c_{a',b'}}
 e\!\left(\frac{N(ab'-a'b)}{bb'}\right).
 \tag{1.1}
\]

The numerator sums in (1.1) have exactly the coprimality and literal-profile support in (138.B4). Uniformly for real \(X\ge2\),

\[
 \boxed{\ |\mathcal F_N|^2=\mathscr C_N^{\star}
       +O_{\varepsilon,V_{\rm low},\eta}(yX^\varepsilon).\ }
 \tag{1.2}
\]

More precisely, the scalar diagonal is \(O(y)\), the entire same-denominator square (including unequal numerators) is \(O(y\log ^2(2X))\), and the absolute mass of every remaining exact phase-one pair is \(O_\varepsilon(yX^\varepsilon)\). Thus (138.T) is reduced to the one-sided bound \(\mathscr C_N^{\star}\ll_\varepsilon yX^\varepsilon\). This is a genuine strict reduction of the exact scalar square: no coefficient, lift, primitive-numerator condition, profile value, floor, or scalar sign has been changed.

I do not obtain the required estimate for (1.1). The first structural obstruction is explicit. Character Poisson summation turns an interior \(d\)-block of (138.B5) into stationary modes with phase \(e(\sqrt{Nhr})\), weight \(N^{1/4}(hr)^{-3/4}\), and the actual sign \(\chi_4(r)\). Their modewise absolute capacity is \(\asymp X^{3/8}\), rather than the target \(X^{1/4}\), and the stationary Legendre transform is involutive. Grouping \(n=hr\) leaves a signed, truncated divisor coefficient and demands a further \(y^{1/4}\)-saving. At fourth-power centres, square \(n\) are exact phase-one modes. Hence the transform is a self-return, not a proved contraction.

## 2. Exact statement and hypotheses

Let \(X,R,y,N,J_{R,y},L_\chi,\lambda_b\) be exactly as in the statement-only problem. Put

\[
 \mathcal A_b:=\{1\le a<b:(a,b)=1, J_{R,y}(a/b)\ne0\}.
\]

The proof of the advertised reduction (138.B5) to (138.B4) uses the following support fact implicit in the words “small positive arc”: every nonzero term of (138.B5) has \(0<h/d<1\) and lies in the unwrapped positive chart on which (138.B1) is defined. This is necessary. The displayed inequality \(h/d<C/R\) by itself would not imply \(h<d\) for all \(X\ge2\) if its unspecified constant were allowed to be large. If the literal multiplier did reach \(h/d\ge1\), then (138.B4), with \(1\le a<b\) and periodic \(J\), would miss those terms and would have to be repaired by retaining all unwrapped coprime numerators \(a\ge b\). Under the stated small-arc convention, no repair is needed.

For every sampled reduced fraction, \(b\le y\) and \(a\ge1\) imply \(ya/b\ge1\). Consequently

\[
 \eta(ya/b)=1,
 \qquad
 J_{R,y}(a/b)=\frac b a
 V_{\rm low}(4R^2a^2/b^2),
 \qquad
 a<Cb/R.
 \tag{2.1}
\]

The alternating odd harmonic sum is not merely bounded above: for every \(T\ge1\),

\[
 \frac23\le L_\chi(T)\le1.
 \tag{2.2}
\]

Indeed its nonzero terms are the successive partial sums of
\(1-1/3+1/5-\cdots\). Thus, for odd \(b\le y\), \(\lambda_b\) has the exact direction \(\chi_4(b)\) and

\[
 \frac{2}{3b}\le |\lambda_b|\le\frac1b,
 \qquad |c_{a,b}|\ll\frac1a.
 \tag{2.3}
\]

Only the upper bound in (2.3) is used in proving (1.2). No positivity or lower envelope for \(V_{\rm low}\) is assumed there. Smooth stationary-phase statements below are applied only after inserting a compactly supported smooth dyadic cutoff strictly inside the \(d\)-range; they are a diagnosis of the remaining survivor, not an input to (1.2).

## 3. Proof or derivation

First verify the lift identity. In a nonzero term of (138.B5), put

\[
 g=(h,d),\qquad h=ag,\qquad d=bg,qquad (a,b)=1.
\]

The small-arc support gives \(1\le a<b\). Since \(d\le y\), one has \(g\le y/b\), and (2.1) gives \(\eta(ya/b)=1\). For a fixed reduced \(a/b\), the sum of all its lifts is exactly

\[
 \begin{aligned}
 &\sum_{g\le y/b}\frac{\chi_4(bg)}{ag}
 V_{\rm low}(4R^2a^2/b^2)e(aN/b)\\
 &\quad=\frac{\chi_4(b)}aL_\chi(y/b)
 V_{\rm low}(4R^2a^2/b^2)e(aN/b)\\
 &\quad=\lambda_bJ_{R,y}(a/b)e(aN/b).
 \end{aligned}
 \tag{3.1}
\]

Even \(b\) vanish because \(\chi_4(b)=0\); even lifts are already zero inside \(L_\chi\). There is no lift multiplicity beyond the single sum in (3.1). The residue centre \(b=1\) is zero because it is the periodic point \(0\) and \(J_{R,y}(0)=0\). This proves the exact identity, including its character direction.

For the scalar diagonal, (2.3) yields

\[
 \sum_b\sum_{a\in\mathcal A_b}|c_{a,b}|^2
 \ll \sum_{b\le y}\sum_{a\le Cb/R}\frac1{a^2}
 \ll y.
 \tag{3.2}
\]

Reduced fractions are unique, so \(ab'-a'b=0\) is exactly \((a,b)=(a',b')\). This proves (138.B8), without an \(X^\varepsilon\) loss.

Now retain all unequal numerators at a fixed denominator instead of calling them diagonal. Let

\[
 A_b:=\sum_{a\in\mathcal A_b}e(aN/b)J_{R,y}(a/b).
\]

By (2.1),

\[
 |A_b|\ll b\sum_{a\le Cb/R}\frac1a
 \ll b\log(2+b/R).
\]

Therefore the complete \(b=b'\) portion of the exact scalar square is

\[
 \mathscr S_=:=\sum_b|\lambda_b|^2|A_b|^2
 \ll y\log^2(2X).
 \tag{3.3}
\]

In particular, if \(\mathscr U_=\) denotes only \(a\ne a'\) at equal \(b\), then
\(|\mathscr U_=|\le \mathscr S_=+(3.2)\ll y\log^2(2X)\). No assertion of termwise positivity for \(\mathscr U_=\) is being made.

It remains to remove exact phase-one pairs at different denominators. The following phase-class count uses the actual coefficient bound and the arithmetic of \(N\). Given \((a,b)=1\), set

\[
 g=(b,N),\qquad q=b/g.
\]

Then \(g\mid N\), \((q,N/g)=1\), and \(e(aN/b)\) is a primitive \(q\)-th root (with the single phase \(1\) when \(q=1\)). Conversely, in a fixed reduced phase class \(r/q\), every possible denominator has the form

\[
 b=qg,qquad g\mid N,qquad (q,N/g)=1,qquad qg\le y,
 \tag{3.4}
\]

and its numerator lies in one invertible residue class \(s=s(q,g,r)\pmod q\). Dropping only the extra condition \((a,g)=1\), define

\[
 H_{q,g,s}:=
 \sum_{\substack{a\le Cqg/R\\a\equiv s\ (q)}}\frac1a.
\]

For \(1\le s\le q\),

\[
 H_{q,g,s}\ll \frac1s+\frac{\log(2+g/R)}q,
\quad
 \sum_{s=1}^qH_{q,g,s}^2
 \ll1+\frac{\log^2(2+g/R)}q.
 \tag{3.5}
\]

Let \(E_0\) be the sum of \(|c_{a,b}c_{a',b'}|\) over all pairs with equal phases. Cauchy--Schwarz over the possible divisors \(g\), followed by (3.5), gives

\[
 \begin{aligned}
 E_0
 &\ll \tau(N)
 \sum_{q\le y}\ \sum_{\substack{g\mid N\\qg\le y}}
 \left(1+\frac{\log^2(2+g/R)}q\right)\\
 &\ll \tau(N)^2\bigl(y+\log^3(2y)\bigr)
 \ll_\varepsilon yX^\varepsilon.
 \end{aligned}
 \tag{3.6}
\]

The \(q=1\) convention in (3.5) simply means the one phase class \(0/1\). This class contains all \(b\mid N\) and all their allowed primitive numerators, so divisors of \(N\) have not been omitted. Equality of the two phases is exactly

\[
 \frac{N(ab'-a'b)}{bb'}\in\mathbb Z
 \quad\Longleftrightarrow\quad
 bb'\mid N(ab'-a'b).
 \tag{3.7}
\]

Splitting the exact square into (3.3), the cross-denominator part of (3.6), and (1.1) proves (1.2).

For completeness, here is the exact stationary obstruction encountered when one tries to estimate (1.1) by undoing its lifts. The character identity

\[
 \chi_4(d)=\frac{e(d/4)-e(-d/4)}{2i}
 \tag{3.8}
\]

retains the true signs. On a smooth dyadic \(d\)-block, Poisson summation gives integrals

\[
 I_{k,\sigma}=\int W(t/D)V_{\rm low}(4R^2h^2/t^2)
 e\!\left(\frac{Nh}{t}+(\sigma/4-k)t\right)dt,
 \qquad \sigma\in\{1,-1\}.
 \tag{3.9}
\]

Stationarity requires \(\rho:=\sigma/4-k>0\). Writing \(r=4\rho\), the two branches give respectively \(r\equiv1\pmod4\) and \(r\equiv3\pmod4\), and their relative sign in (3.8) is exactly \(\chi_4(r)\). The stationary point, phase, curvature, and unchanged literal profile are

\[
 t_0=2\sqrt{Nh/r},\qquad
 \frac{Nh}{t_0}+\frac r4t_0=\sqrt{Nhr},
\]

\[
 \left(\frac{Nh}{t}+\frac r4t\right)''_{t=t_0}
 =\frac{r^{3/2}}{4(Nh)^{1/2}},qquad
 V_{\rm low}(4R^2h^2/t_0^2)
 =V_{\rm low}(R^2hr/N).
 \tag{3.10}
\]

Thus the leading stationary term, after restoring the factor \(1/h\) from (138.B5), has the exact arithmetic shape

\[
 \frac{e(1/8)}i,N^{1/4}
 \frac{\chi_4(r)}{(hr)^{3/4}}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
 \tag{3.11}
\]

times the literal block/endpoint weight. Nonstationary modes are handled by integration by parts, but the modes (3.11) cannot be so removed. Grouping \(n=hr\) produces a truncated signed divisor coefficient

\[
 \mathfrak a_y(n)=
 \sum_{hr=n}\chi_4(r)\,\omega_y(h,r),
 \tag{3.12}
\]

where \(\omega_y\) retains the hard condition \(t_0\le y\), hence
\(r\ge4Nh/y^2\), along with the actual one-sided endpoint factors. The resulting phase sum is of the form

\[
 N^{1/4}\sum_{n\ll N/R^2}
 \frac{\mathfrak a_y(n)}{n^{3/4}}
 V_{\rm low}(R^2n/N)e(\sqrt{Nn}).
 \tag{3.13}
\]

Taking moduli before the \((h,r)\)- or \(n\)-sum costs

\[
 N^{1/4}\sum_{n\ll y}\tau(n)n^{-3/4}
 \ll X^{3/8}\log(2X),
 \tag{3.14}
\]

and this capacity exponent is real, not an artefact of arbitrary coefficients. If the fixed nonzero multiplier has \(|V_{\rm low}(u)|\ge c>0\) on any compact interval, the actual \(h=1\), odd-\(r\) stationary modes with \(R^2r/N\) in that interval already have total individual magnitude \(\asymp X^{3/8}\). They must cancel with their actual phases and signs; no rowwise modulus is affordable.

Finally, the stationary Legendre phase is self-reciprocal. If \(A=Nh\), then the first transform sends \(A/t\) to \(2\sqrt{A\rho}\). Transforming back, the stationary equation for
\(2\sqrt{A\rho}-\rho t\) is \(\rho=A/t^2\), and its value is \(A/t\). Exact Poisson inversion says the same thing without asymptotic notation. Therefore (3.13), absent a new signed estimate, is a return of the original reciprocal-phase problem rather than a contraction.

## 4. First doubtful or unproved step

The first unproved step is a uniform signed estimate for the grouped stationary sum (3.13), together with its one-sided \(d=y\) transition terms. At target scale it would require, schematically,

\[
 \sum_{n\ll y}\frac{\mathfrak a_y(n)}{n^{3/4}}
 V_{\rm low}(R^2n/N)e(\sqrt{Nn})
 \ll_\varepsilon X^\varepsilon,
 \tag{4.1}
\]

where \(\mathfrak a_y(n)\) is the actual truncated divisor-character sum (3.12), not an arbitrary array. Absolute summation gives only \(y^{1/4}X^\varepsilon\), exactly the missing factor.

There is no phase-uniform nonstationary argument for (4.1). At a fourth-power centre \(X=q^4\), one has \(R=q\), \(y=q^2\), \(N=y^2\), and

\[
 e(\sqrt{Nn})=1\qquad(n\text{ a square}).
 \tag{4.2}
\]

For example the interior mode \(h=1,r=25\) has \(t_0=2y/5<y\), actual sign \(\chi_4(25)=1\), and exact phase one. If \(V_{\rm low}(0)\ne0\), its single leading contribution is already a nonzero constant times \(R\), showing that the requested scale is sharp. If \(V_{\rm low}(0)=0\), that particular saturation statement is unavailable from the supplied hypotheses, but the \(X^{3/8}\) modewise capacity on any nonzero profile interval remains. A proof must exploit cancellation among the nonsquare phases and the exact divisor-character coefficient; applying the stationary transform again only recovers the starting phase.

## 5. Required controls and outcomes

- **Literal flat cone to reduced Farey scalar.** Input: (138.B5) with the literal smooth multiplier. Outcome: (3.1) proves the identity term by term, conditional only on the stated small-arc containment \(h<d\). The numerical inequality in (138.B2) alone is insufficient to encode that containment for small \(X\) unless the literal support constant is correspondingly small. Implication: the small-arc convention must remain an explicit hypothesis of the identity.

- **Lift character and the \(b=1\) centre.** Input: \(d=bg,h=ag\). Outcome: all lifts aggregate once and only once to \(\chi_4(b)L_\chi(y/b)/a\); even lifts vanish, and the periodic residue centre is killed by \(J(0)=0\). The stronger bound (2.2) fixes the coefficient direction as \(\chi_4(b)\).

- **Profile, floors, support, and both signs.** Input: literal rational samples. Outcome: \(\eta=1\) at every sample; the upper numerator endpoint remains the smooth condition \(V_{\rm low}(4R^2a^2/b^2)\ne0\), not a sharp substitute. The opposite scalar is the conjugate and gives the same square. No centre averaging is used.

- **Exact scalar square and diagonal.** Input: reduced fractions. Outcome: determinant zero is equality of the fractions, and (3.2) is \(O(y)\) with no logarithmic loss.

- **Same denominator, unequal numerators.** Input: the entire fixed-\(b\) exponential polynomial. Outcome: (3.3) controls its full square by \(O(y\log^2X)\), and hence controls its unequal-numerator remainder. Taking each \((a,a')\) modulus separately is unnecessary.

- **Cross-denominator determinant arithmetic.** Input: \(\Delta=ab'-a'b\). Outcome: exact phase one is precisely (3.7). Reducing each individual phase by \((b,N)\) gives the phase-class parametrisation (3.4), not a rowwise modulus or a separated Fourier-index energy.

- **Exact and near phase one.** Input: all exact classes, including \(b\mid N\). Outcome: their complete absolute mass is (3.6), so exact resonance is target-square affordable. Near resonance is genuinely larger. At \(N=y^2\), writing \(b=y-r\) gives the exact endpoint identity
  \[
  e(aN/b)=e\!\left(\frac{ar^2}{y-r}\right).
  \]
  For fixed \(a\) and \(r\ll\sqrt{\delta y/a}\), these phases lie in a \(O(\delta)\) arc. Thus near phase one cannot be inferred from the exact-class divisor count.

- **Fourth-power centre, \(b\) near \(y\), and character pairing.** Input: \(X=q^4\). For \(b>y/3\), \(L_\chi(y/b)=1\). In the primitive \(a=1\) row, adjacent odd denominators have opposite \(\chi_4\)-signs. Pairing \(r\) and \(r+2\) in the preceding endpoint formula reduces the slowly varying range \(r\le W\ll\sqrt y\) to its endpoint plus total variation \(O(1+W^2/y)\), whereas retaining only one congruence class would have unsigned size \(\asymp W\) whenever the profile has a lower envelope there. Implication: a same-sign subfamily is not evidence for the full scalar; the true character cancels the endpoint centre to first order.

- **Stationary dual modes.** Input: the same exact character pairing away from the endpoint. Outcome: cancellation fails precisely where \(Nh/d^2\) is an integer plus \(1/4\) or \(3/4\). Equations (3.9)--(3.13) retain both branches and show that these modes carry the actual dual sign \(\chi_4(r)\). Square \(n\) at fourth-power centres satisfy the exact dual phase-one test (4.2).

- **Scalar capacity and directionality.** Input: actual \(\lambda_b,J\), and \(\chi_4\). Outcome: the original scalar has absolute capacity \(O(y\log X)\), its square \(O(y^2X^\varepsilon)\), and removing the controlled sets in (1.2) does not lower that exponent. In the dual description, modewise modulus has the sharper diagnosed capacity \(X^{3/8}\), still a factor \(y^{1/4}\) above target. Arbitrary signs, absolute values, or adversarial phases destroy the endpoint pairing and the divisor-character grouping, so none may replace the actual coefficients.

- **Transform contraction or self-return.** Input: exact character Poisson followed by stationary phase. Outcome: the profile becomes \(V_{\rm low}(R^2n/N)\) exactly, the phase becomes \(\sqrt{Nn}\), and the Legendre calculation after (3.14) returns \(Nh/d\). There is no proved contraction.

- **Real-centre and boundary uniformity; downstream scope.** Input: real \(X\). Outcome: \(y\le R^2<y+1\) and \(y^2\le N\le y^2+2y\), so (1.2) and (3.6) are floor-uniform. The fourth-power calculation is a required obstruction test, not an averaging argument. The hard boundary \(d=y\) becomes the exact cutoff \(r\ge4Nh/y^2\) plus one-sided stationary terms and cannot be discarded. The result concerns only (138.T); it proves no blockwise parent, M2 estimate, or Gauss-circle conclusion.

## 6. Dependencies and exact artifacts used

The derivation used only:

- `problems/gauss_circle.md`;
- `state/control_models.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/blind_statement.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/briefs/blind_reduced_fraction_scalar_feasibility.md`.

No strategy file, proof-state file, prior-round artifact, sibling report, web source, numerical experiment, or symbolic computation was used.

## 7. Recommended state effect

**Promote** the exact reduction (1.2) as a candidate lemma after checking that the literal support definition indeed contains the necessary global small-arc condition \(h<d\). It rigorously removes the diagonal, every same-denominator unequal-numerator term, and every cross-denominator exact phase-one pair while preserving the owner coefficients. Do not promote the target estimate: the surviving cross-denominator scalar still has full primal capacity, and its honest character-stationary transform is the self-returning divisor sum (3.13), for which the required \(y^{1/4}\)-saving is unproved.
