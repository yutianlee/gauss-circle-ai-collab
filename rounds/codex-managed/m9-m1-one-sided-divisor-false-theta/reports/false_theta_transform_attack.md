# 1. Result: exact Appell completion and scoped radial-capacity return

Campaign: `m9-m1-one-sided-divisor-false-theta`  
Task: `false_theta_transform_attack`  
Role: discovery  
Graph SHA: `5d91e30572cdd0909abfe7147012a0f34c8e60465ad0bb959d771cbefb79a4a2`

The proposed Lambert identity is exact.  More strongly, its unilateral
series is exactly a torsion-moving specialization of the standard
level-four Appell function.  If

\[
 z=e^{\pi i\tau},\qquad Q=z^2=e^{2\pi i\tau},\qquad \Im\tau>0,
\]

and

\[
 A_\ell(u,v;\tau):=e^{\pi i\ell u}
 \sum_{r\in\mathbb Z}
 \frac{(-1)^{\ell r}Q^{\ell r(r+1)/2}e^{2\pi i r v}}
 {1-e^{2\pi i u}Q^r},
\]

then

\[
 \boxed{\mathscr F(z)=\frac12A_4\!\left(\frac12,-\frac32\tau;\tau\right)-\frac14.}
 \tag{1.1}
\]

This is coefficient preserving: it is obtained by pairing the
bilateral terms (r) and (-r), not by changing coefficients.  It also
shows that the word "false theta" is optional here; the exact object is
a one-variable specialization of a higher-level Appell--Lerch sum.

However, this modular completion does **not** prove the requested
square-root radial estimate on any fixed (0<\nu\le2/5).  Every exact
coefficient-extraction route from the Appell transform to a smooth
radial block returns either

\[
 \sum_n \mathcal D(n)W(n/N)
\]

with (W(n)=n^{-3/4}V(n/N)e(\sqrt{Xn})), or a continuum of additive
twists whose Fourier coefficient integral reconstructs that same sum.
The transform also has indispensable unary-theta and
Mordell/nonholomorphic corrections.  At the natural Abel radius
(\eta\asymp N^{-1}), the elementary Cauchy--Parseval ledger returns
(N^{1/4+o(1)}), while separating the Poisson-periodized radial
kernel into continuous Fourier translates costs
(X^{1/4}N^{-1/2}) at the level of powers.  These are scoped capacity
returns, not universal lower bounds on the recombined kernel.  Thus
the strongest safe state effect is an exact Appell identification plus
a radial-transfer warning, with no new exponent.

# 2. Exact statement and hypotheses

Let

\[
 \mathcal D(n)=\sum_{\substack{hq=n\\q\ {\rm odd}\\q>4h}}\chi_4(q),
 \qquad
 \mathscr F(z)=\sum_{n\ge1}\mathcal D(n)z^n,
\]

where (chi_4(4m+1)=1), (chi_4(4m+3)=-1), and let (|z|<1).
Then:

**(a) Lambert/Appell identity.**  With (z=e^{\pi i\tau}),
(\Im\tau>0),

\[
 \mathscr F(z)
 =\sum_{h\ge1}\frac{z^{4h^2+h}}{1+z^{2h}}
 =\frac12A_4\!\left(\frac12,-\frac32\tau;\tau\right)-\frac14.
 \tag{2.1}
\]

There is no term on (q=4h), since (q) is odd.

**(b) Explicit completion terms.**  In the equivalent normalization

\[
 \mathcal K_\ell(\tau,a,b)=
 \sum_{r\in\mathbb Z}
 \frac{e^{\pi i\ell r^2\tau+2\pi i\ell r a}}
 {1-e^{2\pi i(a+b+r\tau)}},
\]

one has exactly

\[
 A_4\!\left(\frac12,-\frac32\tau;\tau\right)
 =\mathcal K_4\!\left(\tau,\frac18\tau,
 \frac12-\frac18\tau\right).
 \tag{2.2}
\]

The specialization is admissible because
(a+b=\frac12\notin\mathbb Z\tau+\mathbb Z).  The
standard (S)-law is

\[
\begin{aligned}
 \mathcal K_\ell(-1/\tau,a/\tau,b/\tau)
 &=\tau e^{\pi i\ell(a^2-b^2)/\tau}\mathcal K_\ell(\tau,a,b)\\
 &\quad+\tau\sum_{j=0}^{\ell-1}
 e^{\pi i\ell(a+j\tau/\ell)^2/\tau}
 \Phi(\ell\tau,\ell b-j\tau)
 \vartheta(\ell\tau,\ell a+j\tau),
 \tag{2.3}
\end{aligned}
\]

where

