# Round 193 discovery report: gcd-scaled close-orientation sector

- Campaign: m9-m1-t1-core-gcd-scaled-orientation-gate
- Task: gcd_scaled_orientation_sector_attack
- Role: discovery
- Round: 193
- Starting graph SHA-256: 7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9
- Evidence status: candidate evidence only
- Numerical theorem evidence: none

## 1. Result

### Strict double-close sector lemma

There is a stronger target-safe sector than the reference
\((m,m')=1,\ r\equiv2\pmod4\) involutive sector.

Let one original physical high-height opposing incidence be written, in
the required tuple order,

\[
(d,m,d',m'),\qquad N=dm,\qquad N+r=d'm',
\]

where the first and third entries are the lower and upper character
divisors and the second and fourth entries are their complementary
factors. Put

\[
g=(d,d'),\qquad D=D_L=\lceil\sqrt L\rceil .
\]

On the free physical incidence atoms, before the anchor Fourier
expansion, define

\[
P_{\rm cl}
 ={\bf1}_{|d-gm|\le D}\,
  {\bf1}_{|d'-gm'|\le D}.
\tag{193.A1}
\]

No condition on \(k=(m,m')\), and no congruence condition beyond the
already inherited evenness of \(r\), is imposed in (193.A1). Lift this
mask coordinatewise through the exact Round-187--Round-192 linear
decompositions as specified in Section 3. Then, for every nonempty
dyadic \(Y>Q=H_B\), both signs, and the exact Round-192 core (including
its whole inherited rho-large remainder when \(T=0\)),

\[
\boxed{
 \left|P_{\rm cl}\mathscr R_{{\rm core},Y,Q}^{\sigma}\right|
 \ll_{B,\varepsilon}L^2X^\varepsilon .}
\tag{193.A2}
\]

The decisive estimate is an absolute physical incidence count. In
either opposing orientation, the complete double-close live sector has

\[
\#\mathcal I_{\rm cl}
\ll LD\log(2L)+LD^2.
\tag{193.A3}
\]

Thus (193.A3) is target-sized at \(D=\lceil\sqrt L\rceil\), before using
the character reversal, smooth common-cell differences, normalized
dyadic BV, or boundary cancellation. Every literal mask, floor, star,
half-weight, hard sample, crossing, endpoint trace, and zero extension
is therefore harmless on this strict sector simply because it only
deletes or bounds target-many physical atoms.

On the reference sub-sector

\[
P_{\rm inv}:=
P_{\rm cl}{\bf1}_{(m,m')=1}{\bf1}_{r\equiv2\ (4)},
\tag{193.A4}
\]

the proposed map

\[
\tau_g(d,m,d',m')=(gm,d/g,gm',d'/g)
\tag{193.A5}
\]

is, independently, a genuine fixed-point-free multiplicity-one
orientation-reversing involution. It preserves the endpoint products,
shift, \(g\), \(k=1\), phase, and Fejer weight, and reverses the
\(\chi_4\)-product. Its exact coefficient commutator is proved below.
This algebra is not needed for the estimate (193.A2), but it passes all
of the requested normalization and sign controls.

The result is strict. It does not estimate either first-failure
complement

\[
|d-gm|>D,\qquad
|d-gm|\le D,\quad |d'-gm'|>D.
\tag{193.A6}
\]

It closes no complete \(t=1\) relation, parent, bridge, theorem, or
exponent.

## 2. Exact statement and hypotheses

Retain the exact accepted Round-192 core. Thus the Round-191 fast packet
has

\[
Q=H_B,\quad U=\mathfrak m q>4Q,\quad q>Q,\quad
\mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,
\]

the inherited nonempty power-of-two projective band, and every literal
field under one complex aggregate before the final real part. Here
\(\mathfrak m\) denotes the Fourier lift variable, to distinguish it
from the complementary factor \(m\) in the opened endpoint tuple.
For the canonical signed inverse

\[
\rho v_0-\beta U=1
\]

and

\[
T=\min\!\left\{\frac{U-1}{2},
 \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
\]

the exact core convention is:

- if \(T=0\), retain the whole inherited rho-large remainder;
- if \(T\ge1\), retain only rows satisfying

\[
|\rho|\ge(A+1)(T+1),\qquad
|c\beta-d_0\rho|>T
\tag{193.A7}
\]

for every permitted primitive Farey covector
\((c,d_0)\). The symbol \(d_0\) in (193.A7) is a covector coordinate,
not an endpoint divisor.

The physical ancestor of every such spectral/core coordinate is an
opened opposing incidence satisfying

\[
N=dm,\qquad N+r=d'm',\qquad d,d'\ {\rm odd},\qquad
0<r<R_0=\lceil L\rceil,\qquad 2\mid r.
\tag{193.A8}
\]

The endpoint coefficient is the exact zero-extended coefficient
\(\lambda_{N,\sigma}(d)\) from the accepted Round-185 kernel. In
particular, on live support,

\[
d,m,d',m'\asymp L,\qquad
|\lambda_{N,\sigma}(d)|\ll_\eta X^\eta
\tag{193.A9}
\]

for every fresh \(\eta>0\), and all the literal arithmetic and analytic
fields remain present.

The mask \(P_{\rm cl}\) is a diagonal \(0,1\) mask on the original free
physical atoms (193.A8). It is not a Fourier-mode predicate and is not
defined by multiplying a combined height-difference atom by the mask at
only one of its two endpoints. Every descendant copy of a free physical
atom inherits the mask of that atom. A height difference is first
expanded as the signed sum of its two free atoms, and each copy is then
masked separately. Equivalently, the full Round-187--Round-192
decomposition is applied to the zero-extended physical sequence
\(P_{\rm cl}W\). This convention defines

\[
P_{\rm cl}\mathscr F,\qquad
P_{\rm cl}\mathscr S_{\le192},\qquad
P_{\rm cl}\mathscr R_{\rm core}
\tag{193.A10}
\]

without asserting that \(P_{\rm cl}\) commutes with a height
difference.

The conclusions are:

1. the physical count (193.A3) and absolute bound

\[
|P_{\rm cl}\mathscr F_Y^\sigma|
\ll_\varepsilon L^2X^\varepsilon;
\tag{193.A11}
\]

2. deletion-stable inherited safety

\[
|P_{\rm cl}\mathscr S_{\le192,Y}^\sigma|
\ll_{B,\varepsilon}L^2X^\varepsilon;
\tag{193.A12}
\]

3. the exact complex identity

\[
\boxed{
P_{\rm cl}\mathscr R_{\rm core}
=P_{\rm cl}\mathscr F
-P_{\rm cl}\mathscr S_{\le192};}
\tag{193.A13}
\]

4. (193.A2), by (193.A11)--(193.A13);
5. on \(P_{\rm inv}\), the exact involution, primitive-coordinate map,
character reversal, and coefficient commutator described in Section 3.

All assertions are uniform in real \(X\), every nonempty active shell,
both signs, and every dyadic \(Y>Q\). No numerical hypothesis or
experiment is used.

## 3. Proof and derivation

### 3.1 Absolute count for the stronger double-close sector

Consider first the plus orientation. The accepted multiplicity-one
coordinates are

\[
d=\kappa gU,\qquad
d'=g(\kappa U+2S),\qquad
m'=\kappa v,\qquad
m=\kappa v+2w,
\tag{193.A14}
\]

\[
h=Sv-Uw>0,\qquad r=2\kappa gh<R_0,
\tag{193.A15}
\]

with \(S,w>0\). The two close conditions are exactly

\[
d-gm=g\{\kappa(U-v)-2w\},\qquad
d'-gm'=g\{\kappa(U-v)+2S\}.
\tag{193.A16}
\]

Subtracting the two expressions in (193.A16) gives

\[
S+w\le \frac Dg.
\tag{193.A17}
\]

It follows in particular that \(w\ll D/g\), and either expression in
(193.A16) then gives

\[
|\kappa(U-v)|\le \frac{3D}{g}.
\tag{193.A18}
\]

On a live physical atom, the strict hard cone and (193.A9), together
with \(d=gm+O(D)\), force \(g=O(1)\). More explicitly, for sufficiently
large \(L\),

\[
4<\frac dm<16,\qquad
\left|\frac dm-g\right|\ll\frac DL=o(1).
\tag{193.A19}
\]

Since \(g\mid d,d'\), \(g\) is odd; squarefreeness also deletes any
nonsquarefree value. Thus \(g\) ranges over a fixed finite set. The
bounded remaining values of \(L\) have target-sized total capacity and
are absorbed in the constant.

Fix \((\kappa,g,U,v,w)\). From (193.A15),

\[
\frac{Uw}{v}<S<
\frac{Uw}{v}+\frac{R_0}{2\kappa gv}.
\tag{193.A20}
\]

Live upper-endpoint support gives \(\kappa v\asymp L\). Hence the
interval in (193.A20) has length \(O(1)\), uniformly in all asymptotic
variables. It contains \(O(1)\) integer values of \(S\).

For fixed \(\kappa,g\), live lower-endpoint support gives
\(O(L/\kappa)\) possible \(U\)'s (the fixed \(g\) is harmless).
Equation (193.A18) gives \(O(1+D/\kappa)\) possible \(v\)'s per \(U\),
(193.A17) gives \(O(D)\) possible \(w\)'s, and (193.A20) gives
\(O(1)\) possible \(S\)'s. Therefore

\[
\#\mathcal I_{{\rm cl},+}
\ll
\sum_{\kappa\ll L}
\frac L\kappa\left(1+\frac D\kappa\right)D
\ll LD\log(2L)+LD^2.
\tag{193.A21}
\]

In the minus orientation the roles are

\[
d'= \kappa gU,\quad
d=g(\kappa U+2S),\quad
m=\kappa v,\quad
m'=\kappa v+2w,\quad
h=Uw-vS>0.
\]

The same two close equations occur in the opposite order, and, for
fixed \((\kappa,g,U,v,w)\), the allowed \(S\)'s lie in an interval of
length \(R_0/(2\kappa gv)=O(1)\). Thus (193.A21) also holds for the
minus orientation. Every gcd, parity, squarefree, selector, core,
Fourier-band, dyadic-height, endpoint, and zero-extension condition
only deletes atoms.

At \(D=\lceil\sqrt L\rceil\),

\[
LD\log(2L)+LD^2
\ll L^{3/2}\log(2L)+L^2
\ll_\eta L^2X^\eta,
\tag{193.A22}
\]

using only the inherited \(L\ll X^{1/4}\) support to absorb a fixed
logarithm into a fresh epsilon budget. Each physical correlation atom
has modulus \(O_\eta(X^\eta)\) after rebudgeting the two endpoint
coefficients; the character, phase, affine parity, and Fejer weight
have modulus at most one. Equations (193.A21)--(193.A22) prove
(193.A11). Notice that the count already sums the full range
\(0<h<R_0/(2\kappa g)\); it contains no factor \(Y\).

The same proof gives the scale ledger

\[
|P_{{\rm cl},D}\mathscr F|
\ll_\eta\{LD\log(2L)+LD^2\}X^\eta.
\tag{193.A23}
\]

Thus \(D\ll\sqrt L\) is the endpoint power scale for this absolute
deletion argument.

### 3.2 Exact lifting through the Round-187--Round-192 decomposition

Let \(\mathcal V_{\rm phys}\) be the free complex vector space generated
by the complete zero-extended physical atoms, with orientation,
endpoint order, signs, products, phase, Fejer weight, masks, cells,
crossings, births, deaths, and all other literal labels included in a
generator. The anchor Fourier expansion is a coordinatewise linear map
\(\mathcal E\) from this space to the spectral free space. Since
\(P_{\rm cl}\) is independent of the Fourier mode,

\[
\mathcal E(P_{\rm cl}W)
=\widetilde P_{\rm cl}\mathcal E(W),
\tag{193.A24}
\]

where every spectral copy inherits its physical parent's mask.

For a height difference, one must not write
\(P(h)\Delta W(h)\). Instead,

\[
\Delta(PW)(h)=P(h)W(h)-P(h-1)W(h-1)
\tag{193.A25}
\]

is kept as two separately labelled free atoms. If \(P(h)\ne P(h-1)\),
the new mask change remains in the literal-mask/birth/death part of the
remainder. This is precisely why no commutation of \(P\) with
\(\Delta\) is claimed.

All accepted decompositions through Round 192 are finite signed linear
identities in these free generators. Applying them to \(P_{\rm cl}W\)
therefore gives, before a modulus and before the final real part,

\[
P_{\rm cl}\mathscr F
=P_{\rm cl}\mathscr S_{\le192}
+P_{\rm cl}\mathscr R_{\rm core}.
\tag{193.A26}
\]

The safe estimates are deletion-stable:

- the Round-187 \(U=1\), low-conductor, and edge bounds are positive
  atom/mode counts;
- the Round-188 imprimitive-lift bound is a positive count with the
  exact \(\mathfrak m^{-1}c_q(a)\) normalization;
- the Round-189 projectively slow bound counts residue classes and
  then atoms;
- the Round-191 inverse-small bound applies endpoint-exact Abel to the
  deleted zero-extended sequence and then counts the remaining atoms;
- the Round-191 outer terminal still occurs at at most the two outer
  carrier heights, while a new \(P\)-change inside the carrier remains
  in the remainder;
- the isolated Round-191 Fejer term is multiplied by a \(0,1\) live
  mask and retains its accepted absolute derivative count; a
  \(P(h)-P(h-1)\) term is not silently assigned to Fejer;
- the Round-192 Farey union is a single union indicator and its proof
  counts selected rows/atoms positively, so coordinatewise deletion
  only reduces its majorant.

Consequently every accepted outer ledger remains valid and gives
(193.A12). The Round-192 replacement identity continues to replace,
rather than duplicate, selected terminal and Fejer rows. At \(T=0\)
the Farey projector is still identically zero, so the whole inherited
rho-large remainder is retained exactly. This proves
(193.A13), and (193.A2) follows from (193.A11)--(193.A13).

For \(P_{\rm cl}\mathscr F\), the complete anchor Fourier sum is
recombined using (193.A24) before any orientation argument. There is
no modewise pairing: under the involution below the primitive modulus
changes from \(U\) to \(v\), so a retained individual Fourier mode is
not an invariant object.

### 3.3 The scaled involution on the reference sub-sector

Now impose \(k=(m,m')=1\). Because \(d,d'\) are odd and \(r\) is even,
\(m,m'\) have the same parity. They cannot both be even when \(k=1\),
so

\[
m,m'\ {\rm are\ odd}.
\tag{193.A27}
\]

Since \(g\mid d,d'\), (193.A5) is integral and retains the required
tuple order:

\[
(\hbox{character divisor},\hbox{complementary factor},
 \hbox{upper character divisor},\hbox{upper complementary factor}).
\]

The endpoint products are unchanged:

\[
(gm)(d/g)=dm=N,\qquad
(gm')(d'/g)=d'm'=N+r.
\tag{193.A28}
\]

The new character-divisor gcd and complementary-factor gcd are

\[
(gm,gm')=g(m,m')=g,\qquad
(d/g,d'/g)=1.
\tag{193.A29}
\]

Thus the map preserves \(g\) and \(k=1\), and applying it again, with
the canonically recomputed gcd \(g\), returns the original tuple. If a
tuple were fixed, then \(d=gm\) and \(d'=gm'\), which is incompatible
with opposing signs of \(d'-d\) and \(m'-m\) unless \(r=0\). Hence the
map is fixed-point-free on the live opposing sector. It sends plus to
minus and minus to plus with multiplicity one.

For the plus coordinates (193.A14), the image has canonical minus
coordinates

\[
(\kappa,g,U',v',S',w')=(\kappa,g,v,U,w,S).
\tag{193.A30}
\]

Here the word canonical requires proof. Squarefreeness of the live
endpoint product makes the factors \(\kappa,g,U\) in
\(d=\kappa gU\) pairwise coprime, so \((g,U)=1\). The accepted carrier
has \((gU,v)=1\). Moreover

\[
(m,m')=(\kappa v+2w,\kappa v)=1
\]

and \(\kappa v\) is odd, so \((v,w)=1\). From
\(h=Sv-Uw\),

\[
(v,h)=1.
\tag{193.A31}
\]

It follows that

\[
(gv,U)=1,\qquad (v,h)=1,
\tag{193.A32}
\]

which are exactly the image carrier conditions
\((gU',v')=1\) and \((U',h)=1\). Also

\[
(g\kappa v,\kappa U)=\kappa,
\]

so the image cross-gcd is canonically the same \(\kappa\), not merely
a remembered label. Finally,

\[
U'w'-v'S'=vS-Uw=h,
\]

which is the minus primitive equation. The reverse calculation is
identical.

Products, \(N\), \(N+r\), \(r\), the square-root phase, the Fejer
factor \(1-r/R_0\), and the endpoint order are unchanged. The lower
endpoint coefficient remains conjugated. The close mask is invariant
because

\[
gm-g(d/g)=-(d-gm),\qquad
gm'-g(d'/g)=-(d'-gm').
\tag{193.A33}
\]

### 3.4 Character reversal and exact coefficient commutator

On \(r\equiv2\pmod4\), all four factors in (193.A8) and (193.A27) are
odd. Hence \(N\) and \(N+r\) are odd and occupy opposite odd residue
classes modulo four:

\[
\chi_4(N+r)=-\chi_4(N).
\tag{193.A34}
\]

Using complete multiplicativity on odd integers and
\(\chi_4(g^2)=1\),

\[
\begin{aligned}
&\{\chi_4(d')\chi_4(d)\}
 \{\chi_4(gm')\chi_4(gm)\}\\
&\qquad
=\chi_4\!\left(d'd\,g^2m'm\right)
=\chi_4\!\left((N+r)N\right)=-1.
\end{aligned}
\tag{193.A35}
\]

Thus

\[
\boxed{
\chi_4(d')\chi_4(d)
=-\chi_4(gm')\chi_4(gm).}
\tag{193.A36}
\]

This sign is obtained before taking an absolute value.

Let

\[
\Phi_r(N)=
\left(1-\frac r{R_0}\right)
e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
\]

include the unchanged Fejer and square-root phase factors, and set

\[
C(d,m,d',m')
=\lambda_{N+r,\sigma}(d')\,
 \overline{\lambda_{N,\sigma}(d)}.
\tag{193.A37}
\]

After the complete anchor Fourier recombination, ambient zero extension,
and reindexing the whole \(P_{\rm inv}\) physical set by the
fixed-point-free involution, one obtains exactly

\[
\begin{aligned}
P_{\rm inv}\mathscr F
=\frac12\sum_{\iota\in P_{\rm inv}}
&\chi_4(d')\chi_4(d)\,\Phi_r(N)\\
&\times\left\{
\lambda_{N+r,\sigma}(d')
\overline{\lambda_{N,\sigma}(d)}
-\lambda_{N+r,\sigma}(gm')
\overline{\lambda_{N,\sigma}(gm)}
\right\}.
\end{aligned}
\tag{193.A38}
\]

The upper coefficient is never conjugated and the lower coefficient is
always conjugated; reversing orientation does not reverse the ordered
products \(N<N+r\). The factor \(1/2\) counts each two-element orbit
once.

### 3.5 Arithmetic selector and literal-field ledger

For a squarefree endpoint product write \(d=gd_1\). Under (193.A5), a
prime in \(g\) remains on the character leg, while every prime outside
\(g\) is complemented. The Round-184 residual mask has truth table

\[
(00,10,01,11)\longmapsto(1,0,0,1).
\tag{193.A39}
\]

Complementing both selected-prime bits preserves (193.A39); retaining
both bits in \(g\) also preserves it. The only possible mismatch is
that exactly one selected prime divides \(g\).

This exception is absent for all sufficiently large \(L\). Indeed the
active close sector has \(g\le G_*\) for a fixed \(G_*\). If a selected
prime \(p\mid g\), then \(p\le G_*\), whereas its distinct selected
partner \(q\) satisfies

\[
|\log(q/p)|\le C_{\rm sel}L^{-1/2}.
\tag{193.A40}
\]

For large \(L\), (193.A40) first confines \(q\) to a fixed finite prime
set and then contradicts the positive minimum logarithmic separation
between two distinct primes in that set. The finitely many smaller
\(L\)'s cost \(O_{B,\varepsilon}(L^2X^\varepsilon)\) by (193.A21).
This argument is applied separately to the selected pair of \(N\) and
that of \(N+r\).

Squarefreeness, divisor status, oddness, and allocation coprimality are
preserved on the involutive sub-sector because the products are
unchanged and every factorization of a squarefree product splits its
prime set. No such invariance is needed for the larger \(P_{\rm cl}\)
estimate: the literal masks only reduce the absolute count.

For completeness, the two endpoint allocation paths in (193.A38) are

\[
(m,d)\longmapsto(d/g,gm),\qquad
(m',d')\longmapsto(d'/g,gm').
\tag{193.A41}
\]

Each product is fixed, the complementary-factor displacement is at
most \(D/g\), and the character-factor displacement is at most \(D\).
Write the accepted endpoint symbol on a common literal smooth cell as
\(\eta_L(u)b^{\rm sm}(u,v)\), separating the normalized-discrete-BV
dyadic factor from the uniformly \(C^1\) factors. The accepted
moving-factor ledger gives

\[
|b^{\rm sm}(m,d)-b^{\rm sm}(d/g,gm)|
\ll_\eta \frac DL X^\eta,
\tag{193.A42}
\]

and the analogous upper-endpoint estimate. The dyadic-factor
difference is charged separately by normalized BV below. The
product-only \((L^2/N)^{3/4}\) factor is exactly invariant. Applying
the product rule to the smooth part of (193.A37), the deliberately
coarse incidence envelope

\[
\ll LD^2\log(2L)+LD^3
\tag{193.A43}
\]

would give common-cell cost

\[
\ll_\eta
\{D^3\log(2L)+D^4\}X^\eta,
\tag{193.A44}
\]

which is also target-sized at \(D=\sqrt L\).

For a normalized dyadic BV edge, fixing the crossed integer edge
localizes \(\kappa U\) to an \(O(D)\) collar. The close-coordinate
multiplicity at fixed \(\kappa\) is
\(O(D^2(1+D/\kappa)^2)\), whence

\[
\sum_{\kappa\ll L}
D^2\left(1+\frac D\kappa\right)^2
\ll LD^2+D^3\log(2L)+D^4.
\tag{193.A45}
\]

At \(D=\lceil\sqrt L\rceil\), (193.A45) is
\(O_\eta(L^2X^\eta)\). The same localization prices the fixed finite
family of vertical, horizontal, and ratio faces, profile entries and
exits, floor/star/tie/half-weight fields, hard samples, real-\(X\)
crossings, endpoint traces, and endpoint zero extensions. Affine and
outer births/deaths are already individual free atoms and are covered
by (193.A21). Thus the requested common-cell, normalized-BV, collar,
and literal-field ledgers pass even without invoking the stronger
absolute count.

### 3.6 Exact complement and power restoration

Within the exact Round-192 core, assign every descendant coordinate to
the first failed physical condition:

\[
\begin{aligned}
\mathcal C_1&=\{|d-gm|>D\},\\
\mathcal C_2&=\{|d-gm|\le D,\ |d'-gm'|>D\}.
\end{aligned}
\tag{193.A46}
\]

The two sets in (193.A46) are disjoint and, together with
\(P_{\rm cl}\), exhaust the opposing core. Every spectral copy inherits
the class of its physical parent, so there is no Fourier overlap or
double count.

If one instead records the complement of only the reference involutive
sub-sector, the first-failure order is

\[
\begin{array}{ll}
1.&r\equiv0\pmod4,\\
2.&r\equiv2\pmod4,\ (m,m')>1,\\
3.&r\equiv2\pmod4,\ (m,m')=1,\ |d-gm|>D,\\
4.&r\equiv2\pmod4,\ (m,m')=1,\ |d-gm|\le D,\
   |d'-gm'|>D.
\end{array}
\tag{193.A47}
\]

The stronger result proves the close parts of the first two classes in
(193.A47) absolutely, so the actual remaining complement is precisely
(193.A46).

The physical estimate has no \(Y,Q,\mathfrak m,q,a,J,\rho,\beta\)
loss. The restricted inherited safe estimates retain their already
accepted exact lift, coefficient-mass, band, divisor, and shell ledgers:
the Fourier lift factor cancels where required, \(Q\) and all band
counts are fixed polylogarithmic, and no positive power of \(Y\) is
absorbed. Thus (193.A11)--(193.A13) restore the complete
\(L,Y,Q,X\) ledger and prove (193.A2).

## 4. First doubtful or unproved step

There is no unproved mask, BV, collar, projection, or power seam inside
\(P_{\rm cl}\) at \(D=\lceil\sqrt L\rceil\). The estimate is absolute,
and the masked physical-to-core passage is an exact free-atom linear
identity with deletion-stable safe bounds.

The first unproved extension is the double-close scale beyond the
square-root threshold, or either set in (193.A46). If

\[
D=L^{1/2+\delta}\qquad(\delta>0\ {\rm fixed}),
\]

then the positive count (193.A23) contains

\[
LD^2=L^{2+2\delta},
\tag{193.A48}
\]

losing the fixed power \(L^{2\delta}\). The normalized BV/collar ledger
(193.A45) can contain \(D^4=L^{2+4\delta}\). These are upper-capacity
deficits, not literal lower bounds and not a disproof of a wider signed
sector.

For the exact complement (193.A46), neither close-coordinate sparsity
nor the proved involution gives a target-sized count. No accepted
dependency supplies the missing jointly signed estimate. This is the
first remaining seam toward the complete Round-192 core.

## 5. Control tests and outcomes

All controls were analytical; no diagnostic computation was used.

| Control | Outcome |
|---|---|
| exact_round192_core_and_T_zero_scope | PASS. Equation (193.A7) is retained for \(T\ge1\); at \(T=0\) the Farey projector remains zero and the whole inherited rho-large remainder is masked and decomposed. |
| opened_endpoint_tuple_order | PASS. Every occurrence of \((d,m,d',m')\) keeps character divisor, complementary factor, upper character divisor, upper complementary factor. |
| cofactor_gcd_one_forces_odd_cofactors | PASS. Same parity follows from odd \(d,d'\) and even \(r\); gcd one rules out the even-even case. |
| scaled_map_integrality_and_involution | PASS on \(P_{\rm inv}\), by (193.A28)--(193.A29). |
| g_and_cofactor_gcd_preservation | PASS. The recomputed gcds are exactly \(g\) and one. |
| opposing_orientation_bijection_and_multiplicity | PASS. The map is fixed-point-free, self-inverse, and exchanges the two multiplicity-one canonical orientations. |
| primitive_coordinate_image_and_coprimality | PASS. The canonical image is (193.A30), with (193.A31)--(193.A32). |
| product_shift_phase_and_Fejer_preservation | PASS. Both endpoint products and \(r\) are fixed, so the phase and Fejer factor are literal invariants. |
| r_two_mod_four_character_reversal | PASS before absolute value, by (193.A34)--(193.A36). |
| endpoint_order_and_lower_conjugation | PASS. Equation (193.A38) preserves upper-first/lower-conjugated order on both orbit legs. |
| tau_invariant_close_mask | PASS, by (193.A33). |
| active_support_bounds_g | PASS. Equation (193.A19) confines \(g\) to a fixed set; small \(L\) is bounded separately. |
| residual_selector_truth_table_under_g_complement | PASS. Both-bit complement and both-in-\(g\) preserve \(1,0,0,1\). |
| selected_pair_intersects_g_exception | PASS. Exactly-one-in-\(g\) is absent for large \(L\) by fixed-prime separation and target-safe for bounded \(L\). |
| squarefree_divisor_coprimality_and_parity | PASS on the involutive sub-sector; unnecessary but harmless for the larger absolute sector. |
| literal_common_cell_difference | PASS. Equation (193.A42) and product-rule bound (193.A44). |
| dyadic_BV_lift_multiplicity | PASS. Equation (193.A45) is \(O(L^2X^\eta)\) at the frozen scale. |
| all_boundary_collar_floor_star_endpoint_fields | PASS. Every named field is covered by (193.A21) absolutely and, independently, by the fixed-face version of (193.A45). |
| zero_extension_births_and_deaths | PASS. They remain separate free atoms and are counted; no partner is manufactured. |
| complete_close_sector_power_no_hidden_Y | PASS. The count uses the full Fejer range and is uniform in the dyadic \(Y\). |
| complete_anchor_Fourier_recombination_before_pairing | PASS. Equation (193.A24) is recombined before (193.A38); no individual mode is paired. |
| inherited_safe_projection_deletion_stability | PASS. Each Round-187--Round-192 safe estimate has an absolute positive majorant stable under coordinatewise deletion. |
| exact_masked_core_identity_no_double_count | PASS. Equations (193.A25)--(193.A26) give the exact complex identity, and the Round-192 replacement convention is retained. |
| exact_first_failure_complement | PASS. Equations (193.A46)--(193.A47) are disjoint first-failure partitions. |
| no_arbitrary_bounded_coefficient_closure | PASS. Boundedness is used only after proving target cardinality on a strict sector; no conclusion is drawn for the full bounded-array class. |
| diagnostic_only_computation | PASS. No computation was performed. |
| original_t1_only_downstream_scope | PASS. The result is a strict sector of the exact original-\(t=1\) residual only. |
| no_in_round_owner_pivot | PASS. No other owner or exponent was pursued. |
| exponent_quarantine | PASS. The internal \(1/3\), accepted external \(0.3144831759740614\ldots\), and target \(1/4\) scopes are unchanged. |

## 6. Dependencies and exact artifacts used

The derivation used only the permitted context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- state/failure_ledger.md;
- strategy/round193_m1_t1_core_gcd_scaled_orientation_involution_strategy.md;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md;
- proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/synthesis.md;
- rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/conductor_round192_adjudication.md.

The direct accepted mathematical dependencies are the Round-184 through
Round-192 kernels listed above and the elementary divisor bound already
present in their dependency chain. No external theorem, web source, or
numerical experiment was added.

## 7. Recommended state effect

Recommend promotion, after the required independent reviews and a valid
State Patch, of one subordinate proved-internal strict sector:

\[
\boxed{\text{all opposing Round-192-core physical ancestors satisfying
both gcd-scaled close inequalities at }D_L=\lceil\sqrt L\rceil.}
\]

This is stronger than the proposed cofactor-coprime
\(r\equiv2\pmod4\) orientation sector. The scaled involution should be
recorded as certified finite algebra on that sub-sector, but the proof
of the estimate should rest on the stronger absolute count
(193.A21), not on unnecessary literal cancellation.

Retain, without promotion, the exact complement (193.A46), the complete
rho-large core, complete original \(t=1\), every original \(t\ge2\)
range, the remaining hard small-\(t\) owner, both M1 parents, every M2
parent, endpoint uniformity, M9, both bridges, the Gauss-circle target,
and all exponent claims.

Recommended terminal label:

strict_rho_large_gcd_scaled_orientation_sector.
