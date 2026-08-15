# Blind RCS coefficient algebra

Campaign: `m9-m1-dual-r2-recombination`  
Round: 14  
Task: `blind_rcs_coefficient_algebra`  
Role: statement-only exact deriver  
Generated at: `2026-08-12T17:45:25+08:00`  
Proof-graph SHA-256: `ba43cb4e073a06640030a9090df6b57cc4ad8564feada6a0698aa777d1378b14`  
Blind status: independent statement-only derivation; no other Round-14 report read  
Status: candidate evidence only; no shared proof state was edited

## 1. Result

The monomial cancellation requested in the brief is **exact**:

\[
 (hX)^{1/4}q^{-3/4}
 \frac{\Phi(h/(H_D+1))}{h}
 =X^{1/4}(hq)^{-3/4}\Phi(h/(H_D+1)).
\]

After the exact positive/negative-frequency pairing, the stationary part of
the full active M1 aggregate is

\[
 \boxed{
 \sum_{j=0}^{J}\mathcal M_1(D_j;X)
 =-\frac4\pi X^{1/4}\operatorname {Re}\!\left{
 e(1/8)\sum_{1\le n\le16\sqrt X}
 \frac{\mathcal C_X^*(n)}{n^{3/4}}e(\sqrt{Xn})
 \right}+\mathcal E_X .}
 \tag{1.1}
\]

Here the exact restricted divisor coefficient is

\[
 \boxed{
 \mathcal C_X^*(n)
 =\sum_{\substack{h\mid n\\q=n/h\ {\rm odd}}}
 \chi_4(q)\,\Omega_X^*(n,h),}
 \tag{1.2}
\]

with

\[
 \boxed{
 \Omega_X^*(n,h)
 =\sum_{j=0}^{J}
 \mathbf1_{h\le H_j}\,
 \Phi\!\left(\frac{h}{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{\frac Xn}\right)\right]^* .}
 \tag{1.3}
\]

The star preserves the B-process endpoint half weight.  At smooth support
edges it is immaterial because the profile vanishes.  At the hard top it is
supplemented by the explicit one-sided cotangent boundary term displayed
below; the accepted endpoint-separation estimate makes the resulting
two-sided Vaaler boundary contribution (O(1)).

Thus summing the actual frequency shells removes the artificial (L)
partition, but summing the actual spatial scales does **not** remove the
divisor dependence.  The multiplier (1.3) depends on the divisor angle
(h/\sqrt n), on the dyadic phase of that angle, on the exact floors
(H_j=\lfloor D_jX^{-1/4}\rfloor), and on the hard endpoint.  It is not an
(n)-only multiplier.  Consequently (1.2) is not
(r_2(n)/4) times an (n)-only symbol.  It is an exact, finite,
floor-perturbed log-periodic/angular localization of the
(\chi_4)-divisor convolution.

The weakest natural global estimate sufficient for the full active M1
aggregate is

\[
 \boxed{
 \operatorname {Re}\!\left{
 e(1/8)\sum_{n\le16\sqrt X}
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 \right}\ll_\varepsilon X^\varepsilon .}
 \tag{1.4}
\]

The modulus version is stronger than necessary.  Estimate (1.4) is
logically strictly weaker than a uniform blockwise M9-M1 estimate because
it permits cancellation between the actual (D)- and (L)-pieces.  It is,
however, only a return map: by (1.1) and the accepted transform errors it
is equivalent, up to target-sized terms, to bounding the original global
active M1 sum.  The recombination therefore weakens the *formulation* from
blockwise to global but supplies no new cancellation theorem.

## 2. Exact statement and hypotheses

Let (X) be sufficiently large, put

\[
 y=\lfloor\sqrt X\rfloor,
 \qquad \vartheta=\frac{X}{y^2},
 \qquad D_j=2^{-j}y,
 \]

and let

\[
 J=\max\{j\ge0:D_j\ge X^{1/4}\},
 \qquad H_j=\left\lfloor D_jX^{-1/4}\right\rfloor.
 \tag{2.1}
\]

