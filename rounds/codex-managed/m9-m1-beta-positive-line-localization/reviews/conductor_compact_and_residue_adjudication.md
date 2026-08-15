# Conductor adjudication: compact terminal and artificial residue

Campaign: `m9-m1-beta-positive-line-localization`  
Round: 45  
Allocation: 100% analytical/algebraic

## Decision

The central positive-line beta terminal and both alpha-localized artificial
residue shares are proved target-safe. This conclusion is independent of
the still-open large-alpha complement identification.

After the complete finite product Cauchy--Green sum is returned to

\[
 R_uR_v[\psi(\beta)Q_{\rm ef}],
\]

multiply by \(\chi _0(\alpha)\), where \(\alpha=L+\beta\). The terminal
then has exactly three selectors:

\[
 j=0\text{ singular }u^{-1},\qquad
 j=0\text{ regular top},\qquad j\geq1\text{ interior}.
\]

Only the first is interpreted by the signed top Plemelj limit. With

\[
 A=-1-\frac b2-i(L+\beta),\qquad
 D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right),
\]

its exact normalized functional is

\[
 \frac{g(L,\beta)p(L)}A
 -\frac{ig(L,\beta)}{2\pi}
 \int_{\mathbb R}\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)}\,d\nu.
 \tag{45.C1}
\]

The delta half and the constant-numerator principal-value half combine to
the full first term. Absolute values are introduced only after this
recombination. Compact \((L,\beta)\), cubic height decay, and rapid smooth
spatial decay bound the value. The exact combined phase gives

\[
 x\partial_x\{g(L,\beta)p(\nu)\}
 =-i\left(\frac{L+\nu}{2}+\beta\right)g(L,\beta)p(\nu),
\]

and the multiplier divided by \(D\) has modulus at most one. In the
Plemelj remainder the derivative remains the same divided difference,
so there is no false separate \(1/\nu\) tail. Since

\[
 r=\frac54-\frac{a+b}{2}>1,\qquad
 p=\frac54+\frac{a+b}{2}>1,
\]

the \(h,q\) sums converge absolutely; the real scale weights are bounded
and there are \(O(\log X)\) active scales. Therefore

\[
 \sup_{1\le x\le N_X}
 \left(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\right)
 \ll \log^C(2X).                                      \tag{45.C2}
\]

The accepted radial-BV reduction then makes this terminal physically
\(O(X^{1/4}\log^C X)\), with full continuous radial endpoint
coefficients.

## Artificial residue

At \(\rho=1/4-s-v/2=0\), the sign is intrinsic:

\[
 \operatorname {Res}_s\left(-\frac{\pi i\sqrt X}{\rho}I_1(\rho)\right)
 =+\pi i\sqrt X I_1(0).
\]

Direct differentiation of \(e(\sqrt{Xx})\) gives

\[
 \pi i\sqrt X I_1(0)
 =e(\sqrt{XN_X})-e(\sqrt X),                         \tag{45.C3}
\]

so the radial residue coefficient is uniformly bounded. On this pole,

\[
 \alpha_\rho=\frac\mu2,\qquad
 \beta_\rho=-\frac\mu2-\nu.
\]

The arithmetic factor is kept recombined as

\[
 \zeta\left(\frac34+\frac u2+v\right)
 L\left(\frac34-\frac u2,\chi _4\right).
\]

The beta mask makes the zeta height compact and the contour inequalities
keep it away from its pole. Bounded partial sums of \(\chi _4\) give
\(L(\sigma+i\tau,\chi _4)\ll1+|\tau|\). The central alpha share is a
compact signed Plemelj functional. In the complementary share,
\(\nu=-\mu/2+O(1)\), and the singular top tail is

\[
 |\mu|^{-1}(1+|\mu|)(1+|\nu|)^{-3}
 \ll(1+|\mu|)^{-3}.
\]

Thus both separately owned artificial shares are \(O(\log^C X)\)
before the external physical operator. This is an absolute estimate, so
the inherited global contour insertion sign cannot affect it; (45.C3)
fixes the local residue orientation used in the exact ledger.

## Scope

The three Round-45 reports independently validate this core, including a
clean mathematical statement-only rederivation. They do not validate the
full positive-line complement. The accepted Round-41 node proves the two
large-alpha saddle packages with entry and exit, but it does not exhibit a
finite same-antecedent partition summing to \(1-\chi _0\) or a quantitative
bound for every remaining nonsaddle tail. Consequently the complete
positive-line localization certificate and the current aggregate
double-bounded node remain open. The graph may promote only a new scoped
compact/artificial lemma.

