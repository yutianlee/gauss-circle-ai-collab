## 1. Result

**Outcome: `displacement_quadratic_no_go`.**

The exact change of variables \(d=y-v\) exposes a genuine rational-quadratic core, and the core by itself has enough formal Gauss-sum capacity to save the required factor \(R\).  The exact correction prevents that completion from being used on the required range.  Uniformly in \(0\leq q\leq 2y\), the prescribed-centre core is a bounded-variation perturbation only in a top displacement collar of width \(O(R)\) (up to fixed profile constants).  That collar already has literal weighted capacity \(O(R^{1+o(1)})\), so completing it proves nothing needed about the remaining \(R^{2+o(1)}\)-capacity owner.  On the complement the correction must be retained.

If one tries to repair the failure by recentering and completing local quadratics, the cubic remainder forces \(R\) displacement blocks on each critical dyadic denominator scale.  Even granting loss-free second-derivative cancellation inside every block, the resulting ledger is \(R^{3/2+o(1)}\), not \(R^{1+o(1)}\).  The missing \(R^{1/2}\) can only come from cancellation between blocks or between \(h\)-fibres.  Such a statement is again a reciprocal/Farey/Hardy-interface theorem, not a consequence of the prescribed-centre displacement quadratic.

Moreover, \(d\leftrightarrow v=y-d\), multiplication by the exact correction, and an exact completion with every dual mode retained are all invertible.  After squaring, \(d_1\ne d_2\) is exactly \(v_1\ne v_2\).  Hence this mechanism gives neither (139.T) nor a strict owner-complete contraction.  This is a no-go for the stated quadratic-completion mechanism; it is not a claim that the literal scalar fails (139.T).

## 2. Exact statement and hypotheses

Let \(X\geq2\), \(R=X^{1/4}\), \(y=\lfloor R^2\rfloor\), \(N=\lfloor R^4\rfloor=y^2+q\), and let

\[
 a_{h,v}:=\frac1h\,V_{\rm low}\!\left(\frac{4R^2h^2}{(y-v)^2}\right),
 \qquad 0\leq v<y,
\]

with the literal smooth support, endpoint values, and zero extension of \(V_{\rm low}\).  The profile is used only through boundedness, smoothness on its fixed support, and the exact support condition

\[
 \frac{4R^2h^2}{(y-v)^2}\in\operatorname{supp}V_{\rm low}.
\tag{2.1}
\]

On any fixed nonzero compact support band \(J=[a,b]\subset(0,\infty)\), (2.1) is exactly enclosed by

\[
 \frac{\sqrt a}{2}\frac{y-v}{R}\leq h\leq
 \frac{\sqrt b}{2}\frac{y-v}{R};
\tag{2.2}
\]

integer endpoints are included only when the literal profile is nonzero there.  If the lower profile also reaches zero, the additional lower \(h\)-bands contribute harmonic logarithms, hence \(R^{o(1)}\), and do not change any power in the ledger below.

The no-go statement concerns any argument which:

- uses the prescribed core (139.B8), or local recenterings of that core, as a quadratic Gauss/Weyl/Poisson completion;
- controls the omitted exact phase only by bounded phase variation or partial summation;
- estimates the resulting displacement blocks independently; and
- introduces no new cross-block, cross-\(h\), centre-average, or original reciprocal-phase cancellation theorem.

Under precisely those hypotheses, the best power made available by the exact correction range and second-derivative completion is \(R^{3/2+o(1)}\).  A full-period completion of the *uncorrected* core can formally reach \(R^{1+o(1)}\), but it is not an estimate for \(\mathcal F_N\).

## 3. Proof or derivation

**Arithmetic, bijection, and parity.**  Since \(y^2\leq X<(y+1)^2\),

\[
 y^2\leq N\leq y^2+2y,
\]

so \(q=N-y^2\) is an integer with \(0\leq q\leq2y\).  The maps

\[
 d\mapsto v=y-d, \qquad v\mapsto d=y-v
\]

are inverse bijections between \(1\leq d\leq y\) and \(0\leq v<y\); in particular, neither endpoint creates a \(d=0\) row.  Even \(d\) vanish.  Put \(r_y\in\{0,1\}\) for the residue \(r_y\equiv y-1\pmod2\).  The surviving lattice is

\[
 v=r_y+2k.
\tag{3.1}
\]

Thus \(v\) is odd when \(y\) is even and even when \(y\) is odd.  On (3.1),

