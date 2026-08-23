# Round 126 conductor adjudication: a sparse square sector closes, parity does not contract

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`

Starting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`

## 1. Adjudicated result

All three reports reproduce the literal Round-75 vector, its diagonal,
one (h<s) orientation, the parity sign, the hard affine intersection,
and the one-sided Round-110 target.  Their common conclusion is decisive:
the proposed parity high-pass is exact but non-saving.

One positive strict sector survives review.  If

$$
 A_L^{\square}(m,h)=1_{hm\text{ is a square}}A_L(m,h),
 qquad A_*=sup_{m,h}|a_{\rm end}(h,m)|,
$$

then uniformly for (|c_h|\le1),

$$
 \|A_L^{\square}c\|_2^2\ll A_*^2L^{3/2},
 qquad
 \|A_L^{\square}\|_{\rm HS}^2\ll A_*^2L\log(2L).
 	ag{126.R1}
$$

This is a genuinely noninvertible projection of the original finite
matrix and has a power margin below (L^2).  It is not the previously
owned primitive condition (ab=\square): (126.R1) concerns individual
entries with (hm=\square) before the energy is expanded.  The legal
reduction is the norm triangle

$$
 \|A_L\chi\|_2
 \le \|A_L^{\square}\chi\|_2
      +\|A_L^{\rm ns}\chi\|_2,
 qquad A_L^{\rm ns}=A_L-A_L^{\square}.
 	ag{126.R2}
$$

No orthogonality and no additive deletion of cross terms is claimed.

The second promotable result is a one-way inverse localization.  If

$$
 \Delta=\mathcal E_L^{\rm top}-\mathcal D_L>0,
$$

then one complete dyadic physical-offset shell carries real signed mass
at least (Delta/O(\log L)).  Partitioning the primitive (q)-labels
directly gives the same conclusion for one complete dyadic (q)-shell.
These are two lawful partitions of the full oriented sum; a physical
(r)-shell does not map to one fixed (q)-shell because (r=gq).
Every internal lift, ceiling, reciprocal interval, collar, floor, star,
metric centre, entry, exit, and one-count slab remains joint.

## 2. Square-sector proof check

Write uniquely (m=du^2) with (d) squarefree.  Then
(hm=\square) if and only if (h=dv^2).  The hard cone gives
(u\le v\le2u), and (u,v\ll\sqrt{L/d}).  Hence

