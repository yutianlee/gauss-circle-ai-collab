# Round 144 post-unmask review: the gcd average widens the safe cell window

## 1. Result

The apparently sharper count in the blind report is correct. It was
available already from the accepted pointwise root estimate, but Round
141 discarded the gcd before summing the residual. For every integer
\(N\geq1\) and real \(J\geq0\),

\[
 \sum_{1\leq |j|\leq J}\sqrt{(N,j)}
 \ll_\varepsilon JN^\varepsilon ,
\tag{144.R1}
\]

where the sum is empty when \(J<1\). Consequently, on a dyadic block
\(\mathcal I_M\),

\[
 \#\{m\in\mathcal I_M:0<|k_m^2-Nm|\leq J\}
 \ll_\varepsilon JN^\varepsilon .
\tag{144.R2}
\]

The exact channel \(j=0\) is separate. Including it gives the requested
uniform general count

\[
 \boxed{\#\{m\in\mathcal I_M:|k_m^2-Nm|\leq J\}
 \ll_\varepsilon (J+\sqrt M)X^\varepsilon.}
\tag{144.R3}
\]

With \(|C(m)|\leq\tau(m)\), the whole \(J\)-window has weighted cost

\[
 \ll_{\varepsilon,V}
 \left(M^{-3/4}J+M^{-1/4}\right)X^\varepsilon .
\tag{144.R4}
\]

Thus the largest polynomial window certified uniformly by this
absolute congruence ledger is

\[
 \boxed{J_M=M^{3/4}}
\tag{144.R5}
\]

(up to \(X^{o(1)}\) factors). The accepted Round-141 reduction can be
strictly sharpened to

\[
\boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\
 |k_m^2-Nm|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).}
\tag{144.R6}
\]

In particular, the newly deleted band
\(\sqrt M<|k_m^2-Nm|\leq M^{3/4}\) is absolutely target-safe. This is a
genuine stricter support survivor than Round 141, although it is an
arithmetic mask improvement, not a gain produced by automorphy. It
does not prove the target estimate.

The blind completion formula is also correct after normalization. Its
\(\mathcal R(\tau)\) is exactly, not merely asymptotically, the
four-term Appell correction \(\mathcal C_{\rm nh}(\tau)\) in
(144.16) of the discovery report:

\[
 \widehat H(\tau)
 =F(\tau)+\frac14+\mathcal R(\tau)
 =\frac12\widehat A_4\!\left(\frac12,-3\tau;2\tau\right).
\tag{144.R7}
\]

The blind mixed-shadow formula and its scalar cusp/heat identity have
the correct constants and signs. They are alternative aggregate
expressions for the same accepted Round-63 completion; they do not
separate the four Appell correction owners or evade the Round-140
reciprocal self-return.

Accordingly, two qualifications are required. The full cone in (1.8)
of the blind report is target-equivalent to the Round-141 survivor but
is not itself support-smaller. The actually stricter survivor is
(144.R6). Conversely, the earlier discovery report's statement “no
strict survivor” remains correct only when qualified as “no strict
survivor furnished by the Appell/Poisson transform.” It is false as an
unqualified post-unmask statement because (144.R6) is a strict,
owner-complete arithmetic reduction.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,\qquad
 M_*=C_VN/R^2\ll_VN^{1/2},
\tag{144.R8}
\]

with \(X\geq2\); the bounded range is absorbed into the implied
constant. Let the half-open blocks

\[
 \mathcal I_M=[M,2M)\cap[1,M_*]
\tag{144.R9}
\]

be the disjoint dyadic blocks used in Round 141. Here \(N\) is the
fixed centre and \(M\) is a block size; these roles are not
interchanged. Put

\[
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
 j_m=k_m^2-Nm,
\tag{144.R10}
\]

and

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r).
\tag{144.R11}
\]

For an integer residual \(j\), set

\[
 \rho_N(j)=\#\{k\bmod N:k^2\equiv j\pmod N\}.
\tag{144.R12}
\]

The exact arithmetic assertions used below are:

\[
 \rho_N(j)\ll_\varepsilon
 N^\varepsilon\sqrt{(N,j)}
\quad(j\in\mathbb Z),
\tag{144.R13}
\]

