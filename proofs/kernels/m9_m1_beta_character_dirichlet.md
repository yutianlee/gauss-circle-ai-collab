# Finite period-four character Dirichlet kernel

For the primitive odd character modulo \(4\), put

\[
D_M^{\chi}(\theta)=\sum_{q\le M}\chi_4(q)e^{-iq\theta}.
\]

Uniformly for \(Q\ge 1\),

\[
\sup_{0\le M\le Q}|D_M^{\chi}(\theta)|
 \ll \min\{Q,1+|\cos\theta|^{-1}\},                    \tag{1}
\]

and

\[
\int_0^{2\pi}\sup_{0\le M\le Q}|D_M^{\chi}(\theta)|\,d\theta
 \ll \log(2Q).                                        \tag{2}
\]

Indeed, only odd indices contribute, and for
\(K=\lfloor(M-1)/2\rfloor\),

\[
D_M^{\chi}(\theta)
=e^{-i\theta}\sum_{k=0}^{K}(-e^{-2i\theta})^k.
\]

The geometric formula gives the second bound in (1), while the number of
terms gives the first.  Integrating
\(\min(Q,|\theta-\theta_0|^{-1})\) near the two zeros of
\(\cos\theta\) proves (2).

For an interval \(L\le q\le U\le Q\) and a complex sequence \(a_q\),
summation by parts gives

\[
\left|\sum_{q=L}^{U}\chi_4(q)e^{-iq\theta}a_q\right|
\ll \min\{Q,1+|\cos\theta|^{-1}\}
\left(|a_U|+\sum_{q=L}^{U-1}|a_{q+1}-a_q|\right).     \tag{3}
\]

Consequently, if the discrete-BV norm on the right is uniformly
integrable in every remaining variable, one full theta period costs only
\(O(\log(2Q))\). This qualification is essential: (2) is not a pointwise
bound, and it does not by itself control a theta-dependent actual-profile
amplitude.

Finally, for every integer \(D_0\) and odd integer \(q\),

\[
|D_0-q/2|\ge \frac12.                                \tag{4}
\]

This is an exact parity gap only.  It neither excludes continuous near
resonance nor estimates the connector-completed beta-transition operator.

## Operator-scope correction from Round 27

The kernel above is the correct finite character kernel for the unsplit
stationary radial transform G=E1+R1, whose stationary coefficient is
q^0. It must not be used to remove the explicit 1/rho in the post-endpoint
R1 survivor. Away from the artificial-pole and stationary-transition
seams, that denominator gives q^(-1); after the symmetric hard-top
PV/delta convolution the separated local coefficient has q^(-2) decay.
Conversely, uniform pointwise q-BV before that signed split is false at an
actual top-pole sample. Thus (1)-(3) remain valid but are no longer the
principal proposed closure mechanism for the post-endpoint hard-top piece.
