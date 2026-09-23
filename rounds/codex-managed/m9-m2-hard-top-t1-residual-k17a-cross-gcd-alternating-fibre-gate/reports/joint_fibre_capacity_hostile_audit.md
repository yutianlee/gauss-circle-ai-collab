# Round 176 hostile audit: joint cross-gcd fibre capacity

## 1. Result

The cross-gcd coordinate and its character law are exact, but the literal
half-frequency does not by itself supply the missing factor (L).  The
narrowest justified terminal verdict is

\[
 \boxed{\texttt{k17a\_cross\_gcd\_alternating\_fibre\_capacity\_or\_self\_return\_no\_go}.}
\tag{176.H1}
\]

This is a route-scoped no-go for the following mechanisms: internal
alternation followed by a positive sum over fibres; rowwise Abel or
Kusmin--Landau without a new modulo-one separation lemma; rowwise
second-derivative, exponent-pair, (B)-process, or Poisson bounds followed
by absolute values of the dual modes; and a full two-variable Poisson or
stationary-phase transform followed by absolute values of its dual modes.
It is not a lower bound for the literal residual aggregate and does not
exclude a signed joint dual theorem.

There are four exact conclusions.

1. In either opposing orientation, write \(r=\kappa h\), where
   \(\kappa\) is the cross gcd.  Then \(\kappa\) is odd, (h) is even, and
   \(r<R_0\) forces
   \[
     \kappa<R_0/2.
   \tag{176.H2}
   \]
   Every parity-compatible fibre is multiplicity one, has
   \(T\ll1+\kappa\) literal geometric sites, and has exact character
   \(\sigma_0(-1)^t\).

2. On the nonzero squarefree support the original divisor gcd is constant
   on a cross-gcd fibre.  If (h=2c), then in both orientations
   \[
      (d,d')=(u,c)=(u,h/2).
   \tag{176.H3}
   \]
   Thus the original cutoff \((d,d')<\gamma L\) is distinct from
   \(\kappa\), but it does **not** erase the half-frequency by varying with
   (t).  It is not an obstruction.

3. With \(T\asymp\kappa\) on a full relative interior fibre, set
   \[
      A_h={Jh\over L},\qquad F=A_hT\asymp {Jh\kappa\over L}.
   \tag{176.H4}
   \]
   The phase has \(\Phi''\asymp F/T^2\), and the hypotheses imply
   \(F/T^2\gg1\).  A rowwise (B)-process has
   (1+A_h) stationary dual integers, one saddle has size
   \((T/A_h)^{1/2}\), and positive recombination returns
   \[
      \sqrt F+{T\over\sqrt F}>T.
   \tag{176.H5}
   \]
   Taking the minimum with the trivial estimate therefore returns (T).
   The factor ((-1)^t) merely translates the stationary lattice from
   integers to half-integers and changes its cardinality by at most (O(1)).

4. The canonical-solution sawtooth is removable at logarithmic, not power,
   cost.  For odd (u), its exact discrete Fourier algebra norm is
   \(O(\log(2u))\).  After this expansion the open family contains coupled
   inverse-residue phases, the square-root phase, squarefree and residual
   selectors, and hard endpoints.  A positive treatment has (L^3)
   capacity; even granting square-root cancellation in one complete
   inverse-residue variable leaves \(L^{5/2}X^\varepsilon\).  Therefore the
   sawtooth itself is not the first obstruction.  The first analytic
   obstruction is the short-fibre/dual-mode self-return; the first open
   affirmative step is a genuinely signed joint estimate for the expanded
   family.

There is one owner-complete strict sector available without oscillation.
For \(1\le K<R_0/2\), the complete literal sector restricted by
\(\kappa\ge K\) satisfies

\[
 \left|\mathfrak C^{\rm rem}_{\kappa\ge K}\right|
 \ll_\varepsilon {L^3\over K}X^\varepsilon.
\tag{176.H6}
\]

Hence \(\kappa\ge\eta L\), for any fixed \(0<\eta<1/2\), is target-safe.
The hoped-for extension down to \(\kappa\ge\sqrt L\) would require an
(O(1)) bound per fibre: ideal alternation would give (L^3/K^2), but the
literal phase transforms above restore the row length and give only
(L^3/K).  At \(K=\sqrt L\) these are respectively (L^2) and
(L^{5/2}).

## 2. Exact statement and hypotheses

Assume exactly the Round-176 range

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\tag{176.H7}
\]

and

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{176.H8}
\]

The audited aggregate retains one real part outside all incidences and is
restricted by

\[
 R_{\log}<r<R_0,\qquad 2\mid r,\qquad
 (d'-d)(m'-m)<0,\qquad (d,d')<\gamma L.
\tag{176.H9}
\]

Every nonzero endpoint atom retains

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}),\qquad
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),
\tag{176.H10}
\]

