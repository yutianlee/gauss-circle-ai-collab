# Round 153 barrier packet

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Starting graph: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Parent terminal label: `strict_square_root_character_range`

## Accepted incoming object

Let $R=X^{1/4}$, $N=\lfloor X\rfloor$, and

$$
 1\ll M\le R^2,\qquad M^{449}\ll R^{780}.
$$

The literal $D=d=L=1$ wave has already been reduced to

$$
 P_U^*=\sum_{\substack{\ell=\tau s^2\ \mathrm{retained}\\
 |k(\ell)^2-N\ell|>M^{3/4}\\
 1\le s<\lceil M^{1/4}\rceil}}
 \chi_4(\tau)(\tau s^2)^{-3/4}
 A_U(\tau s^2)e(s\sqrt{N\tau}),
\tag{153.B1}
$$

where $\tau$ is odd squarefree, $s$ is odd, $k(\ell)$ is the unique
nearest integer to $\sqrt{N\ell}$, and $A_U$ is the literal zero-extended
Round-148 profile.  The accepted profile satisfies

$$
 \|A_U\|_\infty+\operatorname {Var}A_U
 \ll_\varepsilon X^\varepsilon.
\tag{153.B2}
$$

The coefficient $B_{1,U}(1)$ remains outside the wave and has
$O_\varepsilon(X^\varepsilon)$ size.

Exact squares, $0<|k^2-N\ell|\le M^{3/4}$, and
$s\ge\lceil M^{1/4}\rceil$ are already target-safe and must not be
reintroduced.  The range $M^{449}\gg R^{780}$ is already owned.

## Exact Mobius interface

For fixed $s$, insert

$$
 \mathbf 1_{\tau\ \mathrm{squarefree}}
 =\mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),
 \qquad \tau=a^2b.
\tag{153.B3}
$$

Every variable is odd, so

$$
 \chi_4(a^2b)=\chi_4(b),
 \qquad
 (a^2bs^2)^{-3/4}=a^{-3/2}b^{-3/4}s^{-3/2},
 \qquad
 e(s\sqrt{Na^2b})=e(as\sqrt{Nb}).
\tag{153.B4}
$$

The exact expanded fixed-$s$ summand is therefore

$$
 \sum_{a,b\ \mathrm{odd}}
 \mu(a)\chi_4(b)(a^2bs^2)^{-3/4}
 A_U(a^2bs^2)e(as\sqrt{Nb})
 \mathbf 1_{\mathcal R_*}(a^2bs^2;s),
\tag{153.B5}
$$

where $\mathbf 1_{\mathcal R_*}$ retains the actual support, endpoint, fixed
external $s$, nearest integer, and strict defect condition in (153.B1).
No triangle inequality across $a$ is part of the identity.

On dyadic blocks $a\asymp A$, $b\asymp B$,

$$
 A^2Bs^2\asymp M,\qquad
 as\sqrt{NB}\asymp\sqrt{NM}.
\tag{153.B6}
$$

The second quantity is independent of $A$ and $s$.  The raw block count
is $AB\asymp M/(As^2)$ and the actual weight is
$M^{-3/4}X^\varepsilon$.  The large-$a$ tail may be priced absolutely,
but the $A=1$ term cannot be isolated and estimated with the old
exponent pair if a new range is claimed.

## Accepted obstructions

1. Adjacent odd pairing retains the full oscillatory phase difference.
2. One legal $A$-process erases the variable character.
3. Mellin/functional-equation and a repeated principal $B$-process
   self-return.
4. The audited global exponent-pair envelope reaches the target exactly
   at $M=R^{780/449}$ and does not prove a lower scale.
5. A mismatched coefficient, complete average, hard-endpoint-free weight,
   or fixed nonlinear-twist parameter is not a theorem for (153.B1).
6. An absolute capacity is not a signed lower bound.

## Compulsory controls

- Keep the $s=1$ layer unless the conclusion is explicitly a strict
  $s$-range theorem.
- Keep every $a$, including $a=1$, and the exact Mobius sign.
- Keep $\chi_4(b)$ after inversion; do not silently erase it before a
  legal positive placement.
- Keep the defect mask, nearest-integer convention, actual support, zero
  extension, transitions, and endpoints at $a^2bs^2$.
- Separate raw count, weighted absolute capacity, a positive energy,
  signed bilinear mass, exact frequency collisions, and near-collision
  counts.
- If Cauchy is used, record which arithmetic coefficient survives and
  price the diagonal and pigeonhole multiplicity at every $A,B,s$.
- Treat computation only as falsification or pattern-finding evidence.
- Do not promote any $D>1$, $L>1$, generic, original $t\ge2$, cross,
  M1/M2, endpoint, M9, bridge, target, or exponent statement.

## Required outcome

Prove $|P_U^*|\ll_\varepsilon X^\varepsilon$, prove a strict
owner-complete subrange, or isolate the first exact Mobius-coupling,
Type-I/Type-II, spacing, diagonal, endpoint, or source obstruction with
complete $R,M,A,B,s$ powers.
