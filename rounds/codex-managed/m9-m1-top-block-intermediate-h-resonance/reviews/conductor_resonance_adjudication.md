# Round 56 conductor adjudication: fixed-fibre resonance averaging fails

## 1. Decision

Promote the exact discrete-curvature interface and a scoped positive-
majorant obstruction. Do not promote the residual-core estimate. All
three reports agree that large continuous curvature must be reduced
modulo the integer lattice and that any nonnegative fixed-
\(h\) closure retains an excessive diagonal. The discovery report also
constructs a strict actual-profile singleton-shell witness; the conductor
independently checked its profile, height, endpoint, and counting seams
against the accepted explicit partition.

## 2. Exact discrete interface

For \(q=4m+\rho\), \(\rho\in\{1,3\}\), put

\[
 F_{h,\rho}(m)=\sqrt{Xh(4m+\rho)}.
\]

Then

\[
 \Delta F_{h,\rho}(m)
 ={4\sqrt{Xh}\over\sqrt{q+4}+\sqrt q},
\]

and

\[
 \Delta^2F_{h,\rho}(m)
 =-{32\sqrt{Xh}\over
 (\sqrt{q+8}+\sqrt{q+4})(\sqrt{q+4}+\sqrt q)
 (\sqrt{q+8}+\sqrt q)}.
\tag{56.1}
\]

On \(hq\asymp Y\), \(Y=R^2\),

\[
 |\Delta^2F|\asymp {h^2\over R},\qquad
 |\Delta^3F|\asymp {h^3\over R^3}.
\tag{56.2}
\]

Over a fixed-
\(h\) fibre of length \(M_h\ll R/h+1\), the curvature drift is
\(O(h^2/R^2)\). Thus the lawful lag-\(r\) resonance is the distance of
the exact accumulated second difference from an integer, with tolerance
\(O(rh^2/R^2)\). The real magnitude \(h^2/R\) is not itself a discrete
nonresonance hypothesis.

## 3. Positive-majorant obstruction

On a dyadic shell \(h\asymp H\), a fixed fibre has
\(M\asymp R/H\) samples. Even ideal cancellation of every off-diagonal
term leaves the Fejer diagonal \(\sqrt M\) per fibre. Summing the
nonnegative fixed-
\(h\) majorants gives

\[
 H\sqrt M=\sqrt{RH},
\tag{56.3}
\]

whereas the unweighted window target is \(\sqrt R\). Hence the route
loses \(\sqrt H\) before any detailed resonance count. It can succeed
only if the signed \(h\)-sum remains coupled.

There is a sharper boundary failure. A fixed residue class has product
spacing \(4h\), so for

\[
 R/4<h\le R/2
\tag{56.4}
\]

it contains at most one sample in a length-
\(R\) window. No discrete curvature or positive lag exists there.

## 4. Actual singleton-shell witness

Let \(K\) run through multiples of \(16\), set

\[
 X=K^4,\qquad Y=K^2,qquad R=K,
\]

and take the length-
\(K\) window

\[
 J_K=[K^2-K/2,K^2+K/2-1].
\]

For every integer \(h\in[3K/8,7K/16]\), the odd multiples of \(h\)
have spacing \(2h<K\), so at least one \(hq\) lies in \(J_K\). Each
individual residue progression has spacing \(4h>K\), hence at most one
sample. Moreover

\[
 {2\sqrt{Xh/q}\over\sqrt X}={2h\over\sqrt{hq}}
 \in[3/4+o(1),7/8+o(1)]\Subset[2/3,1].
\]

The explicit top profile is therefore identically one, all interior
profiles vanish, \(H_0=K>h\), the Vaaler factor is at least
\(\Phi(1/2)=1/2\), and every hard, equality, product, and radial star is
strictly avoided. Consequently

\[
 \sum_{h,\rho}|T_{h,\rho}(J_K)|\gg R
\tag{56.5}
\]

before radial normalization, versus target \(\sqrt R\). This proves a
sharp actual-profile obstruction to taking moduli residue by residue. It
does not lower-bound the signed sum across \(h\) and \(\rho\).

## 5. Perfect-fourth-power scope

At \(X=K^4\), exact-center first derivatives may be integral or half-
integral and the leading quadratic coefficient has small rational
denominator. The blind report shows that the exact integer and
polylogarithmic-denominator leading-quadratic resonance families are
sparse enough to be target-safe up to \(X^\varepsilon\). That audit is a
model statement, not a full cubic-phase theorem. The obstruction (56.3)--
(56.5) is more basic: it is the positive diagonal/boundary capacity.

## 6. Scope and evidence

- Discovery and strict witness: `reports/discrete_curvature_resonance_attack.md`.
- Strict statement-only interface and exponent ledger:
  `reports/blind_resonance_average_rederivation.md`.
- Independent hostile correction of lattice, completion, and support
  seams: `reports/resonance_spacing_hostile_audit.md`.
- Conductor cross-check: explicit plateau and dyadic ownership from
  `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
  Vaaler monotonicity and \(\Phi(1/2)=1/2\) from the accepted source card.
- All three reports have seven sections, no forbidden control bytes, and
  clean diff checks. Work was 100% analytical.

## 7. Next action

The next kernel must keep the two character residue classes and distinct
\(h\)-fibres signed. The most local test is exact adjacent-odd-
\(q\) pairing on the singleton shell, including unmatched endpoints and
the actual amplitude difference. If this fails, formulate the complete
signed short-hyperbola-strip/product-fibre sum rather than another
nonnegative resonance count.

Graph-direction correction: the Round-56 obstruction depends on the
Round-55 low-leg decomposition. The already-proved low-leg lemma does not
depend on its later obstruction. A post-application correction therefore
removes the accidentally reversed dependency edge.
