# Round 179 hostile audit: primitive-conductor orientation defect

## 1. Result

The primitive-frequency Möbius projector, its (d=1) trace, the
(q/u_0) normalization, and the exact two-orientation decomposition are
all correct.  For odd (q),

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
 \qquad
 K_q(b)+K_q(-b)=\frac{2\mu(q)}q
 \quad(b\in U(q)).
\tag{179.H1}
\]

Consequently the exact-(q) block is

\[
 \boxed{
 \mathcal C_{u_0,q}
 =\frac q{u_0}\sum_{b\in U(q)}K_q(b)
       \bigl(B^+_{q,b}-B^-_{q,b}\bigr)
  +\frac{2\mu(q)}{u_0}\sum_{b\in U(q)}B^-_{q,b}.}
\tag{179.H2}
\]

There is a stronger exact self-return after centering the projector.  Put

\[
 \widetilde K_q(b)=K_q(b)-\frac{\mu(q)}q.
\tag{179.H2a}
\]

Then (\widetilde K_q(-b)=-\widetilde K_q(b)) on (U(q)), and for every
odd (u_0>1) and (b\in U(u_0)), reduced modulo each (q\mid u_0),

\[
 \boxed{
 \sum_{q\mid u_0}\frac q{u_0}\widetilde K_q(b)
 =E_{u_0}(b).}
\tag{179.H2b}
\]

Thus the centered defect summed over all conductors is exactly the
original literal two-orientation block.  If
(\mathcal O_{u_0}) denotes that original block and
(\widetilde{\mathcal D}_{\le Q_B}),
(\widetilde{\mathcal D}_{>Q_B}) its centered conductor pieces, then

\[
 \boxed{
 \widetilde{\mathcal D}_{>Q_B}
 =\mathcal O_{u_0}-\widetilde{\mathcal D}_{\le Q_B}.}
\tag{179.H2c}
\]

The centered trace is

\[
 \frac{\mu(q)}{u_0}\sum_b(B^+_{q,b}+B^-_{q,b}),
\tag{179.H2d}
\]

and its all-conductor sum vanishes because
\(\sum_{q\mid u_0}\mu(q)=0\).  In particular, with
\(\mathcal C_{\le Q_B}\) the already-safe exact low-conductor block,

\[
 \boxed{
 \mathcal C_{>Q_B}=\mathcal O_{u_0}-\mathcal C_{\le Q_B}.}
\tag{179.H2e}
\]

This is not lower mass; it is an exact algebraic self-return showing that
the primitive-conductor parity resolution, after the safe low packet is
removed, is equivalent to the unresolved original literal orientation
block up to a target-safe term.

The second term is a genuine target-safe primitive trace.  At fixed
((\kappa,u)), summing it over \(q\mid u_0\), (q>Q_B), and
(u_0\mid u) costs only divisor factors and is
(O(LX^\varepsilon)).  It is present only for squarefree (q); for
nonsquarefree (q) it vanishes exactly.  In the centered form (179.H2d),
the squarefree trace terms cancel exactly after all (q\mid u_0), with
the (q=1) trace essential to that cancellation.

The first term is not contracted by the parity identity.  Its
coefficient-uniform positive capacity is still

\[
 \boxed{O_\varepsilon(LqX^\varepsilon)}
\tag{179.H3}
\]

at exact conductor (q).  Thus the projector removes at most the
previous logarithmic loss, not the conductor power.  One square-root
contraction restores to (L\sqrt qX^\varepsilon), still above the local
(L X^\varepsilon) target on the power-size high-(q) range.

The exact self-return (179.H2b)--(179.H2e) already shows that conductor
centering supplies no new contraction.  There is also no literal
orientation involution in the authorized data.
There are two exact algebraic candidates, and each fails at a different
literal seam:

1. The fixed-((u,v,n)) reflection
   ((s,w)\mapsto(u-s,v-w)) keeps (u_0,q,b), but it does not preserve
   the positive displacement domain.  On its small domain intersection
   it reflects, rather than preserves, the two endpoint products, so the
   phases, selectors, squarefree fields, profiles, and hard endpoints are
   not conjugate.
