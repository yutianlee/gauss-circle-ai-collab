# Round 153 strategy: squarefree-kernel bilinear gate

- Starting graph: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Parent result: Round 152 strict arithmetic pruning and $BD$ range
- Allocation: 100% analytical, algebraic, and primary-source work; 0% numerical

## Selected interface

Round 152 reduces the remaining $D=d=L=1$ wave below
$M^{449}\asymp R^{780}$ to

$$
 P_U^*=\sum_{\substack{\ell=\tau s^2\ \mathrm{retained}\\
 |k(\ell)^2-N\ell|>M^{3/4}\\
 1\le s<\lceil M^{1/4}\rceil}}
 \chi_4(\tau)(\tau s^2)^{-3/4}
 A_U(\tau s^2)e(s\sqrt{N\tau}),
$$

where $\tau$ is odd squarefree and the $s=1$ layer is compulsory.  The
new round tests one genuinely different interface: preserve the squarefree
coefficient through exact Mobius inversion and seek a two-variable signed
estimate before any triangle inequality separates the inversion variable.

For fixed $s$, insert

$$
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),\qquad \tau=a^2b.
$$

Since $a$ is odd,

$$
 \chi_4(a^2b)=\chi_4(b),\qquad
 e(s\sqrt{Na^2b})=e(as\sqrt{Nb}).
$$

Thus the exact fixed-$s$ survivor becomes a signed bilinear family with

$$
 a^2bs^2\asymp M,qquad
 A^2Bs^2\asymp M,qquad
 \Phi(a,b)=as\sqrt{Nb}.
$$

The rescaled oscillatory parameter
$as\sqrt{NB}\asymp\sqrt{NM}$ is independent of the dyadic $A$ and $s$.
This invariance is useful, but it also warns that bounding each $a$ block
separately merely returns the Round-152 exponent-pair boundary.  The
$a=1$ term cannot be discarded, and cancellation among Mobius-inversion
terms must remain visible.

## Required proof target

Prove

$$
 |P_U^*|\ll_\varepsilon X^\varepsilon
$$

through a literal coefficient-sensitive bilinear inequality, prove a new
owner-complete subrange, or isolate the first exact Type-I/Type-II,
spacing, diagonal, endpoint, or source obstruction.  A valid partial
result must still include the $s=1$ layer or explicitly state which
strict $s$ range it owns.

## Interfaces that must be priced

1. **Exact inversion.** Retain every odd $a$, including $a=1$, the Mobius
   sign, the exact finite support, the large-defect mask evaluated at
   $a^2bs^2$, and all actual-profile endpoints.
2. **Dyadic geometry.** Record $A^2Bs^2\asymp M$, the raw term count,
   actual $M^{-3/4}$ weight, and the large-$a$ absolute tail before any
   Type-I/Type-II claim.
3. **Cauchy placement.** If Cauchy is applied in $a$ or $b$, write the
   exact surviving coefficient and correlation phase.  Do not replace a
   signed correlation by an absolute spacing energy without pricing the
   resulting pigeonhole diagonal.
4. **Frequency spacing.** The phase is linear in $a$ and square-root in
   $b$.  Classify exact collisions
   $s\sqrt N(\sqrt{b_1}-\sqrt{b_2})\in\mathbb Z$, near collisions modulo
   one, and the relation to $Nb_i$ being squares.
5. **Short-divisor seam.** Any dyadic treatment that separately bounds
   the $A=1$ block inherits the old exponent-pair loss.  A claimed gain
   must explain how the complete Mobius sum couples that block to the
   remaining $a$ values.
6. **Source hypotheses.** Audit bilinear square-root exponential sums,
   Mobius/character bilinear forms, squarefree nonlinear twists, and
   double-large-sieve or spacing theorems against the literal coefficient,
   variable ranges, phase, mask, weight, and endpoint class.

## Frozen routes

- Do not iterate the principal $B$-process or the degree-one functional
  equation as a gain.
- Do not reuse an exponent pair below its exact $M^{449}=R^{780}$
  boundary.
- Do not sum Mobius-inversion blocks by absolute values and call the
  resulting loss an obstruction to the signed sum.
- Do not infer a large-sieve diagonal scale when the frequency family has
  more points than the sampling length without retaining the character or
  proving the required spacing estimate.
- Do not call a raw capacity or a coherent model a signed lower bound.

## Round design

Use three orthogonal tasks:

1. a selected-context derivation of the exact inversion, dyadic
   Type-I/Type-II ledger, and strongest legal bilinear attack;
2. a statement-only feasibility analysis of the squarefree-kernel
   bilinear sum and its unavoidable short-divisor/spacing seam; and
3. a primary-source audit of bilinear square-root, Mobius, squarefree
   nonlinear-twist, and spacing inputs.

Close under exactly one of:

- `squarefree_kernel_bilinear_target`;
- `strict_squarefree_kernel_bilinear_range`;
- `squarefree_kernel_bilinear_no_go`.