Use the authorized profile construction

\[
 W(t)=\eta(t)-\eta(2t),
 \]

where (W\in C_c^\infty([1/2,4/3])), (0\le W\le1), and
(W=1) on ([2/3,1]).  The active spatial weights are

\[
 w_0(d)=\mathbf1_{d\le y}W(d/y),
 \qquad
 w_j(d)=W(d/D_j)\quad(1\le j\le J).
 \tag{2.2}
\]

The bottom remainder is

\[
 w_{\rm bot}(d)=\eta(d/D_{J+1}),
 \]

and the continuous telescoping algebra gives

\[
 w_0(d)+\sum_{j=1}^{J}w_j(d)+w_{\rm bot}(d)
 =\mathbf1_{0<d\le y}.
 \tag{2.3}
\]

On positive integers this is the exact denominator partition used before
Vaaler expansion.  The inactive bottom term is not Fourier expanded and
costs (O(X^{1/4})).

For (1\le h\le H_j), the actual Vaaler coefficient is

\[
 \alpha_{h,H_j}
 =-\frac{\Phi(h/(H_j+1))}{2\pi i h}
 =\frac{i}{2\pi h}\Phi\!\left(\frac h{H_j+1}\right),
 \tag{2.4}
\]

where

\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
 \qquad 0<u<1.
 \tag{2.5}
\]

Let (v_{j,L}(h)) denote the actual positive-frequency shell partition.
Only its exact partition identity is needed here:

\[
 \sum_Lv_{j,L}(h)=\mathbf1_{1\le h\le H_j}.
 \tag{2.6}
\]

Thus the (u_{L,H}) suppressed in the Round-13 RCS can be made exact by

\[
 u_{j,L,H_j}(h)
 =v_{j,L}(h)\frac{\Phi(h/(H_j+1))}{h};
 \tag{2.7}
\]

the universal leading factor (-2e(1/8)/\pi) is kept outside the RCS.
The authorized packet does not specify a particular formula for
(v_{j,L}), but (2.6) shows that the globally recombined coefficient is
independent of that choice.

Define

\[
 B_{j,h}(X)=\sum_{d\ge1}\chi_4(d)w_j(d)e(hX/d).
 \tag{2.8}
\]

Since the weights are real, the raw two-sided M1 block is exactly

\[
 \mathcal M_1(D_j;X)
 =2\operatorname {Re}\left{
 -4\sum_{h=1}^{H_j}\alpha_{h,H_j}B_{j,h}(X)
 \right}.
 \tag{2.9}
\]

The odd-lattice B-process uses

\[
 d_{h,q}=2\sqrt{\frac{hX}{q}},
 \qquad q\in2\mathbb Z+1,\quad q>0.
 \tag{2.10}
\]

For an interior profile, its stationary main term is

\[
 B_{j,h}^{\rm stat}(X)
 =\frac{e(1/8)}{i}(hX)^{1/4}
 \sum_{\substack{q>0\ {\rm odd}\\
 d_{h,q}\in\operatorname {supp}w_j}}^{*}
 \frac{\chi_4(q)}{q^{3/4}}
 w_j(d_{h,q})e(\sqrt{Xhq}).
 \tag{2.11}
\]

For the hard top, the accepted one-sided formula additionally has the
explicit boundary

\[
 E_{0,h}^{\chi}(X)
 =\frac1{2i}\left{
 \frac{e(hX/y+y/4)}{1-e(h\vartheta-1/4)}
 -\frac{e(hX/y+3y/4)}{1-e(h\vartheta-3/4)}
 \right},
 \tag{2.12}
\]

and, equivalently to (2.11),