\[
 \sum_{1\leq |j|\leq J}\rho_N(j)
 \ll_\varepsilon JN^\varepsilon
\quad(J\geq1),
\tag{144.R14}
\]

and (144.R2)--(144.R3). Formula (144.R14) concerns only nonzero
residuals. When \(0\leq J<1\), its left side is zero; a window
\(|j_m|\leq J\) then consists only of exact radicals.

Write \(N=Du^2\) with \(D\) squarefree. The exact-radical
parametrization is

\[
 j_m=0\quad\Longleftrightarrow\quad m=Dt^2,\qquad
 k_m=Du\,t.
\tag{144.R15}
\]

It follows, uniformly for squareful as well as squarefree \(N\), that

\[
 \sum_{j_m=0}m^{-3/4}
 \left|V_{\rm low}(R^2m/N)C(m)\right|
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{144.R16}
\]

For the completion audit, use the accepted Appell normalization

\[
 A_4(u,v;\sigma)
 =e(2u)\sum_{n\in\mathbb Z}
 \frac{e(\sigma)^{2n(n+1)}e(nv)}
 {1-e(u)e(n\sigma)}.
\tag{144.R17}
\]

At

\[
 (u,v,\sigma)=\left(\frac12,-3\tau,2\tau\right),
\qquad \tau\in\mathbb H,
\tag{144.R18}
\]

the denominator is \(1+e(2n\tau)\), hence never vanishes. The exact
holomorphic identity is

\[
 F(\tau)+\frac14
 =\frac12A_4\!\left(\frac12,-3\tau;2\tau\right).
\tag{144.R19}
\]

With \(y=\Im\tau\), define

\[
 \mathcal R(\tau)
 =\frac14\sum_{\substack{h,r\in\mathbb Z\\r\ {\rm odd}}}
 \chi_4(r)
 \left[
 E\!\left(\frac{(r-4h)\sqrt y}{2}\right)
 -\operatorname {sgn}(r-4h)
 \right]e(hr\tau),
\tag{144.R20}
\]

where \(E(x)=2\int_0^xe^{-\pi t^2}\,dt\). This sum is absolutely and
locally uniformly convergent. Equations (144.R7) and (144.R20) are the
precise reconciliation with the accepted four-term completion.

Finally, for
\(\gamma=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)
\in\Gamma_0(4)\), with \(C>0\), the scalar heat identity is asserted
only under

\[
 AD-BC=1,\qquad 4\mid C,\qquad y>0.
\tag{144.R21}
\]

No coefficient estimate is included in this modular identity.

## 3. Proof and derivation

### 3.1 Prime powers and the gcd average

Let \(p^a\Vert N\), and put
\(t=\min(v_p(j),a)\). If \(t<a\), a solution of
\(k^2\equiv j\pmod {p^a}\) forces \(t=2s\) and \(v_p(k)=s\).
After division by \(p^{2s}\), the unit congruence has at most two roots
for odd \(p\) and at most four roots for \(p=2\); each has \(p^s\)
lifts. If \(t=a\), then

\[
 \#\{k\bmod p^a:k^2\equiv0\pmod {p^a}\}
 =p^{\lfloor a/2\rfloor}\leq p^{a/2}.
\tag{144.R22}
\]

The Chinese remainder theorem gives

\[
 \rho_N(j)\leq4^{\omega(N)+1}\sqrt{(N,j)}
 \ll_\varepsilon N^\varepsilon\sqrt{(N,j)}.
\tag{144.R23}
\]

This includes arbitrary squareful \(N\). For the average, let
\(L=\lfloor J\rfloor\). If \(L=0\), the nonzero sum is empty. If
\(L\geq1\), then

\[
\begin{aligned}
 \sum_{1\leq|j|\leq J}\sqrt{(N,j)}
 &=2\sum_{j=1}^{L}\sqrt{(N,j)}\\
 &\leq
 2\sum_{j=1}^{L}\sum_{d\mid(N,j)}\sqrt d\\
 &=2\sum_{d\mid N}\sqrt d\,\left\lfloor\frac Ld\right\rfloor\\
 &\leq2L\sum_{d\mid N}d^{-1/2}
 \leq2J\tau(N)
 \ll_\varepsilon JN^\varepsilon .
\end{aligned}
\tag{144.R24}
\]