2. The exchange
   ((u,v,s,w,+)\mapsto(v,u,w,s,-)) preserves the two products and the
   square-root phase, but it changes the primitive modulus and replaces
   the selected divisor at both endpoints by its complementary factor.
   That complement is below the literal upper near-square divisor window
   in the odd branch and is even in the even branch.  A live atom is
   therefore sent to the zero extension, not to the opposite live
   orientation.

Prime and prime-square adversarial bucket arrays, with the same unit
support and bucket-count shadow, attain capacity (\asymp Lq).  They
rule out any coefficient-uniform contraction from (179.H1), but they are
not lower mass for the actual selected amplitudes.  Conversely, no exact
relation between the actual (B^+_{q,b}) and (B^-_{q,b}) is proved.

The narrowest justified exit is therefore

\[
 \boxed{
 \texttt{primitive\_conductor\_orientation\_defect\_capacity\_or\_self\_return\_no\_go}.}
\tag{179.H4}
\]

This is a route-scoped no-go for primitive parity alone, the exact
all-conductor centered resolution, the two evident orientation
involutions, and coefficient-uniform or one-square-root closures.  It is
not a disproof of (177.K34).

## 2. Exact statement and hypotheses

Assume the complete literal Round-176/177 residual range

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

\[
 R_{\log}<2\kappa n<R_0,\qquad
 \kappa<\delta L,\qquad (u,n)<\gamma L,
 \qquad u\asymp v\asymp L/\kappa,
\tag{179.H5}
\]

where (\kappa,u) are odd, ((u,v)=1), both opposing orientations are
retained, and every squarefree, coprimality, parity-branch, Fejér,
selected/no-pair, displacement, profile, floor, star, hard-value,
endpoint-conjugation, and zero-extension field remains inside the
literal amplitudes.  Put

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,
 \qquad(n_0,u_0)=1,
\tag{179.H6}
\]

and retain only the already isolated complement

\[
 q=\frac{u_0}{(\ell,u_0)}>Q_B=(\log(2X))^B,
 \qquad
 \ell=\frac{u_0}{q}a,\quad a\in U(q).
\tag{179.H7}
\]

All of (u_0,q) are odd.  The exact coefficient is

\[
 c_{u_0}(\ell)=\frac q{u_0}c_q(a),
 \qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{179.H8}
\]

For a literal atom (z) in the plus or minus orientation, remove only
the exact-conductor phase and write

\[
 A_z^\pm=\Lambda_z^\pm e(\Psi_z^\pm+t_z/2),
 \qquad b_z=\bar v n_0\pmod q,
\tag{179.H9}
\]

\[
 B^\pm_{q,b}=\sum_{z\text{ in the }\pm\text{ orientation}\atop b_z=b}
 A_z^\pm.
\tag{179.H10}
\]

Because ((v,u)=1), (q\mid u_0\mid u), and
((n_0,u_0)=1), every occupied (b_z) lies in (U(q)).  No density,
periodicity, separability, variation, Fourier norm, phase cancellation,
or selector correlation is assumed for (179.H9).

Under these hypotheses this report proves:

1. the exact projector and sign law (179.H1), including the (d=1)
   contribution;
2. the exact normalized block identity (179.H2);
3. the all-conductor centered identity (179.H2b), exact self-return
   (179.H2c)--(179.H2e), the (q=1) boundary, and trace cancellation;
4. target-safe summation of the trace over \(q\mid u_0\) and
   (u_0\mid u), without using or recounting (q\le Q_B);
5. the restored defect capacity (179.H3), including all physical lifts;
6. exact failure of the two natural orientation maps at domain,
   endpoint, conductor, and selector seams; and
7. the coefficient-uniform adversarial limitation, explicitly
   quarantined from the actual literal coefficients.

No claim is made that the literal defect attains (179.H3), that
(177.K34) is false, or that a different selector- and phase-aware signed
theorem cannot prove it.

## 3. Proof or derivation

### 3.1 Möbius projector and the (d=1) trace

For odd (q), Fourier inversion for (E_q(x)=(-1)^{[x]_q}) gives

\[
 c_q(a)=\frac1q\sum_{x\bmod q}E_q(x)e(-ax/q).
\tag{179.H11}
\]

Let

\[
 K_q(b)=\sum_{a\in U(q)}c_q(a)e(ab/q).
\]

