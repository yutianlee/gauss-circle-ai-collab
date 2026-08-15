# Round 60 conductor adjudication

Campaign: `m9-m1-critical-radial-terminal-return`

## Decision

Promote the smooth critical radial terminal-transfer lemma.  In fact the
accepted positive-frequency transform proves the stronger complex modulus
estimate, while the frozen real GAR projection follows by conjugate pairing.

Let

\[
 R=X^{1/4},\qquad Y=\sqrt X,
\]

let (V\in C_c^\infty((c,C))), (0<c<C<16), and let

\[
 \mathcal G_V(X)=\sum_{n\le16Y}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn}),
\]

where \(\mathcal C_X^*\) is the exact accepted Round-14 angular
coefficient.  Then

\[
 \boxed{|\mathcal G_V(X)|\ll_{\varepsilon,V}X^\varepsilon.}
 \tag{60.1}
\]

For real (V), the required consequence is

\[
 \operatorname {Re}\{e(1/8)\mathcal G_V(X)\}
 \ll_{\varepsilon,V}X^\varepsilon.
 \tag{60.2}
\]

## Common antecedent

For every active scale put

\[
 \mathcal B_{j,V}=\sum_{h\ge1}\eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V\!\left({4Xh^2\over d^2Y}\right)e(hX/d).
 \tag{60.3}
\]

The support identity

\[
 V(4R^2h^2/d^2)w_j(d)\ne0
 \quad\Longrightarrow\quad
 h={d\over2R}\sqrt z\gg_V H_j
\]

together with the inherited exact condition (h\le H_j) puts every
surviving frequency in a terminal shell.  The lower cutoff \(\eta_j\)
is one on every contribution.  The upper endpoint is not smoothed: the
zero-extension jump of the exact factor \(\mathbf1_{h\le H_j}\) is
\(O(H_j^{-1})\).

With

\[
 \widehat V(t)=\int_0^\infty V(z)z^{-it}{dz\over z},
\]

Mellin inversion gives the exact mode

\[
 u_{j,t}(h)=\eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}h^{2it},
 \qquad a_{j,t}(d)=\chi_4(d)w_j(d)d^{-2it}.
\]

It satisfies

\[
 \|u_{j,t}\|_\infty+\sum_h|\Delta u_{j,t}(h)|
 \ll_V {1+|t|\over H_j},\qquad |a_{j,t}(d)|\le1.
\]

The accepted terminal divisor theorem and the Schwartz decay of
\(\widehat V\) therefore give

\[
 \left|\sum_j\mathcal B_{j,V}\right|
 \ll_{\varepsilon,V}RX^\varepsilon.
 \tag{60.4}
\]

Bounded positive heights are (O_V(R)) directly; height zero is empty.

## Positive-frequency readback

The accepted interior and one-sided top transforms are identities before
frequency-sign pairing.  At

\[
 d_*=2\sqrt{hX/q},\qquad n=hq,
\]

the Mellin multiplier satisfies

\[
 \left({4X\over Y}\right)^{it}h^{2it}d_*^{-2it}
 =\left({n\over Y}\right)^{it},
\]

and the stationary monomial is

\[
 (hX)^{1/4}q^{-3/4}h^{-1}=R(hq)^{-3/4}.
\]

Consequently the complete positive-frequency identity is

\[
 \boxed{
 \sum_j\mathcal B_{j,V}
 ={e(1/8)\over i}R\mathcal G_V(X)
 +\mathcal Q_{0,V}+\mathcal R_V,}
 \tag{60.5}
\]

where the retained hard-top cotangent boundary is
\(\mathcal Q_{0,V}=O_V(1)\), and the interior/top remainder sum is
\(\mathcal R_V=O_V(\log^2X)\).  Floors, profile overlaps, hard samples,
and equality stars occur exactly once.  Equations (60.4)--(60.5), divided
by (R), prove (60.1).  Pairing the negative frequencies gives the
accepted factor

\[
 -{4\over\pi}R\operatorname {Re}\{e(1/8)\mathcal G_V(X)\}
\]

and hence (60.2).

## Scope and corrections

The derivation packet's original display (60.8) omitted
\(\mathbf1_{h\le H_j}\); it has been corrected.  The initial blind
report correctly proved the frozen real target from its declared paired
interface, but initially withheld the modulus because the unpaired
identity was not in its statement-only packet.  The discovery and hostile
audits independently checked the already accepted positive-frequency
interior/top identities and established (60.5).  The blind provenance is
retained; a later authorized-interface addendum audits the stronger
conclusion separately.

No claim is made at the sharp product endpoint (n=16Y), for sharp radial
cutoffs, for (n/Y\to0), for the alpha transition, full GAR, blockwise
M9-M1, M9, or the discrepancy exponent.  The Round-59 length-(R)
moving strip is not a fixed relative-width radial multiplier and is not
closed by this theorem.

## State effect

- Create `M9-M1-smooth-critical-radial-terminal-transfer` as
  `proved_internal` with (60.1)--(60.5).
- Add it as positive evidence and a dependency of the open global angular
  radial estimate.
- Record that every fixed smooth sector (n\asymp\sqrt X), compactly
  inside the product range, is closed; the remaining radial obstruction is
  (n=o(\sqrt X)) plus endpoint/sharp-cutoff completion.
- Do not promote M9-M1, M9, or `GC-target`.