Combining (144.R23) and (144.R24), with epsilon renaming, proves
(144.R14). The old estimate
\(\sqrt{(N,j)}\leq |j|^{1/2}\) lost exactly this divisor-average gain.

### 3.2 Injection, the zero channel, and endpoints

On the entire effective range,

\[
 0\leq k_m\leq\sqrt{2NM_*}+\frac12
 \ll_VN^{3/4}<N
\tag{144.R25}
\]

for all sufficiently large \(N\); bounded \(N\) is absorbed in the
implied constant. For fixed \(j\), the map \(m\mapsto k_m\) is
injective because

\[
 m=\frac{k_m^2-j}{N}.
\tag{144.R26}
\]

Moreover, (144.R25) means that each such \(k_m\) occupies its residue
class modulo \(N\) at most once. Thus the fixed-\(j\) multiplicity is
at most \(\rho_N(j)\), proving (144.R2).

The \(j=0\) term cannot be inserted into (144.R24). Formula
(144.R15) instead gives directly

\[
\begin{aligned}
 \sum_{j_m=0}m^{-3/4}|V_{\rm low}C(m)|
 &\ll_{\varepsilon,V}
 X^\varepsilon D^{-3/4}\sum_{t\geq1}t^{-3/2}\\
 &\ll_{\varepsilon,V}X^\varepsilon .
\end{aligned}
\tag{144.R27}
\]

Equivalently, \(N\mid k^2\) iff
\(\prod_{p^a\Vert N}p^{\lceil a/2\rceil}\mid k\). That modulus is at
least \(\sqrt N\), so a block \(k\)-interval of length
\(O(\sqrt{NM})\) contains \(O(1+\sqrt M)\) zero roots. When \(N\) is a
square this \(\sqrt M\) scale can occur, which is why the zero channel
must not be called \(O(1)\). This proves the \(+\sqrt M\) term in
(144.R3).

The half-open blocks in (144.R9) are disjoint, including the terminal
truncation. An integer at \(2M\) belongs only to the next block, whose
threshold is then used. Equality \(|j_m|=M^{3/4}\) belongs to the
deleted side. Changing a closed/open endpoint convention moves
\(O(1)\) integers per block and has globally target-safe weighted cost.
There is also no nearest-integer tie: such a tie would imply
\(4Nm=(2k+1)^2\), impossible modulo \(4\).

### 3.3 The maximal certified window and strictness

The divisor bound and (144.R2) give

\[
 \sum_{\substack{m\in\mathcal I_M\\0<|j_m|\leq J}}
 m^{-3/4}|V_{\rm low}(R^2m/N)C(m)|
 \ll_{\varepsilon,V}M^{-3/4}JN^\varepsilon.
\tag{144.R28}
\]

Taking \(J=M^{3/4}\) makes every block \(O(N^\varepsilon)\);
the \(O(\log X)\) blocks are absorbed by epsilon renaming. Combined
with (144.R27) and the accepted Round-141 equivalence, this proves
(144.R6).

More generally, a power window \(J=M^\beta\) leaves
\(M^{\beta-3/4}\) in this absolute ledger. Hence
\(\beta=3/4\) is the maximal polynomial exponent certified by this
method. This is not a lower bound and does not rule out a larger
window obtained from a new signed correlation. It only states the
limit of the present root-count-plus-divisor-bound proof.

The predicate \(|j_m|>M^{3/4}\) is strictly stronger than
\(|j_m|>\sqrt M\) once \(M>1\), although a particular intervening band
may be empty. The remaining block still has the generic absolute
capacity

\[
 M^{-3/4}\sum_{m\asymp M}|C(m)|
 \ll_\varepsilon M^{1/4+\varepsilon}.
\tag{144.R29}
\]

Thus the improvement is a real owner reduction but not a target bound.

### 3.4 Exact comparison of the two completion formulas

Use the standard Zwegers conventions