Interchanging the two finite sums and using the Ramanujan-sum identity

\[
 \sum_{a\in U(q)}e(a r/q)
 =\sum_{d\mid(q,r)}d\mu(q/d)
\tag{179.H12}
\]

yields

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)d
 \sum_{x\bmod q\atop x\equiv b\ (d)}E_q(x).
\tag{179.H13}
\]

Write (x=[b]_d+dj), (0\le j<q/d).  Both (d) and (q/d) are odd,
so

\[
 \sum_{x\bmod q\atop x\equiv b\ (d)}E_q(x)
 =(-1)^{[b]_d}\sum_{j=0}^{q/d-1}(-1)^j
 =E_d(b).
\tag{179.H14}
\]

This proves the first identity in (179.H1).  The arithmetic divisor
(d=1) contributes exactly

\[
 \frac{\mu(q)}qE_1(b)=\frac{\mu(q)}q,
\tag{179.H15}
\]

and must not be deleted.  If (b\in U(q)) and (d>1), then
(b\not\equiv0\pmod d) and, since (d) is odd,

\[
 [-b]_d=d-[b]_d,
 \qquad E_d(-b)=-E_d(b).
\tag{179.H16}
\]

Every (d>1) term cancels in (K_q(b)+K_q(-b)), while the two (d=1)
terms add.  This proves the second identity in (179.H1).  In particular,
the trace is nonzero precisely when (q) is squarefree.

### 3.2 Exact block decomposition and normalization

For the exact conductor (q), (179.H8)--(179.H10) give

\[
\begin{aligned}
 \mathcal C_{u_0,q}
 =\frac q{u_0}\sum_{a\in U(q)}c_q(a)
 \sum_{b\in U(q)}
 \left\{B^+_{q,b}e(ab/q)+B^-_{q,b}e(-ab/q)\right\}.
\end{aligned}
\tag{179.H17}
\]

There is no additional (q), (\varphi(q)), (g), or (u_0/q)
multiplicity in (179.H17): the sum over (a\in U(q)) is exactly the
set of aliases of conductor (q), and every physical lift is already in
the buckets.  Applying the definition of (K_q) gives

\[
 \mathcal C_{u_0,q}
 =\frac q{u_0}\sum_{b\in U(q)}
 \{K_q(b)B^+_{q,b}+K_q(-b)B^-_{q,b}\}.
\tag{179.H18}
\]

Substitution of (K_q(-b)=2\mu(q)/q-K_q(b)) proves (179.H2), including
the exact trace coefficient (2\mu(q)/u_0).

Equivalently, centering as in (179.H2a) gives the symmetric formula

\[
 \mathcal C_{u_0,q}
 =\frac q{u_0}\sum_{b\in U(q)}\widetilde K_q(b)
       (B^+_{q,b}-B^-_{q,b})
 +\frac{\mu(q)}{u_0}\sum_{b\in U(q)}
       (B^+_{q,b}+B^-_{q,b}).
\tag{179.H18a}
\]

The asymmetric trace in (179.H2) and the symmetric trace in
(179.H18a) differ only by the target-safe rank-one term moved between the
two displayed summands; both formulas are exact.

### 3.3 Centered all-conductor identity and exact self-return

Removing the (d=1) term from (179.H1) gives

\[
 \widetilde K_q(b)
 =\frac1q\sum_{d\mid q\atop d>1}\mu(q/d)dE_d(b).
\tag{179.H18b}
\]

Let (u_0>1) and (b\in U(u_0)).  Reducing (b) modulo every divisor
(q\mid u_0), and then interchanging the two divisor sums, gives

\[
\begin{aligned}
 \sum_{q\mid u_0}\frac q{u_0}\widetilde K_q(b)
 &=\frac1{u_0}\sum_{q\mid u_0}
   \sum_{d\mid q\atop d>1}\mu(q/d)dE_d(b)\\
 &=\frac1{u_0}\sum_{d\mid u_0\atop d>1}dE_d(b)
   \sum_{r\mid u_0/d}\mu(r).
\end{aligned}
\tag{179.H18c}
\]

The inner Möbius sum is zero unless (d=u_0), when it is one.  This
proves (179.H2b).  The (q=1) centered kernel is