\[
 \Phi(\tau,b)=-\frac{i}{2\sqrt{-i\tau}}
 -\frac12\int_{\mathbb R}e^{-\pi x^2}
 \frac{\sinh(\pi x\sqrt{-i\tau}(1+2b/\tau))}
 {\sinh(\pi x\sqrt{-i\tau})}\,dx.
 \tag{2.4}
\]

Consequently (2.3) has four theta--Mordell correction terms for
(\ell=4).  It is not legitimate to retain only the transformed
holomorphic Appell term.

**(c) Radial-transfer return lemma.**  Let

\[
 W_{X,N}(x)=x^{-3/4}V(x/N)e(\sqrt{Xx}),
 \]

with (V\in C_c^\infty((0,\infty))), and write

\[
 \widehat W_{X,N}(t)=\int_{\mathbb R}W_{X,N}(x)e(-tx)\,dx
\]

after smooth extension by zero.  There is no assertion that the
pointwise boundary value (\mathscr F(e(t))) exists.  The exact
coefficient-preserving statement is the joint Abel identity: for
every (\eta>0),

\[
 \mathcal L_{X,V}(N)
 =\int_0^1\mathscr F(e^{-\eta+2\pi it})
 \sum_{m\ge1}W_{X,N}(m)e^{\eta m}e(-mt)\,dt.
 \tag{2.5}
\]

Equivalently, (2.5) defines the distributional boundary pairing

\[
 \mathcal L_{X,V}(N)
 =\lim_{\eta\downarrow0}
 \left\langle\mathscr F(e^{-\eta+2\pi it}),
 \sum_{m\ge1}W_{X,N}(m)e^{\eta m}e(-mt)\right\rangle_{\mathbb R/\mathbb Z}.
 \tag{2.6}
\]

Put

\[
 K_\eta(t)=\sum_{m\ge1}W_{X,N}(m)e^{\eta m}e(-mt).
 \tag{2.7}
\]

For (\eta\asymp N^{-1}), positivity on the real radius, the divisor
bound, and Parseval give

\[
 \mathscr F(e^{-\eta})\asymp\eta^{-1/2},
 \qquad
 \|\mathscr F(e^{-\eta+2\pi it})\|_2
 \ll_\varepsilon\eta^{-1/2-\varepsilon},
 \qquad
 \|K_\eta\|_2\asymp_V N^{-1/4}.
 \tag{2.8}
\]

Consequently the elementary Cauchy--Parseval ledger gives only
(N^{1/4+\varepsilon}), not the target.  Improving it requires information
about the joint Appell--radial pairing (or a stronger estimate for the
periodized kernel); (2.8) is not a lower bound forbidding such
cancellation.

For comparison, the continuous Fourier transform of the smooth radial
weight has stationary points when

\[
 \frac{\sqrt X}{2\sqrt x}-t=0,
 \quad\text{so on }x\asymp N,
 \quad t\asymp T:=\sqrt{X/N}.
 \tag{2.9}
\]

Stationary phase gives, for such (t),

\[
 |\widehat W_{X,N}(t)|\asymp_V X^{-1/4},
 \tag{2.10}
\]

over a (t)-window of length (\asymp T).  Hence

\[
 \|\widehat W_{X,N}\|_1\asymp_V X^{1/4}N^{-1/2}
 \tag{2.11}
\]

at the level of powers (upper bound, and lower bound on any subinterval
where the stationary leading coefficient does not vanish).  Poisson
summation periodizes these translates:

\[
 K_0(t)=\sum_{k\in\mathbb Z}\widehat W_{X,N}(k-t).
 \tag{2.12}
\]

Thus bounding the translates separately costs
(X^{1/4}N^{-1/2}); cancellations in (2.12) may reduce that cost, and
must not be discarded.  A target-sized proof needs new joint or
periodized cancellation; modularity alone does not supply it.

# 3. Proof or derivation

Absolute convergence for (|z|<1) permits all rearrangements.  Split
the odd integer (q) into (q=4m+1) and (q=4m+3).  In either residue
class (q>4h) is exactly (m\ge h).  Thus

\[
\begin{aligned}
 \mathscr F(z)
 &=\sum_{h\ge1}\sum_{m\ge h}
   \left(z^{h(4m+1)}-z^{h(4m+3)}\right)\\
 &=\sum_{h\ge1}z^{4h^2+h}
   \frac{1-z^{2h}}{1-z^{4h}}
 =\sum_{h\ge1}\frac{z^{4h^2+h}}{1+z^{2h}}.
 \tag{3.1}
\end{aligned}
\]

This proves (63.3), including the strict boundary.

For the Appell identification, insert
((\ell,u,v)=(4,\frac12,-\frac32\tau)) in the definition of
(A_\ell).  Since (e^{4\pi i}=1), ((-1)^{4r}=1), and (Q=z^2),
the (r)-th summand is

\[
 \frac{Q^{2r(r+1)}Q^{-3r/2}}{1+Q^r}
 =\frac{z^{4r^2+r}}{1+z^{2r}}.
 \tag{3.2}
\]

