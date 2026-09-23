# Statement-only packet: complete \(P_2\) failure-boundary complex

This packet is self-contained for an independent derivation.  Do not read a
proof graph, strategy file, prior report, source card, sibling report,
review, control, candidate, kernel or synthesis.  The task is to prove the
stated estimate by the specified physical cellular mechanism or isolate its
first exact mechanism-scoped self-return.

## 1. Physical source and coefficient

Fix \(X\ge2\), a nonempty hard shell \(L\ge2\),
\(\sigma\in\{+1,-1\}\), fixed \(B,C_0,K_{\rm sel}>0\), and put

\[
 y=\lfloor\sqrt X\rfloor,\quad H=\lfloor yX^{-1/4}\rfloor,
 \quad H_B=\lfloor(\log(2X))^B\rfloor,
 \quad R_0=\lceil L\rceil,\quad D_L=\lceil\sqrt L\rceil.
\tag{B199.1}
\]

For squarefree \(N\), let \(\lambda_{N,\sigma}(d)\) be a total
zero-extended endpoint coefficient supported on positive odd divisors
\(d\mid N\):

\[
 \lambda_{N,\sigma}(d)=
 \mu^2(N)\rho_N(d)a_{L,X}^{\rm lit,\sigma}(N/d,d)
\tag{B199.2}
\]

on its full literal domain and zero otherwise.  Its literal symbol contains
all shell, height, strict cone, profile, floor, star, tie, half-weight,
hard-sample, cell, crossing, endpoint, sign, arithmetic, selector,
conjugation and zero-extension data.  On support
\(|\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon\).

Open the even-shift source as

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\ \hbox{odd},
 \quad0<r<R_0,\quad2\mid r,
\tag{B199.3}
\]

and define

\[
 \Phi_{r,\sigma}(N)=
 \left(1-\frac r{R_0}\right)
 e\!\left(\frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}\right),
\tag{B199.4}
\]

\[
 W(d,m,d',m')=
 \chi_4(d')\chi_4(d)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)}.
\tag{B199.5}
\]

Every physical mask below acts on (B199.5) before Fourier, height, anchor,
Farey or orientation decomposition.

## 2. Exact \(P_2\) failure filtration

Write

\[
 g=(d,d'),\qquad d=g\alpha,\qquad d'=g\beta,
 \qquad(\alpha,\beta)=1,
\tag{B199.6}
\]

and set

\[
 P_2=\mathbf1_{|d-gm|\le D_L}
     \mathbf1_{|d'-gm'|>D_L}.
\tag{B199.7}
\]

For a lower allocation \(N=uv\), its sharp code
\(\mathfrak c_{N,\sigma}(u,v)\) is \(\dagger\) if any named arithmetic,
support or zero-extension predicate is dead.  Otherwise it is the tuple of
the exact branch labels

\[
 (\ell_{\rm shell},\ell_{\rm frequency},\ell_{\rm height},
 \ell_{\rm cone},\ell_{\rm profile},\ell_{\rm floor},
 \ell_{\rm star},\ell_{\rm tie},\ell_{1/2},\ell_{\rm hard},
 \ell_{\rm cell},\ell_{\rm crossing},\ell_{\rm endpoint},
 \ell_{\rm sign}).
\tag{B199.8}
\]

The code records no evaluated smooth coefficient.  Define

\[
 C_{\rm lit}=\mathbf1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
 =\mathfrak c_{N,\sigma}(\alpha,gm)\}}.
\tag{B199.9}
\]

The exact disjoint masks are

\[
\begin{aligned}
 P_{\rm cc}&=P_2\mathbf1_{(m,\beta)=1}
 \mathbf1_{\chi_4(\alpha m)=-1}C_{\rm lit},\\
 P_{\partial\rm lit}&=P_2\mathbf1_{(m,\beta)=1}
 \mathbf1_{\chi_4(\alpha m)=-1}(1-C_{\rm lit}),\\
 P_{s\rm f}&=P_2\mathbf1_{(m,\beta)=1}
 \mathbf1_{\chi_4(\alpha m)\ne-1},\\
 P_{g\rm f}&=P_2\mathbf1_{(m,\beta)>1},
\end{aligned}
\tag{B199.10}
\]

