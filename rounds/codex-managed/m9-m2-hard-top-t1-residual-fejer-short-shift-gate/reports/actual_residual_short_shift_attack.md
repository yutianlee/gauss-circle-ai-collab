# Round 165 discovery report: exact parity connector and residual short-shift normal form

## 1. Result

The full residual Fejer target is not proved.  Two exact reductions are
proved, and they isolate a smaller sufficient actual-direction theorem.
The terminal label of this report is

\[
 \boxed{\texttt{hard\_top\_t1\_residual\_fejer\_no\_go}.}
\tag{165.D1}
\]

First, the odd shifts can be removed at constant cost *before* any
shiftwise absolute value.  If

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D=\sum_N|c_N^{\rm rem}|^2,
\]

and

\[
 \mathfrak E_R
 =D+2\Re\sum_{1\le r<R}\left(1-\frac rR\right)
       \sum_N z_{N+r}\overline{z_N},
\]

then the even-gap energy

\[
 \mathfrak E_R^{(2)}
 :=D+2\Re\sum_{\substack{1\le r<R\\2\mid r}}
       \left(1-\frac rR\right)
       \sum_Nz_{N+r}\overline{z_N}
\tag{165.D2}
\]

is nonnegative and satisfies the endpoint-exact inequality

\[
 \boxed{\mathfrak E_R\le 2\mathfrak E_R^{(2)}.}
\tag{165.D3}
\]

Consequently the complete residual scalar follows from the strictly
smaller one-sided theorem

\[
 \boxed{
 \Re\sum_{1\le q<R/2}\left(1-\frac{2q}{R}\right)
 \sum_Nc_{N+2q}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+2q}-\sqrt N)\right)
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{165.D4}
\]

This is a genuine scalar connector: it is an inequality between the full
sliding energy and an owner-complete same-parity energy.  It is not a
claim that the accepted XOR scalar has comparable Fejer energy.

Second, the literal divisor opening has a multiplicity-one
complement-gcd normal form.  Put

\[
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),\qquad
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
                  \chi_4(d)\lambda_N(d),
\tag{165.D5}
\]

with every quantity zero off its literal domain.  For a tuple in the
shift-
\(r\) opening, write

\[
 m=Gu,\qquad m'=Gv,\qquad (u,v)=1,\qquad r=Gh.
\tag{165.D6}
\]