\[
 K_1(0)=1,\qquad \widetilde K_1(0)=0.
\tag{179.H18d}
\]

Thus (179.H2b) is false at (u_0=1): its left side is zero while
(E_1=1).  This is harmless and must not be hidden.  The only conductor
is then (q=1\le Q_B), so (u_0=1) contributes nothing to the high-(q)
defect.  The uncentered identity does hold for every \(u_0\), because for
(u_0>1)

\[
 \sum_{q\mid u_0}\frac q{u_0}K_q(b)
 =E_{u_0}(b)+\frac1{u_0}\sum_{q\mid u_0}\mu(q)
 =E_{u_0}(b),
\tag{179.H18e}
\]

and the case (u_0=1) is (K_1(0)=E_1=1).

For fixed (u_0>1), let (b_z\in U(u_0)) be the unreduced primitive
bucket of an atom, and put

\[
 \mathcal O_{u_0}
 =\sum_{z\in+}E_{u_0}(b_z)A_z^+
  +\sum_{z\in-}E_{u_0}(-b_z)A_z^-.
\tag{179.H18f}
\]

Since (E_{u_0}(-b_z)=-E_{u_0}(b_z)), applying (179.H2b) atom by atom
shows

\[
 \sum_{q\mid u_0}\frac q{u_0}\sum_{b\in U(q)}
 \widetilde K_q(b)(B^+_{q,b}-B^-_{q,b})
 =\mathcal O_{u_0}.
\tag{179.H18g}
\]

For either orientation, (\sum_{b\in U(q)}B^\pm_{q,b}) is the same
unphased atom sum for every (q\mid u_0).  Therefore the centered traces
in (179.H18a) satisfy

\[
 \sum_{q\mid u_0}\frac{\mu(q)}{u_0}
 \sum_b(B^+_{q,b}+B^-_{q,b})=0.
\tag{179.H18h}
\]

The (q=1) term is essential in (179.H18h).  Splitting (179.H18g)--
(179.H18h) at (Q_B) proves, exactly,

\[
 \widetilde{\mathcal D}_{>Q_B}
 =\mathcal O_{u_0}-\widetilde{\mathcal D}_{\le Q_B},
 \qquad
 \widetilde{\mathcal T}_{>Q_B}
 =-\widetilde{\mathcal T}_{\le Q_B},
\tag{179.H18i}
\]

and hence (179.H2e).  The accepted low-(q) exact block is target-safe;
its centered defect is also target-safe because it differs from that
block by the target-safe centered trace.  Thus the high centered defect
is exactly the unresolved original literal orientation block minus an
already-safe piece.  This is an algebraic self-return, not a lower bound
for either side.

### 3.4 Trace capacity, divisor sums, and the low-(q) boundary

At fixed ((\kappa,u,u_0)), either orientation contains at most
(O(u_0L)) literal atoms, and (|A_z^\pm|\ll1) on its support.  Hence,
for a fixed (q\mid u_0),

\[
 \left|\frac{2\mu(q)}{u_0}
       \sum_{b\in U(q)}B^-_{q,b}\right|
 \ll L.
\tag{179.H19}
\]

For nonsquarefree (q), the left side is zero.  For squarefree (q),
the fixed-(q) cost is (O(L)), not (O(Lq)).  At fixed
((\kappa,u)), direct target-safe summation gives

\[
\begin{aligned}
 \sum_{u_0\mid u}\sum_{q\mid u_0\atop q>Q_B}
 \left|\frac{2\mu(q)}{u_0}\sum_bB^-_{q,b}\right|
 &\ll L\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|\\
 &\le L\,\tau(u)2^{\omega(u)}
 \ll_\varepsilon LX^\varepsilon.
\end{aligned}
\tag{179.H20}
\]

The restriction (q>Q_B) is kept throughout (179.H20).  Thus no atom or
alias from the already proved (q\le Q_B) packet is counted again.
Also (q=1), although it is the trivial primitive modulus, is always in
the excluded low-conductor packet.  The phrase “(d=1) trace” in
(179.H15) refers to the (d=1) term inside the projector for every high
conductor (q), not to the separate (q=1) packet.

### 3.5 Physical lift multiplicity