\[
 \vartheta(z;T)
 =\sum_{\lambda\in\mathbb Z+1/2}
 e^{\pi i\lambda^2T+2\pi i\lambda(z+1/2)}
\tag{144.R30}
\]

and

\[
\begin{aligned}
 R_{\rm Zw}(w;T)
 =\sum_{\nu\in\mathbb Z+1/2}
 &\left[
 \operatorname {sgn}\nu-
 E\!\left(\left(\nu+\frac{\Im w}{\Im T}\right)
 \sqrt{2\Im T}\right)
 \right]\\
 &\times(-1)^{\nu-1/2}
 e^{-\pi i\nu^2T-2\pi i\nu w}.
\end{aligned}
\tag{144.R31}
\]

The accepted correction is

\[
 \mathcal C_{\rm nh}(\tau)
 ={i\over4}\sum_{\alpha=0}^{3}(-1)^\alpha
 \vartheta((2\alpha-3)\tau+3/2;8\tau)
 R_{\rm Zw}(1/2+(3-2\alpha)\tau;8\tau).
\tag{144.R32}
\]

In a product summand put

\[
 \lambda=t+\frac12,\qquad \nu=n+\frac12,\qquad
 h=\lambda+\nu=t+n+1,
\tag{144.R33}
\]

\[
 r=4(\lambda-\nu)+2\alpha-3
   =4(t-n)+2\alpha-3.
\tag{144.R34}
\]

As \(\alpha,t,n\) vary, this is a bijection onto
\((h,r)\in\mathbb Z\times(2\mathbb Z+1)\): for each odd \(r\), the two
possible \(\alpha\)'s modulo \(4\) have opposite parity condition, and
exactly one makes the inverse \(t,n\) integral. Under this map,

\[
 (-1)^\alpha=\chi_4(r),\qquad
 4(\lambda^2-\nu^2)+(2\alpha-3)(\lambda+\nu)=hr.
\tag{144.R35}
\]

Also, with

\[
 A_0=8n+7-2\alpha,
\tag{144.R36}
\]

one has

\[
 r-4h=-A_0,\qquad
 \operatorname {sgn}\nu=\operatorname {sgn}A_0.
\tag{144.R37}
\]

The constant factors in (144.R30)--(144.R32) give
\(i(-i)/4=1/4\). The sign-minus-error kernel in
\(R_{\rm Zw}\) becomes

\[
 \operatorname {sgn}A_0-E(A_0\sqrt y/2)
 =E((r-4h)\sqrt y/2)-\operatorname {sgn}(r-4h).
\tag{144.R38}
\]

Equations (144.R33)--(144.R38) transform (144.R32) term by term into
(144.R20). Hence

\[
 \boxed{\mathcal C_{\rm nh}(\tau)=\mathcal R(\tau).}
\tag{144.R39}
\]

This proves the blind correction formula from the accepted Appell
normalization without assigning any one of the four Appell summands to
a separate Poisson owner.

### 3.5 Mixed shadow

Since \(e(hr\tau)\) is holomorphic and
\(\partial_{\bar\tau}y=i/2\), differentiating (144.R20) gives

\[
 \partial_{\bar\tau}\widehat H(\tau)
 ={i\over16\sqrt y}
 \sum_{\substack{h\in\mathbb Z\\r\ {\rm odd}}}
 \chi_4(r)(r-4h)
 e^{-\pi(r-4h)^2y/4}e(hr\tau).
\tag{144.R40}
\]

Put \(a_0=r-4h\) and \(u_0=8h+a_0\). Then

\[
 hr=\frac{u_0^2}{16}-\frac{a_0^2}{16},\qquad
 e^{-\pi a_0^2y/4}q^{-a_0^2/16}
 =\overline{q^{a_0^2/16}},
\tag{144.R41}
\]

and \(u_0\equiv a_0\pmod8\). Grouping by the odd residue
\(\mu\bmod8\) yields exactly

\[
 \partial_{\bar\tau}\widehat H(\tau)
 ={i\over16\sqrt y}
 \sum_{\mu\in\{1,3,5,7\}}
 \Theta_\mu(\tau)\overline{G_\mu(\tau)},
\tag{144.R42}
\]