so

\[
 P_2=P_{\rm cc}\dot\cup P_{\partial\rm lit}
 \dot\cup P_{s\rm f}\dot\cup P_{g\rm f}.
\tag{B199.11}
\]

You may take as an input that the complete physical \(P_{\rm cc}\) sector
is already bounded by \(O(L^2X^\varepsilon)\).  No nonemptiness, density or
lower-mass claim is part of that input.

## 3. Open packets and target

The physical inward cross gcd \(\kappa\) is fixed before spectral packets.
In the two orientations it is respectively \((d,m')\) and \((d',m)\).
The exact open packet set is

\[
 \mathcal P_{\rm open}
 =\{\kappa<D_L:\min(Y,D_L)>H_B\mathfrak m\kappa\}.
\tag{B199.12}
\]

Let \(\mathscr R_{\rm open,out}^\sigma\) be the accepted linear map which
restores all packet, lift, anchor, band, divisor, shell, dyadic and physical
orientation sums without taking a modulus at fixed height, orientation,
anchor, conductor or Fourier mode.  It includes the full \(T=0\) branch and
all simultaneous strict \(T\ge1\) Farey-core conditions.  The single outer
real part occurs only after the whole assembly.

Prove

\[
 \boxed{
 \left|\mathscr R_{\rm open,out}^\sigma
 ((P_{\partial\rm lit}+P_{s\rm f}+P_{g\rm f})W)\right|
 \ll_{B,C_0,K_{\rm sel},\varepsilon}L^2X^\varepsilon,}
\tag{B199.13}
\]

or give the first exact no-go for the mechanism in Section 5.  A theorem on
only one or two pieces, \(\kappa=1\), one orientation or one branch does not
complete the task.

## 4. Accepted local identities and capacities

When \((m,\beta)=1\), the lower allocation map

\[
 \tau_0(g\alpha,m,g\beta,m')=(gm,\alpha,g\beta,m')
\tag{B199.14}
\]

is an involution with unchanged recomputed gcd \(g\).  Its character
multiplier is \(s_0=\chi_4(\alpha m)\).  On \(s_0=-1\), summing the two
physical corners produces the actual lower endpoint difference

\[
 \chi_4(g\beta)\chi_4(g\alpha)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(g\beta)
 \overline{\lambda_{N,\sigma}(g\alpha)-
           \lambda_{N,\sigma}(gm)}.
\tag{B199.15}
\]

On a common live sharp cell, the evaluated symbol has a smooth,
normalized-BV and selector product rule.  The smooth part gains
\(D_L/L\); the aggregate BV part costs \(D_L^2X^\varepsilon\); the selector
commutator vanishes for all sufficiently large shells by the bounded-\(g\),
distinct-selected-prime gap argument, and bounded shells are absolutely
safe.  These facts prove the already accepted \(P_{\rm cc}\) result.

They do not apply without repair to the complement.  The aligned-face
identity is

\[
 \left(\frac{g\alpha}{m}-g\right)
 \left(\frac{gm}{\alpha}-g\right)
 =-\frac{g^2(\alpha-m)^2}{\alpha m}.
\tag{B199.16}
\]

Thus all \(O(LD_L)\) close pairs can cross a ratio face aligned with \(g\),
leaving positive capacity \(D_LL^2X^\varepsilon\).  This is not a lower
bound for the literal coefficient.

The complete cross-coprime lower/upper four-corner rectangle has character
table \((+,-,-,+)\) on its alternating sector, but it forces physical
\(\kappa=1\); its simultaneous swap has relative sign \(+1\).  It does not
cover every \(2\le\kappa<D_L\) packet.

For a fixed packet, the inherited positive bound is

\[
 \ll u(\kappa+M)X^\varepsilon,qquad M=\min(Y,D_L),
\tag{B199.17}
\]

whereas the sufficient target scale is
\[
 H_B\mathfrak m\kappa uX^\varepsilon.
\tag{B199.18}
\]
On (B199.12), the positive route misses by
\(M/(H_B\mathfrak m\kappa)>1\).  Globally the raw physical capacity is
\(D_LL^2X^\varepsilon\) and the desired bound is
\(L^2X^\varepsilon\).

