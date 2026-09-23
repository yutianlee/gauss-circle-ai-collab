# Round 189 strategy: dual height frequency and projective resonance

## Decision

Round 189 keeps the exact Round-188 complement as its sole owner. It
tests one new interface:

\[
 j_q(a,v)=|a\bar v|_q,
 \qquad U=mq,quad q\mid U\mid u,quad (u,v)=1.
\]

The first aim is to prove the complete subpacket

\[
 1\le j_q(a,v)\le \left\lfloor\frac {mq}Y\right\rfloor
 =\left\lfloor\frac UY\right\rfloor
\]

absolutely target-safe by projective residue sparsity. The remainder is
kept exact and signed. Only then may a height or joint \((h,v)\)
argument use the actual endpoint coefficient.

## Power design

At fixed \((\kappa,u,U,m,q,a)\), multiplication and inversion permute
the units modulo \(q\). The slow set occupies at most
\(2\lfloor mq/Y\rfloor\) residue classes of \(v\bmod q\). The literal
\(v\)-range has length \(O(u)\), and \(q\mid u\), so it contains
\(O(um/Y)\) such values. There are \(O(Y)\) heights and
\(O(\kappa)\) live affine sites per oriented row. The resulting factor
\(m\) is cancelled exactly by \(c_U(ma)=m^{-1}c_q(a)\). Since
\(u\kappa\asymp L\), the factor \(Y\) is removed before positivity.
The remaining mass over \(a\) is \(O(\log(2q))\), followed only by
elementary divisor sums over \(mq\mid u\).

## Complementary mechanism

On \(j_q(a,v)>mq/Y=U/Y\), a constant coefficient would admit

\[
 \left|\sum_{h\in I}e(a\bar v h/q)\right|
 \ll \min\{Y,q/j_q(a,v)\}.
\]

Dyadically, projective \(v\)-class volume grows like \(j_q\) while the
Dirichlet bound falls like \(j_q^{-1}\). This balance is unavailable for
an arbitrary bounded amplitude. The reports must prove the required
discrete variation or discrepancy for the literal zero-extended
amplitude, or stop at its first exact jump term and restored deficit.

## Mandatory falsifier

For prime conductor \(p\), \(K_p^\circ(b)=E_p(b)=(-1)^{[b]_p}\).
At \(b=-2\), the first \((p-1)/2\) unit heights have one sign, giving
prefix discrepancy \((p-1)/2\). Thus uniform polylogarithmic height
prefix bounds are forbidden. This is not literal lower mass.

## Interfaces and scope

The discovery task proves the strict sector and attacks the complement;
the hostile task audits multiplicity, powers, centered kernels, bad
slopes, and literal jumps; the statement-only task rederives the result.
No subagent edits proof state. Any graph mutation requires full review,
State Patch validation, and reverse/replay audit.

Success can affect only the original-\(t=1\) high-height residual chain.
It cannot close original \(t\ge2\), the large-\(G\) near-resonant packet,
either M1 parent, any M2 parent, endpoint uniformity, M9, either bridge,
the quarter theorem, or an exponent. Round 190 is the mandatory full-
proof strategy and current-primary-literature checkpoint.
