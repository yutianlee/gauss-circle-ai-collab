# Conductor Round 115 prechecks

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

Evidence level: exact algebra and strategy control only. No estimate for
the double-far energy is asserted.

## 1. Literal charts

For

\[
 C_B(n,r)=
 \sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')},
\]

substitution of the divisors gives

\[
 hk'-h'k
 ={h(n+r)\over h'}-{h'n\over h}
 ={h^2(n+r)-h'^2n\over hh'}.
\]

With \(h'=h+p\), \(k'=k+q\),

\[
 r=hq+kp+pq,\qquad \rho=hq-kp,
\]

\[
 r+\rho=q(2h+p),\qquad r-\rho=p(2k+q).
\]

Nonzero character factors force \(h,h'\) odd and therefore \(p\) even.
For such atoms,

\[
 \chi_4(h)\chi_4(h+p)=(-1)^{p/2}.
\]

Thus at a fixed even \(p\) the character is a constant sign. Any proposed
cancellation in the \(h\)-sum at fixed \(p\) is a false character shadow;
the only immediate alternating mechanism is across the \(p\)-sum itself.

Writing \(p=2s\) turns that sign into \(e(s/2)\). Poisson summation in the
shift therefore displaces the dual stationarity condition by a
half-integer; it does not remove the many nonzero stationary modes. For
the phase in the second atom the condition has the form

\[
 R\sqrt{{k+q\over h+2s}}\equiv {1\over2}\pmod{\mathbb Z}.
\]

Consequently “the character kills the zero mode” is not enough: a proof
must estimate the complete displaced dual family. Treating zero-mode
vanishing as cancellation of the whole shift sum would be another
invertible-transform error.

For the fixed-increment phase

\[
 F_{p,q}(x,y)=\sqrt{(x+p)(y+q)}-\sqrt{xy},
\]

direct differentiation gives

\[
 \det \nabla^2F_{p,q}(x,y)
 =
 -{\sqrt{xy}\sqrt{(x+p)(y+q)}(qx-py)^2
 \over
 16x^2(x+p)^2y^2(y+q)^2}.
\]

Hence on the critical support

\[
 \bigl|\det\nabla^2(RF_{p,q})\bigr|\asymp \rho^2.
\]

This proves real two-dimensional nondegeneracy on the determinant-far
branch. It does not prove lattice cancellation: a Poisson transform sees
all integer gradients, and the number and phases of the dual stationary
points must still be controlled. Treating the determinant magnitude as
modulo-one separation would repeat a rejected Round-114 shadow.

There is also an exact radial-angular chart. Put

\[
 t=\log {h\over\sqrt n},\qquad
 t'=\log {h'\over\sqrt{n+r}}.
\]

Then

\[
 \rho=2\sqrt{n(n+r)}\sinh(t-t').
\]

On balanced support the determinant-far gate is therefore angular
divisor-ratio separation \(|t-t'|\gg L^{-1}\), whereas the outer phase
depends only on the radial variables \(n,n+r\). This makes precise why
angular separation is not itself phase oscillation.

## 2. Critical outer B-process scale

For \(f(t)=R\sqrt t\),

\[
 f'(t)={R\over2\sqrt t},\qquad
 f''(t)=-{R\over4t^{3/2}}.
\]

At \(t\asymp L^2\) and \(R\asymp L^3\),

\[
 f'(t)\asymp L^2,\qquad |f''(t)|\asymp1.
\]

The stationary equation for the Poisson frequency \(m\) is

\[
 m={R\over2\sqrt t},\qquad
 t={X\over4m^2},
\]

and the Legendre phase is

\[
 f(t)-mt={X\over4m}.
\]

The dual frequencies again occupy a range of length comparable to \(L^2\),
and the stationary amplitude has no positive power of \(L\). Therefore a
plain one-variable outer Poisson/B-process is critical and
capacity-preserving. Applied separately to \(n\) and \(n+r\), it returns a
two-variable reciprocal-phase object of the same raw capacity. This is a
scale obstruction to claiming a saving from the transform alone; it is not
a lower bound for the actual signed sum.

## 3. Primary-source fit controls

Alex Cowan, A twisted additive divisor problem,
https://arxiv.org/abs/2304.12572, studies complete generalized divisor
coefficients with nonzero complex powers and nontrivial characters under
the hypotheses of its Theorem 1.1. The published theorem also requires the
product of the two characters to be nontrivial. The Round-115
self-correlation has zero powers and
\(\chi_4\chi_4\) principal. It additionally has balanced divisor
truncations, a nonseparable slanted weight, determinant deletion, and an
outer nonlinear phase with varying shift. Hence Cowan's stated theorem is
not a literal antecedent.

Fernando Chamizo, The Additive Problem for the Number of Representations
as a Sum of Two Squares,
https://doi.org/10.1007/s00009-021-01959-3, proves an asymptotic and
uniform-shift error estimates for the complete correlation
\(\sum_{n\le x}r_2(n)r_2(n+m)\). Its Theorem 1.1 contains an explicit
nonzero main term. This verifies that the complete
\((1*\chi_4)\)-self-correlation is not generically main-term-free.
However, the theorem does not state the Round-115 balanced divisor
truncation, determinant deletion, coupled oscillatory weight, or a
simultaneous signed sum over all shifts. It is a source analogue and a
main-term warning, not an applicable estimate.

There is also a capacity mismatch even under an optimistic formal
completion. In Chamizo's hardest \(m\asymp x\) range, the unconditional
error is \(O_\varepsilon(x^{17/23+\varepsilon})\). Here
\(x\asymp L^2\), and there are \(O(L^2)=O(x)\) shifts. A triangle sum of
those errors has size

\[
 x^{40/23+\varepsilon}
 =L^{80/23+\varepsilon},
\]

whereas the Round-115 budget is

\[
 L^3=x^{3/2}.
\]

The deficit is \(x^{11/46}=L^{11/23}\). Thus even a hypothetical
literal-weight extension of the fixed-shift theorem would still need an
average or signed saving across shifts; fixed-shift asymptotics followed by
the triangle inequality cannot close the target.

## 4. Exit test

A spectral or dispersion proposal passes only if it:

1. derives the literal incomplete coefficient rather than replacing it by
   \(r_2\);
2. computes the principal-product constant term;
3. supplies uniform control for the derivative/conductor of the coupled
   oscillatory weight;
4. sums the full shift range without paying an \(L^2\) triangle cost; and
5. retains the determinant deletion or restores its target-safe corridor
   exactly once.

Failure of any one item is a theorem-fit no-go, not a proof that the actual
double-far energy is large.
