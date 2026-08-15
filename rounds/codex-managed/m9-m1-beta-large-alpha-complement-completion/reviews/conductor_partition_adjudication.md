# Conductor adjudication: exact subordinate alpha partition

Campaign: `m9-m1-beta-large-alpha-complement-completion`  
Round: 46  
Allocation: 100% analytical/algebraic

## Decision

The normalized preliminary weights in the frozen packet are nonnegative
and sum to one, but they are not subordinate to the stationary geometry.
Indeed, at (t=|\alpha|/\lambda=1),

\[
 (\widetilde\vartheta_0,\widetilde\vartheta_1,
   \widetilde\vartheta_\infty)(1)=(0,1/2,1/2),
\]

so the preliminary outer class contains the saddle.  The following repair
is exact and will be promoted as a scoped reduction.

Choose smooth (c_0,c_1,c_\infty:[0,\infty)\to[0,1]) such that

\[
 c_0+c_1+c_\infty=1,
\]

\[
 \operatorname{supp}c_0\subset[0,3/4],\qquad
 \operatorname{supp}c_1\Subset(2/3,3/2),\qquad
 \operatorname{supp}c_\infty\subset[4/3,\infty),
\]

and (c_1=1) on ([3/4,4/3]).  For example, take disjoint smooth
transitions from (c_0=1) to zero on ([2/3,3/4]) and from
(c_\infty=0) to one on ([4/3,3/2]), and put
(c_1=1-c_0-c_\infty).  Choose a smooth signed partition
(s_++s_-=1) whose transition lies wholly in the open set on which
(1-\chi_0=0).  Then

\[
 \eta_{\sigma,k,\ell}(\alpha,\lambda)
 =(1-\chi_0(\alpha))s_\sigma(\alpha)
 \widetilde\vartheta_k(|\alpha|/\lambda)
 c_\ell(|\alpha|/\lambda)
\]

is a finite, smooth, nonnegative, one-count refinement and

\[
 \sum_{\sigma,k,\ell}\eta_{\sigma,k,\ell}=1-\chi_0.
\]

After grouping over (k), the inner and outer supports have

\[
 |\Psi'|=\left|\log\frac{|\alpha|}{\lambda}\right|
 \ge \log(4/3),
\]

and every unsafe collar belongs to the middle class.  Differentiating a
ratio cutoff gives the exact (\lambda^{-1}) factor in (L), while
(x\partial_x c_\ell(|\alpha|/\lambda)=-(t/2)c_\ell'(t)) is order one
on its collar and must remain in the radial ledger.

## Scope and mismatch

This algebra does not identify the repaired middle aggregate with the
accepted Round-41 saddle/entry/exit package.  At (t=1), the repaired
middle aggregate is one, whereas the packet's original
(\widetilde\vartheta_1) is one half.  The accepted Round-41 graph node
states a fixed-ratio saddle/entry/exit theorem but does not expose its
literal cutoff family or a cutoff-invariance theorem.  Support
compatibility therefore cannot be upgraded to exact antecedent identity.

The repaired partition is nevertheless durable progress: it closes the
finite partition-existence subproblem without importing a stationary
numerator, taking an absolute value before the hard-top Plemelj section,
or reintroducing any routed module.