including the squarefree shell, normalization, canonical neither/both or
no-pair selector, both parity branches, profiles, floors, stars, point
values, hard endpoints, and full-line zero extension.  On support,
\(d,m,d',m'\asymp L\) and the literal amplitude is bounded by
\(X^\varepsilon\).

For the orientation

\[
 d'=d+p>d,\qquad m=m'+q>m',
\tag{176.H11}
\]

write (p=2s), (q=2w), and

\[
 \kappa=(d,m'),\qquad d=\kappa u,\qquad m'=\kappa v,
 \qquad (u,v)=1.
\tag{176.H12}
\]

Then

\[
 r=2\kappa(sv-wu)=\kappa h,\qquad h=2c,\qquad c=sv-wu>0.
\tag{176.H13}
\]

For a chosen solution ((s_0,w_0)), all solutions are exactly

\[
 s=s_0+ut,\qquad w=w_0+vt,
\tag{176.H14}
\]

on the literal finite interval of (t).  The products advance by

\[
 N(t)=N_0+K_\kappa t,\qquad N(t)+r=N_0+r+K_\kappa t,
 \qquad K_\kappa=2\kappa uv.
\tag{176.H15}
\]

The opposite orientation is

\[
 d=d'+2s>d',\qquad m'=m+2w>m,
\tag{176.H16}
\]

with \(\kappa=(d',m)\), \(d'=\kappa u\), \(m=\kappa v\), and

\[
 c=uw-sv>0.
\tag{176.H17}
\]

It has the same solution step \((s,w)\mapsto(s+u,w+v)\), the same product
increment, and the same character law.  No conjugation or deletion of one
orientation is used.

The no-go proved below applies only when one of the named rowwise or joint
transforms is recombined positively.  Signed cancellation among dual
integers, determinants, (u,v), cross gcds, Möbius openings, selectors, or
the two orientations is outside the conclusion.

## 3. Proof or derivation

### 3.1 Multiplicity, parity, character, and the two gcds

The ordered divisor incidence uniquely chooses one of (176.H11) and
(176.H16).  In the first orientation, division of

\[
 (d+2s)m'-d(m'+2w)=r
\]

by \(\kappa=(d,m')\) gives (176.H13).  Since ((u,v)=1), the standard
primitive Diophantine solution gives (176.H14); choosing a different base
solution only translates (t).  Conversely, every admissible (t)
recovers one ordered incidence.  This proves multiplicity one.  The same
argument applied inward from (176.H16) proves the opposite orientation.

Because (d) and (d') are odd, \(\kappa\) and (u) are odd.  Since (r)
is even, (176.H13) forces (h) even.  Thus \(h\ge2\), and
\(\kappa h<R_0\) proves (176.H2).  The parity of (v) is unrestricted and
is precisely the retained odd-complement/even-complement branch.

For (176.H11),

\[
 \chi_4(d')\chi_4(d)=(-1)^s
 =(-1)^{s_0}(-1)^{ut}=\sigma_0(-1)^t,
\tag{176.H18}
\]

because (u) is odd.  Equation (176.H15) follows by substituting
(w=w_0+vt) in the lower product and (s=s_0+ut) in the upper product.
The calculation for (176.H16) is identical.

It remains essential not to confuse \(\kappa\) with
\(g=(d,d')\).  On a nonzero atom, the upper product in (176.H11) is
squarefree.  Hence ((d',m')=1).  Since \(\kappa\mid m'\) and
\(d'=\kappa u+2s\),

\[
 (\kappa,s)=1.
\tag{176.H19}
\]

Therefore, using that \(\kappa u\) is odd,

\[
 g=(\kappa u,\kappa u+2s)=(\kappa u,s)=(u,s).
\tag{176.H20}
\]

Reducing (sv-wu=c) modulo (u), and using ((u,v)=1), gives

\[
 (u,s)=(u,c).
\tag{176.H21}
\]

In (176.H16), squarefreeness of the lower product gives
\((\kappa,s)=1\), and (uw-sv=c) gives the same conclusion.  This proves
(176.H3) in both orientations.  The low-(g) selector is thus constant on
each fibre and is not a source of (t)-variation.

The physical ranges for \(d,d',m,m'\) have width (O(L)), whereas one
step in (176.H14) changes (d') and (m), or the mirrored pair, by
\(2u,2v\asymp L/\kappa\).  Hence the literal interval has

\[
 T\ll1+\kappa.
\tag{176.H22}
\]

For fixed \(\kappa\), there are \(O(L/\kappa)\) choices for each of
(u,v,h), and a full row has \(O(\kappa)\) sites.  Consequently

\[
 \sum_{\kappa\ge K}
 O\!\left((L/\kappa)^3\kappa\right)
 \ll {L^3\over K},
\tag{176.H23}
\]

which proves (176.H6), for both orientations and with all literal
restrictions restored by deletion.  If a uniform (O(1)) alternating
bound per row were available, the corresponding capacity would instead be

\[
 \sum_{\kappa\ge K}O((L/\kappa)^3)
 \ll {L^3\over K^2}.
\tag{176.H24}
\]

Equations (176.H23)--(176.H24) give the exact
\(K=\sqrt L\) comparison stated in Section 1.  The sector
\(\kappa\ge\eta L\) is nonempty only below the forced ceiling (R_0/2),
but (176.H23) is target-sized there.

### 3.2 Exact phase ledger and rowwise self-return

Absorb (176.H18) into the phase.  With \(x=N_0+K_\kappa t\),

\[
 \Phi(t)=J\{\sqrt{x+\kappa h}-\sqrt x\}+{t\over2}.
\tag{176.H25}
\]

Direct differentiation gives

\[
\begin{aligned}
 \Phi'(t)&={JK_\kappa\over2}
 \{(x+\kappa h)^{-1/2}-x^{-1/2}\}+{1\over2},\\
 \Phi''(t)&={JK_\kappa^2\over4}
 \{x^{-3/2}-(x+\kappa h)^{-3/2}\},\\
 \Phi'''(t)&={3JK_\kappa^3\over8}
 \{(x+\kappa h)^{-5/2}-x^{-5/2}\}.
\end{aligned}
\tag{176.H26}
\]

On a fixed-relative interior fibre,

\[
 |\Phi'-1/2|\asymp {Jh\over L},\qquad
 \Phi''\asymp {Jh\over\kappa L},\qquad
 |\Phi'''|\asymp {Jh\over\kappa^2L}.
\tag{176.H27}
\]

For \(T\asymp\kappa\), this is the standard derivative parameter

\[
 F\asymp {Jh\kappa\over L},\qquad
 |\Phi^{(j)}|\asymp F T^{-j}\quad(j=2,3).
\tag{176.H28}
\]

Moreover

\[
 {F\over T^2}\asymp {Jh\over\kappa L}
 \ge {Jh^2\over L^2}\gg1,
\tag{176.H29}
\]

because \(\kappa h<L+O(1)\), \(h\ge2\), and (L^2=o(J)).

The exact Poisson formula for a smooth row is

\[
 \sum_t A(t)e(\Phi(t))
 =\sum_{n\in\mathbb Z}\int A(x)e(\Phi(x)-nx)\,dx.
\tag{176.H30}
\]

Its stationary equation is

\[
 J{K_\kappa\over2}
 \{(x+\kappa h)^{-1/2}-x^{-1/2}\}=n-{1\over2}.
\tag{176.H31}
\]

Thus the character translates the dual lattice to
\(\mathbb Z+1/2\); it does not reduce its density.  The derivative image
has length

\[
 \Phi''T\asymp {Jh\over L}=A_h,
\tag{176.H32}
\]

so there are (O(1+A_h)) central dual integers.  One stationary integral
has scale

\[
 (\Phi'')^{-1/2}\asymp\left({\kappa L\over Jh}\right)^{1/2}
 ={T\over\sqrt F}.
\tag{176.H33}
\]

Taking absolute values of the central modes restores

\[
 (1+A_h){T\over\sqrt F}
 \asymp \sqrt F+{T\over\sqrt F}.
\tag{176.H34}
\]

By (176.H29), the first term exceeds (T), so the trivial estimate wins.
The classical second-derivative inequality gives the same expression.
Kusmin--Landau would require a new lower bound for the distance of
\(\Phi'\) or the discrete first difference to \(\mathbb Z\).  The exact
hypotheses provide none: the (1/2) only moves the resonant lattice, and
the derivative interval crosses (O(1+A_h)) lattice levels.

Abel summation does not recover the pure alternating bound.  Even for
constant amplitude it gives

\[
 \left|\sum_t(-1)^t e(\Psi(t))\right|
 \ll1+\sum_t|e(\Psi(t+1))-e(\Psi(t))|\ll T,
\tag{176.H35}
\]

and no smaller variation estimate follows from (176.H27).  The literal
squarefree and selector fields only add unpriced variation.

For an exponent pair \((\alpha,\beta)\) in the usual convention
\(|f^{(j)}|\asymp FT^{-j}\), the restored row expression is

\[
 (F/T)^\alpha T^\beta
 =\left({Jh\over L}\right)^\alpha\kappa^\beta.
\tag{176.H36}
\]

Summing this positively over (u,v,h) and \(\kappa\ge K\) gives the
formal capacity

\[
 J^\alpha L^3
 \sum_{\kappa\ge K}\kappa^{\beta-\alpha-3}
 \ll J^\alpha L^3K^{\beta-\alpha-2}.
\tag{176.H37}
\]

Every nontrivial classical placement with \(\alpha>0\) retains a positive
power of (J); at \(K=\sqrt L\), (176.H37) is

\[
 J^\alpha L^{2+(\beta-\alpha)/2},
\tag{176.H38}
\]

while the trivial tail is (L^{5/2}).  Since \(J/L^2\to\infty\), neither
restored certificate is \(L^2X^\varepsilon\) uniformly in the assigned
range.  This does not rule out a new exponent-pair-like theorem with
additional arithmetic cancellation; it records the power returned by the
ordinary one-row interface.

### 3.3 Squarefree progressions, selector fields, and endpoints

The squarefree openings do not algebraically change the half-frequency to
a constant.  If (v) is odd, every product on the geometric row is odd.
If (v) is even, literal squarefreeness gives \(\nu_2(v)=1\), and
\(K_\kappa=2\kappa uv\) is divisible by (4); both endpoint products stay
congruent to \(2\pmod4\).  Thus every square-divisor opening that can occur
is odd.

For an odd square (a^2), a solvable condition
\(a^2\mid N_0+K_\kappa t\) selects one class modulo

\[
 q_a={a^2\over(a^2,K_\kappa)},
\tag{176.H39}
\]

and (q_a) is odd.  Intersections of the two endpoint openings still have
odd step (q), so

\[
 (-1)^{t_0+qj}=(-1)^{t_0}(-1)^j.
\tag{176.H40}
\]

Hence an individual odd Möbius progression preserves the half-frequency.
However, positive recombination over all nonempty openings has up to
\(T X^\varepsilon\) incidence capacity (count pairs ((t,a)) first), so
singleton and short progressions restore the row length.  Cancellation of
the Möbius signs across openings remains an unexcluded route.

The low-(g) cutoff is constant by (176.H3).  In contrast, no bounded-
variation, periodicity, or transform-norm estimate is available in the
authorized artifacts for the canonical residual selector
\(\rho_N(d)\), its selected/no-pair transitions, or all floor, star,
profile, and hard endpoint fields in (A_N(d)).  Treating those fields as
smooth would be an unproved step.  Zero extension is exact but turns every
birth or death into a boundary contribution; charging such contributions
positively over the \(O(L^3/\kappa^3)\) fibres provides no missing power.

This amplitude failure is not needed for the analytic no-go: the
rowwise ledger (176.H30)--(176.H35) already self-returns for constant
amplitude with the actual square-root phase.  Conversely, the absence of
an amplitude theorem is not evidence of physical lower mass.

### 3.4 Canonical sawtooth: exact Fourier removal and remaining family

Choose the canonical solution \(s_0(c)\in\{0,\ldots,u-1\}\).  Then

\[
 s_0(c)=[\bar v c]_u,
\tag{176.H41}
\]

where \(\bar v\) is the inverse of \(v\pmod u\).  Define on
\(\mathbb Z/u\mathbb Z\)

\[
 E_u(a)=(-1)^{[a]_u}.
\tag{176.H42}
\]

For odd (u), its exact discrete Fourier transform is

\[
 \widehat E_u(k)
 =\sum_{a=0}^{u-1}(-1)^a e(-ka/u)
 ={2\over1+e(-k/u)}.
\tag{176.H43}
\]

Indeed this is a finite geometric series and
((-e(-k/u))^u=-1).  Moreover

\[
 {1\over u}\sum_{k\bmod u}|\widehat E_u(k)|
 ={1\over u}\sum_{k\bmod u}{1\over|\cos(\pi k/u)|}
 \ll\log(2u).
\tag{176.H44}
\]

Therefore

\[
 (-1)^{s_0(c)}
 ={1\over u}\sum_{k\bmod u}\widehat E_u(k)
 e(k\bar v c/u)
\tag{176.H45}
\]

at only logarithmic Fourier-algebra cost.  Canonical jumps cannot be
claimed as a power obstruction.

The exact family produced by (176.H45), schematically and with every
literal field retained in \(\mathcal A\), is

\[
 \sum_{\kappa,u}\sum_{k\bmod u}{\widehat E_u(k)\over u}
 \sum_{\substack{v,c,t\\(u,v)=1\\
 R_{\log}<2\kappa c<R_0\\(u,c)<\gamma L}}
 \mathcal A_{\kappa,u,v,c}(t)
 e\!\left(\Psi_{\kappa,u,v,c}(t)+{t\over2}
            +{k\bar v c\over u}\right).
\tag{176.H46}
\]

This is an inverse-residue/square-root/selector family, not a completed
Kloosterman sum.  The weights depend jointly on \(v,c,t\), and completing
the inverse phase alone can produce a Ramanujan zero mode as large as its
gcd.  Even if one grants the optimistic bound
\(O((L/\kappa)^{1/2}X^\varepsilon)\) for every \(v\)-sum, the remaining
counts give

\[
 \sum_\kappa
 \underbrace{(L/\kappa)}_{u}
 \underbrace{(L/\kappa)}_{c}
 \underbrace{\kappa}_{t}
 \underbrace{(L/\kappa)^{1/2}}_{v\text{ saving}}
 \ll L^{5/2}.
\tag{176.H47}
\]

The logarithmic norm (176.H44) is absorbed in \(X^\varepsilon\).  Thus one
pointwise square-root saving, even before selector and endpoint costs, is
still a factor (L^{1/2}) above target.  A second signed family saving is
required.

There is also an exact geometric control showing that the base sign need
not alternate with the determinant.  Let \(\kappa=1\), let (u) be odd,
put (v=(u+1)/2), and take (c=n) with \(1\le n<u/2\).  Then

\[
 s_0=2n,\qquad w_0=n,\qquad
 p=4n,\qquad q=2n,\qquad h=2n,
\tag{176.H48}
\]

because (2v-u=1).  Hence (pv-qu=h), while
\(\chi_4(d')\chi_4(d)=(-1)^{s_0}=+1\) throughout this half determinant
range.  Taking (u) prime gives the geometric original gcd
((u,n)=1).  For, say, \(u/16\le n\le u/8\),

\[
 (d,m',d',m)
 =(u,(u+1)/2,u+4n,(u+1)/2+2n)
\tag{176.H49}
\]

lies in fixed relative near-square boxes, has the correct opposing
orientation, \(r=2n\asymp u<R_0\) after a compatible choice of block, and
has a one-point-scale cross-gcd fibre.  This control refutes an automatic
alternation in (h), but it does not assert that both products satisfy the
literal squarefree selector or that the literal profile has positive
density.  Dechirping its square-root phase would also be an adversarial,
not physical, coefficient choice.  It is quarantined accordingly.

### 3.5 Full joint transform and dual-volume restoration

The sawtooth can also be removed without Fourier expansion by returning to
the original lattice variables ((s,w)).  For fixed \(\kappa,u,v\), the
phase in (176.H11), including the character, is

\[
 \Theta(s,w)=
 J\!\left\{
 \sqrt{\kappa v(\kappa u+2s)}
 -\sqrt{\kappa u(\kappa v+2w)}\right\}+{s\over2}.
\tag{176.H50}
\]

Its Hessian is diagonal and, on a fixed-relative interior cell,

\[
 \Theta_{ss}=-{J(\kappa v)^2
 \over\{\kappa v(\kappa u+2s)\}^{3/2}}\asymp-{J\over L},
 \qquad
 \Theta_{ww}={J(\kappa u)^2
 \over\{\kappa u(\kappa v+2w)\}^{3/2}}\asymp {J\over L},
\tag{176.H51}
\]

and

\[
 |\det\operatorname{Hess}\Theta|\asymp {J^2\over L^2}.
\tag{176.H52}
\]

Because ((u,v)=1), there is an integral unimodular change of variables
whose first coordinate is (c=sv-wu).  The continuous strip has
(c)-length \(O(L/\kappa)\), (t)-length \(O(\kappa)\), and hence area
(O(L)), matching its (O(L)) lattice-point capacity.  A two-variable
Poisson transform has gradient-image volume

\[
 O\!\left({J^2\over L^2}\,L\right)=O(J^2/L),
\tag{176.H53}
\]

while one nondegenerate stationary coefficient has scale

\[
 |\det\operatorname{Hess}\Theta|^{-1/2}\asymp {L\over J}.
\tag{176.H54}
\]

Absolute recombination therefore has (O(J)) dual capacity per
\((\kappa,u,v)\), worse than the (O(L)) physical count because
(L^2=o(J)).  Taking the minimum returns (O(L)); summing over
\(u,v,\kappa\) restores

\[
 \sum_\kappa (L/\kappa)^2L\ll L^3.
\tag{176.H55}
\]

The term (s/2) only translates the first dual coordinate by one half and
does not alter (176.H53).  Literal discontinuities make a direct smooth
Poisson theorem harder, not stronger.  Equations (176.H53)--(176.H55)
scope the no-go only to a joint transform whose dual modes are estimated
termwise positively.  A signed estimate among those modes remains open.

## 4. First doubtful or unproved step

There is no doubtful step in the two orientations, multiplicity-one
coordinate, the restrictions \(\kappa\) odd, \(h\) even and
\(\kappa<R_0/2\), the half-frequency, the product increment, the constant
original-gcd identity (176.H3), the derivative ledger, the DFT identity,
or the restored positive capacities.

The first unproved affirmative step is a literal signed estimate for
(176.H46), or an equivalent signed dual form, that saves one full factor
(L) **before** taking absolute values over (t)-dual modes,
determinants, (u,v), cross gcds, Möbius openings, selector classes, or
endpoints.  Such an estimate must simultaneously:

1. exploit cancellation beyond the half-lattice translation, especially
   on the \(\kappa=O(1)\) one-point fibres;
2. control the inverse-residue and square-root phases jointly in at least
   two long labels, since one optimistic square-root saving leaves
   (176.H47);
3. retain signed Möbius recombination and prove an actual norm or
   correlation estimate for the selected/no-pair field; and
4. price hard births, deaths, floors, stars, and both parity branches.

No exact sign-reversing involution or signed dual theorem with those
properties appears in the authorized context.  This leaves open a bespoke
joint large-sieve, spectral, delta, bilinear Kloosterman, or signed Poisson
theorem for the actual coefficient.  It also leaves open cancellation
between the two opposing orientations.  The report does not generalize
beyond the positively recombined mechanisms explicitly audited.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_residual_coefficient` | **GREEN quarantine.** The literal coefficient is retained in \(\mathcal A\) in (176.H46).  No bounded-variation or density property is invented. |
| `nonpolylog_shift_complement` | **GREEN.** The exact range is \(R_{\log}<2\kappa c<R_0\); the accepted polylogarithmic sector is removed once. |
| `both_opposing_orientations` | **GREEN.** Equations (176.H11)--(176.H17) derive both orientations separately with inward anchors. |
| `cross_gcd_multiplicity` | **GREEN.** The primitive equation and the step ((u,v)) give every parity-compatible incidence once. |
| `cross_gcd_vs_original_gcd` | **GREEN repair.** On literal squarefree support, \(\kappa\) is distinct from \(g=(u,h/2)\); \(g\) is constant along the fibre and is not blamed for variation. |
| `parity_and_two_adic_branches` | **GREEN.** \(\kappa,u\) are odd, (h) is even, \(\kappa<R_0/2\), and both odd and even (v) branches are retained.  The even branch stays \(2\pmod4\). |
| `half_frequency_character_law` | **GREEN.** The exact law is (176.H18), and Poisson shifts the dual lattice by (1/2) as in (176.H31). |
| `squarefree_Mobius_progressions` | **GREEN route audit.** Every square-divisor progression has odd step and preserves alternation, but positive recombination over singleton progressions restores \(T X^\varepsilon\). |
| `selected_and_no_pair_rows` | **OPEN literal estimate.** Both remain in the amplitude.  No selector smoothness, periodicity, balance, or cancellation is assumed. |
| `short_cross_gcd_fibres` | **GREEN obstruction.** \(\kappa=O(1)\) gives (T=O(1)) and (O(L^3)) row capacity; internal alternation cannot save a factor (L). |
| `high_cross_gcd_sector` | **GREEN strict sector / failed extension.** Raw counting proves (176.H6), hence fixed-proportion \(\kappa\) is safe.  The \(\sqrt L\) extension needs (O(1)) per row, while the phase transform returns (T). |
| `canonical_solution_sawtooth` | **GREEN repair.** The exact DFT (176.H43)--(176.H45) removes the sawtooth at \(O(\log u)\) algebra norm.  It is not promoted as an obstruction. |
| `phase_alias_and_dual_mode_capacity` | **GREEN no-go.** Rowwise capacity is (176.H34); joint capacity is (176.H53)--(176.H55).  Both half-shifts preserve the number of dual modes. |
| `endpoints_and_zero_extension` | **GREEN scope.** They remain literal; positive endpoint charging supplies no saving, and no smoothing theorem is claimed. |
| `constant_amplitude_full_fibre` | **GREEN hostile audit.** Pure alternation would give (176.H24), but Abel with the actual phase gives (176.H35), and (B)-process/Poisson returns the row length. |
| `base_character_determinant_control` | **GREEN quarantine.** The family (176.H48)--(176.H49) has constant base character on a half determinant range, but squarefree/profile density and phase alignment are not asserted. |
| `false_coefficient_controls` | **GREEN quarantine.** Filter erasure, arbitrary dechirping, and positive dual capacities falsify only coefficient-uniform mechanisms; none is physical lower mass. |
| `residual_only_owner_scope` | **GREEN.** The strict sector and no-go concern only the complete nonpolylogarithmic K17a residual aggregate. |
| `no_in_round_pivot` | **GREEN.** No fixed-shift triangle, Grimmelt--Merikoski placement, K26 scale, or product-collar route is substituted. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This report used exactly the assigned brief and these authorized files:

1. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/briefs/joint_fibre_capacity_hostile_audit.md`;
2. `protocol.md`;
3. `state/active_campaign.yml`, at starting graph
   `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`;
4. `strategy/round176_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_strategy.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
6. `proofs/kernels/m9_m2_hard_top_t1_residual_determinant_endpoint_polylog_shift_reduction.md`;
7. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
8. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/short_shift_arithmetic_hostile_audit.md`; and
9. `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/oscillatory_source_power_hostile_audit.md`.

No web source, unlisted repository artifact, or computation was used.  No
shared state, sibling artifact, candidate, review, control, synthesis, or
proof kernel was edited.

## 7. Recommended state effect

**Retain** as exact candidate evidence the multiplicity-one cross-gcd
coordinate in both orientations; the restrictions \(\kappa\) odd, (h)
even, and \(\kappa<R_0/2\); the half-frequency and derivative ledger; the
constant original-gcd formula (g=(u,h/2)); the logarithmic DFT removal of
the canonical sawtooth; and the owner-complete strict bound (176.H6).

**Record a route-scoped no-go** for fibrewise alternating/Abel,
Kusmin--Landau without a new separation lemma, positively recombined
rowwise derivative/exponent-pair/(B)-process/Poisson estimates, positive
Möbius progression recombination, and positively recombined full joint
Poisson.  These routes restore \(L^3X^\varepsilon\) globally (or
\(L^{5/2}X^\varepsilon\) after one optimistic inverse-residue square-root
saving) and do not prove the frozen \(L^2X^\varepsilon\) target.

**Do not promote** the constant-sign base family, raw capacities,
filter-erased arrays, dechirped weights, or dual-mode counts to literal
lower mass.  Do not blame the original gcd cutoff or the canonical
sawtooth: the former is constant on a fibre and the latter has logarithmic
Fourier algebra norm.

Unless a sibling report supplies the signed estimate in Section 4, close
the round under the label in (176.H1).  Leave open the full K17a target and
all broader hard-TOP channels, BAL, UNBAL, M9--M2, M9--M1 or GAR, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent owner.