Put

\[
 h=\frac{u_0}{q},\qquad u=ghq.
\tag{179.H21}
\]

For a fixed ordered unit residue pair ((v\bmod q,n_0\bmod q)), the
physical (v)-interval has (O(gh)) lifts, the (n_0)-interval has
(O(h)) lifts, and the fibre has (O(\kappa)) sites.  Its multiplicity
is therefore

\[
 O(\kappa gh^2)=O(Lh/q).
\tag{179.H22}
\]

For fixed (b=\bar v n_0\pmod q), there are (O(q)) ordered unit
residue pairs, so one bucket has available multiplicity

\[
 O(Lh)=O(Lu_0/q).
\tag{179.H23}
\]

Summing over the (O(q)) unit buckets restores (O(Lu_0)), exactly the
literal fixed-((\kappa,u,u_0)) count.  Completion modulo (q) cannot
replace (179.H22) by one representative without erasing the physical
(g,h,\kappa) lifts.

### 3.6 Defect capacity and squarefree/nonsquarefree controls

The projector gives the uniform pointwise estimate

\[
 |K_q(b)|
 \le\frac1q\sum_{d\mid q}d|\mu(q/d)|
 =\prod_{p\mid q}\left(1+\frac1p\right)
 \ll_\varepsilon q^\varepsilon.
\tag{179.H24}
\]

The same estimate, with a harmless additional (1/q), holds for
(\widetilde K_q).  Thus centering changes no power.

Because the two orientations together have (O(u_0L)) atoms,

\[
 \left|\frac q{u_0}\sum_b\widetilde K_q(b)
 (B^+_{q,b}-B^-_{q,b})\right|
 \ll_\varepsilon LqX^\varepsilon.
\tag{179.H25}
\]

Thus exact parity improves the inherited (Lq\log(2q)) positive ledger
only by a logarithm.  It supplies no conductor power.

This is sharp for coefficient-uniform bucket algebra.  If (q=p) is an
odd prime, then

\[
 K_p(b)=E_p(b)-\frac1p,
 \qquad \widetilde K_p(b)=E_p(b),
 \qquad
 \sum_{b\in U(p)}|\widetilde K_p(b)|=p-1.
\tag{179.H26}
\]

Here the asymmetric trace coefficient is \(-2/u_0\), while the centered
trace coefficient is \(-1/u_0\); the centered defect kernel still has
full \(p\)-mass.  If \(q=p^2\), then

\[
 \widetilde K_{p^2}(b)=K_{p^2}(b)
 =E_{p^2}(b)-\frac1pE_p(b),
 \qquad \mu(p^2)=0,
\tag{179.H27}
\]

and every unit value has magnitude between (1-1/p) and (1+1/p).
Hence

\[
 \sum_{b\in U(p^2)}|K_{p^2}(b)|\asymp p^2.
\tag{179.H28}
\]

The nonsquarefree packet is therefore a pure orientation defect of full
coefficient-uniform capacity; disappearance of the trace gives no saving.

For the mandatory adversarial false control, take (u_0=q=p) or (p^2),
set (B^-_{q,b}=0), and assign artificial bounded atoms so that

\[
 B^+_{q,b}=M\,\frac{\overline{\widetilde K_q(b)}}
                         {|\widetilde K_q(b)|},
 \qquad M\asymp L.
\tag{179.H29}
\]

This uses (O(L)) atoms per bucket and (O(Lq)=O(Lu_0)) in total, so it
respects the bucket-count shadow (179.H23).  Equations (179.H26)--(179.H28)
then give

\[
 \left|\frac q{u_0}\sum_b\widetilde K_q(b)B^+_{q,b}\right|
 \asymp Lq.
\tag{179.H30}
\]

These arrays do not preserve the literal (\lambda)-field, phases,
squarefree masks, endpoints, or selectors.  Equation (179.H30) is
therefore a counterexample only to a coefficient-uniform deduction from
parity and bucket sizes; it is not literal K17a lower mass.

A single square-root saving applied to (179.H25) restores only

\[
 L\sqrt qX^\varepsilon
\tag{179.H31}
\]