\[
 \begin{aligned}
 B_{0,h}(X)
 ={}&E_{0,h}^{\chi}(X)
 +\frac{e(1/8)}{i}(hX)^{1/4}
 \sum_{\substack{4h<q<16h\\q\ {\rm odd}}}
 \frac{\chi_4(q)}{q^{3/4}}
 W\!\left(\sqrt{\frac{4\vartheta h}{q}}\right)
 e(\sqrt{Xhq})\\
 &+O_W(\log(2+h)).
 \end{aligned}
 \tag{2.13}
\]

The hard cutoff inside (W(t)\mathbf1_{t\le1}) supplies the exact full
endpoint convention.  In the general RCS notation, a stationary point
lying exactly on a transform endpoint has half weight.  At the lower and
upper smooth support edges (W=0), so that convention changes nothing.
At the hard point (d=y), it is retained together with (2.12).  The
accepted separation of the denominators in (2.12) makes their full
two-sided Vaaler contribution (O(1)).

The precise individual ranges are as follows.  For the top block,

\[
 1\le h\le H_0,\qquad q>0\text{ odd},\qquad
 \frac{4hX}{y^2}\le q\le\frac{16hX}{y^2},
 \tag{2.14}
\]

with support and star conventions deciding equality.  For (j\ge1),

\[
 1\le h\le H_j,\qquad q>0\text{ odd},\qquad
 \frac{9hX}{4D_j^2}\le q\le\frac{16hX}{D_j^2}.
 \tag{2.15}
\]

Writing (n=hq), these become respectively

\[
 \frac{4h^2X}{y^2}\le n\le\frac{16h^2X}{y^2},
 \tag{2.16}
\]

and

\[
 \frac{9h^2X}{4D_j^2}\le n\le\frac{16h^2X}{D_j^2}.
 \tag{2.17}
\]

Since (h\le D_jX^{-1/4}), all stationary products satisfy

\[
 1\le n\le16\sqrt X.
 \tag{2.18}
\]

The parity condition is exactly (q=n/h) odd, or equivalently
(v_2(h)=v_2(n)).  This is compatible with

\[
 \frac{r_2(n)}4=\sum_{q\mid n}\chi_4(q)
 =\sum_{\substack{q\mid n\\q\ {\rm odd}}}\chi_4(q),
 \tag{2.19}
\]

but compatibility of parity does not remove the angular multiplier.

For errors, the statement packet supplies (O_W(1)) after each smooth
interior Vaaler shell transform.  There are (O(\log^2X)) pairs ((j,L)).
For the top block, weighting the (O_W(\log(2+h))) remainder in (2.13) by
(\Phi(h/(H_0+1))/h) gives (O_W(\log^2(2H_0))), and (2.12) contributes
(O(1)) after the actual two-sided weights.  Hence the total transform and
hard-boundary error in (1.1) satisfies

\[
 \boxed{\mathcal E_X=O_W(\log^2(2X)).}
 \tag{2.20}
\]

Returning all the way to the pre-Fourier decomposition adds the separate
inactive-bottom cost (O(X^{1/4})); it is not a transform error.

## 3. Proof and derivation

### 3.1 Odd-lattice stationary constant

For odd (d),

\[
 \chi_4(d)=-ie(d/4).
 \]

Put (d=2m+1).  The absorbed phase is

\[
 f_h(m)=\frac{hX}{2m+1}+\frac{2m+1}{4}.
 \]

In the Poisson mode (k\in\mathbb Z), stationarity of
(f_h(m)-km) means

\[
 -\frac{2hX}{d^2}+\frac12=k.
 \]

Set (q=1-2k).  Then (q) is odd and

\[
 q=\frac{4hX}{d^2},
 \qquad d=d_{h,q}=2\sqrt{\frac{hX}{q}}.
 \tag{3.1}
\]

At the stationary point,

\[
 f_h(m)-km
 =\sqrt{Xhq}-\frac{q-1}{4}.
 \]

Since (q) is odd,

\[
 e\!\left(-\frac{q-1}{4}\right)=\chi_4(q).
 \tag{3.2}
\]

Also

\[
 f_h''(m)=\frac{8hX}{d^3}>0,
 \]

