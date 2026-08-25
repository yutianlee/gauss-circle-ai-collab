# Statement-only packet: balanced signed cluster-defect kernel

## Frozen problem

Let \(X\ge 2\), \(R=\sqrt X\), and \(L\asymp X^{1/6}\). Consider one
fixed smooth balanced physical block. Its already-isolated interior bulk
kernel is

\[
 \mathcal K_B^{\rm bulk}
 =
 \sum_{\substack{h\ {\rm odd},\ k,k'}} b_B(h,k)
 \sum_{\substack{d\mid k'\\ d\ {\rm odd}}}\gamma_d
 \sum_J
 \sum_{\substack{\mu\in\mathbb Z+1/2,\ \mu>0\\t_*\in J}}^{\rm bulk}
 \mathcal A_{d,J}(h,k,k';\mu)e(\Theta_{d,\mu}).
\tag{136.B1}
\]

The outer support contains \(O(L^3)\) triples \((h,k,k')\), with all
variables in fixed dyadic intervals of their natural balanced scales.
The literal smooth coefficient \(b_B\) contains a slanted profile and
the first low-gcd weight. The second low-gcd weight has the signed divisor
expansion \(\sum_{d\mid k'}\gamma_d\), with
\(\sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon\).

## Divisor progression and phase

Write

\[
 h'=h+2s=d(\ell_d+2t),\qquad
 s=s_d+dt,\qquad h+2s_d=d\ell_d,
\tag{136.B2}
\]

where \(d\) is odd and \(s_d\pmod d\) is fixed. Put

\[
 \mu=\tfrac12-m\in\mathbb Z+\tfrac12,qquad
 \lambda={\mu\over d},\qquad
 q=k'-k,qquad
 x_*={Xk'\over\lambda^2}.
\tag{136.B3}
\]

The stationary phase is exactly

\[
 \begin{aligned}
 \Theta_{d,\mu}
 &=R\sqrt{hk}-{Xk'\over2\lambda}
   -{\lambda h\over2}+s_d(\tfrac12-\lambda)\\
 &=-{h(\lambda-\lambda_0)^2\over2\lambda}
   -{Xq\over2\lambda}+s_d(\tfrac12-\lambda),
 \qquad \lambda_0=R\sqrt{k/h}.
 \end{aligned}
\tag{136.B4}
\]

On the bulk stationary range,

\[
 \mu\asymp dL^3,qquad
 \#\{\mu:t_*\in J\}\asymp dL^3,qquad
 |\mathcal A_{d,J}|\ll(dL)^{-1}.
\tag{136.B5}
\]

Distinct lifts \((d,\mu)\) are distinct even when they give the same
rational \(\lambda\), because \(\gamma_d\), \(s_d\), the progression,
and the literal amplitudes depend on \(d\).

## Coupled far gates

With

\[
 \lambda_r={Rk'\over\sqrt{hk}},
\]

the two determinant coordinates at \(x_*\) are

\[
 \rho=hk'-x_*k
 ={hk'\over\lambda^2}(\lambda^2-\lambda_0^2),
\qquad
 \Delta=x_*k'-hk
 ={hk\over\lambda^2}(\lambda_r^2-\lambda^2).
\tag{136.B6}
\]

Every term in (136.B1) obeys both strict gates
\(|\rho|>L\) and \(|\Delta|>L\), together with the exact relation
\(\Delta+\rho=q(h+x_*)\). The interval label \(J\) retains the literal
support and both gates. Gate crossings and incomplete stationary modes are
not part of the bulk.

## What is already controlled

All finite-Poisson boundary tails, nonstationary modes, support crossings,
gate transitions, and stationary remainders have total size
\(O_\varepsilon(L^3X^\varepsilon)\). The phase-free mode is also
\(O_\varepsilon(L^3X^\varepsilon)\), but only after the full signed
assembly. Thus the sole target in this packet is

\[
 \boxed{
 |\mathcal K_B^{\rm bulk}|
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{136.B7}
\]

The following standalone mechanisms are unavailable: aliaswise absolute
values, merging equal rational \(\lambda\), reciprocal-frequency
counting in one variable, coefficient-uniform spacing large sieves followed
by outer positive norms, a second one-variable B-process, and treating a
positive row Gram as equivalent to (136.B7).

## Required analysis

Construct an explicit broad--narrow partition using joint phase gradients,
slopes, or rational-cluster data at a stated resolution. For the broad
part, prove and price a determinant/transversality inequality. For every
narrow class, identify the literal arithmetic ruling in
\((d,\mu,h,k,k')\) and either exploit the actual \(\chi_4\) and residue
phase \(s_d(1/2-\lambda)\), or exhibit a lawful coherent packet showing
why the proposed closure fails.

Test at least same-lift, equal-rational-\(\lambda\), same-denominator,
phase-adapted, opposite-character, and gate-boundary configurations.
Preserve the fixed block, both low-gcd weights, slanted profiles, both
gates, and every literal sign. Close with a proof of (136.B7), a strictly
smaller exact survivor, or the first exact broad/narrow obstruction.