\[
 \chi_4(y-v)=e\!\left(\frac{y-v-1}{4}\right),
\]

with no real-part replacement.  The opposite scalar sign is the stipulated complex conjugate and has identical support and absolute estimates.

**Literal weighted capacity.**  Write \(d\asymp D\) and, on a fixed positive support band, \(h\asymp H:=D/R\).  There are \(O(D)\) denominators, \(O(H)\) \(h\)-values per denominator, and the literal coefficient is \(h^{-1}\asymp H^{-1}\).  Hence

\[
 \sum_{d\asymp D}\sum_h \frac1h
 \left|V_{\rm low}\!\left(\frac{4R^2h^2}{d^2}\right)\right|
 \ll D R^{o(1)}.
\tag{3.2}
\]

Summing the dyadic scales up to \(D\asymp y\asymp R^2\) gives the stated \(R^{2+o(1)}\) capacity.  If \(0\leq v\leq A R\), then \(d\asymp y\), \(h\ll R\), and the harmonic \(h\)-mass per \(v\) is \(R^{o(1)}\).  Therefore

\[
 \sum_{0\leq v\leq AR}\sum_h |a_{h,v}|
 \ll_A R^{1+o(1)}.
\tag{3.3}
\]

This is already the target scale, without using a quadratic sum.

**The exact correction gate.**  Set

\[
 f(v)=\frac{q+v^2}{y-v}=\frac{N}{y-v}-y-v.
\tag{3.4}
\]

Then

\[
 f(v)=\frac qy+\frac{v^2}{y}
 +\frac{v(q+v^2)}{y(y-v)},
 \qquad
 \mathcal E_{h,q,y}(v)=h\frac{v(q+v^2)}{y(y-v)}.
\tag{3.5}
\]

For \(0\leq v\leq y/2\), positivity gives the two-sided comparison

\[
 h\frac{v(q+v^2)}{y^2}
 \leq \mathcal E_{h,q,y}(v)
 \leq 2h\frac{v(q+v^2)}{y^2}.
\tag{3.6}
\]

On a nonzero top support band \(h\asymp R\).  At the two required endpoint centres, (3.6) yields

\[
 q=2y:\quad \mathcal E_{h,2y,y}(v)\gg \frac vR,
 \qquad
 q=0:\quad \mathcal E_{h,0,y}(v)\gg \left(\frac vR\right)^3.
\tag{3.7}
\]

Since \(\mathcal E(0)=0\) and the correction is increasing, these are also lower bounds for its phase variation from \(0\) to \(v\).  Conversely, for \(v\leq AR\), (3.5) gives \(\mathcal E=O_A(1)\), with bounded total variation.  Thus \(v=O(R)\) is the sharp uniform prescribed-centre perturbative scale: the \(q=2y\) linear defect and the fourth-power \(q=0\) cubic defect independently force it.

If \(v=y-d\) is near \(y\), then

\[
 \mathcal E_{h,q,y}(y-d)
 =h\frac{(y-d)(q+(y-d)^2)}{yd}.
\tag{3.8}
\]

On a surviving band \(h\asymp d/R\) with \(d\ll y\), its generic size is \(R^3\), not a perturbation.  Rows below the literal threshold allowed by (2.1) are exactly zero; the first surviving integer row and its endpoint value must not be inferred from a rounded support inequality.

**What local recentering costs.**  Recentring is not the prescribed-centre argument, but granting it gives a useful upper limit on the proposed repair.  On \(d=d_0-u\), \(|u|\leq d_0/2\), the exact reciprocal expansion is

\[
 \frac{hN}{d_0-u}
 =\frac{hN}{d_0}+\frac{hNu}{d_0^2}
 +\frac{hNu^2}{d_0^3}
 +\frac{hNu^3}{d_0^3(d_0-u)}.
\tag{3.9}
\]

For \(d_0\asymp D\), on the critical support band \(h\asymp H=D/R\), the last phase in (3.9) has size

\[
 \asymp \frac{hR^4L^3}{D^4}
 =\left(\frac LH\right)^3
\tag{3.10}
\]

on a block of length \(L\).  Bounded quadratic remainder therefore forces \(L\ll H=D/R\), hence \(D/L\gg R\) blocks on every dyadic \(D\)-scale.

The exact second derivative (the character contributes only a linear phase on the parity lattice) satisfies