(or (L\sqrt q\log(2q)X^\varepsilon) if one starts from the unprojected
alias (\ell^1) ledger).  Neither is (O(LX^\varepsilon)) uniformly for
power-size (q).

### 3.7 The fixed-modulus orientation reflection fails

For fixed (u,v,n), define the two Diophantine lattices

\[
 \mathscr P=\{(s,w):sv-wu=n\},\qquad
 \mathscr M=\{(s,w):uw-sv=n\}.
\tag{179.H32}
\]

The map

\[
 I(s,w)=(u-s,v-w)
\tag{179.H33}
\]

is an exact involution from (\mathscr P) to (\mathscr M).  It keeps
(u,v,n,g,u_0,q), and the bucket (b=\bar v n_0\pmod q) fixed.  If
((s_t,w_t)=(s_0+ut,w_0+vt)) is the plus parametrization, then the minus
canonical data satisfy

\[
 s_0^-=u-s_0,\qquad w_0^-=v-w_0,
 \qquad I(s_t,w_t)=(s^-_{-t},w^-_{-t}).
\tag{179.H34}
\]

This algebraic involution is not a literal-domain involution.  The plus
domain requires (s,w\ge1), whereas its image is live only if

\[
 1\le s\le u-1,\qquad1\le w\le v-1.
\tag{179.H35}
\]

Because a fibre advances by ((u,v)), at most one site of a row can lie
in (179.H35); the remaining positive tail, when present, maps outside the
opposite displacement domain.  Thus orientation-domain bijectivity fails
before any cancellation argument.

Even on (179.H35), endpoints do not pair.  Put

\[
 x=\kappa u(\kappa v+2w),\qquad r=2\kappa n,
 \qquad C=2\kappa^2uv+2\kappa uv.
\tag{179.H36}
\]

The plus endpoint pair is ((x,x+r)), while the reflected minus pair is

\[
 (C-x-r,C-x).
\tag{179.H37}
\]

Accordingly

\[
 \Psi^+ =J(\sqrt{x+r}-\sqrt x),\qquad
 \Psi^-\!\circ I
 =J(\sqrt{C-x}-\sqrt{C-x-r}),
\tag{179.H38}
\]

which are neither equal nor negatives in general.  Equality would require
the exceptional midpoint relation (2x+r=C), and even there the literal
coefficients are evaluated at different products and different divisors.
The selected/no-pair mask, squarefree support, profiles, hard endpoints,
and zero extensions have no reflection law about (C/2).  Hence
(A_z^+) is not equal to, or the conjugate of, the reflected (A_z^-).

### 3.8 The endpoint-preserving exchange fails by complementary support

The other exact algebraic map is

\[
 J:(u,v,s,w,+)\longmapsto(v,u,w,s,-).
\tag{179.H39}
\]

It preserves (n), the ordered endpoint products, and the square-root
phase.  But it changes the outer row (u), the gcd stratum, the primitive
modulus (u_0=u/(u,n)), and generally the conductor and bucket.  It is
therefore not an involution inside a fixed
((\kappa,u,u_0,q,b)) defect block.

More decisively, at the lower product

\[
 x=(\kappa u)(\kappa v+2w)
\]

the plus atom uses the divisor (\kappa u), while the exchanged minus
atom uses its complement (\kappa v+2w).  At the upper product

\[
 x+r=(\kappa u+2s)(\kappa v)
\]

the plus atom uses (\kappa u+2s), while the exchanged minus atom uses
its complement (\kappa v).  In the odd branch, a live selected divisor
lies in the upper near-square window.  Since the endpoint is squarefree
and greater than one, its complementary factor is strictly below the
square root and is in the zero extension.  In the even branch, the
complement is even and is not an allowed character-bearing divisor.

Thus (179.H39) sends every live complementary-divisor candidate to a
nonlive term.  Its shared live selector sector is empty in the literal
range.  The endpoint-preserving map supplies no orientation equality,
and the fixed-modulus map (179.H33) supplies no endpoint or selector
equality.  No nontrivial strict orientation-stable defect sector follows.

### 3.9 Outer absolute value and restored-power boundary

After the exact algebraic split, the high-conductor local block satisfies