so the (e(t)=e^{2\pi it}) stationary-phase factor is

\[
 \frac{e(1/8)}{\sqrt{f_h''(m)}}
 =e(1/8)(hX)^{1/4}q^{-3/4}.
 \tag{3.3}
\]

Restoring the initial factor (-i=1/i) gives exactly (2.11).  This proves
the constants (e(1/8)/i), the odd dual support, the character
(\chi_4(q)), and the amplitude ((hX)^{1/4}q^{-3/4}).

### 3.2 Vaaler constant and positive/negative pairing

From (2.4),

\[
 -4\alpha_{h,H_j}
 =-\frac{2i}{\pi h}\Phi\!\left(\frac h{H_j+1}\right).
 \]

Multiplying this by the stationary constant (e(1/8)/i) gives

\[
 -\frac{2e(1/8)}\pi
 \frac{\Phi(h/(H_j+1))}{h}.
 \tag{3.4}
\]

The negative-frequency half is the complex conjugate because (w_j) is
real and (alpha_{-h,H_j}=\overline{\alpha_{h,H_j}}).  Therefore the full
block is twice the real part, changing the leading coefficient in (3.4)
from (-2/\pi) to the (-4/\pi\) in (1.1).

### 3.3 Product grouping and the formal cancellation

Let (n=hq).  Then, without an estimate or discarded sign,

\[
 \begin{aligned}
 (hX)^{1/4}q^{-3/4}\frac{\Phi(h/(H_j+1))}{h}
 &=X^{1/4}h^{1/4}(n/h)^{-3/4}h^{-1}
 \Phi\!\left(\frac h{H_j+1}\right)\\
 &=X^{1/4}n^{-3/4}
 \Phi\!\left(\frac h{H_j+1}\right).
 \end{aligned}
 \tag{3.5}
\]

Thus the power weight is radial, but the Vaaler and spatial symbols remain
on the divisor (h).  For a single ((D_j,L)) shell, the exact product
coefficient (with the universal constant outside) is

\[
 \sum_{\substack{hq=n\\q\ {\rm odd}}}
 \chi_4(q)v_{j,L}(h)
 \Phi\!\left(\frac h{H_j+1}\right)
 [w_j(d_{h,q})]^*.
 \tag{3.6}
\]

Summing (L) and using (2.6) gives the (j)-summand in (1.3).  Summing
(j) gives (1.2), and the common phase becomes (e(\sqrt{Xn})).  This proves
(1.1)--(1.3).

### 3.4 Why the (D)-sum does not produce (r_2(n)/4)

If the multiplier of every divisor (q=n/h) in (1.2) were one common
quantity (M_X(n)), then (2.19) would give

\[
 \mathcal C_X^*(n)=M_X(n)\frac{r_2(n)}4.
 \]

The exact multiplier is instead (1.3).  To display its angular dependence,
put

\[
 t_j=\frac{d_{h,q}}{D_j}
 =\frac{2h\sqrt X}{D_j\sqrt n},
 \qquad z_n=\frac{\sqrt n}{2X^{1/4}},
 \qquad
 \rho_j=\frac{D_jX^{-1/4}}{\lfloor D_jX^{-1/4}\rfloor+1}.
 \]

Then the identity

\[
 \boxed{
 \frac{h}{H_j+1}=\rho_jt_jz_n}
 \tag{3.7}
\]

is exact.  Moreover

\[
 t_j=2^{j+1}\sqrt\vartheta\,\frac h{\sqrt n}.
 \tag{3.8}
\]

Thus, away from the top and bottom truncations, a summand of (1.3) has the
form

\[
 W(t_j)\Phi(\rho_jt_jz_n).
 \tag{3.9}
\]

The active (j)'s are precisely the dyadic windows for which (t_j) lies
in the fixed support of (W).  Scaling (h/\sqrt n) by (2) shifts this
window index, which is the log-periodic angular structure.  The finite
range of (j), the top indicator, the bottom removal, and the factors
(\rho_j) from the exact floors perturb that periodicity.  Formula (3.9)
is therefore not exactly log-periodic, and it is certainly not radial.