\[
 \left|\frac{d^2}{du^2}\frac{hN}{d_0-u}\right|
 \asymp \frac{hR^4}{D^3}=\frac{R}{H^2}.
\tag{3.11}
\]

On a permitted block \(L\asymp H\), the second-derivative estimate, even with no completion, gcd, or boundary loss, gives

\[
 \left|\sum_{u\ {\rm in\ one\ parity\ block}}e(\Psi(u))\right|
 \ll \min\{H,\sqrt R+H/\sqrt R\}
 \ll \min\{H,\sqrt R\}.
\tag{3.12}
\]

There are \(O(H)\) values of \(h\asymp H\), each weighted by \(H^{-1}\), so one block costs \(\min(H,\sqrt R)\).  The \(R\) blocks cost

\[
 R\min(H,\sqrt R).
\tag{3.13}
\]

The complete \(R\)-power ledger at the required denominator endpoints is therefore

| denominator scale | \(H=D/R\) | literal capacity \(D\) | optimistic local-quadratic bound |
|---|---:|---:|---:|
| \(D=X^{1/4}=R\) | \(1\) | \(R\) | \(R\) |
| \(D=X^{3/8}=R^{3/2}\) | \(R^{1/2}\) | \(R^{3/2}\) | \(R^{3/2}\) |
| \(D=X^{1/2}=R^2\) | \(R\) | \(R^2\) | \(R^{3/2}\) |

Dyadic and harmonic losses are \(R^{o(1)}\).  Thus the quadratic mechanism saves at most \(R^{1/2}\) on the top scale and still misses (139.T) by \(R^{1/2}\).  Equivalently, applying the second-derivative estimate directly to the exact reciprocal phase on \(d\asymp D\), \(h\asymp H\leq D/R\), gives

\[
 \min\!\left\{D,
 \frac{R^2\sqrt H}{\sqrt D}
 +\frac{D^{3/2}}{R^2\sqrt H}\right\};
\tag{3.14}
\]

after the literal \(h^{-1}\) summation, its worst allowed band is again \(R^{3/2+o(1)}\).  Formula (3.14) retains the exact rational phase, but it does not supply the missing inter-band cancellation.

**The tempting core completion and its modulus.**  On \(v=r_y+2k\), the prescribed core (139.B8) is

\[
 C_{h,q,y}+\frac{4h}{y}k^2
 +\left(\frac{4hr_y}{y}-\frac12\right)k
 =C_{h,q,y}+\frac{8hk^2+(8hr_y-y)k}{2y}.
\tag{3.15}
\]

Let

\[
 \delta=\gcd(8h,8hr_y-y,2y)=\gcd(8h,y),
\quad Q=\frac{2y}{\delta},
\quad a=\frac{8h}{\delta},
\quad b=\frac{8hr_y-y}{\delta}.
\tag{3.16}
\]

Then \(\gcd(a,b,Q)=1\).  For the complete sum modulo \(Q\), if \(g=\gcd(a,Q)>1\), the sum vanishes because \(g\nmid b\); if \(g=1\), the usual even/odd quadratic Gauss alternatives give magnitude at most \(\sqrt{2Q}\).  This checks both parity cases and every gcd case.  For an incomplete literal interval, Fourier completion changes \(b\) to \(b+m\); the formerly vanishing gcd cases then have nonzero modes \(g\mid b+m\), of size at most \(O(\sqrt{gQ})\), and the cutoff costs the usual logarithmic \(L^1\) factor.  Thus a complete-sum zero cannot be assigned to a truncated support interval.

Ignoring (3.5), a global core completion has square-root size \(y^{1/2}=R\).  The possible gcd loss is harmless after the literal coefficient sum, since

\[
 \sum_{h\ll R}\frac{\sqrt{\gcd(h,y)}}h
 \ll (\log R)\sum_{g\mid y}g^{-1/2}
 \ll_\varepsilon R^\varepsilon.
\tag{3.17}
\]

This explains exactly where the apparently sufficient factor \(R\) comes from.  It also exposes the invalid step: (3.7) forbids using that full-period core for the exact scalar.

**Half-integer aliases.**  For two successive allowed parity points and \(d=y-v\geq3\), the *exact* phase increment is

\[
 \Psi(v+2)-\Psi(v)
 =2h\left(\frac{N}{d(d-2)}-1\right)-\frac12
 =2h\frac{q+2y(v+1)-v(v+2)}{d(d-2)}-\frac12.
\tag{3.18}
\]

