# Round 86 derivation packet: interior four-Kloosterman ambiguity

This packet is the complete statement-only input for the isolated task.
It records accepted facts, not a requested conclusion.

## 1. Scales and frozen range

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

and work only in

\[
 J^{13/18}<C\leq J^{3/4}.
\]

The target for each dyadic conductor block is

\[
 \mathfrak Y_C\ll_\varepsilon X^\varepsilon {J^2\over T}
 =X^\varepsilon J^{7/5}.
\]

For the three local classes,

\[
 (g,M,K)\in
 \{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},
 \qquad gM=4b,
\]

with \(b\asymp B\). No squarefree or prime modulus hypothesis is
available, and nonzero differences divisible by \(M\) must remain.

## 2. Accepted stationary row and exact survivor

For a fixed compatible class, alias, sign, and reflected orientation, let

\[
 I_b(n)=\int_{\mathbb R}F_b(t)e(-nt/M)\,dt.
\]

The principal stationary profile is supported on an integer interval
\(\mathscr N_b=[N_b^-,N_b^+]\) with

\[
 \Delta_b=N_b^+-N_b^-\asymp Q^2,
 \qquad |I_b(n)|\ll_\varepsilon X^\varepsilon H,
 \qquad H={C\sqrt T\over J}.
\]

Its critical phase is

\[
 -\eta\lambda_b\sqrt{|n|},\qquad
 \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b},
\]

with Gaussian \(e(-\eta/8)\). The complete phase-removed profile has the
accepted normalized smooth hierarchy and sampled bounded variation.

Let

\[
 A_{M,K,d}(n)=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).
\]

Round 84 proves every

\[
 0<|d|\leq D_0:=\lfloor J^{17/30}\rfloor
\]

target-safe. Round 85 proves every

\[
 |d|\geq\Delta_b-E_*,\qquad
 E_*:=\lfloor Q^2J^{-1/20}\rfloor=\lfloor J^{3/4}\rfloor,
\]

target-safe, including entry/exit, stationary errors, wrong signs,
exterior tails, Ramanujan terms, prime-power modes, both signs, and all
orientations. Therefore the exact smooth-principal survivor is

\[
 \boxed{
 \mathfrak Y_{\rm int}={1\over M^2}\sum_{b\asymp B}
 \sum_{D_0<|d|<\Delta_b-E_*}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.}
 \tag{86.1}
\]

Raw Farey-transition errors and axes are separately owned and are not
part of (86.1).

## 3. Exact continuously twisted physical-row identity

For a unit residue \(x\bmod M\), set

\[
 \mathcal R_{b,x}(\theta)
 =\sum_{\ell\in\mathbb Z}F_b(x+M(\ell+\theta)),
 \qquad 0\leq\theta<1.
\]

Poisson summation gives

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta).
 \tag{86.2}
\]

With \(u_b(x)=e_M(K\bar x)\), define

\[
 \mathcal S_b(\theta)=\sum_{x\bmod M}^{*}
 u_b(x)\mathcal R_{b,x}(\theta),
\]

\[
 \mathcal G_b(\theta)=|\mathcal S_b(\theta)|^2
 -\sum_{x\bmod M}^{*}|\mathcal R_{b,x}(\theta)|^2.
\]

Then exactly

\[
 \boxed{
 \mathcal G_b(\theta)={1\over M^2}\sum_{d,n}
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}e(d\theta).}
 \tag{86.3}
\]

The reciprocal-row estimate is uniform in the real shift:

\[
 |\mathcal R_{b,x}(\theta)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
 \tag{86.4}
\]

Thus the inherited energy saving is \(Q^{-5/12}\). For a multiplier
\(w(d)\), (86.3) gives an integral against
\(K_w(\theta)=\sum_dw(d)e(-d\theta)\), but triangle inequality yields
only

\[
 X^\varepsilon\|K_w\|_1{C^3\over TQ^{5/12}},
 \tag{86.5}
\]

with no power of \(B\). A unit-plateau multiplier satisfies
\(\|K_w\|_1\geq1\).

