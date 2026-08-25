# Round 147 terminal source reread

## 1. Result

**GREEN.** The repaired conductor candidate closes every requested source seam. No further correction is required at the exact \(\mathscr K_p\) identity/C24a, fixed-parameter unitary continuation, direct \(z=0\) formula, finite-\(K_F\) convolution, per-\(k\) tail cancellation, or fixed-order promotion boundary.

This green verdict applies only to the fixed-parameter identities and the scoped method obstruction. The growing-complex-order Bessel estimate and signed \(H\)-resonance correlation remain explicitly open, as they should.

## 2. Exact corrected statements

For odd \(p\), the candidate now uses

\[
 \mathscr K_p
 =\frac{1+a+b}{(1+a)(1+b)(1-ab)}
 =1+\frac{a^2b+ab^2+a^2b^2}{(1+a)(1+b)(1-ab)}.
\]

For \(z=c+iv\), it follows on closed sub-half-planes that

\[
 |\mathscr K_p-1|
 \ll p^{-(3\Re w-c)}+p^{-(3\Re w+c)}+p^{-4\Re w},
\]

so \(\mathscr K\) is absolutely convergent, uniformly in \(v\), when

\[
 |c|<\frac12,\qquad \Re w>\frac{1+|c|}{3}.
\]

The fixed-parameter conductor-four identity is stated for every \(|\Re z|<1/4\), with the source theorem used first on \(0<\Re z<1/4\) and the compact-smooth Mellin--Barnes identity continued to the unitary line. It is not claimed to be a growing-order estimate.

## 3. Verification

1. **Exact \(\mathscr K_p\) repair:** pass. Every numerator monomial is mixed in \(a,b\); C24a controls the full remainder rather than only its first formal terms. The condition \(3\Re w-|c|>1\) controls both cubic terms, while \(4\Re w>1\) follows automatically. The \(p=2\) factor is regular because \((1+|c|)/3>|c|\) for \(|c|<1/2\).

2. **Fixed-parameter unitary line:** pass. The candidate distinguishes exact analytic continuation in the parameter from any uniform estimate as \(|\Im z|\) grows. The unitary normalization \(z=i(\tau+t/2)\), radial twist \(s^{-it/2}\), and external constants are retained.

3. **Direct \(z=0\) provenance:** pass. The candidate now attributes C28 to a direct Mellin-functional-equation derivation, not to the strict source strip. Its constants agree: \(A_0=r_2/4\), \(L(1,\chi _4)=\pi/4\), \(\mathscr B_0=J_0\), and the dual scalar is \(\pi\).

4. **Finite physical convolution:** pass. With \(K_F=\lfloor\sup\operatorname{supp}F\rfloor\), C29 keeps \(k\le K_F\), so both the polar and dual sums are finite in the physical convolution. The scalings \(k^{z-1}\) and \(1/k\) in C30 are exact.

5. **Per-\(k\) tail cancellation:** pass. For \(k>K_F\), the primal sum vanishes and the corresponding polar and dual scalars cancel for that same \(k\). The candidate permits an all-\(k\) form only as an iterated identity with those zero pairs inseparable, and records the summable powerful-support tail \(O(K_F^{-1/2+2c+\varepsilon})\) for \(0<c<1/4\).

6. **Promotion boundary:** pass. The candidate promotes only the exact fixed-order coefficient/Euler/Voronoi reduction and fixed-order conductor-four resonance ledger. It expressly withholds the growing-order kernel estimate, the signed correlation, the \(t=1\) target, and every downstream exponent claim.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the repaired seams. The first unproved analytic assertion remains, correctly, the uniform small/transition/large-argument Bessel analysis for the full growing unitary range and moving prefixes. Granting that, the signed powerful-index correlation remains the first missing arithmetic saving.

Neither open problem is silently used in the fixed-order promotion.

## 5. Control outcomes

| Control | Outcome |
|---|---|
| Exact \(\mathscr K_p\) identity and C24a | **GREEN** |
| \(\mathscr K\) convergence domain and \(p=2\) regularity | **GREEN** |
| Fixed-parameter continuation to \(\Re z=0\) | **GREEN** |
| Direct \(z=0\) normalization | **GREEN** |
| Finite \(K_F\) convolution and C30 scaling | **GREEN** |
| Optional all-\(k\) ordering and per-\(k\) cancellation | **GREEN** |
| Fixed-order versus growing-order boundary | **GREEN** |
| Growing-order estimate | **OPEN, correctly excluded** |
| Signed \(H\)-resonance saving | **OPEN, correctly excluded** |

## 6. Dependency

Only the current conductor candidate was reread:

- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md`.

No numerical experiment or additional source claim was introduced.

## 7. Recommended state effect

**Source seam: GREEN.** The corrected fixed-parameter reduction and scoped `squarefree_H_resonance_no_go` are eligible for final conductor adjudication. This review authorizes no growing-order estimate, signed target bound, downstream theorem, proof-draft conclusion, or exponent change.