There is also an immediate hard-cone obstruction to a full divisor sum.
Every active term has (d_{h,q}\le y), hence

\[
 h\le\frac{y}{2\sqrt X}\sqrt n
 =\frac{\sqrt n}{2\sqrt\vartheta}.
 \tag{3.10}
\]

So complementary divisors with (h) above this angular boundary are
absent.  For example, for fixed (n=5) and sufficiently large (X), the
divisor pair (h=1,q=5) lies on the top plateau because
(d_{1,5}/y=2\sqrt\vartheta/\sqrt5\in[2/3,1]), whereas
(h=5,q=1) violates (3.10).  The two divisor multipliers are therefore
unequal even though both occur in (r_2(5)/4=2).  This refutes the proposed
common-multiplier factorization at the exact support level, before any
analytic estimate.

If one formally replaced every (Omega_X^*(n,h)) by (1) and restored
all divisor angles, then (1.1) would become the usual Hardy-type radial
sum with coefficient (r_2(n)): indeed

\[
 -\frac4\pi\cdot\frac{r_2(n)}4
 \operatorname {Re}e(\sqrt{Xn}+1/8)
 =\frac{r_2(n)}\pi
 \operatorname {Re}e(\sqrt{Xn}-3/8).
 \]

That replacement is false for the actual M1 partition.  The smallest
exact remainder preventing the Hardy collapse is not a scalar error term;
it is the whole angular variation

\[
 \sum_{\substack{h\mid n\\n/h\ {\rm odd}}}
 \chi_4(n/h)\bigl(\Omega_X^*(n,h)-M_X(n)\bigr)
 \]

for any chosen radial reference (M_X(n)).  No canonical choice makes this
variation target-sized by algebra alone.

### 3.5 Weakest sufficient estimate and logical strength

Equation (1.1), (2.20), and the (O(X^{1/4})) inactive-bottom estimate show
that (1.4) implies the total M1 contribution required by the final
conditional assembly.  If desired, (1.4) can be restricted to the
currently unresolved corridor \(\mathcal U_1\), because the complementary
frequency regions are already controlled in the accepted graph.

Uniform blockwise M9-M1 implies (1.4), after summing the (O(\log X))
blocks and absorbing logarithms into (X^\varepsilon).  The converse does
not follow: (1.4) controls only the one actual signed aggregate and has no
projection that recovers an individual (D_j) or (L) shell.  Thus it is
strictly weaker as a sufficient hypothesis for the final sum.  On the
other hand, the B-process identities run both ways up to (2.20), so (1.4)
is not a new theorem about a simpler (r_2)-weighted object.  It is the
global M1 problem in recombined coordinates.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in the stationary constant, the
Vaaler constant, the cancellation (3.5), the (L)-sum, the (D)-sum, or
the refutation of the (r_2(n)/4) factorization.  These use only exact
identities and the already accepted interior and one-sided B-process
statements.

The first unproved step is precisely the global signed estimate (1.4), or
its restriction to \(\mathcal U_1\).  Product-fiber absolute values discard
the (chi_4(q)) signs and recover only the accepted
(\sqrt{LX/D}) capacity.  No estimate in the authorized packet controls
the angular restricted convolution (1.2).  Moreover, because (1.4) is
equivalent to the original global active M1 sum up to target-sized errors,
calling it a Hardy estimate would conceal rather than solve the return
map.

The only definitional omission in the Round-13 RCS is a concrete formula
for the artificial frequency-shell weights (v_{j,L}).  This omission has
no effect after the exact (L)-sum (2.6), but a shell-by-shell formula more
specific than (3.6) would require that convention to be frozen.

## 5. Required controls and outcomes

### Monomial cancellation control: pass

The exponent of (h) in (3.5) is
(1/4+3/4-1=0).  No factor (h^{\pm1/2}), (q^{\pm1/2}), (2), or
(\pi) survives.  The universal full two-sided constant is exactly
(-4e(1/8)/\pi) outside the real part.