The \(-1/2\) is the character alias and may not be dropped.  For \(h\asymp R\) and \(v=O(R)\), its zero-frequency alias is located at

\[
 v+1=\frac{y}{8h}-\frac{q}{2y}+O(1),
\tag{3.19}
\]

up to choosing the nearest allowed parity point.  The full range \(0\leq q\leq2y\) moves this centre by at most one unit; fourth-power centres have \(q=0\).  The increment changes by \(\asymp R^{-1}\) per parity step, so a coherent alias tube contains \(O(R^{1/2})\) points.  For \(O(R)\) top-band \(h\)'s with coefficient \(h^{-1}\asymp R^{-1}\), the union of one such tube per \(h\) has absolute coefficient mass \(O(R^{1/2+o(1)})\); both conjugate signs merely double it.  The enclosing paired carrier collar has the \(O(R^{1+o(1)})\) capacity in (3.3).  Hence aliases do not disprove (139.T), but they do disprove a nonstationary or principal-only completion formula.  All integral aliases of (3.18), not just the displayed one, must be retained in Poisson completion.

**No strict contraction.**  Squaring (139.B5) produces the phase difference \(\Psi_{h_1,q,y}(v_1)-\Psi_{h_2,q,y}(v_2)\).  Because \(d_i=y-v_i\) is a bijection,

\[
 d_1=d_2\iff v_1=v_2,
 \qquad d_1\ne d_2\iff v_1\ne v_2.
\tag{3.20}
\]

Thus diagonal rows, cross-denominator rows, support boundaries, and repeated denominators are preserved exactly.  Multiplication by \(e(\mathcal E)\) is an invertible diagonal operation, and a completion retaining all dual frequencies is an invertible Fourier operation.  Discarding the correction or stationary dual aliases is the only apparent contraction, and (3.7), (3.18), and the incomplete-modulus analysis show that neither discard is licensed.  Retaining them returns to the original reciprocal owner.

## 4. First doubtful or unproved step

The first invalid step in a positive prescribed-centre proof is the assertion that \(e(\mathcal E_{h,q,y}(v))\) is a bounded-variation weight on the full \(v\)-range to which the modulus-\(y\) quadratic completion is applied.  Equations (3.6)--(3.8) refute that assertion: its variation is already \(\gg v/R\) at \(q=2y\), \(\gg(v/R)^3\) at fourth-power centres, and of order \(R^3\) near the lower surviving denominator edge.

After imposing the correct local range, the first genuinely unproved step is a uniform \(R^{1/2}\) cancellation among the \(R\) local blocks (or an equivalent cancellation among \(h\)-fibres), with the exact correction, literal support boundaries, parity, gcd classes, and every stationary alias retained.  No such lemma follows from quadratic completion.  Proving it would be a new reciprocal/Farey/Hardy-interface result and would also require an explicit map to the surviving signed cross-denominator owner.

## 5. Required controls and outcomes

