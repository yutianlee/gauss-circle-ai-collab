# Conductor candidate: the parity mode survives every height-only spectral filter

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`

Starting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`

Status: exact functional identities and a scoped method no-go.  No
actual-symbol energy estimate or lower bound is claimed.

## 1. Exact spectral presentation

Enumerate the active odd heights as (h=h_0+2t), set

$$
 z_t=v_{h_0+2t}\inell^2_m,
 qquad
 widehat z(\theta)=\sum_tz_te^{-it\theta},
 	ag{126.C1}
$$

and zero extend in (t).  Since
(chi_4(h_0+2t)=\sigma_0(-1)^t),

$$
 \mathcal E_L^{\rm top}=\|\widehat z(\pi)\|_2^2.
 	ag{126.C2}
$$

The nonnegative height spectral density

$$
 F(\theta)=\|\widehat z(\theta)\|_2^2
 	ag{126.C3}
$$

has exact mean

$$
 {1\over2\pi}\int_0^{2\pi}F(\theta),d\theta
 =\sum_t\|z_t\|_2^2=\mathcal D_L\ll L^2.
 	ag{126.C4}
$$

Thus the frozen target is a prescribed-point anti-concentration theorem

$$
 F(\pi)\ll_\varepsilon X^\varepsilon
 {1\over2\pi}\int_0^{2\pi}F(\theta),d\theta.
 	ag{126.C5}
$$

The sharp coefficient-blind comparison is only
(F(\pi)\ll L\mathcal D_L), so (126.C5) must save the full factor
(L) on the literal actual vector.

## 2. Spectral-filter dichotomy

Let (K) be any finite translation-invariant convolution in the
zero-extended height index,

$$
 (Kz)_t=\sum_jc_jz_{t-j},
 qquad k(\theta)=\sum_jc_je^{-ij\theta}.
 	ag{126.C6}
$$

Then exactly

$$
 \widehat{Kz}(\pi)=k(\pi)\widehat z(\pi).
 	ag{126.C7}
$$

There are only two cases.

1. If (k(\pi)\ne0), estimating the selected coefficient after (K)
   is exactly equivalent to estimating the original coefficient, up to
   the fixed factor (|k(\pi)|).  The filter supplies no contraction.
2. If (k(\pi)=0), the filter deletes the target mode.  It cannot control
   that mode without a separate actual-symbol estimate.  On an even
   cyclic interval the sequence (z_t=(-1)^tw) lies exactly in its
   kernel; on a zero-extended interval a fixed-radius filter sees only
   boundary terms while (|\widehat z(\pi)\|=N\|w\|).

The Round-126 high-pass is (K=I-S), so

$$
 k(\theta)=1-e^{i\theta},
 qquad |k(\pi)|=2,
 qquad \|\widehat{Kz}(\pi)\|_2^2=4\mathcal E_L^{\rm top}.
 	ag{126.C8}
$$

It amplifies the selected mode by its maximal multiplier.  Iterated
differences, finite Poincare filters, and height-only spectral
projections obey the same dichotomy.  A lawful continuation must couple
height and (m) through the actual phase and amplitude; a height-only
filter cannot be the source of the missing factor.

## 3. Fixed direction versus ambient spectrum

Let (V e_h=v_h), (G=V^*V), (N=|\mathscr H_L|), and
(u_\chi=N^{-1/2}(\chi_4(h))_h).  Then

$$
 \mathcal E_L^{\rm top}=N\langle Gu_\chi,u_\chi\rangle,
 qquad \mathcal D_L=\operatorname {tr}G.
 	ag{126.C9}
$$

Writing (U_\chi=\operatorname {diag}(\chi_4(h))), the matrices
(V) and (VU_\chi) have identical singular values.  Consequently an
ambient operator, Schatten, Schur, Frobenius, or coefficient-uniform
Bessel estimate is character-blind.  The minimal positive statement is
the fixed-direction bound

$$
 \langle Gu_\chi,u_\chi\rangle
 \ll_\varepsilon {X^\varepsilon\over N}\operatorname {tr}G,
 	ag{126.C10}
$$

on populated blocks.  This is equivalent in scale to the frozen target,
not a consequence of the spectrum alone.

The distinction is sharp under the literal affine supports.  All
intervals attached to odd (h\in[L,2L]) contain the common interval
([\lceil L/2\rceil,\lfloor L\rfloor]).  For any bounded vector (w)
on that interval, the admissible coefficient control

$$
 z_h=\chi_4(h)w
 	ag{126.C11}
$$

has diagonal capacity (N\|w\|_2^2\asymp L^2) and parity energy
(N^2\|w\|_2^2\asymp L^3).  This proves optimality of the blind factor
(N\asymp L), but it is not a lower bound for the physical vectors.

## 4. Exact inverse localization

For the one-orientation physical offsets, put

$$
 \Gamma_r=(-1)^r
 \sum_{h,h+2r\in\mathscr H_L}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}
 e\!\left(-{2rJ\sqrt m\over\sqrt h+\sqrt{h+2r}}\right).
 	ag{126.C12}
$$

Then

$$
 \mathcal E_L^{\rm top}-\mathcal D_L
 =2\Re\sum_{r\ge1}\Gamma_r.
 	ag{126.C13}
$$

There are (O(\log L)) nonempty dyadic (r)-shells.  Hence, if the
left side is (V>0), one complete shell (mathcal R) satisfies

$$
 \Re\sum_{r\in\mathcal R}\Gamma_r
 \ge {V\over O(\log L)}.
 	ag{126.C14}
$$

Unique primitive factorization gives the identical conclusion for one
complete dyadic primitive-(q) family.  Every lift, ceiling, reciprocal
interval, collar, entry, exit, floor, star, metric centre, and one-count
slab remains inside the selected family.  This is a signed pigeonhole
inverse theorem, not a bound.

The Round-110 comparison between the completed scalar and the physical
off-diagonal is global in real part.  It transfers a global violation
above its target-safe error, but supplies no shellwise completed-to-
physical connector.  No completed tagged shell is therefore promoted.

## 5. Resonance and scope

Same-character offsets survive the parity selector with positive sign.
The accepted square-ray theorem makes their complete contribution
target-safe only after its actual reciprocal cancellation; parity alone
does not do so.  Pell and the strict-interior fourth-power control likewise
exclude a uniform phase gap.  These families do not prove a lower bound
for the complete energy, but they forbid random-character or automatic
spectral-gap credit.

The maximal safe conclusion is the filter obstruction (126.C7), the
fixed-direction correction (126.C10), and the inverse localization
(126.C14).  The first open seam remains the literal actual-symbol estimate

$$
 \left\|\sum_h\chi_4(h)v_h\right\|_2^2
 \ll_\varepsilon L^2X^\varepsilon,
 	ag{126.C15}
$$

equivalently the Round-110 one-sided completed real scalar.  No hard-TOP
estimate, M9-M2 parent, M1 parent, endpoint theorem, or exponent follows.
