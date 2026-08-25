# Round 156 strategy: exact arithmetic of the D=1 theta zero row

## Inherited frontier

Round 155 proves that complete $v\bmod(2N/d)$ resummation exactly inverts
the ambient quadratic Gauss completion. The first source-unproved term is
therefore the literal zero row

$$
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,\widehat B_j(0)K(0,-j;c),
 \qquad q=4N,\quad c=q/d.
\tag{156.S1}
$$

The target is $\mathcal Z_U(V)\ll_{\varepsilon,A}X^\varepsilon$
uniformly for

$$
 M^{3/4}(\log(2X))^A<V\le\sqrt{NM},
\tag{156.S2}
$$

both signs, every odd $d\mid N$, the actual profile, and all endpoints.

## Primary algebraic test

Write $c=4m$, where $m=N/d$. For odd units $a\bmod4m$,

$$
 \epsilon_a=\frac{1+i}{2}+\frac{1-i}{2}\chi_4(a),
 \qquad
 \left(\frac{4m}{a}\right)=\left(\frac ma\right).
\tag{156.S3}
$$

Thus the exact zero-frequency theta sum should first be decomposed as

$$
 \begin{aligned}
 K(0,-j;4m)
 ={}&\frac{1+i}{2}
 \sum_{a\bmod4m}^{*}\left(\frac ma\right)e_{4m}(-aj)\\
 &+\frac{1-i}{2}
 \sum_{a\bmod4m}^{*}\chi_4(a)\left(\frac ma\right)e_{4m}(-aj).
 \end{aligned}
\tag{156.S4}
$$

Equation (156.S4) is only the starting identity. The round must determine
the primitive conductors, induced-modulus factors, exact local support in
$j$, two-adic signs, prime-power values, and interaction with the outer
$d$-sum. No squarefree, odd-$N$, primitive-character, or coprimality
shortcut is licensed.

## Analytical routes

1. Derive the complete local factorization of both additive transforms in
   (156.S4), including principal-character and repeated-prime cases.
2. Decide whether their support forces useful valuations of $j$, whether
   the two character pieces cancel, and how the support changes with $d$.
3. Restore the exact prefactor in (156.S1) before claiming a saving.
4. Sum against the literal
   $\widehat B_j(0)=\sum_xB_j(x)$ without replacing it by a constant.
   Derive every needed $j$-variation, endpoint, or partial-summation norm
   from the actual profile.
5. Test direct interchange of the $j$ and unit sums, induced-character
   Gauss evaluation, Pólya--Vinogradov or Burgess input, conductor
   lowering, divisor switching, and both reciprocal-arc branches.
6. Separate an exact target theorem, a strict owner-complete range, and an
   upper capacity. A large theorem right side is never a signed lower
   bound.

## Orthogonal task design

- A discovery task derives the exact local factors and attacks the
  normalized weighted zero row.
- A statement-only task independently rederives the two-character
  decomposition, all local support conditions, and the sharpest elementary
  weighted partial-sum seam.
- A source task audits primitive and imprimitive quadratic Gauss sums,
  maximal short real-character sums, conductor-lowering, and zero-argument
  Salié or theta formulas against the exact arbitrary-$N$ row.

## Exit gates

Close under exactly one label:

- outer_defect_zero_mode_target;
- strict_outer_defect_zero_mode_range; or
- outer_defect_zero_mode_arithmetic_no_go.

No next round begins before this one is closed. No result transfers to the
nonzero matrix, $D>1$, $L>1$, generic $t=1$, original $t\ge2$, the cross
owner, another M1 or M2 owner, endpoint assembly, M9, the bridge, the
quarter target, or a global exponent without a separate proof.

