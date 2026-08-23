# Round 126 blind statement: literal hard-TOP actual-character vector

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`

Starting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`

Status: frozen statement only. No proposed proof or strategy is included.

Let (X\ge2), put

$$
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor.
\tag{126.B1}
$$

Fix one dyadic polynomial intermediate block (1\ll L\ll H). Bounded
blocks and the terminal (L\asymp H) block are excluded as already owned.
Let (\eta_L) be the literal half-open dyadic height profile, let
(\Phi) be the actual Vaaler taper, and let (W) be the actual real
compact endpoint profile. For odd positive (h), define

$$
 a_{\rm end}(h,m)=\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right),
\tag{126.B2}
$$

and extend it by zero away from the literal hard affine range

$$
 \lceil h/4\rceil\le m\le h.
\tag{126.B3}
$$

Let (\mathscr H_L) denote the exact finite odd support of (\eta_L).
For every integer (m), put

$$
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a_{\rm end}(h,m)e(J\sqrt{hm}),
\tag{126.B4}
$$

with zero extension before every change of variables. The scalar hard cone
and its positive transposed energy are

$$
 \mathcal T_L=\sum_mR_m,
 \qquad
 \mathcal E_L^{\rm top}=\sum_m|R_m|^2.
\tag{126.B5}
$$

The exact regrouping and Cauchy inequality are

$$
 \mathcal T_L
 =\sum_{h\in\mathscr H_L}\chi_4(h)
 \sum_{m=\lceil h/4\rceil}^{h}
 a_{\rm end}(h,m)e(J\sqrt{hm})
 =\sum_mR_m,
\tag{126.B6}
$$

$$
 |\mathcal T_L|^2\ll L\mathcal E_L^{\rm top}.
\tag{126.B7}
$$

Expanding the energy and writing the second odd frequency as (h+2r)
gives exactly

$$
 \mathcal E_L^{\rm top}=\mathcal D_L+2\Re\mathcal C_L^{\rm off},
\tag{126.B8}
$$

where

$$
 \mathcal D_L
 =\sum_{h\in\mathscr H_L}
 \sum_{m=\lceil h/4\rceil}^{h}|a_{\rm end}(h,m)|^2
 \ll L^2,
\tag{126.B9}
$$

and

$$
 \begin{aligned}
 \mathcal C_L^{\rm off}
 ={}&\sum_{r\ge1}(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}\\
 &\hspace{12mm}\times
 e\!\left(-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}\right).
 \end{aligned}
\tag{126.B10}
$$

The parity sign is literal:

$$
 \chi_4(h)\chi_4(h+2r)=(-1)^r.
\tag{126.B11}
$$

Use one representative orientation (h<s) and the single outer
(2\Re) in (126.B8). Including both conjugate orientations and then an
outer (2\Re) double counts the off-diagonal.

After all previously proved diagonal, endpoint, collar, original-mode,
square-ray, exact-centre, positive-safe, (q=1), and
prescribed-polylogarithmic owners are removed exactly once, the accepted
completed directional scalar satisfies

$$
 \mathcal E_L^{\rm top}
 =\widetilde{\mathcal E}_{\rm owned,L}
 +2\Re\mathfrak C_{L,{\rm tag}}^{\rm comp},
 \qquad
 |\widetilde{\mathcal E}_{\rm owned,L}|
 \ll_\varepsilon L^2X^\varepsilon,
\tag{126.B12}
$$

and

$$
 \Re\!\left(\mathfrak C_{L,{\rm tag}}^{\rm comp}
 -\mathcal C_L^{\rm off}\right)
 =O_\varepsilon(L^2X^\varepsilon).
\tag{126.B13}
$$

Every tag in (126.B12) retains its half-open scale cell, fixed integer
lattice, open reciprocal interval, terminal metric member, exact-centre
atom, collar, floor, star, equality convention, entry/exit data, and
one-count slab. Only the real part in (126.B13) is accepted.

The frozen target is

$$
 \boxed{\mathcal E_L^{\rm top}
 \ll_\varepsilon L^2X^\varepsilon,}
\tag{126.B14}
$$

equivalently the one-sided upper estimate

$$
 \boxed{\Re\mathfrak C_{L,{\rm tag}}^{\rm comp}
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{126.B15}
$$

Energy positivity supplies the lower real-part bound. Complex modulus,
fixed-(a) Gram, rowwise absolute mass, offsetwise absolute values,
one-count-slab norms, adjacent total variation, and coefficient-uniform
Bessel inequalities are stronger and are not target-equivalent without a
proved connector.

The coefficient-blind coherent capacity of (126.B5) is (L^3), while the
diagonal and target have size (L^2). Thus the actual character/phase
mechanism must save a full energy factor (L). Arbitrary aligned vectors,
random signs, square, Pell, fourth-power, exact-centre, hard-face, and
zero-extension controls are mandatory. No estimate for (126.B14) is
assumed.

Owner scope: the polynomial intermediate hard TOP (M2) vector only.
BAL, UNBAL, complete (M9\!-!M2), every (M1) owner, endpoint
uniformity, (M9), the quarter theorem, and all exponent conclusions are
excluded.