For (r>0), the (-r) summand satisfies

\[
 \frac{z^{4r^2-r}}{1+z^{-2r}}
 =\frac{z^{4r^2+r}}{1+z^{2r}}.
 \tag{3.3}
\]

The (r=0) term is (1/2), proving (2.1).  To translate
normalizations, compare denominators and numerators in (A_4) and
(\mathcal K_4): take (a=\tau/8) and
(b=1/2-\tau/8).  Then
(a+b+r\tau=1/2+r\tau), and the numerators agree; this proves
(2.2).

To distinguish conventions, the tempting value
`\mathcal K_4(\tau,0,1/2)` is not our series: its numerator is
`z^{4r^2}`, and its bilateral pairing gives a different theta
expression.  Only the moving arguments in (2.2) match (3.2).

The exact external transform (2.3)--(2.4) is Theorem 1.1, equations
(1.1), (1.3), and (1.4), of A. M. Semikhatov, A. Taormina, and I. Yu.
Tipunin, *Higher-Level Appell Functions, Modular Transformations, and
Characters*, Commun. Math. Phys. 255 (2005), 469--512,
arXiv:math/0311314v3.  Its hypotheses are: integer (\ell>0),
(\tau\in\mathbb H), and (a+b\notin\mathbb Z\tau+\mathbb Z); all
hold above.  Their formula explicitly has the sum (0\le j<\ell) and
the integral (\Phi), so no holomorphic modular shortcut is licensed.
The moving specialization is another seam: after (S), both elliptic
arguments are divided by (\tau), while our required section is again
tied to the *new* modular variable.  Elliptic/open-quasiperiodic shifts
are therefore required and themselves add theta terms.

Formula (2.5) is ordinary Fourier coefficient extraction on
(|z|=e^{-\eta}); compact support of (W) makes the compensating
(e^{\eta m}) harmless.  It also makes the expression independent of
(\eta).  Passing to (\eta\downarrow0) is therefore valid only as the
joint distributional pairing (2.6), not as a pointwise boundary value
of (\mathscr F).

For (0<\eta\le1), the positive radial series satisfies

\[
 \mathscr F(e^{-\eta})=
 \sum_{h\ge1}\frac{e^{-\eta(4h^2+h)}}{1+e^{-2\eta h}}
 \asymp \sum_{h\ge1}e^{-4\eta h^2}\asymp\eta^{-1/2}.
 \tag{3.4}
\]

The first comparison follows by restricting to
(h\ll\eta^{-1/2}) for the lower bound and dropping the denominator
for the upper bound.  Since (|\mathcal D(n)|\le\tau(n)) and
(\tau(n)\ll_\varepsilon n^\varepsilon), Parseval also gives

\[
 \|\mathscr F(e^{-\eta+2\pi it})\|_2^2
 =\sum_{n\ge1}|\mathcal D(n)|^2e^{-2\eta n}
 \ll_\varepsilon\eta^{-1-\varepsilon}.
 \tag{3.5}
\]

For (\eta\asymp N^{-1}), Parseval and (m\asymp N) on the support of
(V) further give

\[
 \|K_\eta\|_2^2
 =\sum_m |W_{X,N}(m)|^2e^{2\eta m}
 \asymp_V N\,N^{-3/2}=N^{-1/2}.
 \tag{3.6}
\]

This proves (2.8) and the stated elementary
(N^{1/4+\varepsilon}) return.

Finally, with (x=Nu),

\[
 \widehat W(t)=N^{1/4}
 \int u^{-3/4}V(u)e\!\left(\sqrt{XN}\sqrt u-tNu\right)du.
 \tag{3.7}
\]

The stationary equation is (2.9).  The second derivative of the
unscaled phase in (x) at (x_0=X/(4t^2)) is of size
(t^3/X).  One-dimensional stationary phase therefore contributes
(x_0^{-3/4}(X/t^3)^{1/2}\asymp X^{-1/4}), proving (2.10); the
(t^{3/2}) factors cancel exactly.  The stationary (t)-window has
length (\asymp T), giving (2.11).  Poisson summation gives (2.12),
with the sign fixed by the convention
(\widehat W(t)=\int W(x)e(-tx)dx).  Therefore the continuous
(L^1) cost is an obstruction only to a proof that takes absolute
values before periodization; it is not a lower bound for (K_0).

# 4. First doubtful or unproved step

There is no doubtful step in the algebraic identities (3.1)--(3.3),
the normalization map (2.2), or the deperiodized translate-wise
(L^1) calculation.
The first genuinely unproved step needed for a positive result is:

\[
 \lim_{\eta\downarrow0}
 \left\langle\mathscr F(e^{-\eta+2\pi it}),
 \sum_m W_{X,N}(m)e^{\eta m}e(-mt)\right\rangle
 \ll X^\varepsilon
\]