### Character and parity control: pass

The original identity (chi_4(d)=-ie(d/4)) forces
(q=1-2k) odd, and the stationary phase contributes
(e(-(q-1)/4)=\chi_4(q)).  Grouping (n=hq) preserves, rather than
averages, this character.  Even (q) never occurs; equivalently it would
have zero (chi_4)-weight in (2.19).

### Negative-frequency control: pass

The positive transformed sum is not itself the M1 block.  Restoring
negative frequencies gives exactly twice its real part and changes the
constant from (-2/\pi) to (-4/\pi), as recorded in (1.1).

### Hard-endpoint and star control: pass

The top profile is (W(d/y)\mathbf1_{d\le y}), not a smooth full-line
profile.  Its exact cotangent boundary is retained in (2.12), and its
actual two-sided Vaaler contribution is (O(1)).  Stationary endpoint
terms carry half weight under the star convention.  Smooth support-edge
half weights vanish with (W).  No hard endpoint was absorbed into an
interior (C_c^\infty) symbol.

### (L)-partition control: pass

Summing the actual shell weights uses only the exact identity (2.6), so no
factor (O(\log H_j)) enters the main coefficient.  Logarithms occur only
in the accumulated transform errors.

### Spatial telescoping control: pass, with the proposed conclusion refuted

Equation (2.3) telescopes exactly, but it cannot be inserted into (1.3)
because each (w_j) is multiplied by the scale-dependent
(Phi(h/(H_j+1))), the frequency cutoff (h\le H_j), and the endpoint
star.  The surviving exact multiplier is (3.9), not (1-w_{\rm bot}).

### (r_2) control: fail for the proposed factorization

The parity support agrees with the classical divisor identity, but the
hard angular restriction (3.10) and the exact scale multiplier (3.9) give
different weights to different divisor pairs of the same (n).  Hence no
common (n)-only factor can be pulled in front of the divisor sum.

### Error control: pass at the stated scope

The active interior and top transform errors total
(O_W(\log^2(2X))).  The inactive spatial remainder costs the separate
(O(X^{1/4})) already present before Fourier expansion.  Neither error can
certify (1.4), but both are within the target scale once (1.4) is assumed.

No web search and no numerical experiment were used.

## 6. Dependencies and exact artifacts used

Only the brief-authorized files were read:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/synthesis.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/briefs/blind_rcs_coefficient_algebra.md`.

No other Round-14 report, legacy claimant derivation, web source, or
numerical artifact was read.  The exact top boundary formula and its error
status are used from the authoritative `M9-M1-top-endpoint-transform`
entry in `state/proof_obligations.yml`; the interior stationary kernel and
RCS equivalence are used from the Round-13 synthesis.

## 7. Recommended state effect

**Promote the coefficient algebra, retain the analytic obligation.**  The
conductor may promote an exact reduction stating (1.1)--(1.3), the
constant (-4e(1/8)/\pi), the product range (n\le16\sqrt X), the
odd-co-divisor restriction, and the endpoint-star convention.

**Reject the proposed exact (r_2(n)/4) collapse for M1 alone.**  The
actual coefficient is the angular, floor-dependent restricted convolution
(mathcal C_X^*(n)).  The formal power cancellation is true, but it does
not cancel (Phi), the spatial profile, the height floor, the frequency
cutoff, or the hard cone.

**Allow a weaker global replacement only with an explicit bridge edit.**
The global estimate (1.4) is sufficient and strictly weaker than uniform
blockwise M9-M1, but the current authoritative bridge names blockwise M9.
Any state change should introduce a separate global-M1 obligation and
prove its implication into the conditional assembly rather than silently
marking M9-M1 complete.

**Retain RCS/M9-M1 as open.**  The recombined bound remains equivalent to
the original global active M1 problem up to controlled errors.  No
asymptotic cancellation estimate has been proved in this report.