## 5. Frozen cellular-boundary mechanism

For every physical allocation vertex define four cross-gcd factors

\[
 G_{00}=(d,d'),\quad G_{10}=(m,d'),\quad
 G_{01}=(d,m'),\quad G_{11}=(m,m').
\tag{B199.19}
\]

Squarefreeness makes them pairwise coprime and gives

\[
 G_{00}G_{10}G_{01}G_{11}=\gcd(N,N+r),
 \qquad G_{00}=g,\quad G_{10}=(m,\beta).
\tag{B199.20}
\]

Construct, if possible, a complete physical allocation two-chain whose
edges transfer explicit prime-factor blocks among the four states in
(B199.19), preserve \((N,N+r)\), and are bijections on their stated live
domains.  Every recomputed gcd and inverse edge must be displayed.  The
twisted incidence on an edge is the actual quotient of its
\(\chi_4(d)\chi_4(d')\) factors; no formal sign may be assigned.

The desired exact identity is of the form

\[
 \partial_{\chi,\rm lit}\mathcal C
 =(P_{\partial\rm lit}+P_{s\rm f}+P_{g\rm f})W
 +E_{\rm safe},
\tag{B199.21}
\]

where every term of \(E_{\rm safe}\) belongs to an already target-safe
physical sector and keeps its licensed masked-operator passage.  A term in
the unestimated two-far mask \(P_1\), another original-\(t\) incidence, an
unpriced changed-gcd allocation or a deleted live corner is not safe.

After the exact physical identity, expand the actual endpoint products.
Every complete cell must produce a \(D_L/L\) close-leg difference or an
explicit target-safe boundary.  Restore transported-mask commutators,
unequal endpoint translations, carries, births/deaths, cells, crossings,
all Fourier signs, both physical orientations, both \(T\)-branches and all
zero extensions before the only outer real part.

## 6. Mandatory first stress test and no-go gate

Test \(P_{\partial\rm lit}\) first.  Write the actual sharp-code jump
cochain across (B199.14), including its numerical endpoint multiplier and
orientation, as a complete twisted boundary.  A formal
\(\partial^2=0\) does not suffice if an ordinary face survives with
coefficient one.

Stop with a mechanism-scoped no-go, without changing to another analytic
mechanism, if the exact first stress test:

1. returns an aligned face having only
   \(D_LL^2X^\varepsilon\) positive control;
2. requires the \(\kappa=1\) rectangle or assigns its simultaneous swap a
   false negative sign;
3. moves a face into an unproved \(P_1\) or changed-gcd boundary;
4. deletes a live or zero-extended corner;
5. takes a positive norm before joint restoration.

If the face test passes, extend the same chain to the \(+1\) character edge
on \(P_{s\rm f}\) and the nontrivial \(G_{10}\) state on
\(P_{g\rm f}\).  Failure of bijectivity, merger of two cross-gcd states, a
missing inverse cell, an orbit tail, an unpriced branch or the unchanged
packet deficit is also a valid first self-return.

The no-go conclusion must be restricted to (B199.21).  Positive capacity
does not prove nonemptiness, nonvanishing, lower mass or failure of
(B199.13) by a different coefficient-sensitive method.

## 7. Mandatory controls and report contract

Reject unsigned, character-erased, phase-conjugated and arbitrary-array
shadows.  Reject fixed-conductor cancellation after the literal conductor
factor is restored, the formal negative live/dead wrap, a false common
height-event step, deletion of changed-gcd corners, smoothing of the
aligned face, post-spectral masking and all separate component norms.  Do
not use a capacity as a lower bound.

The report must contain:

1. Result: theorem or mechanism-scoped no-go.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required controls and outcomes.
6. Dependencies: only this packet and the protocol.
7. Recommended state effect: promote, retain, revise, reject, or no change.

No numerical theorem evidence is allowed.  Any finite symbolic table is
diagnostic only.  Even a proof of (B199.13) closes only this remaining
\(P_2\) sector and implies no complete original \(t=1\), hard M1, smooth
M1, M2, endpoint, global or exponent result by itself.
