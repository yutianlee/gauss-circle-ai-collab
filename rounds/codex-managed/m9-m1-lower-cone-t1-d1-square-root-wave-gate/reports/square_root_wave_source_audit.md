# Round 152 primary-source audit: the actual-profile square-root character wave

- Campaign: `m9-m1-lower-cone-t1-d1-square-root-wave-gate`
- Research round: 152
- Role: primary-source auditor
- Graph SHA-256: `d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`
- Allocation used: 100% analytical/algebraic and source verification; 0% numerical
- Recommended terminal label: `strict_square_root_character_range`

## 1. Result

There is a source-legal strict range inside the interval left open by Round 151.  Put

\[
 N=\lfloor X\rfloor,\qquad R=X^{1/4},\qquad 1\ll M\leq R^2,
\]

and retain the literal zero-extended Round-148 profile
\(\mathscr A_{1,M,U}(1,\ell)\).  Then the exponent pair

\[
 (k_*,\lambda_*)=
 B D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right)
\tag{152.S1}
\]

is licensed by Bourgain's Theorem 6 together with Tao--Trudgian--Yang's
Lemmas 13--15.  After the exact two residue classes modulo four and Abel
summation with the actual profile, it gives

\[
 \boxed{
 |P_U|\ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 X^\varepsilon.}
\tag{152.S2}
\]

Consequently

\[
 \boxed{M^{449}\gg R^{780}}
\tag{152.S3}
\]

is a source-legal target range.  It is genuinely wider than the already
owned Tao--Trudgian--Yang range because

\[
 \frac{780}{449}<\frac{1424}{819}
 \quad\left(780\cdot819=638820<639376=1424\cdot449\right).
\tag{152.S4}
\]

Thus (152.S3) contributes the nonempty strict sliver

\[
 R^{780/449+\delta}\ll M\ll R^{1424/819-\delta}
\tag{152.S5}
\]

for any fixed power margin
\(0<\delta<278/367731\), since
\(1424/819-780/449=556/367731\); the pre-existing owner is subtracted
rather than counted again.  The literal row component remains
\(\widetilde S_U=B_{1,U}(1)S_U\), and multiplication by
\(|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon\) preserves the target.

Below (152.S3), none of the audited primary inputs closes the target.  The
first exact exponent-pair power obstruction occurs at

\[
 \alpha_* = \frac{127}{322},\qquad
 \mu_* = \frac{780}{449},
\tag{152.S6}
\]

where \(M=R^\mu\), the dual exponent-sum coordinate is
\(\alpha=(4-\mu)/(4+\mu)\), and Tao--Trudgian--Yang Table 1's relevant line

\[
 \beta(\alpha)\leq \frac{18}{199}+\frac{521}{796}\alpha
\tag{152.S7}
\]

meets the required line \(\beta(\alpha)\leq(1+\alpha)/4\).  For
\(\mu<780/449\), hence \(\alpha>127/322\), this printed bound is too large.
This is a no-go for the audited exponent-pair input, not a lower bound for
\(P_U\) and not a literature impossibility theorem.

The other audited routes fail earlier or self-return.  Fixed-modulus mixed
Burgess theorems do not accept a square-root phase and do not provide an
\(R\)- or \(M\)-saving when the modulus is the fixed number four.  Pointwise
Dirichlet-\(L\) subconvexity, even replaced by Lindelöf, leaves a factor
\(R\) after the literal Mellin transform.  The exact degree-one functional
equation/character Poisson formula has dual length
\(Q\asymp R^2M^{-1/2}\) and reconstructs the accepted reciprocal row.
GL(2) or higher Voronoi formulae have the wrong coefficient class.  The
nonlinear-resonance theorems inspected have fixed twist parameters and no
uniformity strong enough for the growing parameter \(\sqrt N\); their
degree-one standard twist is linear, not square-root.  Exact products
\(N\ell=\square\) have total actual-weight mass
\(O(M^{-1/4})\), while elementary near-square spacing returns the full
\(M^{1/4}\) absolute capacity.

## 2. Exact statement and hypotheses

### 2.1 Literal project object

The audited object is exactly

\[
 P_U=\sum_{\substack{\ell>0\\ \ell\ \mathrm{odd}}}
 \chi_4(\ell)W_U(\ell)e(\sqrt{N\ell}),
 \qquad
 W_U(\ell)=\ell^{-3/4}\mathscr A_{1,M,U}(1,\ell).
\tag{152.S8}
\]

The permitted Round-151 candidate supplies the following accepted
project-side facts, which are not external-source assertions.

1.  The actual profile is compact smooth after the previously owned hard
    radial-prefix and cone collars are removed, is extended by zero, and is
    supported on finitely many literal components with \(\ell\asymp M\).
