# Round 46 frozen derivation packet

This packet states the exact positive-line complement and the required
partition. It is a statement packet, not a proof. A statement-only task
may use only this packet and its brief.

## 1. Positive-line antecedent

Round 45 leaves the direct endpoint-free beta terminal after all global
endpoint, radial-side, arithmetic, artificial, axial, connector-axis,
collision, and corner modules are owned once. On

\[
 u=a+i(L-\nu),\quad v=b+i\nu,\quad
 s=\frac54+i\left(\frac L2+\beta\right),
\]

put

\[
 \alpha=L+\beta,\qquad
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j},qquad
 A=-1-\frac b2-i\alpha,qquad
 D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
\]

The complete direct complement is obtained by multiplying the same
positive-line terminal by \(1-\chi _0(\alpha)\). The central terminal and
both artificial residue shares are already closed and must not be
reinserted.

For one spatial share the exact raw terminal numerator is

\[
\begin{aligned}
 \mathscr H^{\rm raw}(L,\nu)={}&
 \mathfrak a_{j,h,q,x}\,c_{\sigma,\zeta}R_\beta(\beta)
 \psi(\beta)e^{-i\beta\log(hqx)}\\
 &\times R_\alpha(\alpha)e^{i\omega_LL}
 \{\widehat\phi(b+i\nu)e^{i\omega_\nu\nu}\}
 W_j(L-\nu),                                      \tag{46.1}
\end{aligned}
\]

where

\[
 \omega_L=\log\frac{D_j}{2\sqrt X}-\log q-\frac12\log x,
\quad
 \omega_\nu=-\log\frac{D_j}{2\sqrt X}
 +\log(H_j+1)-\frac12\log x,                     \tag{46.2}
\]

\[
 \mathfrak a_{j,h,q,x}=(-\pi i\sqrt X)e(\sqrt{Xx})
 h^{-r}q^{-p}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 x^{-3/2-b/2}.                                    \tag{46.3}
\]

For the singular \(j=0\) share, \(W_0=1\) after signed Plemelj; the
regular top and \(j\ge1\) shares retain their rapidly decreasing Mellin
profiles. Floors, stars, equality restrictions, \(\chi _4(q)\), contour
constants, and the external physical operator remain attached once.

## 2. Required finite partition

Choose fixed smooth functions \(\vartheta_0,\vartheta_1\) on
\([0,\infty)\) such that

\[
 \vartheta_0(t)=1\ (t\le1/2),\qquad
 \vartheta_0(t)=0\ (t\ge3/4),
\]

\[
 \vartheta_1(t)=1\ (3/4\le t\le4/3),\qquad
 \vartheta_1(t)=0\ (t\le2/3\text{ or }t\ge3/2).
\]

First form normalized nonnegative weights

\[
 b_0(t)=\vartheta_0(t),\qquad b_1(t)=\vartheta_1(t),\qquad
 b_\infty(t)=1,
\]

\[
 \widetilde\vartheta_k(t)=
 \frac{b_k(t)}{b_0(t)+b_1(t)+b_\infty(t)}
 \quad(k\in\{0,1,\infty\}).                       \tag{46.4}
\]

Then \(0\le\widetilde\vartheta_k\le1\), the denominator is at least one,
all derivatives are uniformly bounded, and
\(\sum_k\widetilde\vartheta_k=1\). Refine the middle weight by a fixed
finite signed saddle/entry/exit partition subordinate to
\(2/3<|\alpha|/\lambda<3/2\); its pieces add back to
\(\widetilde\vartheta_1\).

Define, separately on \(\alpha>0\) and \(\alpha<0\),

\[
 \eta_{\pm,0}(\alpha,\lambda)
 =(1-\chi _0(\alpha))\mathbf1_{\pm\alpha>0}
 \widetilde\vartheta_0(|\alpha|/\lambda),          \tag{46.5}
\]

\[
 \eta_{\pm,1}(\alpha,\lambda)
 =(1-\chi _0(\alpha))\mathbf1_{\pm\alpha>0}
 \widetilde\vartheta_1(|\alpha|/\lambda),          \tag{46.6}
\]

and

\[
 \eta_{\pm,\infty}(\alpha,\lambda)
 =(1-\chi _0(\alpha))\mathbf1_{\pm\alpha>0}
 \widetilde\vartheta_\infty(|\alpha|/\lambda).     \tag{46.7}
\]

Replace the half-line indicators near zero by a fixed smooth signed
partition subordinate to the region where \(1-\chi _0=0\), so every
multiplier is smooth. Then

\[
 \sum_{\sigma=\pm}\sum_{k\in\{0,1,\infty\}}
 \eta_{\sigma,k}(\alpha,\lambda)=1-\chi _0(\alpha) \tag{46.8}
\]

pointwise. The refined \(k=1\) cells are proposed as the signed
saddle/entry/exit cells of the accepted Round-41 theorem. The other two
normalized weights overlap these collars. Their pieces on which
\(|\log(|\alpha|/\lambda)|\) is small must be reassigned to the refined
middle cells before nonsaddle integration by parts. Constructing this
subordinate repair without changing the sum (46.8) is part of the theorem
to prove or refute. The final nonsaddle pieces must have a fixed positive
lower bound for \(|\Psi'|\).

## 3. Nonsaddle target

The exact phase on either signed branch satisfies

\[
 \Psi_\pm'(L)=\log\frac{|\alpha|}{\lambda},qquad
 \Psi_\pm''(L)=\frac1\alpha.                       \tag{46.9}
\]

The desired repaired inner nonsaddle support away from the zero set of
\(1-\chi_0\) is
\(|\alpha|\le3\lambda/4\), where
\(|\Psi_\pm'|\ge\log(4/3)\), and the repaired outer support is
\(|\alpha|\ge4\lambda/3\), where
\(|\Psi_\pm'|\ge\log(4/3)\). Every transition collar between these
regions belongs to the refined middle package.

Prove a finite, entry-compatible integration-by-parts theorem for the
complete singular signed Cauchy section and all smooth shares, retaining
every moving trace and cutoff derivative, which yields a normalized bound
strong enough that the exact \(h,q,j,x\) ledger is
\(O(X^{1/4+\varepsilon})\) after the external operator. The proof must
handle the unbounded outer sector and the inner sector adjacent to the
already closed compact box. It may invoke the accepted Round-41 theorem
only on the literal \(k=1\) cells.

If a single integration by parts is insufficient, isolate the first exact
coefficient or boundary term and its power capacity. Do not hide the
remaining tails in an unrestricted \(C_{X,b}\).

## 4. Controls

1. Same direct positive-line antecedent; no retransferred connectors.
2. Exact pointwise partition (46.8), smooth at the signed origin and with nonnegative one-count cutoffs after the subordinate-support repair above.
3. Literal match of \(k=1\) to the accepted saddle/entry/exit cells.
4. Both signed nonsaddle sectors and every cutoff collar.
5. Signed Cauchy section before absolute values for the singular top.
6. Moving traces, radial endpoints, floors, stars, equality restrictions,
   character, and external factor once.
7. Exact coefficient and scale sums.

The round is 100% analytical/algebraic. No numerical experiment or
external theorem is authorized or needed.