by cancellation **between** the stationary radial kernel and the
completed Appell boundary value, with all four theta--Mordell terms
and the periodized kernel recombined.  The audited Appell (S)-law does
not by itself imply this correlation.  Two specifically delimited
ledgers fail: elementary Cauchy--Parseval control returns
(N^{1/4+\varepsilon}), and applying the modular formula translate by translate
before periodization loses (X^{1/4}N^{-1/2}).  Neither statement rules
out cancellation in the exact periodized pairing.  No nonempty
(\nu)-range of (63.2) is proved here.

# 5. Required control test and outcome

**Coefficient and cone boundary: PASS.**  Expanding (3.1) shows the
first terms (z^5-z^7+z^9-z^{11}+\cdots), agreeing with direct
incidence counting.  Equality (q=4h) is impossible by parity, so no
half-star appears.

**Bilateral Appell pairing: PASS.**  Equations (3.2)--(3.3) show
termwise that (r) and (-r) are equal; (r=0) contributes exactly
(1/2).  Thus (1.1) has constants (1/2) and (1/4) exactly.

**Completion terms: PASS/OBSTRUCTION.**  The primary (S)-formula has
four (\Phi\vartheta) terms at level four.  Discarding them fails the
source theorem's exact identity.

**Radial-transform uniformity: PASS/SCOPED OBSTRUCTION.**  Stationary
phase locates additive frequencies (t\asymp\sqrt{X/N}) and yields
(\|\widehat W\|_1\asymp X^{1/4}N^{-1/2}).  This rules out only
deperiodized translate-wise absolute integration.  The exact kernel
is the signed periodization (2.12), which may cancel.

**Rational cusps and perfect-fourth coherence: NOT RESOLVED BY
MODULARITY.**  The Appell formula describes boundary behavior only
after Mordell correction and does not create a derivative gap for the
radial phase.  The exact Fourier inversion retains every additive
frequency, including coherent rational neighborhoods; no claim of
their cancellation is made.

**Target power ledger: PASS.**  The promoted content is the exact
representation and two scoped capacity returns.  The elementary
Cauchy--Parseval ledger gives (N^{1/4+\varepsilon}); the deperiodized
translate-wise ledger gives
(X^{1/4}N^{-1/2}=X^{1/4-\nu/2}).  Neither is target-sized, but neither
is a lower bound on the exact periodized pairing.  There is no exponent
improvement.

# 6. Dependencies and exact artifacts used

- `protocol.md`.
- `state/proof_obligations.yml`, graph SHA
  `5d91e30572cdd0909abfe7147012a0f34c8e60465ad0bb959d771cbefb79a4a2`.
- `state/active_campaign.yml`, Round 63.
- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/derivation_packet.md`.
- `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md`.
- A. M. Semikhatov, A. Taormina, I. Yu. Tipunin,
  *Higher-Level Appell Functions, Modular Transformations, and
  Characters*, Commun. Math. Phys. 255 (2005), 469--512,
  [arXiv:math/0311314v3](https://arxiv.org/abs/math/0311314): definition
  (1.1), Theorem 1.1 formulas (1.3)--(1.4), and the explicit
  hypotheses stated with (1.1).  This source is used only for the
  exact Appell transformation and correction ledger, not for an
  exponential-sum bound.
- S. Zwegers, *Rank-Crank type PDE's for higher level Appell
  functions*, Acta Arith. 144 (2010), 263--273,
  [arXiv:0908.4007](https://arxiv.org/abs/0908.4007): equation (1.2)
  confirms the (A_\ell) normalization (the paper's PDE theorem is
  for odd (\ell) and is **not** invoked at (\ell=4)).

No other Round-63 report was read.  Numerical work was limited to a
small coefficient sanity check and is diagnostic only.

# 7. Recommended state effect

**Promote** a scoped internal reduction, tentatively
`M9-M1-one-sided-divisor-Appell-identification`: equations (2.1)--(2.4)
give the exact level-four Appell representation and its indispensable
four theta--Mordell corrections.

**Promote** a scoped capacity return, tentatively
`M9-M1-Appell-radial-norm-ledger-return`: at (\eta\asymp N^{-1}),
elementary (L^2\times L^2) control returns (N^{1/4+\varepsilon}), while
deperiodized translate-wise absolute integration costs
(X^{1/4}N^{-1/2}).  Explicitly exclude the exact signed periodization
(2.12) from this no-go; its cancellation remains open.

**Retain open** `M9-M1-global-angular-radial-estimate` and the signed
target (63.2).  **No change** to `M9-M1`, `M9`, `GC-target`, or the
record exponent.  The next useful task must estimate the complete
oscillatory pairing of the radial stationary transform with the
Appell plus all theta--Mordell corrections; it must not bound those
pieces separately.
