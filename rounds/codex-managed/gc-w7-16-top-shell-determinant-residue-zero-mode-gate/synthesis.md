# Round 131 synthesis: exact residue masks, terminal cross-ray residual

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`

Starting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`

## Frozen question

Round 131 tested whether the sole exponent-critical \(B\asymp D\) shell
admits a legal periodic-arithmetic/BV decomposition in the determinant
coordinate \(n=aq-bp\), whether the physical M1/M2 resonance is a shifted
mode rather than a naive zero mode, and whether that structure gives a signed
bank, a physical obstruction, or terminal degeneracy.

## Exact outcome

The terminal label is

\[
\boxed{\texttt{degenerate}}.
\]

There is an exact finite support-mask kernel. Fix one primitive outer ray,
one physical \(p\), and put \(m=a+p\), \(M=|m|_{\rm odd}\). After physical
primitive support is established, the stripped M1 mask

\[
w_{1,m}(q)=\chi_4(b+q)\mathbf1_{(M,b+q)=1}
\]

admits the completion-modulus \(4M\) transform

\[
\widehat w_{1,m}(k)=
{e(kb/(4M))\over4M}G_{4,M}(k)c_M(k).
\]

The fixed mod-four Gauss factor vanishes for even \(k\), has magnitude two
for odd \(k\), and

\[
|\widehat w_{1,m}(M)|=|\widehat w_{1,m}(3M)|
={\varphi(M)\over2M}.
\]

Thus the naive M1 zero mode vanishes, but the two physical quarter modes are
of natural density. The remaining odd Ramanujan modes also survive.

For active odd \(m\), the stripped M2 mask satisfies

\[
\widehat w_{2,m}(k)=
{\epsilon_{\rm sgn}\chi_4(|m|)\over|m|}
e(kb/|m|)c_{|m|}(k),
\]

so its fixed-\(p\), \(q\)-arithmetic zero coefficient is

\[
\epsilon_{\rm sgn}\chi_4(|m|){\varphi(|m|)\over|m|}\ne0.
\]

This Fourier \(k=0\) coefficient is not the determinant point \(n=0\).
The latter remains excluded from the one-sided scalar and is separately
target-safe.

The normalized Fourier \(\ell^1\) cost of both masks is divisor-sized. This
licenses the finite support-mask expansion but gives no cancellation because
the displayed coefficients are natural.

## Period, reassembly, and M2 corrections

The carrier period \(4|a|\) is not the full primitive period. Minimal
fixed-\(p\) \(q\)-periods are

\[
4\operatorname{rad}(|m|_{\rm odd})\quad\text{(M1)},
\qquad
\operatorname{rad}(|m|)\quad\text{(M2)}.
\]

The displayed conductor moduli \(4M\) and \(|m|\) are valid overperiods. In
determinant order they acquire the factor \(|a|\). After a post-reassembly
support divisor expansion, the weakest atom periods are
\(|a|\operatorname{lcm}(4,\rho)\) for M1 and \(|a|\rho\) for M2.

This does not factor the weighted Möbius reassembly. The physical atoms retain
\(\rho\)-dependent profiles, stars, and owners, so the bare incidence identity
\(\sum\mu=\mathbf1_{(m,b')=1}\) does not prove a periodic-mask-times-envelope
identity for the full coefficient. A controlled complete-progression
extension remains open.

For M2, fixed \(p\) has the arithmetic zero coefficient above. After
interlacing active even \(p\), the outer/inner character product is \(e(p/4)\).
If \(b\) is odd and \(q\pmod4\) is fixed, it becomes one determinant quarter
mode. If \(b\) is even, no character modulo \(4|a|\) represents it; a repair
needs an extra two-adic coordinate or period \(2^{v_2(b)+2}|a|\), which is not
a free \(Y^\varepsilon\) cost. There is no universal M2 shifted mode.

## Resonant controls and capacity

The correct one-sided same-denominator controls start at nonzero determinant:

- M1: \(q=0\), \(p=-t\), \(n=bt>0\), integral \(c/b\);
- M2: \(q=0\), \(p=-2j\), \(n=2bj>0\), odd integral \(c/b\).

Their taper mass is \(\asymp R=D/W=Y^{3/48}\) per packet. They refute
character-forced per-ray vanishing but do not prove a family lower bound:
their centres vary with \(b\), and the retained physical amplitudes and outer
coefficients may vanish or cancel.

The exact capacity ladder is

\[
Y^{35/48}\longrightarrow Y^{31/48}
\longrightarrow Y^{30/48}\longrightarrow
Y^{27/48}=Y^{9/16}\longrightarrow Y^{24/48}=Y^{1/2},
\]

corresponding respectively to no residue gain, a formal square-root residue
gain, one aligned length-\(D/W\) packet, one term per ray, and the determinant
target. The \(O(1+WL/D)\) packet cover recovers \(Y^{35/48}\) only as a
worst-case upper capacity, not as proved resonant mass.

Even ideal one-term-per-ray collapse reaches only the persistence threshold
\(Y^{9/16}\). A strict global improvement needs an actual cross-ray power;
the determinant target needs an additional \(Y^{-1/16}\) after that ideal
per-ray collapse.

## Method classification and first residual

The exact complete arithmetic is fixed-modulus-four Gauss\(\times\)Ramanujan,
not a growing quadratic-Gauss or Salié sum. The analytic phase still contains
a real reciprocal, with no complete unit variable paired with its modular
inverse and no controlled completion boundary.

The first open object is the actual signed family scalar

\[
\mathfrak R_i^{\rm res}(c)=
\sum_{r=(a,b)}^{\rm lit}A_i(r)R_{i,r}^{\rm phys}(c),
\]

where each \(R_{i,r}^{\rm phys}\) retains the variable primitive modulus,
lift selector, thresholds, profiles, reciprocal aliases, taper, stars, cells,
and owners. Neither a saving nor a lower bound is proved for this scalar.
Positive energies and coefficient-blind completions remain ineligible
substitutes.

The statement-only diagonal construction is explicitly retracted: it used
\(p=q=n=0\), outside the frozen \(n>0\) target. Its \(4\mid|a|\) M2 subcase
is also inactive because the actual outer M2 numerator is odd.

## Proof status and strategy consequence

The complete critical fixed block remains

\[
|\mathfrak O_i|\ll_\varepsilon Y^{35/48+\varepsilon}.
\]

No global exponent improves: the internally proved exponent remains \(1/3\).
M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, and the
quarter target all remain open.

The internal per-ray graded lane is now terminally parked. In accordance with
`strategy/conductor_0823_full_proof_strategy.md`, the next eligible work is an
exact source-audited cross-ray mechanism map, followed by rotation back to the
M2 UNBAL/BAL/TOP and M1 lower-GAR endpoint conjunction. No theorem name is an
accepted input without an exact source card and parameter map.

No computation or external theorem was used. Round 131 was 100% analytical
and algebraic.

Resulting graph SHA-256:
`328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`.