## 4. Exact arithmetic ambiguity identities

Write

\[
 A_{M,K,d}(n)=\sum_{h\ne0}\mathcal C_{M,K}(d,h)e_M(hn).
\]

With

\[
 N_M(h)=\#\{y\bmod M:(y(y+h),M)=1\},
\]

finite orthogonality gives

\[
 \sum_{a\bmod M}|\mathcal C_{M,K}(a,h)|^2=MN_M(h),
 \tag{86.6}
\]

\[
 \sum_{a\bmod M}\mathcal C_{M,K}(a+u,h)
 \overline{\mathcal C_{M,K}(a,h)}
 =Me_M(uh)\sum_{\substack{y\bmod M\\(y(y+h),M)=1}}e_M(uy).
 \tag{86.7}
\]

At \(u\equiv0\pmod M\), (86.7) is the exact self-return
\(MN_M(h)\). For \(p^\nu\Vert M\), local Fourier modes can have size
\(p^{\nu-1/2}=p^{\nu(1-1/(2\nu))}\); no coefficientwise square-root
bound is uniform.

The stationary ambiguity weights

\[
 W_{b,r,d}=\sum_{\ell\in\mathbb Z}
 I_b(r+M\ell+d)\overline{I_b(r+M\ell)}
\]

obey only the formal Parseval interface

\[
 |\mathfrak Y_{E,b}|\ll\sqrt{D/M}
 \left(\sum_{d\in E}\sum_{r\bmod M}|W_{b,r,d}|^2\right)^{1/2}
 \tag{86.8}
\]

for a shell \(|E|\asymp D\). Trivial ambiguity energy cancels the
apparent Parseval gain.

## 5. Literal d-A-process survivor

For a middle-difference interval of length \(D\), put schematically

\[
 Z_b(d)=M^{-2}\sum_nA_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)}.
\]

The exact Fejer/van der Corput inequality with shift height \(U\) retains
its diagonal and prefactor. Opening a nonzero shifted correlation gives

\[
 \sum_d Z_b(d+u)\overline{Z_b(d)}
 =M^{-4}\sum_{d,n,m}
 A_{d+u}(n)\overline{A_d(m)}
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).
 \tag{86.9}
\]

Opening the two \(A\)'s produces a weighted four-Kloosterman main term,
two Ramanujan cross terms, and a Ramanujan-square term. The accepted
diagonal is target-safe. The first unsupported estimate is the
off-diagonal in (86.9), before absolute values, with the complete
\((b,d,u,n,m)\)-dependent stationary symbol.

If one uses only the diagonal and takes \(U\leq M\asymp B\), the maximum
formal gain is \(B^{-1/2}\), which reaches only
\(C\leq J^{56/75}\). Closing the endpoint \(C=J^{3/4}\) requires the
equivalent of \(B^{-5/9}\). Taking \(U>M\) crosses the exact self-return
shifts in (86.7), which must be estimated jointly rather than deleted.

## 6. Required controls

Any positive result must retain:

1. the external \(M^{-2}\) normalization and all three local classes;
2. the physical \(Q^{-5/12}\) energy factor;
3. both signs, reflected orientations, and the exact middle support;
4. nonzero modulus multiples and prime-power gcd modes;
5. Ramanujan cross and square terms exactly once;
6. the Fejer/A-process prefactor and diagonal;
7. entry/exit and stationary errors already routed outside (86.1);
8. exact square/fourth-power phase resonances;
9. complete-transform and \(u=M\) self-return;
10. literal hypotheses of any imported theorem.

The statement-only task must not assume any arbitrary-weight trace bound
or read another Round-86 report.

## 7. Exit gate

Prove (86.1), obtain a fixed power of \(B\), close a nonempty interior
subrange or shell with the full actual symbol, or derive a strictly
smaller exact signed survivor/no-go with its target normalization.

No conclusion is authorized for \(C>J^{3/4}\), raw transitions, axes,
cone edges, other radial sectors, full `M9-M1`, `M9-M2`, `M9`, endpoint
uniformity, `R5-Full`, or the global exponent.
