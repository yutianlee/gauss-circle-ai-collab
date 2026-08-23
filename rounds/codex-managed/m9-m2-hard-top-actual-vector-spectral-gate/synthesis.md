# Round 126 synthesis: the parity high-pass selects rather than contracts

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`

Starting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`

## Frozen objective

The round tested whether the literal hard-TOP vector

$$
 R_m=\sum_{h\in\mathscr H_L,,m\le h\le4m}
 \chi_4(h)a_{\rm end}(h,m)e(\sqrt{Xhm})
$$

admits a genuinely noninvertible parity spectral/operator estimate at
diagonal energy scale,

$$
 \mathcal E_L^{\rm top}=\sum_m|R_m|^2
 \ll_\varepsilon L^2X^\varepsilon.
 	ag{126.1}
$$

All three reports retain the exact hard affine support, zero extension,
character before squaring, one (h<s) orientation, one outer (2\Re),
and every prior owner.

## One strict sector is target-safe

Let (A_L) be the literal (m\)-by-(h) matrix and insert the arithmetic
entry projection

$$
 A_L^{\square}(m,h)=1_{hm\text{ is a square}}A_L(m,h).
$$

Writing (m=du^2) with (d) squarefree forces (h=dv^2); the hard
support gives (u\le v\le2u).  Direct counting proves, uniformly for
(|c_h|\le1),

$$
 \boxed{\|A_L^{\square}c\|_2^2\ll_\varepsilon L^{3/2}X^\varepsilon,}
 	ag{126.2}
$$

and

$$
 \|A_L^{\square}\|_{\rm HS}^2
 \ll_\varepsilon L\log(2L)X^\varepsilon.
 	ag{126.3}
$$

This is a complete noninvertible actual-matrix sector with a power margin.
It is distinct from the prior primitive (ab=\square) off-diagonal
owner.  It is removed only through

$$
 \|A_L\chi\|_2
 \le \|A_L^{\square}\chi\|_2
      +\|A_L^{\rm ns}\chi\|_2,
 	ag{126.4}
$$

not through a false orthogonal energy split.

## Parity is a prescribed spectral coefficient

For (h=h_0+2t), put (z_t=v_h).  Then exactly

$$
 \mathcal E_L^{\rm top}=\|\widehat z(\pi)\|_2^2,
 qquad
 {1\over2\pi}\int_0^{2\pi}\|\widehat z(\theta)\|_2^2d\theta
 =\mathcal D_L\ll L^2.
 	ag{126.5}
$$

The high-pass identity

$$
 2\sum_t(-1)^tz_t=\sum_t(-1)^t(z_t-z_{t+1})
$$

has multiplier (1-e^{i\theta}), of maximal modulus (2) at
(\theta=\pi).  It therefore changes the selected energy into exactly
(4\mathcal E_L^{\rm top}); it supplies no contraction.  Any finite
height-only spectral filter either has nonzero multiplier at (pi) and
is invertible on the target mode, or kills that mode and needs a separate
estimate for it.

The support-sharp adversary (z_h=\chi_4(h)w) on the common hard-cone
interior has diagonal capacity (L^2) and parity energy (L^3).  It is
not a physical lower bound, but it proves that support, boundedness,
parity, positivity, and zero extension alone retain the entire missing
factor (L).

## Ambient operator bounds are character-blind

With (V e_h=v_h), (G=V^*V), (N=|\mathscr H_L|), and
(u_\chi=N^{-1/2}\chi),

$$
 \mathcal E_L^{\rm top}=N\langle Gu_\chi,u_\chi\rangle,
 qquad \mathcal D_L=\operatorname {tr}G.
 	ag{126.6}
$$

Column multiplication by
(\operatorname {diag}(\chi_4(h))) is unitary and leaves all singular
values unchanged.  Hence an operator, Schatten, Frobenius, Schur, or
coefficient-uniform Bessel estimate cannot exploit character insertion.
The missing theorem is the fixed actual-direction bound

$$
 \langle Gu_\chi,u_\chi\rangle
 \ll_\varepsilon {L^2X^\varepsilon\over N},
 	ag{126.7}
$$

equivalently the Round-110 one-sided real scalar.  No report proves it.

## Positive violations localize, but do not contract

Let (Gamma_r) be the complete one-orientation signed physical offset,
including the factor ((-1)^r).  Then

$$
 \mathcal E_L^{\rm top}-\mathcal D_L
 =2\Re\sum_{r\ge1}\Gamma_r.
 	ag{126.8}
$$

If the left side is (Delta>0), signed pigeonhole gives one complete
dyadic (r)-shell with real part at least
(Delta/O(\log L)).  Partitioning the primitive labels directly gives
one complete dyadic (q)-shell with the same logarithmic loss.  At any
resolution (R\le N_L), one consecutive interval of at most (R)
physical offsets carries at least (R\Delta/(4N_L)).  All one-count
slabs and literal tags remain joint.

This is a quantitative inverse localization, not a bound on the selected
shell.  Round 110 supplies only a global completed-to-physical real-part
comparison, so a selected physical shell cannot be identified with one
completed tagged shell without a new connector.

## Decision and full-proof status

Promote (126.2)--(126.4), the parity-filter/operator obstruction, and the
one-way complete-offset inverse theorem.  Reject an automatic high-pass
gain, ambient singular-value credit, coefficient-blind Bessel contraction,
slabwise absolute values, and the claim that localization proves the
selected band.

The square-entry sector is closed, but the nonsquare actual-vector
complement and the equivalent global one-sided completed real scalar
remain open.  This parity-spectral mechanism is parked under the August
21 stop rule.

Hard TOP therefore remains open.  BAL, every UNBAL owner, complete
M9-M2, both direct M1 parents, the lower GAR alternative, endpoint
uniformity, M9, and the quarter theorem also remain open.  The strongest
internally proved global exponent is still (1/3); the audited external
benchmark remains

$$
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
$$

Round 126 proves no exponent improvement.

Resulting graph SHA-256:
`fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`.