where

\[
 \Theta_\mu=\sum_{u_0\equiv\mu(8)}q^{u_0^2/16},
\qquad
 G_\mu=\sum_{a_0\equiv\mu(8)}\chi_4(a_0)a_0 q^{a_0^2/16}.
\tag{144.R43}
\]

Thus the blind factor \(i/(16\sqrt y)\), conjugation, four odd
components, and level-\(16\) unary constituents are all compatible
with the scalar level-\(4\) Appell section. The different component
level is not a contradiction.

### 3.6 Scalar heat identity and owner status

The accepted completed section obeys

\[
 \widehat H(\gamma\tau)
 =\chi_4(D)(C\tau+D)\widehat H(\tau)
\quad(\gamma\in\Gamma_0(4)).
\tag{144.R44}
\]

Set

\[
 z=-\frac DC+\frac{i}{C^2y}.
\tag{144.R45}
\]

Then

\[
 \gamma z=\frac AC+iy,\qquad Cz+D=\frac{i}{Cy}.
\tag{144.R46}
\]

Expanding
\(\widehat H=F+1/4+\mathcal R\) on both sides gives

\[
\begin{aligned}
 \sum_{m\geq1}C(m)e(Am/C)e^{-2\pi my}
={}&{i\chi_4(D)\over Cy}
 \sum_{n\geq1}C(n)e(-Dn/C)e^{-2\pi n/(C^2y)}\\
&+{i\chi_4(D)\over4Cy}-{1\over4}\\
&+{i\chi_4(D)\over Cy}
 \mathcal R\!\left(-{D\over C}+{i\over C^2y}\right)
 -\mathcal R\!\left({A\over C}+iy\right).
\end{aligned}
\tag{144.R47}
\]

This is exactly (2.14) of the blind report. Its individual additive
direction, cusp constant, and two correction occurrences are correct.
Since \(AD\equiv1\pmod4\), one has
\(\chi_4(D)=\chi_4(A)\); the leading term
\(i\chi_4(A)/(4Cy)\) agrees with the Abel form of the accepted
Round-142 rational mean.

Equation (144.R47) is an exact identity for exponentially damped
coefficients, not the missing estimate for the oscillatory weight
\(e(\sqrt{Nm})\). Keeping both \(\mathcal R\)-terms returns the
aggregate accepted completion owner. Applying the lawful
character-Poisson transform to a smooth radial block still returns the
Round-140 reciprocal height-alias family with its half-boundary,
subtraction, negative aliases, and entry/exit ledger.

## 4. First doubtful or unproved step

After the new absolute deletion, the first unproved signed assertion is

\[
\boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\
 |k_m^2-Nm|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon.}
\tag{144.R48}
\]

Neither (144.R47), the mixed shadow, nor the root count proves
(144.R48). The remaining support has the same
\(M^{1/4+\varepsilon}\) absolute block capacity, and the completed
character-Poisson transform still has the accepted reciprocal
capacity.

