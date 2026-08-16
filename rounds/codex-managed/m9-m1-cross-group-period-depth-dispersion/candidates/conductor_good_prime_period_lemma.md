# Conductor candidate: good-prime masked-period rigidity and graph bound

Status: Round-88 conductor candidate; independently certified at the
restricted scope below. It becomes accepted mathematics only through the
validated Round-88 State Patch.

## 1. Local rigidity

Let \(q=p^\nu\), where \(p\geq11\), \(p\nmid K\), and let

\[
 \Phi(x)=x^{-1}-(x-A)^{-1}-(x-V)^{-1}
          +(x-V-B)^{-1}
\]

on the nonempty unit mask

\[
 \Omega=\{x\bmod q:p\nmid x(x-A)(x-V)(x-V-B)\}.
\]

Extend \(w(x)=1_\Omega(x)e_q(K\Phi(x))\) by zero. Assume that this
**reciprocal masked weight** (not the total affine phase
\(e_q(ux)w(x)\)) has exact nontrivial period \(p^{\nu-j}\), with
\(1\leq j\leq\nu-1\). Put

\[
 a=\min(j,\nu-j).
\]

Then

\[
 p^a\mid(B-A),\qquad p^a\mid AV,\qquad
 p^a\mid AV(V+B).                                      \tag{C88.3}
\]

Indeed, translation by any multiple of the given period is again a
period. Taking a shift \(p^s\), where
\(s=\nu-a=\max(j,\nu-j)\), gives \(2s\geq\nu\), so inverse Taylor
expansion is exact modulo \(p^\nu\) and yields

\[
 p^a\mid\Phi'(x)\qquad(x\in\Omega).                    \tag{C88.4}
\]

Writing \(\Phi=N/D\), the numerator of \(\Phi'\) has degree at most
five. There are at least \(p-4\geq7\) allowed residue classes. Values
at six of them form a Vandermonde system with \(p\)-adic-unit
determinant, so every coefficient of the derivative numerator is
divisible by \(p^a\). Modulo \(p\), the rational function \(N/D\) has
zero derivative, degrees smaller than \(p\), and limit zero at infinity;
hence \(p\mid N\). Divide by \(p\) and repeat. Thus \(p^a\mid N\)
coefficientwise. Since

\[
 N(x)=(B-A)x^2+2AVx-AV(V+B),
\]

(C88.3) follows.

This proof uses the literal mask. It does not apply to empty masks,
affine cancellation in \(u+K\Phi'\), \(p\leq7\), \(p\mid K\), or the
full \(2\)-part.

## 2. Tensor conductor and graph degree

For the unique maximal reciprocal-mask period vector of a complete
physical \((A,B,V)\)-fibre, define

\[
 \mathfrak a=
 \prod_{\substack{p^\nu\Vert M\\p\geq11,\ p\nmid K}}
 p^{\min(j_p,\nu-j_p)},
\]

where the factor is \(1\) when \(j_p=0\). For a fixed first physical
ordered pair, (C88.3) leaves at most \(q^2/p^a\) partners locally, and
hence at most

\[
 X^\varepsilon {M^2\over\mathfrak a}
\]

partners globally. Swapping the two pairs translates and conjugates the
masked weight, preserving its period depth, so the same estimate is the
in-degree. The divisor-number count of depth vectors is absorbed by
\(X^\varepsilon\).

Remove the already-owned coarse-congruence shells first. For the
remaining directed graph, Schur's inequality, the normalized physical
row bound, and

\[
 \mathcal K_D^\circ=|D_D|^2-D,\qquad
 \|\mathcal K_D^\circ\|_1\leq2D,
\]

give

\[
 \boxed{
 |\mathcal G_{\rm good\ depth}(D)|
 \ll_\varepsilon X^\varepsilon
 DB^3{M^2\over\mathfrak a}T^4Q^{-5/6}.}                \tag{C88.5}
\]

No additional \(M^{-2}\) occurs: it is already present in the product
of the two normalized physical rows.

## 3. Target-safe range

Put

\[
 \rho_*=min\!\left(M,
 \left\lfloor J^{11/30}B^{-2}\right\rfloor\right).
\]

The ratio of (C88.5) to the frozen target
\(X^\varepsilon(D/B)J^{14/5}\) is

\[
 {M^2\over\mathfrak a}B^4J^{-11/15}.
\]

Therefore the complete reciprocal-period fibres satisfying

\[
 \boxed{\mathfrak a\geq M^2/\rho_*^2}                  \tag{C88.6}
\]

are target-safe. This is applied only after the exact coarse-shell
deletion, so overlap can only decrease the directed degrees.

## 4. Exact scope and survivor

The lemma proves no estimate for:

- affine periods of the full phase \(e_q(ux)w(x)\);
- masked accidental periods at \(p=3,5,7\);
- nonunit-\(K\) conductor loss;
- the full \(2\)-adic factor;
- good-prime fibres with \(\mathfrak a<M^2/\rho_*^2\);
- Fourier-projection-only or genuinely aperiodic tensors.

Those pieces remain in the Round-88 hard survivor. In particular,
divisor-lattice inversion of coarse physical groups must not be relabelled
as a classification of every functional period.