\[
\begin{aligned}
 \left|\sum_{u_0\mid u}\sum_{q\mid u_0\atop q>Q_B}
       \mathcal C_{u_0,q}\right|
 &\le
 \left|\sum_{u_0\mid u}\sum_{q\mid u_0\atop q>Q_B}
 \frac q{u_0}\sum_b\widetilde K_q(b)
       (B^+_{q,b}-B^-_{q,b})\right|\\
 &\quad+
 \sum_{u_0\mid u}\sum_{q\mid u_0\atop q>Q_B}
 \left|\frac{\mu(q)}{u_0}
       \sum_b(B^+_{q,b}+B^-_{q,b})\right|.
\end{aligned}
\tag{179.H40}
\]

Only the target-safe trace is separated by triangle inequality.  The
defect retains one outer absolute value after all high conductors,
divisor strata, buckets, and both orientations are recombined.  Taking
absolute values inside that first term returns (179.H25) and cannot prove
(177.K34).  Before taking any absolute value, (179.H18i) identifies this
complete high centered defect exactly with the original literal block
minus its low centered conductor packet.

## 4. First doubtful or unproved step

After the exact trace (179.H19)--(179.H20) is removed, the first unproved
statement is precisely

\[
 \boxed{
 \left|\sum_{u_0\mid u}\sum_{q\mid u_0\atop q>Q_B}
 \frac q{u_0}\sum_{b\in U(q)}\widetilde K_q(b)
 \bigl(B^+_{q,b}-B^-_{q,b}\bigr)\right|
 \ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.}
\tag{179.H41}
\]

By (179.H18i), this is the original unresolved literal orientation block
minus an already-safe low-conductor centered packet.  The all-conductor
identity therefore supplies an exact self-return, not an estimate.
Parity proves only the scalar relation between (K_q(b)) and
(K_q(-b)); it proves no relation between (B^+_{q,b}) and
(B^-_{q,b}).  The first invalid affirmative step would be to assert
that these two buckets are equal, conjugate, paired by (t\mapsto-t),
or paired by complementary-divisor exchange.  Sections 3.7--3.8 locate
the exact failures: displacement-domain leakage for the fixed-modulus
map, endpoint/selector mismatch on its overlap, and zero-extension failure
for the endpoint-preserving complementary map.