There is also a proof-presentation gap in the blind report that should
not be promoted independently: the sentence “Direct Poisson summation
for this completed kernel ... proves (1.4)” does not by itself justify
Poisson summation across the Abel-regularized isotropic line. The
formula is nevertheless certified here by the termwise identity
(144.R39) with the already accepted Appell completion. Likewise, the
blind sentence that smooth transforms follow by “justified
Laplace/Mellin superposition” is only a route description unless the
superposition and both transformed \(\mathcal R\)-terms are actually
controlled; it supplies no proof of (144.R48).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| \(J<1\) | **Pass.** The nonzero sum in (144.R1) is empty; only \(j=0\) remains, handled by (144.R15)--(144.R16). |
| Squareful \(N\) | **Pass.** The prime-power proof includes every valuation. The divisor reversal in (144.R24) is uniform in the exponents of \(N\). |
| \(j=0\) | **Pass/separate.** For square \(N\), \(O(\sqrt M)\) exact radicals can occur on a block, but their \(m^{-3/4}\) mass is globally summable. |
| \(k\)-range injection | **Pass.** Equations (144.R25)--(144.R26) put \(k_m\) in one complete residue interval and make fixed-\(j\) recovery of \(m\) unique. |
| Nearest-integer and dyadic endpoints | **Pass.** There are no half-integer ties; half-open blocks assign every endpoint and its block threshold exactly once. |
| Maximal window | **Pass/scoped.** \(J_M=M^{3/4}\) is target-safe. Any exponent \(>3/4\) is not certified by this absolute ledger; no impossibility theorem is claimed. |
| Appell correction normalization | **Pass.** The bijection (144.R33)--(144.R38) proves \(\mathcal R=\mathcal C_{\rm nh}\), including the factor \(1/4\) and the sign. |
| Mixed shadow | **Pass.** Direct differentiation gives the blind \(i/(16\sqrt y)\) factor and the four odd residue components. |
| Heat identity | **Pass.** Equations (144.R45)--(144.R47) reproduce every constant, phase direction, and correction term. |
| Round-142 rational compatibility | **Pass.** Its Abel leading constant matches \(i\chi_4(A)/(4Cy)\); no coefficient is silently changed from \(C\) to \(r_2/4\). |
| Strict-survivor ownership | **Pass with revision.** The new strict survivor is (144.R6), not the blind full-cone sum. The Appell transform itself still supplies no strict survivor. |

No numerical experiment is used. All controls are algebraic.

## 6. Dependencies and exact artifacts used

The review used:

- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/blind_cone_automorphy_feasibility.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_lattice_completion_attack.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/near_radical_phase_cell_attack.md;
- rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/synthesis.md;
- the accepted Round-63 Appell normalization and completion artifacts
  listed in Section 6 of the discovery report; and
- sources/semikhatov_taormina_tipunin_2005.md.

The only external theorem interface is the already audited completed
higher-Appell Jacobi law:

1. A. M. Semikhatov, A. Taormina, and I. Yu. Tipunin,
   *Higher-Level Appell Functions, Modular Transformations, and
   Characters*, Commun. Math. Phys. 255 (2005), 469--512,
   https://arxiv.org/abs/math/0311314.
2. S. Zwegers, *Multivariable Appell functions and nonholomorphic
   Jacobi forms*, Res. Math. Sci. 6 (2019), article 16,
   https://doi.org/10.1007/s40687-019-0178-0.

The required hypotheses are met: the Appell level is the positive
integer \(4\), the modular variable is in the upper half-plane, the
specialized denominator \(1+e(2n\tau)\) has no pole there, and the
scalar specialization is used only for \(\Gamma_0(4)\). The stricter
double-cone expansion domain from Semikhatov--Taormina--Tipunin is not
invoked. No source theorem is used for the new cell estimate or for
the still-open signed bound.

## 7. Recommended state effect

**Promote after conductor validation** the gcd-average lemma
(144.R1), the uniform cell count (144.R2)--(144.R3), and the sharper
owner-complete reduction (144.R6).

**Revise** the Round-141 statements that the congruence ledger is
\(M^{-3/4}J^{3/2}\) and exhausts its target-safe range at
\(J=\sqrt M\). The correct averaged ledger is
\(M^{-3/4}J\), and it exhausts the presently certified polynomial
range at \(J=M^{3/4}\).

**Retain** the accepted Appell-completion no-go: the completion,
mixed shadow, and heat identity are exact but aggregate to the same
Round-63/Round-140 owner and prove no cancellation for the new
survivor.

**Revise** any unqualified claim that Round 144 yields no strict
owner-complete survivor. The accurate statement is that it yields no
strict *automorphic-transform* survivor; the post-unmask gcd average
does yield the strict arithmetic survivor (144.R6).

**Reject** the description of the blind full-cone expression as the
support-smaller survivor. It is a useful target-equivalent unmasking,
but (144.R6) is the actual strict support reduction.

Leave (144.R48) open. This review makes no state, graph, campaign,
synthesis, validation, or downstream proof change. In particular, it
proves no lower-GAR, M1, M9-M1, M9, endpoint, cross-term, internal
\(1/3\), Li--Yang, quarter, or Gauss-circle exponent claim.