2.  Its bulk, radial-transition, cone-transition, stationary-buffer, tail,
    and endpoint ledger gives

    \[
    \|\mathscr A_{1,M,U}(1,\cdot)\|_\infty+
    \operatorname {Var}_{\ell}
       \mathscr A_{1,M,U}(1,\ell)
    \ll_\varepsilon X^\varepsilon.
    \tag{152.S9}
    \]

    Therefore, on every retained component and after zero extension,

    \[
    \boxed{
    \|W_U\|_\infty+\operatorname {Var}W_U
    \ll_\varepsilon M^{-3/4}X^\varepsilon.}
    \tag{152.S10}
    \]

3.  The boundary-complete first transform is already accepted as

    \[
    S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
    \tag{152.S11}
    \]

    and the actual row is \(B_{1,U}(1)S_U\), with
    \(|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon\).

The permitted context does not print the factor-by-factor Round-148 formula
or numerical endpoint constants.  This audit does not invent replacements:
all endpoint sets remain the literal zero-extended sets in (152.S8), and only
the accepted norm (152.S10), which is sufficient for the source theorem, is
used.

### 2.2 Exponent-pair source card and the new pair

**Source fact.**  Bourgain,
[*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2),
Theorem 6, states that

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\]

is an exponent pair.  Section 5 treats lengths above \(\sqrt T\) and proper
subintervals; the direct Theorem-4 window is not a hypothesis of Theorem 6.

**Source fact.**  Tao, Trudgian, and Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1),
Definition 5, define model phases by

\[
 F^{(p+1)}(u)=\frac{d^p}{du^p}u^{-\sigma}+o(1)
 \quad(p\geq0)
\tag{152.S12}
\]

for a fixed \(\sigma>0\).  Definitions 11--12 give, for every proper
interval \(I\subset[H,2H]\) and \(T\geq H\),

\[
 \sum_{n\in I}e(TF(n/H))
 \ll_\varepsilon (T/H)^{k+\varepsilon}H^{\lambda+\varepsilon}
\tag{152.S13}
\]

for an exponent pair \((k,\lambda)\), with a finite-derivative
non-asymptotic formulation.  Lemma 13 gives

\[
 B(k,\lambda)=(\lambda-1/2,k+1/2),
\tag{152.S14}
\]

Lemma 14 gives Sargos's \(D\)-process

\[
 D(k,\lambda)=
 \left(
 \frac{5k+\lambda+2}{8(5k+3\lambda+2)},
 \frac{29k+21\lambda+10}{8(5k+3\lambda+2)}
 \right),
\tag{152.S15}
\]

and Lemma 15 identifies the global exponent-pair condition with the
corresponding bounds for the exponent-sum growth function \(\beta\).  Their
Table 1 explicitly records

\[
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right)
\tag{152.S16}
\]

and the line (152.S7) on the relevant \(\alpha\)-cell.  Theorem 20 separately
lists four new pairs, including
\((89/1282,997/1282)\).

**Project inference.**  Formulae (152.S14)--(152.S16) give (152.S1).  There
is no extra character, conductor, modulus, main term, exceptional spectrum,
root number, or endpoint term in (152.S13).  The project character is made
constant on each of the two exact residue progressions before the theorem is
used, and the actual weight is inserted only afterwards by Abel summation.

### 2.3 Mixed-character source card