A valid continuation must instead prove a new literal selector-, phase-,
endpoint-, and lift-aware signed theorem that gains the full conductor
factor, two coupled square roots, or an equivalent cancellation across
the still jointly retained (u_0,q,b), gcd, lift, fibre, and orientation
labels.  No such theorem occurs in the authorized context.  The actual
coefficients might have additional cancellation, so (179.H41) and
(177.K34) remain open rather than rejected.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| (d=1) primitive trace | **PASS.** The (d=1) projector term is exactly (\mu(q)/q); the asymmetric split gives (2\mu(q)/u_0), while centering gives the symmetric trace (\mu(q)(B^++B^-)/u_0). |
| all-conductor centered identity | **PASS / exact self-return.** For (u_0>1), Möbius inversion gives (\sum_{q\mid u_0}(q/u_0)\widetilde K_q(b)=E_{u_0}(b)).  The high centered defect is the original literal block minus the low centered packet. |
| (q=1) normalization | **PASS.** (K_1(0)=1) and (\widetilde K_1(0)=0).  The centered identity is not asserted at (u_0=1), whose entire block is low conductor; for (u_0>1), the (q=1) trace is essential to trace cancellation. |
| all-conductor trace cancellation | **PASS.** (\sum_{q\mid u_0}\mu(q)=0) for (u_0>1), and the unphased bucket total is independent of (q).  Hence high trace equals minus low trace. |
| squarefree versus nonsquarefree (q) | **PASS.** The trace is present only for squarefree (q).  For (q=p^2) it vanishes, but (K_{p^2}) still has unit size and the defect has full (Lq) capacity. |
| (b\in U(q)) | **PASS.** It follows from ((v,u)=1), (q\mid u_0\mid u), and ((n_0,u_0)=1).  The sign law is never applied to a nonunit bucket. |
| exact (q/u_0) coefficient | **PASS.** It appears once in (179.H17); the trace is consequently (2\mu(q)/u_0), not (2\mu(q)/q) or (2\mu(q)q/u_0). |
| atom and divisor multiplicities | **PASS.** A fixed stratum has (O(u_0L)) atoms.  Trace summation costs (\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|\ll X^\varepsilon). |
| orientation-domain bijectivity | **FAIL for the proposed route.** The fixed-modulus reflection is live only on (179.H35), at most one site per fibre; it is not a bijection of the complete positive domain. |
| complementary-divisor support | **FAIL for the proposed route.** The endpoint-preserving exchange maps a live selected divisor below the upper near-square window in the odd branch or to an even complement in the even branch. |
| selector and endpoint matching | **FAIL for the proposed route.** The fixed-modulus reflection sends ((x,x+r)) to ((C-x-r,C-x)); no phase, selector, squarefree, profile, or hard-endpoint conjugacy follows. |
| physical lift multiplicity | **PASS.** A residue pair carries (O(\kappa gh^2)=O(Lh/q)) lifts, and a product bucket carries (O(Lu_0/q)); summing buckets restores (O(Lu_0)). |
| defect positive capacity | **PASS as an upper/countermodel ledger only.** The centered projector gives (O(LqX^\varepsilon)), and prime/prime-square artificial buckets attain (\asymp Lq).  This is not actual lower mass. |
| one-square-root restoration | **PASS obstruction.** One square root leaves (L\sqrt qX^\varepsilon) (or (L\sqrt q\log qX^\varepsilon) before the parity reorganization), above target for power-size (q). |
| adversarial buckets versus actual coefficients | **PASS quarantine.** (179.H29) respects unit and count shadows but discards the literal coefficient field.  It rejects coefficient-uniform algebra only; actual signed cancellation remains open. |
| low-(q) exclusion | **PASS.** Every displayed block and trace sum retains (q>Q_B); (q=1) is not reintroduced. |
| outer absolute-value placement | **PASS.** Only the safe trace is peeled off.  The complete defect in (179.H41) keeps one final outer absolute value. |
| owner scope | **PASS.** The result concerns only the high-conductor primitive-orientation route inside residual K17a.  It proves no other hard-TOP channel or parent. |
| exponent quarantine | **PASS.** No parent, bridge, quarter theorem, internal exponent, external benchmark, or target exponent is changed. |

No numerical experiment, web search, or external theorem was used.  The
audit is entirely finite algebra, literal-domain analysis, and power
bookkeeping.

## 6. Dependencies and exact artifacts used

The project instructions and task brief were read, followed by exactly the
authorized context:

1. `AGENTS.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/briefs/hostile_orientation_defect_capacity_audit.md`;
3. `protocol.md`;
4. `state/proof_obligations.yml`;
5. `state/active_campaign.yml`;
6. `strategy/round179_m2_hard_top_t1_residual_k17a_primitive_conductor_orientation_defect_strategy.md`;
7. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`;
8. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md`;
9. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reports/hybrid_large_sieve_capacity_audit.md`; and
10. `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`.

No unlisted research artifact was used.  No shared state, proof draft,
kernel, strategy, validation artifact, synthesis, control, review, or
sibling report was edited.

## 7. Recommended state effect

**Retain** the accepted primitive alias-conductor reduction and, after the
required independent seam review, **promote** the finite projector
(179.H1), exact decomposition (179.H2), centered all-conductor identity
(179.H2b), self-return (179.H2c)--(179.H2e), and target-safe primitive
trace (179.H19)--(179.H20).

**Record** the route-scoped exit
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go` for:

- parity without a literal relation between the two orientation buckets;
- centered exact-conductor summation, which reconstructs the original
  literal orientation block and makes the high defect exactly the original
  block minus the safe low packet;
- the fixed-modulus reflection, which fails domain and endpoint/selector
  preservation;
- the endpoint-preserving complementary-divisor exchange, which fails
  literal support;
- coefficient-uniform positive or norm contraction of the defect; and
- one reciprocal square-root saving after all physical lifts are restored.

**Do not promote** the prime or prime-square bucket controls to literal
lower mass, and do not reject (177.K34).  Leave the complete high-(q)
defect (179.H41), complete K17a, the residual scalar, every other hard-TOP
channel, complete hard TOP, BAL, UNBAL, M9--M2, both M1 routes or GAR,
endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent owner unchanged and open at their inherited status.
