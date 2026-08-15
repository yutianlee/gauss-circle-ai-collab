# Conductor proposal: define the common kernel after endpoint collapse

Campaign: `m9-m1-beta-complete-physical-height-symbol`  
Role: conductor reduced-kernel derivation  
Allocation: 100% analytical/algebraic

## 1. Boundary modules are already closed in the physical limit

The authoritative graph proves:

- the finite endpoint Cauchy identity
  \(T_\xi+S_\xi+P_\xi=D_\xi-A_\xi\);
- the lower endpoint is target-safe;
- the physical upper endpoint prefix is target-safe by \(\chi_4\)-Abel;
- the recombined physical \(R_1\) arithmetic residue is target-safe.

These statements are not uniform arbitrary-finite-top-height estimates.
Therefore they license endpoint removal only in the declared symmetric
physical-profile limit, not pointwise deletion inside an arbitrary finite
box.

## 2. Side-collapsed common kernel

At finite heights first keep the exact endpoint Cauchy identity. After the
accepted nested order of physical limits, assign \(D_1,D_N\) and the
recombined arithmetic residue to their proved modules. Let
\(\mathcal V_{\rm nonend}\) denote the surviving beta vertical plus
Cauchy--Green connector with those modules removed once.

Apply the exact omega recombination inside \(\mathcal V_{\rm nonend}\),
then take the signed top Plemelj limit with identical masks and domains, and
subtract one combined diagonal/log term. The resulting integrand is the
proposed reduced common kernel

\[
 K_{\rm red}(L,\nu)=\operatorname {Reg}_{\mu=0}
 \Big[\mathcal V_{\rm nonend}
 \{\omega G+(1-\omega)R_1-\omega E_1\}\Big]_{\mu=L-\nu}. \tag{32.C3}
\]

This formula is an ownership definition; an explicit analytic expression
still requires inserting the accepted finite vector integrand and doing the
same endpoint collapse on each beta share.

## 3. Correct target

The local symbol target should be imposed on \(K_{\rm red}\), not on the
full side-bearing boundary operator:

\[
 |K_{\rm red}(L,\nu)|\ll X^\varepsilon\lambda^{-2}w_b(\nu),
 \qquad
 |\partial_LK_{\rm red}(L,\nu)|
 \ll X^\varepsilon\lambda^{-3}w_b(\nu).             \tag{32.C4}
\]

The axial \(v=0\) residue stays outside \(K_{\rm red}\) until its separate
ledger is reconciled. The constants in (32.C4) need only be polylogarithmic
for \(b=1/\log(2X)\).

## 4. Remaining seam

The graph does not yet contain an exact identity showing that the beta
transition's finite radial sides and endpoint shares match the already
closed endpoint modules under precisely the same beta mask and
Cauchy--Green connector. Round 32 must prove this mask-compatible transfer.
Without it, (32.C3) is a candidate ownership convention, not accepted
algebra.

If the transfer is proved, radial-side exhaustion ceases to be part of the
local BV estimate; the remaining hard step is (32.C4) plus the axial limit.
If it fails because the beta mask leaves an unclosed endpoint share, that
masked boundary operator is the next exact survivor.
