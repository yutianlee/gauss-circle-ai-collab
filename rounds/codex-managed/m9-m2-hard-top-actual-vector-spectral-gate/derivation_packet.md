# Round 126 conductor derivation packet: vector-level parity spectral gate

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`

Starting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`

Status: accepted Round-75/Round-110 identities plus one untrusted
noninvertible proof direction. No estimate below is accepted unless every
literal coefficient, face, tag, capacity, and false control passes.

## 1. Exact vector interface

Use (126.B1)--(126.B15) from `blind_statement.md`. Define the literal
(m)-vector carried by one odd height (h) by

$$
 v_h(m)=1_{\lceil h/4\rceil\le m\le h}
 a_{\rm end}(h,m)e(J\sqrt{hm}).
\tag{126.D1}
$$

Then

$$
 \mathcal E_L^{\rm top}
 =\left\|\sum_{h\in\mathscr H_L}\chi_4(h)v_h\right\|_{\ell^2_m}^2,
 \qquad
 \mathcal D_L=\sum_h\|v_h\|_2^2\ll L^2.
\tag{126.D2}
$$

There are (O(L)) active rows, each with (O(L)) entries of bounded
size. Aligned coefficient vectors can have energy (L^3); the actual
target (L^2X^\varepsilon) requires the full square-root row saving at
energy level. This capacity must be declared before any comparison norm.

## 2. Vector parity high-pass

Enumerate the odd heights as (h=h_0+2t), extend (v_t) by zero in (t),
and use (\chi_4(h)=\sigma_0(-1)^t). Finiteness gives the exact
Hilbert-space identity

$$
 2\sum_t(-1)^tv_t
 =\sum_t(-1)^t(v_t-v_{t+1}).
\tag{126.D3}
$$

Taking (\sum_t\|v_t-v_{t+1}\|_2), total variation, or an offsetwise norm
is strictly stronger and retains full capacity. The candidate new route is
to estimate the single high spectral coefficient in (126.D3) directly in
(\ell^2_m), before expanding one-count slabs or reciprocal modes.

Equivalently split

$$
 U_1=\sum_{h\equiv1(4)}v_h,\qquad
 U_3=\sum_{h\equiv3(4)}v_h,
\tag{126.D4}
$$

and seek a literal actual-symbol contraction

$$
 \|U_1-U_3\|_2^2\ll_\varepsilon L^2X^\varepsilon.
\tag{126.D5}
$$

The comparison must remain actual-coefficient: arbitrary vectors with
(v_h=\chi_4(h)v) make the left side coherent of size (L^3), while
(v_h=v) can cancel. A coefficient-uniform Bessel statement is false.

## 3. Allowed noninvertible mechanisms

A candidate may use a vector-valued Fourier multiplier in the odd-height
index, a sign-preserving (TT^*) inequality for the complete actual
matrix, an exact product/ray incidence inequality, or a direct spectral
contraction of the two residue-class vectors. It must prove why the actual
(a_{\rm end}(h,m)e(J\sqrt{hm})) avoids the aligned-vector control.

It may not claim gain from:

1. the adjacent phase-preserving dilation or scaled-comb total variation;
2. a fixed-(a) Gram, complex modulus, or blockwise absolute completion;
3. separate offset, lift, reciprocal-mode, or one-count-slab norms;
4. another Poisson/B-process or Hessian rank by itself;
5. random (\chi_4) square-root credit;
6. both orientations followed by an outer (2\Re); or
7. deleting square, Pell, fourth-power, exact-centre, endpoint, collar,
   floor, star, entry, or exit controls without their accepted owner.

## 4. Exact off-diagonal interface

If the energy is expanded, retain the single one-orientation scalar

$$
 \mathcal C_L^{\rm off}
 =\sum_{r\ge1}(-1)^r
 \sum_h\sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}
 e\!\left(-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}\right),
\tag{126.D6}
$$

with both height memberships understood. Primitive factorization gives

$$
 \mathcal C_L^{\rm off}
 =\sum_{\substack{a>0\\a\text{ odd}}}\sum_{q\ge1}(-1)^qF_{L,a}(q),
\tag{126.D7}
$$

but every coprimality, lift, ceiling, reciprocal interval, collar,
entry/exit, floor, star, metric-centre, and one-count tag remains inside
(F_{L,a}(q)).

Round 111 proves that phase-preserving adjacent transport has a bulk comb
commutator of full coefficient-blind capacity. The present gate is lawful
only if it works on the unsplit vector or complete real scalar and does not
take the modulus of that commutator or its slabs.

## 5. Exit test

A positive result must exhibit the full factor (L) from coherent energy
to (126.B14), or a strict complete subrange with its exact capacity. A
negative result must identify the first unavoidable aligned actual-symbol
or resonance seam, without calling a coefficient-blind countermodel a
lower bound for the physical vector.

If neither a target, strict saving, nor stronger inverse localization is
proved, park hard TOP at the exact vector (126.D2), equivalently the
Round-110 one-sided tagged real scalar. Nothing in this packet licenses a
BAL, UNBAL, complete (M9\!-!M2), (M9), or exponent conclusion.