Choose one odd solution \((d_*,d'_*)\) of

\[
 vd'-ud=h.
\tag{165.D7}
\]

All odd solutions are then

\[
 d_n=d_*+2vn,\qquad d'_n=d'_*+2un,\qquad n\in\mathbb Z.
\tag{165.D8}
\]

Let \(K=Guv\), \(x_n=Gu d_n=x_0+2Kn\), and
\(\epsilon_{G,h,u,v}=\chi_4(d_*)\chi_4(d'_*)\).  On every nonzero
literal term,

\[
 G\mid r,\qquad v-u\equiv h\pmod2,\qquad
 \chi_4(d_n)\chi_4(d'_n)
 =\epsilon_{G,h,u,v}(-1)^{rn}.
\tag{165.D9}
\]

Thus the complete correlation is exactly

\[
\begin{aligned}
 \mathfrak C_{R,J,L}^{\rm rem}
 ={}&\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_{G\mid r}
 \sum_{\substack{u,v\ge1,(u,v)=1\\v-u\equiv r/G\ (2)}}
 \epsilon_{G,r/G,u,v}\sum_{n\in\mathbb Z}(-1)^{rn}\\
 &\quad\times
 \lambda_{x_n+r}(d'_n)\overline{\lambda_{x_n}(d_n)}
 e\!\left(J(\sqrt{x_n+r}-\sqrt{x_n})\right).
\end{aligned}
\tag{165.D10}
\]

There is no hidden multiplicity in (165.D10).  In particular, the
character is constant along every contributing progression when \(r\) is
even.  When \(r\) is odd it alternates, but the literal squarefree
indicators, two independent selectors, hard values, and square-root phase
remain inside the alternating sum.  Equation (165.D4), the sufficient
same-parity sector, therefore consists entirely of the frozen-character
case of (165.D10).

This proves a route-scoped no-go: triangle inequality, bounded-amplitude
progression counting, character-only Abel summation, or a positive norm
applied separately to these progressions does not prove (165.D4).  The
literal opening has positive capacity

\[
 \ll_\varepsilon L^3X^\varepsilon,
\tag{165.D11}
\]

one factor \(L\) above the Fejer-correlation target.  Through the accepted
sliding inequality this is exactly the missing \(L^{1/2}\) in the scalar.
This is an upper-capacity statement, not a physical lower bound.

## 2. Exact statement and hypotheses

Assume

\[
 J=\sqrt X,\quad y=\lfloor J\rfloor,\quad q_X=X/y^2,\quad
 H=\lfloor yX^{-1/4}\rfloor,\quad
 1\ll L\ll H\le J^{1/2},\quad R=\lceil L\rceil.
\tag{165.D12}
\]

Let \(\mathcal I_L^{\rm lit}\) be the exact inherited half-open product
shell.  For squarefree \(N=2^{\nu_N}M_N\), with \(M_N\) odd, set

\[
 A_N(d)=
 {\bf1}^{\rm lit}_{\{\sqrt N\le d\le2\sqrt N\}}
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\tag{165.D13}
\]

The literal indicator in (165.D13) retains the cone, floors, ceilings,
stars, profile entries and exits, point values, endpoints, and zero
extension.  If the canonical Round-163 pair \(p_N,q_N\) is selected, set

\[
 \rho_N(d)=1-{\bf1}_{p_N\mid d}-{\bf1}_{q_N\mid d}
              +2{\bf1}_{p_N\mid d}{\bf1}_{q_N\mid d};
\tag{165.D14}
\]

if no pair is selected, set \(\rho_N(d)=1\).  Finally put

\[
 \omega_L(N)={\bf1}_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
              \left(\frac{L^2}{N}\right)^{3/4},
 \qquad \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),
\tag{165.D15}
\]

and extend \(\lambda_N(d)\) by zero for every unsupported \((N,d)\).
Then (165.D5) is literal: \(d\) is odd, \(m=N/d\) retains a factor
\(2\) when \(N\) is even, and squarefreeness in \(\omega_L\) enforces
the required coprimality and multiplicity one.

For use below define

\[
 \mathfrak C_{R,J,L}^{\rm rem}
 =\sum_{1\le r<R}\left(1-\frac rR\right)
   \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
   e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\tag{165.D16}
\]

The conclusions proved here are:

1. the parity-window connector (165.D3), hence sufficiency of (165.D4);
2. the literal multiplicity-one expansion (165.D10);
3. the exact tangent and determinant coordinates below;
4. the phase derivative and modulo-one resonance ledger below; and
5. failure of the specified positive and character-only progression
   routes at the restored powers.

No density statement, shifted-convolution source theorem, smooth
replacement of the literal coefficient, or numerical input is assumed.

## 3. Proof or derivation

### 3.1 Endpoint-exact parity-window connector

Extend \(z_N=c_N^{\rm rem}e(J\sqrt N)\) by zero on the full integer line.
For every sliding window put

\[
 Y_s=\sum_{j=0}^{R-1}z_{s+j},\qquad
 Y_s^{(\epsilon)}=
 \sum_{\substack{0\le j<R\\s+j\equiv\epsilon\ (2)}}z_{s+j}
 \quad(\epsilon=0,1).
\tag{165.D17}
\]

Then \(Y_s=Y_s^{(0)}+Y_s^{(1)}\), so

\[
 |Y_s|^2\le2\bigl(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\bigr).
\tag{165.D18}
\]

A pair \((z_N,z_{N+r})\) occurs in the right side of (165.D18) if and
only if \(r\) is even.  When it occurs, it lies in exactly \(R-r\)
windows, exactly as in the full Fejer count.  Therefore

\[
 {1\over R}\sum_s\bigl(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\bigr)
 =\mathfrak E_R^{(2)}.
\tag{165.D19}
\]

The zero extension makes this identity exact at both ends.  Summing
(165.D18), dividing by \(R\), and using the accepted identity
\(R^{-1}\sum_s|Y_s|^2=\mathfrak E_R\) proves (165.D3).
Equivalently, if \(C\) is the real part of (165.D16) and \(C_2\) is the
real part of its even-shift subaggregate, then

\[
 \boxed{C\le \frac12D+2C_2.}
\tag{165.D20}
\]

Since \(D\ll_\varepsilon L^2X^\varepsilon\), (165.D4) implies the
Round-164 correlation target.  No individual odd shift was bounded or
made positive.  For even \(R=2S\), (165.D19) is also the sum of the two
ordinary length-\(S\) Fejer energies of the subsequences \(z_{2n}\) and
\(z_{2n+1}\).  For odd \(R\), (165.D19) itself is the exact positive
definition, so no endpoint rounding is needed.

### 3.2 Literal opening and complement-gcd progression

Opening (165.D16) with (165.D5) gives

\[
\begin{aligned}
 \mathfrak C_{R,J,L}^{\rm rem}
 ={}&\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_{\substack{d,m,d',m'\ge1\\d,d'\ {\rm odd}\\d'm'-dm=r}}
 \chi_4(d')\chi_4(d)\\
 &\quad\times\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\end{aligned}
\tag{165.D21}
\]

All support, squarefree, selector, parity, profile, and endpoint
conditions are in the two zero-extended \(\lambda\)'s.  Conversely, a
nonzero tuple in (165.D21) determines \(N=dm\), \(N+r=d'm'\), and the
two divisor incidences uniquely.  Hence the opening has multiplicity one.

Let \(G=(m,m')\), \(m=Gu\), and \(m'=Gv\).  Then \((u,v)=1\), and
(165.D21) forces

\[
 G(vd'-ud)=r.
\tag{165.D22}
\]

Thus \(G\mid r\), and with \(h=r/G\) the remaining equation is
(165.D7).  Its general integral solution has step \((v,u)\).  The
condition that both \(d,d'\) be odd selects one parity class of that
parameter, giving exactly (165.D8).  Existence of an odd solution is
equivalent to

\[
 v-u\equiv h\pmod2.
\tag{165.D23}
\]

The identity

\[
 \chi_4(a+2k)=(-1)^k\chi_4(a)\qquad(a\ {\rm odd})
\tag{165.D24}
\]

now gives

\[
 \chi_4(d_n)\chi_4(d'_n)
 =\epsilon_{G,h,u,v}(-1)^{(u+v)n}.
\tag{165.D25}
\]

If \(r\) is odd, then \(m,m'\) have opposite parity; hence \(G\) is
odd and \(u,v\) have opposite parity.  If \(r\) is even, then \(m,m'\)
have the same parity.  When both are odd, \(G,u,v\) are odd.  When both
are even, squarefreeness gives exactly one common factor \(2\), and after
division by \(G\), both \(u,v\) are again odd.  In the latter case
(165.D23) also forces \(h\) even.  Therefore

\[
 u+v\equiv r\pmod2
\tag{165.D26}
\]

on every nonzero literal term.  Equations (165.D25)--(165.D26) prove
(165.D9).  Moreover,

\[
 x_n=dm=Gu(d_*+2vn)=x_0+2Guvn,\qquad
 x_n+r=Gv(d'_*+2un).
\tag{165.D27}
\]

Substitution into (165.D21) proves (165.D10), including its multiplicity.

### 3.3 Tangent and determinant coordinates

There is a second exact classification which is useful for checking that
the small product difference does not force small coordinate differences.
Write

\[
 d'=d+a,\qquad m'=m+b.
\]

Since \(d,d'\) are odd, \(a\) is even, and reduction modulo two gives
\(b\equiv r\pmod2\).  The product equation is

\[
 \boxed{bd+am=r-ab.}
\tag{165.D28}
\]

If \(\delta=(a,b)>0\), then \(\delta\mid r\), and after writing
\(a=\delta A\), \(b=\delta B\), \((A,B)=1\), every integral solution
lies on the affine tangent progression

\[
 d=d_0+At,\qquad m=m_0-Bt.
\tag{165.D29}
\]

The cases \(a=0\) or \(b=0\) obey the evident one-variable version;
\(a=b=0\) is impossible because \(r>0\).  The character is fixed on a
whole tangent line:

\[
 \boxed{\chi_4(d')\chi_4(d)=(-1)^{a/2}.}
\tag{165.D30}
\]

For the determinant

\[
 \Delta=dm'-d'm=db-am,
\]

one has exactly

\[
 2db=r-ab+\Delta,\qquad 2am=r-ab-\Delta.
\tag{165.D31}
\]

Thus \(r<L\) permits large \(a,b,\Delta\) through tangent cancellation;
it does not make either factor displacement small.  Along (165.D29), the
base product \(dm\) is quadratic in \(t\), while the literal selectors
and squarefree indicators remain discontinuous.  Taking a modulus on each
tangent line discards both the \((-1)^{a/2}\) interaction between lines
and the complete Fejer real part.

### 3.4 Exact phase and resonance ledger

The complement-gcd coordinate has the advantage that its base product is
linear.  With \(K=Guv\), let a real variable \(t\) interpolate
\(x(t)=x_0+2Kt\), and absorb the exact character alternation into

\[
 \psi(t)=J\bigl(\sqrt{x(t)+r}-\sqrt{x(t)}\bigr)
          +\vartheta_rt,\qquad
 \vartheta_r=\begin{cases}0,&2\mid r,\\[2pt]1/2,&2\nmid r.\end{cases}
\tag{165.D32}
\]

Then

\[
 \psi'(t)=
 -\frac{JKr}{\sqrt{x(t)}\sqrt{x(t)+r}
                  (\sqrt{x(t)}+\sqrt{x(t)+r})}
 +\vartheta_r,
\tag{165.D33}
\]

and

\[
 \boxed{
 \psi''(t)=JK^2\bigl(x(t)^{-3/2}-(x(t)+r)^{-3/2}\bigr)>0.}
\tag{165.D34}
\]

By the mean-value theorem,

\[
 \psi''(t)=\frac32JK^2r\,\xi_t^{-5/2}
 \quad\text{for some }x(t)<\xi_t<x(t)+r.
\tag{165.D35}
\]

On literal support, all four physical factors are \(\asymp L\).  Since
\(G\mid r<R\), this gives

\[
 u,v\asymp L/G,\qquad K\asymp L^2/G,\qquad
 \#\{n:\lambda_{x_n+r}(d'_n)\lambda_{x_n}(d_n)\ne0\}
 \ll G+1,
\tag{165.D36}
\]

and, with \(h=r/G\),

\[
 |\psi'(t)-\vartheta_r|\asymp Jh/L,\qquad
 \psi''(t)\asymp Jh/(GL).
\tag{165.D37}
\]

These are real-derivative sizes, not modulo-one separation.  The exact
one-step increment is

\[
 \psi(n+1)-\psi(n)
 =J\{\Delta_r(x_n+2K)-\Delta_r(x_n)\}+\vartheta_r,
 \qquad \Delta_r(x)=\sqrt{x+r}-\sqrt x.
\tag{165.D38}
\]

Therefore the relevant exceptional sets for a first-difference argument
are

\[
 \left\{n:
 \left\|J\{\Delta_r(x_n+2K)-\Delta_r(x_n)\}
       +\vartheta_r\right\|_{\mathbb R/\mathbb Z}<\eta\right\}.
\tag{165.D39}
\]

For even shifts the resonance is near an integer; for odd shifts it is
near a half-integer before the character is absorbed.  Although
\(\psi'\) is increasing, its real variation can cross many integers.
A large value of (165.D34) does not by itself bound (165.D39) on an
integer lattice.  A phase argument must control these weighted resonant
sets, all integer-crossing transition intervals, and both progression
endpoints.  The hard endpoints and isolated star values occur in
\(\lambda\) and have not been smoothed.

### 3.5 Restored positive ledger and the no-go

Each individual literal divisor amplitude in (165.D15) is bounded, and
the number of product rows is \(O(L^2)\).  Hence

\[
\begin{aligned}
 &\sum_{1\le r<R}\sum_N
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \sum_{\substack{d'\mid N+r\\d'\ {\rm odd}}}
 |\lambda_{N+r}(d')\lambda_N(d)|\\
 &\hspace{35mm}\ll_\varepsilon
 R L^2X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
\tag{165.D40}
\]

The equality of incidence sets between (165.D21) and (165.D10) shows that
the sum of all progression lengths, with divisor powers allowed, has this
same capacity.  Thus taking absolute values by shift, tuple, progression,
selector, parity branch, or squarefree opening yields (165.D40), not the
target \(L^2X^\varepsilon\).

Character-only Abel summation also does not close.  On even shifts the
character in (165.D9) is constant.  On odd shifts it alternates, but the
amplitude being summed is

\[
 \lambda_{x_n+r}(d'_n)\overline{\lambda_{x_n}(d_n)}
 e\!\left(J(\sqrt{x_n+r}-\sqrt{x_n})\right),
\tag{165.D41}
\]

whose squarefree values, row-dependent canonical selectors, two profiles,
hard faces, and phase are not known to have bounded discrete variation.
The trivial variation is proportional to the progression length, so Abel
summation restores (165.D40).  Opening squarefreeness and then taking a
positive norm is precisely an unlicensed loss of the signed aggregate.

The Fejer inequality has prefactor \((M_L+R-1)/R\asymp L\).  If one uses
only the positive capacity \(\mathfrak E_R\ll L^3X^\varepsilon\), it gives

\[
 |\mathcal S_{L,1}^{\rm rem}|^2\ll L^4X^\varepsilon,
 \qquad |\mathcal S_{L,1}^{\rm rem}|\ll L^2X^\varepsilon,
\tag{165.D42}
\]

instead of \(L^{3/2}X^\varepsilon\).  This is the exact restored
\(L^{1/2}\) loss.

The arbitrary-array control survives the parity reduction.  On
\(\asymp L^2\) ambient sites take \(a_N=e(-J\sqrt N)\), so the modulated
sequence is constant.  The two parity pieces of a length-\(R\) window
then each contain \(\asymp R/2\) terms, and (165.D19) has size
\(\asymp L^3\) although \(\sum|a_N|^2\asymp L^2\).  The usual cosine and
sine split gives a real diagnostic with the same capacity.  These arrays
are not (165.D5), so they prove no physical lower bound; they show that
(165.D4) must use the actual residual arithmetic.

Finally, (165.D21) is an additive physical product shift.  It is not the
separate multiplicative character-Poisson collar
\(|s\ell-XQR|\ll QRJ/L\).  Applying that positive collar separately to
the two coefficient legs would destroy (165.D20) and restore its accepted
adverse capacity; the collar obstruction neither proves nor disproves
(165.D4).

## 4. First doubtful or unproved step

All identities through (165.D40), including the parity-window connector,
multiplicity-one divisor opening, complement-gcd and tangent coordinates,
character parity, derivative formulas, endpoint handling, and positive
power ledger, are proved.

The first unproved analytic assertion is (165.D4).  In the normal form
(165.D10), it asks for an aggregate bound over even \(r\), where the
character is frozen on every complement-gcd progression.  A proof must
therefore obtain the missing factor \(L\) in the correlation from at least
one mechanism that is absent from the positive ledger:

- cancellation of \(\chi_4(uv)\)-type signs across primitive complement
  slopes after the bases and selectors are retained;
- a uniform weighted bound for the exact integer/half-integer resonance
  sets (165.D39), including transition and boundary terms; or
- a genuinely signed shifted-divisor or spectral theorem applied to the
  complete aggregate before a positive norm.

No such theorem is proved in the permitted artifacts.  The odd-shift
alternation is not the first missing mechanism because (165.D3) gives a
constant-cost route which discards all odd shifts and leaves only the
frozen-character even sector.

There is also no proved connector from the accepted target-safe XOR scalar
to its sliding Fejer energy.  Expanding the full scalar as XOR plus
residual would create XOR-XOR and two cross energies; the scalar estimate
alone bounds none of them.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `actual_residual_coefficient_domain` | **GREEN.** Equations (165.D13)--(165.D15) retain squarefreeness, the no-pair branch, selected \(00/11\) incidences, normalization, and literal zero extension. |
| `aggregate_one_sided_real_part` | **GREEN reduction, OPEN estimate.** Equations (165.D3), (165.D20), and (165.D4) use one complete real aggregate; no shiftwise modulus is introduced. |
| `additive_product_shift_multiplicity` | **GREEN.** Equation (165.D21) is exactly \(d'm'-dm=r\), and the maps to (165.D10) and back are unique. |
| `gcd_tangent_and_determinant_coordinates` | **GREEN.** Equations (165.D6)--(165.D10) give complement-gcd progressions; (165.D28)--(165.D31) give the affine tangent and determinant identities. |
| `chi4_progression_or_pairing` | **GREEN classification, NO TARGET.** Equation (165.D9) proves frozen character for even shifts and alternation for odd shifts.  The sufficient sector (165.D4) is entirely frozen-character. |
| `square_root_phase_resonance` | **GREEN ledger, OPEN estimate.** Equations (165.D33)--(165.D39) give exact derivatives, scales, integer/half-integer resonances, and transition requirement. |
| `selected_and_no_pair_rows` | **GREEN.** The row-dependent \(\rho_N\) is retained independently on both legs; no selected-pair density or no-pair cancellation is assumed. |
| `odd_divisor_and_even_complement_branch` | **GREEN.** The divisors remain odd.  For even products, the factor \(2\) remains in \(m,m'\); the parity classification after (165.D25) includes the even-even branch. |
| `hard_profile_endpoint_and_zero_extension` | **GREEN.** They remain inside \(\lambda\); (165.D19) is exact at both outer endpoints and no progression boundary is smoothed. |
| `phase_aligned_arbitrary_array` | **GREEN false control.** It has even-gap energy \(\asymp L^3\) at coefficient energy \(\asymp L^2\), so the proposed theorem cannot be coefficient-uniform. |
| Unit-profile four-prime capacity | **GREEN scope.** The accepted family remains a coefficient-uniform positive-capacity diagnostic.  No profile lower bound, phase alignment, adjacent-row density, or physical mass is inferred. |
| `scalar_vs_energy_connector` | **GREEN distinction.** Equation (165.D3) is an actual energy connector.  No energy consequence is drawn from the XOR scalar bound. |
| `rank_one_collar_geometry_separation` | **GREEN.** The additive equation (165.D21) is not the multiplicative dual collar, and no collar estimate is imported. |
| `missing_L_half_power` | **GREEN ledger, OPEN saving.** Equations (165.D40)--(165.D42) restore the factor \(L\) in energy and \(L^{1/2}\) in the scalar. |
| `remaining_few_point_and_downstream_scope` | **GREEN quarantine.** Nothing here treats other few-point channels, hard TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the quarter theorem, or a global exponent. |
| Numerical experimentation | **NOT USED.** The report is entirely algebraic and analytic. |

## 6. Dependencies and exact artifacts used

Only the authorized context was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round165_m2_hard_top_t1_residual_fejer_short_shift_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_short_shift_seed.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reports/complete_residual_transport_attack.md`; and
- the generated Round-165 task brief.

No external source, sibling Round-165 report, computation, or numerical
experiment was used.

## 7. Recommended state effect

**Retain and seam-review** the parity-window connector (165.D2)--(165.D4)
as a candidate proved-internal reduction.  It replaces the full residual
short-shift target by a strict same-parity/even-shift sufficient theorem at
constant cost, without claiming scalar-to-energy equivalence for the XOR
sector.

**Retain and seam-review** the multiplicity-one normal forms
(165.D6)--(165.D10) and (165.D28)--(165.D31), together with the exact phase
and resonance ledger (165.D32)--(165.D39).  They show that the even-shift
sufficient theorem has no character cancellation along a fixed
complement-gcd progression.

**Record only a route-scoped no-go** for shiftwise or progressionwise
triangle inequality, bounded-amplitude counting, character-only Abel
summation, and positive opening/norm placements.  Their restored capacity
is (165.D40).  This does not disprove the actual residual theorem or a
bespoke signed shifted-convolution estimate.

**No downstream promotion** is recommended.  The residual target, full
\(t=1\) face, remaining few-point channels, both hard-TOP parents, BAL,
UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, the conditional bridge,
the quarter theorem, and both global exponents remain unchanged.