$$
 \begin{aligned}
 \|A_L^{\square}c\|_2^2
 &\le A_*^2\sum_{d\ll L}\sum_{u\ll\sqrt{L/d}}
       \left(\#\{v:u\le v\le2u\}\right)^2\\
 &\ll A_*^2\sum_{d\ll L}(L/d)^{3/2}
 \ll A_*^2L^{3/2}.
 \end{aligned}
 	ag{126.R3}
$$

Counting entries instead gives (A_*^2L\log(2L)).  Floors and the
actual support can only shorten these sets.  The proof does not use the
phase or parity, so it is uniform for the actual vector and every bounded
coefficient control.  Since (A_*\ll_\varepsilon X^\varepsilon), the
usual epsilon renaming makes this target-safe.

## 3. Exact spectral obstruction

For (h=h_0+2t), put (z_t=v_h).  Then

$$
 \mathcal E_L^{\rm top}=\|\widehat z(\pi)\|_2^2,
 qquad
 {1\over2\pi}\int_0^{2\pi}\|\widehat z(\theta)\|_2^2d\theta
 =\mathcal D_L.
 	ag{126.R4}
$$

The difference identity has multiplier
(1-e^{i\theta}), whose modulus at the selected point (pi) is (2).
Thus its selected energy is exactly (4\mathcal E_L^{\rm top}).  More
generally, a height-only convolution with symbol (k(\theta)) either has
(k(\pi)\ne0), in which case its selected coefficient is an invertible
multiple of the target, or has (k(\pi)=0), in which case it deletes the
target and requires a separate estimate.  Finite zero-extension does not
repair the loss: the aligned alternating control retains a Bessel constant
of order (L).

In matrix form, if (V e_h=v_h), (G=V^*V),
(N=|\mathscr H_L|), and (u_\chi=N^{-1/2}\chi), then

$$
 \mathcal E_L^{\rm top}=N\langle Gu_\chi,u_\chi\rangle,
 qquad \mathcal D_L=\operatorname {tr}G.
 	ag{126.R5}
$$

Right multiplication of (V) by
(U_\chi=\operatorname {diag}(\chi_4(h))) is unitary and leaves every
singular value unchanged.  Ambient operator, Schatten, Frobenius, Schur,
and coefficient-uniform Bessel estimates therefore cannot obtain a gain
from inserting the character.  The missing statement is fixed-direction
anti-concentration,

$$
 \langle Gu_\chi,u_\chi\rangle
 \ll_\varepsilon {L^2X^\varepsilon\over N},
 	ag{126.R6}
$$

or the equivalent one-sided physical/completed real scalar.  A relative
version with (operatorname {tr}G/N) is stronger unless a diagonal lower
bound is separately proved, so only the absolute form (126.R6) is retained.

## 4. Sharp false control and resonances

The literal intervals for (h\in[L,2L]) have a common (m)-interval of
length comparable to (L).  The bounded support-adversary
(z_h=\chi_4(h)w) therefore has diagonal capacity (L^2) and parity
energy (L^3).  This proves that the blind factor (L) is optimal under
support, boundedness, parity, and zero extension alone.  It is not a
lower bound for the physical phase vectors.

Square, Pell, strict-metric, and the interior fourth-power families also
defeat any uniform derivative or parity gap.  Their accepted owners or
aggregate cancellation keep the certified pieces target-safe; they do
not prove the complete energy large.  The new (hm=\square) projection
is independently safe by (126.R1), while every nonsquare resonance not
already owned remains in (A_L^{\rm ns}).

## 5. Inverse localization and its limit

Let

$$
 \Gamma_r=(-1)^r\sum_{h,h+2r\in\mathscr H_L}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}
 e\!\left(-{2rJ\sqrt m\over\sqrt h+\sqrt{h+2r}}\right).
$$

Then

$$
 \Delta=2\Re\sum_{r\ge1}\Gamma_r.
$$

There are (O(\log L)) dyadic shells.  Signed pigeonhole therefore
selects one shell with real part at least (Delta/O(\log L)).  More
generally, at any resolution (1\le R\le N_L), one consecutive interval
of at most (R) offsets has real part at least
(R\Delta/(4N_L)).  The conclusion is one-way and conditional on a
positive excess; it proves no bound inside the selected family.

Round 110 compares the completed and physical sums only after global
real summation.  Large bandwise completion errors may cancel globally,
so no selected physical shell is identified with a completed tagged
shell.  The global completed target remains equivalent to the global
physical energy only.

## 6. Strategy and state decision

The August 21 strategy assigned one bounded test to a discrete Poincare
or actual-vector spectral gap.  Round 126 executes that test.  It closes
the sparse (hm=\square) entry sector and proves a useful inverse
localization, but the proposed height-parity mechanism fails at its first
inequality.  The exact survivor is the nonsquare actual vector

$$
 \|A_L^{\rm ns}\chi\|_2^2\ll_\varepsilon L^2X^\varepsilon,
$$

under the norm connector (126.R2), equivalently the original global
one-sided real scalar modulo a target-safe component.  No shellwise
completed connector is available.

Promote the square-entry sector, the height-filter/operator obstruction,
and the one-way complete-offset inverse theorem.  Reject parity-only
contraction, ambient singular-value credit, adjacent total variation,
and any claim that localization estimates the selected band.  Park this
hard-TOP mechanism; no TOP parent, M9-M2 parent, M1 parent, endpoint
uniformity statement, M9 theorem, or exponent changes.