| control | exact input and expected invariant/failure | analytic outcome | implication |
|---|---|---|---|
| \(q\)-range and both directions | \(y^2\leq N<(y+1)^2\); use both \(v=y-d\) and \(d=y-v\) | \(q\in\{0,\ldots,2y\}\), and the endpoint sets are bijective | no row or centre average is hidden |
| odd parity, both \(y\)-parities, both signs | \(v\equiv y-1\pmod2\), exact \(\chi_4\), and the conjugate scalar | \(y\) even gives odd \(v\); \(y\) odd gives even \(v\); (3.15) retains \(-k/2\); the other sign is conjugate | no parity averaging or real-part shortcut is used |
| literal support and endpoints | exact membership (2.1), integer \(h\geq1\), literal endpoint values and zero extension | (2.2) is only an enclosure; rows below the first allowed integer \(h\) vanish, while boundary rows are retained exactly | no rounded cutoff, sharp/smooth substitution, or endpoint crossing is licensed |
| exact correction and extreme centres | (3.5) at \(q=0,2y\), \(v=0\), \(v=O(R)\), and \(v=y-d\) | (3.7) forces the \(O(R)\) top collar; (3.8) is nonperturbative near the lower surviving edge; \(v=0\) has zero correction | global quadratic completion fails uniformly |
| fourth-power centres | \(X=t^4\), so \(R=t\), \(y=t^2\), \(N=t^4\), \(q=0\) | the exact defect is \(hv^3/[y(y-v)]\), giving the same \(v\asymp R\) gate | the worst correction is not caused only by \(q=2y\) |
| half-integer aliases and paired tubes | exact parity increment (3.18), exact aliases versus near aliases | (3.19) persists for every \(q\); coherent width is \(R^{1/2}\); narrow-tube mass is \(R^{1/2+o(1)}\) and enclosing-collar mass is \(R^{1+o(1)}\) | no nonstationary, principal-only, or exact-to-near inference is valid |
| modulus, gcd, and completion boundary | the polynomial (3.15), modulus \(2y\), reduction (3.16), and the literal incomplete interval | complete sums split into \(g=1\) Gauss cases and \(g>1\) zero cases; Fourier boundary modes revive the latter and cost completion loss | a complete Gauss value cannot replace the literal truncated scalar |
| contraction versus return | exact square and the equivalence (3.20) | the coordinate change, correction multiplier, and full Fourier completion are invertible | no strict owner-complete reduction occurs |
| `raw-vs-weighted` | raw \((d,h)\) counts versus \(|V_{\rm low}|/h\) | (3.2), (3.3), and (3.17) use the genuine \(1/h\) mass on every band; no raw exponent is transferred | the power ledger is a weighted ledger |
| `signed-vs-unsigned` | true \(\chi_4\), absolute values, random signs, and adversarial phases of the same magnitude | only the true sign gives the exact \(-1/2\) alias; absolute/adversarial capacity remains \(R^{2+o(1)}\), and random signs supply no theorem | any missing \(R^{1/2}\) cancellation must use a stated literal-sign property |
| `known-lower-bound-families` | UNC, TS, and W-1 must test any absolute near-collision assertion | no absolute near-collision upper bound is asserted here; their family definitions, parity envelopes, and lift data are not present in the three permitted statement-only artifacts | no family-specific compatibility is claimed, and this absence blocks promotion of a positive collision lemma |
| `dyadic-endpoints` | \(D=R,R^{3/2},R^2\) separately | the table following (3.13) gives \(R,R^{3/2},R^{3/2}\) | no estimate silently crosses the \(D=R^2\) endpoint |
| `real-vs-complex-pairing` | literal real character/profile and the stipulated conjugate sign versus complex or asymmetric weights | conjugacy is used only for the stipulated opposite scalar; no \(\operatorname{Re}B_h\) identity is used | the conclusion survives arbitrary phases as a no-go, but no signed positive bound is transferred |
| `exact-vs-near-resonance` | exact integral values of (3.18) versus a width-\(R^{-1/2}\) coherent neighbourhood | exact aliases and near tubes are kept separate; no Fejér or positive energy is invoked | exact resonance energy is not used to control a fat band |
| `coefficient-adversary` | fixed \(\Phi,\chi_4\) structure versus coefficients of equal magnitude | the capacity and correction obstruction survive adversarial phases; the alias location itself uses the literal character | a future saving cannot be claimed for arbitrary coefficients unless separately proved |
| `support-and-degeneracy` | smooth/sharp cutoffs, truncation edges, \(v=0\), any differencing zero shift, repeated denominators, and reduced-modulus boundaries | \(v=0\) is retained; a zero differencing shift would be the diagonal; (3.20) retains repeated denominators; (3.16) retains every reduced modulus; no \(uv=0\) or lift branch is silently created or deleted | the no-go has no hidden degeneracy deletion |

No numerical experiment, centre average, displacement-block substitute scalar, positive separated energy, or desired Gauss-circle estimate was used.

## 6. Dependencies and exact artifacts used

- `problems/gauss_circle.md`.
- `state/control_models.md`.
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md`.

No proof graph, strategy file, nonblind Round 121--139 artifact, sibling report, manifest, brief, external source, or numerical computation was inspected or used.

## 7. Recommended state effect

**Promote the mechanism-specific no-go; reject `target_bound` and `strict_displacement_quadratic_reduction` for this gate.**  The promotable content is the exact \(v=O(R)\) correction gate, the modulus/parity/alias audit, the \(R^{3/2+o(1)}\) optimistic local-completion ledger, and the invertible-return statement (3.20).  Retain (139.B5) as an exact reparametrization only.

This state effect licenses no lower GAR, blockwise M1 parent, M9-M1, M2 parent, endpoint-uniform theorem, M9, quarter theorem, or exponent.  No shared state file is edited.