**Source fact.**  Heath-Brown and Pierce,
[*Burgess bounds for short mixed character sums*](https://arxiv.org/html/1404.1677),
Theorems 1.2--1.8, treat

\[
 \sum_{N_0<n\leq N_0+H}\chi(n)e(f(n))
\tag{152.S17}
\]

for a nonprincipal character to a **prime** modulus \(q\), with \(f\) a
real polynomial of fixed degree, and with length hypotheses expressed in
powers of \(q\).  The paper says only that suitable general smooth phases
might be approached by polynomial approximation; it does not print a
square-root-phase theorem with the required uniform derivative and cell
ledger.

**Project mismatch.**  Here \(q=4\) is fixed and composite,
\(f(x)=\sqrt{Nx}\) is not a fixed-degree polynomial on the full interval,
and every Burgess saving is a power of the modulus rather than a power of
\(R\) or \(M\).  No theorem in that paper yields the missing
\(M^{1/4}\) saving.  The exact fixed-modulus operation is instead the two
residue classes used in Section 3.1 below.

### 2.4 Boundary transform, theta/Voronoi, and coefficient cards

**Source fact.**  Lutsko, Sourmelidis, and Technau,
[*Pair correlation of the fractional parts of
\(\alpha n^\theta\)*](https://ems.press/journals/jems/articles/14297682),
Theorem 1.3, is a half-open unweighted van der Corput \(B\)-transform under
the printed \(C^4\) second-through-fourth derivative hypotheses; its dual
main sum and both half-open endpoints are part of the theorem itself.
Lemma 1.4 is the partial-summation lemma that transfers an unweighted
bound to a weighted one.  Uniform use on prefixes followed by that
partial summation is the source-legal weighted interface.

**Project inference.**  Applied to the two additive representations of
\(\chi_4\), it gives the already accepted principal transform (152.S11),
with dual length \(Q\), not an error term.  Section 3.5 derives its constants
directly from character Poisson summation.

**Source fact.**  Miller and Schmid,
[*A general Voronoi summation formula for
\(GL(n,\mathbb Z)\)*](https://arxiv.org/html/0912.1065), Theorem 1.10,
is a Voronoi formula for Fourier--Whittaker coefficients of a cuspidal
automorphic representation, with the prescribed additive twists,
archimedean transform, divisor variables, and hyper-Kloosterman sums.

**Project mismatch.**  The literal coefficient in (152.S8) is the degree-one
Dirichlet coefficient \(\chi_4(\ell)\), multiplied by the actual project
profile.  It is not a GL(2) or higher cuspidal Hecke sequence.  Adjoining a
zeta factor would change it to a convolution coefficient, and a theta lift
would put coefficients on squares (for the odd character, the usual theta
kernel also carries the corresponding odd polynomial factor).  Neither is
the literal all-odd-\(\ell\) wave.  At degree one the valid Voronoi formula is
exactly character Poisson summation, which self-returns to the reciprocal
row.

### 2.5 Dirichlet-\(L\) and nonlinear-resonance cards

For the primitive odd real character \(\chi_4\), direct Gauss-sum
calculation gives

\[
 \tau(\chi_4)=2i,\qquad
 \varepsilon(\chi_4)=\frac{\tau(\chi_4)}{i\sqrt4}=1,
\tag{152.S18}
\]

and the completed function is

\[
 \Lambda(s,\chi_4)=
 \left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi_4),
 \qquad \Lambda(s,\chi_4)=\Lambda(1-s,\chi_4).
\tag{152.S19}
\]

Thus

\[
 L(s,\chi_4)=
 \left(\frac4\pi\right)^{1/2-s}
 \frac{\Gamma((2-s)/2)}{\Gamma((s+1)/2)}
 L(1-s,\chi_4),
\tag{152.S20}
\]

with root number \(+1\).  On the Mellin spectrum relevant below, the
analytic conductor and central approximate-functional-equation length are

\[
 \mathcal C\asymp4T_0,\qquad
 \mathcal C^{1/2}\asymp R M^{1/4},\qquad
 T_0:=\sqrt{NM}\asymp R^2M^{1/2}.
\tag{152.S21}
\]

Bourgain's Theorem 5 is a pointwise theorem for \(\zeta(1/2+it)\), not a
literal theorem for the localized wave (152.S8).  Even granting the
stronger conjectural fixed-character Lindelof bound does not close the
Mellin integral; Section 3.5 gives the exact loss.  Therefore no delicate
choice among currently known positive subconvex exponents can repair this
interface.

**Source fact.**  Kaczorowski and Perelli,
[*Twists and resonance of L-functions, I*](https://arxiv.org/html/1304.4734),
Theorems 1--5 and their discussion of (1.8)--(1.10), concern analytic
continuation and polar structure of nonlinear twists of a fixed
\(L\)-function.  The paper expressly notes that useful smoothed-sum
applications require uniform bounds in the twist parameters and that the
available quality is weak.  For degree \(d=1\), the standard resonant
exponent \(1/d\) is linear.  A square-root twist is substandard, and its
analytic-continuation statement does not provide the uniform
\(\alpha=\sqrt N\), scale-\(M\), actual-weight bound required here.

The current 2026 continuation, Kaczorowski and Perelli,
[*Multiple standard twists of L-functions*](https://arxiv.org/html/2603.13885),
condition (1.3) imposes \(\sum d_\nu\kappa_\nu=1\); in a one-function
degree-one specialization this forces \(\kappa=1\), again not the square-root
phase.  Theorem 1 itself is stated for \(N\ge2\).  It supplies meromorphic
continuation, not the uniform finite-sum estimate (152.S2).

## 3. Proof/derivation

### 3.1 Literal character placement and proof of the strict range

Zero extension makes the residue decomposition exact, including all
endpoints:

\[
 P_U=\sum_{a\in\{1,3\}}\chi_4(a)
 \sum_{n\in\mathbb Z}W_U(4n+a)
 e\!\left(\sqrt{N(4n+a)}\right).
\tag{152.S22}
\]

On one retained component put \(n\asymp H\asymp M\) and

\[
 T=\sqrt{NH}\asymp R^2M^{1/2},\qquad
 F_a(u)=2\sqrt{u+\frac{a}{4H}}.
\tag{152.S23}
\]

Then

\[
 \sqrt{N(4n+a)}=T F_a(n/H),
\]

and, for every fixed \(p\geq0\),

\[
 F_a^{(p+1)}(u)=\frac{d^p}{du^p}u^{-1/2}+O_p(H^{-1}).
\tag{152.S24}
\]

This is the Tao--Trudgian--Yang model class with \(\sigma=1/2\).  Moreover

\[
 \frac TH\asymp R^2M^{-1/2}\geq R,
\tag{152.S25}
\]

so the source convention \(T\geq H\) has a power margin throughout the
growing range \(M\leq R^2\).  Definitions 11--12 include every proper
subinterval.

The arithmetic in the \(D\)-process is exact.  From (152.S15),

\[
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right).
\tag{152.S26}
\]

For \(0\leq\alpha\leq1/2\), the \(D\)-line dominates the auxiliary line in
Tao--Trudgian--Yang Lemma 14 because

\[
 \left(\frac{18}{199}+\frac{521}{796}\alpha\right)
 -\left(\frac1{12}+\frac23\alpha\right)
 =\frac{17-29\alpha}{2388}\geq\frac5{4776}>0.
\tag{152.S27}
\]

Here \(593/796-18/199=521/796>1/2\), so Remark 16 says that
the half-range just checked is sufficient.  Lemma 15 and the symmetry
recorded after it therefore make (152.S26) a global exponent pair.  Lemma
13's \(B\)-process gives (152.S1).

Apply (152.S13) to every partial interval in (152.S22), and only then use
Abel summation with (152.S10).  The two residue classes and the finitely many
actual support components cost \(X^\varepsilon\).  Hence

\[
\begin{aligned}
 |P_U|
 &\ll_\varepsilon
 M^{-3/4}
 \left(R^2M^{-1/2}\right)^{195/796}
 M^{235/398}X^\varepsilon\\
 &=R^{780/1592}M^{-449/1592}X^\varepsilon,
\end{aligned}
\tag{152.S28}
\]

which is (152.S2).  No arbitrary bounded coefficient has replaced the
actual profile, and no character theorem has been applied to a weighted
sum: character splitting precedes the unweighted source theorem, while
weight insertion follows it.

### 3.2 Complete derivative/exponent-pair power ledger

For any source-legal exponent pair \((k,\lambda)\) used directly on the
square-root phase, the same calculation gives

\[
 |P_U|\ll_\varepsilon
 R^{2k}M^{\lambda-k/2-3/4}X^\varepsilon.
\tag{152.S29}
\]

The important specializations are:

| Input | Literal \(P_U\) bound | Target condition |
|---|---:|---:|
| second derivative, \(|f''|\asymp R^2M^{-3/2}\) | \(R M^{-1/2}+R^{-1}\) | only \(M\gg R^2\) |
| classical \((1/6,2/3)\) | \((R^2/M)^{1/6}\) | only \(M\gg R^2\) |
| Bourgain \((13/84,55/84)\), fixed by \(B\) | \((R^{52}/M^{29})^{1/168}\) | \(M^{29}\gg R^{52}\) |
| \(B(89/1282,997/1282)\) | \((R^{1424}/M^{819})^{1/2564}\) | \(M^{819}\gg R^{1424}\) |
| \(BD(13/84,55/84)\) | \((R^{780}/M^{449})^{1/1592}\) | \(M^{449}\gg R^{780}\) |

For completeness, applying \(B\) to all four pairs printed in
Tao--Trudgian--Yang Theorem 20 gives, in their displayed order,

\[
 \left(\frac{R^{1424}}{M^{819}}\right)^{1/2564},
 \quad
 \left(\frac{R^{10971152}}{M^{6294987}}\right)^{1/19427972},
\tag{152.S30}
\]

\[
 \left(\frac{R^{1032884}}{M^{566241}}\right)^{1/1404384},
 \quad
 \left(\frac{R^{26528}}{M^{14437}}\right)^{1/34780}.
\tag{152.S31}
\]

Their threshold ratios are all larger than \(780/449\).  Using those pairs
without \(B\) is also weaker for this weight.  Thus the improvement comes
from the source's \(D\)-line, not from silently relabelling one of Theorem
20's four pairs.

The same conclusion is visible in the source's \(\beta\)-coordinates.  Put
\(M=R^\mu\) and use the reciprocal side of the exact \(B\)-transform.  Its
length and phase parameter are

\[
 Q\asymp R^2M^{-1/2},\qquad T_0\asymp R^2M^{1/2},
\tag{152.S32}
\]

so

\[
 \alpha=\frac{\log Q}{\log T_0}=\frac{4-\mu}{4+\mu},
 \qquad
 \frac{\log R}{\log T_0}=\frac{1+\alpha}{4}.
\tag{152.S33}
\]

Since \(P_U=N^{-1/4}\) times that reciprocal sum, the target is precisely

\[
 \beta(\alpha)\leq\frac{1+\alpha}{4}.
\tag{152.S34}
\]

Equating (152.S7) and (152.S34) gives \(322\alpha=127\), then
\(\mu=4(1-\alpha)/(1+\alpha)=780/449\).  The crossing lies inside the
printed Table-1 cell

\[
\frac{1508}{3825}<\frac{127}{322}<\frac{62831}{155153}.
\tag{152.S35}
\]

Indeed, the two cross-product gaps are respectively
\(127\cdot3825-1508\cdot322=199\) and
\(62831\cdot322-127\cdot155153=527151\), both positive.

This supplies the exact current-source boundary for the audited
exponent-pair route.

### 3.3 Adjacent pairing and one legal character-aware \(A\)-process

Adjacent pairing is the exact finite difference

\[
\begin{aligned}
 P_U=\sum_n\{&W_U(4n+1)e(\sqrt{N(4n+1)})\\
              &-W_U(4n+3)e(\sqrt{N(4n+3)})\},
\end{aligned}
\tag{152.S36}
\]

with zero extension at both ends.  Its phase increment is

\[
 \sqrt{N(4n+3)}-\sqrt{N(4n+1)}
 =\frac{2\sqrt N}{\sqrt{4n+3}+\sqrt{4n+1}}
 \asymp R^2M^{-1/2}.
\tag{152.S37}
\]

This is large as a real number but can be arbitrarily close to an integer.
Thus \(1-e(\Delta_n)\) is not controlled by an ordinary derivative bound;
replacing (152.S36) by a small derivative is illegal and gives no uniform
character saving.

For one van der Corput \(A\)-process, shifts must be even.  Write the shift
as \(2h\).  For odd \(\ell\), exactly

\[
 \chi_4(\ell+2h)\chi_4(\ell)=(-1)^h.
\tag{152.S38}
\]

The character has therefore become a constant sign, not a second source of
cancellation.  The correlation phase and its second derivative are

\[
 g_h(x)=\sqrt{N(x+2h)}-\sqrt{Nx},
 \qquad
 g_h''(x)\asymp hR^2M^{-5/2}
\tag{152.S39}
\]

on an intersection interval of length \(\asymp M\), for \(1\leq h\leq
cM\).  If the shift cutoff is \(J\), the even-shift van der Corput
inequality, the actual product-weight variation, and the second-derivative
test give

\[
 |P_U|^2\ll_\varepsilon
 \left(
 \frac{M^{1/2}}J
 +R M^{-3/4}J^{1/2}
 +R^{-1}M^{3/4}J^{-1/2}
 \right)X^\varepsilon.
\tag{152.S40}
\]

Indeed the diagonal is \(M^{-1/2}\), the outer factor is \(M/J\), and a
shifted unweighted phase sum is

\[
 \ll R h^{1/2}M^{-1/4}+R^{-1}h^{-1/2}M^{5/4}.
\tag{152.S41}
\]

Already the first two terms in (152.S40) would require simultaneously

\[
 J\gg M^{1/2},\qquad J\ll R^{-2}M^{3/2},
\tag{152.S42}
\]

which is possible only when \(M\gg R^2\).  Thus one legal \(A\)-process
followed by the second-derivative test gives no new part of the frozen open
range.  Higher source-legal differencing is exactly the domain encoded by
the exponent-pair ledger above; it does not restore the lost character.

### 3.4 Squarefree kernels, exact squares, and near squares

Every odd \(\ell\) has the unique form \(\ell=ts^2\), with \(t\) odd and
squarefree.  No coprimality between \(t\) and \(s\) is inserted.  Therefore

\[
 P_U=\sum_{\substack{t\geq1\\t\ \mathrm{odd\ squarefree}}}
 \chi_4(t)t^{-3/4}
 \sum_{s\geq1\ \mathrm{odd}}s^{-3/2}
 \mathscr A_{1,M,U}(1,ts^2)e(s\sqrt{Nt}).
\tag{152.S43}
\]

Write \(N=2^\nu n_0\), with \(n_0\) odd.  An exact resonance
\(Nt=\square\) with odd squarefree \(t\) exists if and only if \(\nu\) is
even.  In that case it is unique:

\[
 t=t_N:=\prod_{p\mid n_0\atop \nu_p(n_0)\ \mathrm{odd}}p.
\tag{152.S44}
\]

On the literal support \(ts^2\asymp M\), its full actual-weight absolute
mass is

\[
 \ll_\varepsilon
 t_N^{-3/4}\left(\sqrt{M/t_N}\right)^{-1/2}X^\varepsilon
 =M^{-1/4}t_N^{-1/2}X^\varepsilon.
\tag{152.S45}
\]

Thus exact square products are target-safe and are not evidence for a
signed lower bound.

For \(Nt\) nonsquare,

\[
 \|\sqrt{Nt}\|\gg (Nt)^{-1/2}.
\tag{152.S46}
\]

The fixed-\(t\) linear sum consequently has the elementary bound

\[
 \min\left\{\sqrt{M/t},\ \|\sqrt{Nt}\|^{-1}\right\}
 \ll \min\left\{\sqrt{M/t},\ R^2\sqrt t\right\}.
\tag{152.S47}
\]

Since \(M\leq R^2\), the first entry is always the smaller one for
\(t\geq1\).  Summing (152.S47) with the literal weight gives

\[
 M^{-3/4}\sum_{t\ll M}\sqrt{M/t}
 \ll M^{1/4},
\tag{152.S48}
\]

exactly the absolute capacity.  A useful near-square theorem would have to
average the distances in (152.S46) while retaining the squarefree
condition and the sampled two-variable actual profile.  The audited
nonlinear-twist theorems do not print such a uniform estimate.

### 3.5 Exact character Poisson transform and Mellin conductor

Let

\[
 F_U(x)={\bf1}_{x>0}x^{-3/4}\mathscr A_{1,M,U}(1,x)e(\sqrt{Nx}),
\]

with the actual zero extension, and use
\(\widehat F(\xi)=\int_{\mathbb R}F(x)e(-x\xi)\,dx\).  Primitive-character
Poisson summation gives the exact identity

\[
 P_U=\frac{\tau(\chi_4)}4
 \sum_{m\in\mathbb Z}\chi_4(m)\widehat F_U(m/4)
 =\frac i2\sum_{m\in\mathbb Z}\chi_4(m)\widehat F_U(m/4).
\tag{152.S49}
\]

For \(m>0\), the Fourier phase

\[
 \phi_m(x)=\sqrt{Nx}-\frac{mx}{4}
\]

has

\[
 x_m=\frac{4N}{m^2},\qquad
 \phi_m(x_m)=\frac Nm,
 \qquad
 |\phi_m''(x_m)|=\frac{m^3}{32N}.
\tag{152.S50}
\]

The literal principal stationary amplitude is

\[
 x_m^{-3/4}|\phi_m''(x_m)|^{-1/2}=2N^{-1/4}.
\tag{152.S51}
\]

The negative curvature contributes \(e(-1/8)\); multiplication by
\(\tau(\chi_4)/4=i/2\) gives \(e(1/8)N^{-1/4}\).  Hence the principal term
is exactly

\[
 P_U=e(1/8)N^{-1/4}
 \sum_{\substack{m>0\\m\ \mathrm{odd}}}
 \chi_4(m)\mathscr A_{1,M,U}(1,4N/m^2)e(N/m)
 +\text{accepted boundary/lower-symbol terms}.
\tag{152.S52}
\]

The stationary condition \(x_m\asymp M\) gives

\[
 m\asymp2\sqrt{N/M}=Q,
\tag{152.S53}
\]

including the reversed literal half-open endpoints.  Formula (152.S52) is
the accepted reciprocal row and (152.S11), not a new dual error.  Its two
elementary capacities for \(P_U\) are

\[
 \min\{M^{1/4},\ N^{-1/4}Q\}X^\varepsilon
 =\min\{M^{1/4},\ R M^{-1/2}\}X^\varepsilon.
\tag{152.S54}
\]

They meet at \(M=R^{4/3}\), but neither is target-sized throughout the
intermediate range.

The Mellin normalization makes the source mismatch equally explicit.  Put

\[
 h_U(u)=u^{-1/4}\mathscr A_{1,M,U}(1,Mu)
 e(\sqrt{NM u}).
\]

After shifting the entire \(L(s,\chi_4)\) to the central line,

\[
 P_U=\frac{M^{-1/4}}{2\pi}
 \int_{\mathbb R}\widehat h_U(t)M^{it}
 L(1/2+it,\chi_4)\,dt.
\tag{152.S55}
\]

On each actual smooth component the Mellin phase is stationary at

\[
 t=-\pi\sqrt{NM u},
\tag{152.S56}
\]

so its spectral center and width are both \(\asymp T_0=R^2M^{1/2}\), a
stationary transform has size \(T_0^{-1/2}\), and

\[
 \|\widehat h_U\|_1\ll_\varepsilon T_0^{1/2}X^\varepsilon.
\tag{152.S57}
\]

Even the conjectural pointwise bound
\(L(1/2+it,\chi_4)\ll T_0^\varepsilon\) inserted by absolute integration
would give only

\[
 |P_U|\ll M^{-1/4}T_0^{1/2}X^\varepsilon
 \asymp R X^\varepsilon.
\tag{152.S58}
\]

Every known positive subconvex exponent is weaker.  Cancellation in the
\(t\)-integral would require more than a pointwise subconvex theorem.  If
one instead applies the exact functional equation (152.S20), its gamma
phase, root number \(+1\), and the Mellin kernel reproduce (152.S49)--
(152.S53).  The central approximate-functional-equation length
\(R M^{1/4}\) in (152.S21) must not be confused with the final additive
dual length \(Q=R^2M^{-1/2}\); performing the oscillatory Mellin integral is
what produces the latter.  Thus the complete functional-equation route
self-returns to the accepted reciprocal wave.

## 4. First doubtful or unproved step

The strict estimate (152.S2) has no unproved external-source step under the
frozen accepted profile lemma (152.S9).  The phase is literally in the
source model class, the character is removed only by exact residue classes,
proper intervals are printed in the source definition, the source estimate
is used unweighted, and the actual weight and endpoints enter only through
Abel summation and zero extension.

After removing bounded \(M\), the old Tao--Trudgian--Yang owner, and the new
range (152.S3), the first unproved object is still (152.S8) in

\[
 1\ll M,\qquad M^{449}\ll R^{780}.
\tag{152.S59}
\]

For the audited exponent-pair route, the first failed inequality is
(152.S34) immediately above \(\alpha=127/322\).  A continuation must improve
the source's relevant \(\beta\)-line or exploit arithmetic/profile structure
not present in a model-phase theorem.

For the character route, the first invalid step would be to infer a small
adjacent difference from the real size of (152.S37), or to claim character
gain after (152.S38).  For the squarefree route it would be to replace the
sum of the near-square family by the single exact family; (152.S48) shows the
missing averaged spacing estimate.  For Mellin it would be to identify
pointwise subconvexity with cancellation in \(t\), or to call the reciprocal
main wave an error.  For theta/Voronoi it would be to replace
\(\chi_4(\ell)\) by a degree-two Hecke, divisor-convolution, or square-supported
theta coefficient.

The permitted context's omission of the factor-by-factor Round-148 profile
and numerical endpoint constants is a documentation limitation, not a new
mathematical hypothesis here: (152.S9)--(152.S10) are frozen accepted input.
Any standalone publication of (152.S2) should quote that profile lemma and
its literal endpoint list verbatim.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_square_root_wave` | **GREEN.** Equation (152.S8) retains odd \(\ell\), \(\chi_4\), \(\ell^{-3/4}\), the actual profile, the literal phase, and zero extension. |
| `owned_range_exclusion` | **GREEN.** Bounded \(M\) and \(M^{819}\gg R^{1424}\) are subtracted once.  The new contribution is only the sliver (152.S5); (152.S3) may also be stated as a stronger overlapping owner. |
| `actual_profile_and_B11_coefficient` | **GREEN.** The only weight input is the accepted actual-profile variation (152.S10).  \(B_{1,U}(1)\) remains outside \(P_U\) and is multiplied back with its \(X^\varepsilon\) bound. |
| `adjacent_odd_character_pairing` | **GREEN/no gain.** Equations (152.S36)--(152.S37) are the exact finite difference with endpoints; no uncontrolled derivative is substituted. |
| `A_process_character_survival` | **GREEN/no character gain.** Even shifts are compulsory and (152.S38) is a constant sign.  Length, diagonal, phase, derivatives, and powers are (152.S39)--(152.S42). |
| `squarefree_kernel_and_exact_square_resonance` | **GREEN/open split.** The unique exact family and its \(M^{-1/4}t_N^{-1/2}\) mass are (152.S43)--(152.S45).  Near squares return absolute capacity in (152.S48). |
| `Mellin_conductor_and_dual_length` | **GREEN.** Spectral scale and width are \(T_0=R^2M^{1/2}\), analytic conductor is \(4T_0\), AFE length is \(RM^{1/4}\), and final additive dual length is \(Q=R^2M^{-1/2}\). |
| `boundary_complete_transform` | **GREEN as inherited transform; no gain.** Gauss factor, Gaussian unit, stationary amplitude, root number, reversed support, and full dual main wave are retained in (152.S49)--(152.S53). |
| `derivative_and_exponent_pair_power` | **GREEN.** Direct second/third tests, Bourgain, all four Theorem-20 pairs, and the new \(BD\) pair have their exact \(R,M\) powers in (152.S28)--(152.S31) and the table in Section 3.2. |
| `source_theorem_square_root_match` | **GREEN for (152.S2).** The square-root phase is a model phase with \(\sigma=1/2\), \(T/H\gg R\), and arbitrary subintervals.  **No match** for mixed Burgess, higher Voronoi, or nonlinear-resonance theorems for the reasons printed in Section 2. |
| `absolute_capacity_vs_signed_sum` | **GREEN.** \(M^{1/4}\), \(RM^{-1/2}\), and the near-square mass (152.S48) are upper capacities only.  No signed lower bound is asserted. |
| `bounded_intermediate_TTY_endpoint` | **GREEN/open split.** Bounded \(M\) is inherited; (152.S3) strictly improves the TTY boundary; the range (152.S59) remains open. |
| `N_parity_and_near_square_controls` | **GREEN/open split.** Exact resonance exists only when \(\nu_2(N)\) is even and is then unique.  Both parities enter the same residue/exponent-pair and Poisson arguments.  Near-square averaging remains open. |
| `D_L_generic_tge2_cross_and_downstream_scope` | **GREEN.** The result is only the actual \(D=d=L=1\), \(t=1\) scalar.  It does not control \(D>1\), \(L>1\), growing-\(M\) generic terms, any \(t\ge2\) layer, the Round-138 cross owner, M9--M1/M2, endpoint assembly, M9, the bridge, or either global exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts inspected were exactly the task brief and its permitted
context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, parsed for the four active obligations;
3. `state/active_campaign.yml`;
4. `strategy/round152_d1_square_root_wave_strategy.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/candidates/conductor_round151_character_ranges_and_bprocess_boundary.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reports/large_wrap_shifted_divisor_source_audit.md`;
8. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/source_conductor_round151_final.md`;
9. `sources/tao_trudgian_yang_2025.md`; and
10. `sources/bourgain_2017_exponent_pair.md`.

Primary sources checked were:

1. Jean Bourgain,
   [*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2),
   Theorems 4--6 and Sections 3--5;
2. Terence Tao, Tim Trudgian, and Andrew Yang,
   [*New exponent pairs, zero density estimates, and zero additive energy
   estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1),
   Definitions 5 and 9--12, Lemmas 13--15, Table 1, and Theorem 20;
3. D. R. Heath-Brown and L. B. Pierce,
   [*Burgess bounds for short mixed character sums*](https://arxiv.org/html/1404.1677),
   Theorems 1.2--1.8;
4. Christopher Lutsko, Athanasios Sourmelidis, and Niclas Technau,
   [*Pair correlation of the fractional parts of
   \(\alpha n^\theta\)*](https://ems.press/journals/jems/articles/14297682),
   Theorem 1.3 and Lemma 1.4;
5. Stephen D. Miller and Wilfried Schmid,
   [*A general Voronoi summation formula for
   \(GL(n,\mathbb Z)\)*](https://arxiv.org/html/0912.1065), Theorem 1.10;
6. Jerzy Kaczorowski and Alberto Perelli,
   [*Twists and resonance of L-functions, I*](https://arxiv.org/html/1304.4734),
   Theorems 1--5 and the smoothed-sum discussion following (1.8); and
7. Jerzy Kaczorowski and Alberto Perelli,
   [*Multiple standard twists of L-functions*](https://arxiv.org/html/2603.13885),
   Theorem 1 and condition (1.3).

Every statement labelled “Source fact” above is a printed source statement.
Every conductor, scale, residue, profile, stationary-phase, resonance, or
\(R,M\)-power specialization labelled “Project inference” is derived in this
report.  No Round-152 sibling report, shared proof draft, validation matrix,
strategy beyond the permitted file, synthesis, or state file was edited.

## 7. Recommended state effect

**Promote the strict range (152.S2)--(152.S3); retain the remaining target as
open.**

1. Record the source-legal pair
   \(BD(13/84,55/84)=(195/796,235/398)\) and the literal bound
   \[
   |P_U|\ll_\varepsilon(R^{780}/M^{449})^{1/1592}X^\varepsilon.
   \]
2. Promote `strict_square_root_character_range` for
   \(M^{449}\gg R^{780}\), while crediting only the previously unowned
   portion below the Round-151 TTY boundary as new coverage.
3. Leave \(1\ll M\) with \(M^{449}\ll R^{780}\) open.  Record
   \(\alpha=127/322\) as the first exact audited exponent-pair power boundary,
   not as a signed lower bound or impossibility theorem.
4. Retain adjacent pairing, one legal \(A\)-process, elementary near-square
   spacing, pointwise Mellin subconvexity, repeated bare \(B\)-processing,
   higher Voronoi, and current nonlinear-resonance inputs only as the scoped
   no-gain or no-match results stated above.
5. Do not change any \(D>1\), \(L>1\), generic, \(t\ge2\), Round-138 cross,
   M9--M1/M2, endpoint, M9, bridge, target, or exponent obligation on the
   strength of this scalar strict range.
