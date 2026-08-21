# Conductor review: the returned character restores the dual stationary lattice

Campaign: m9-m2-dual-square-actual-symbol-transfer

Starting graph SHA-256:
2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de

## Question

Could the exact factor \(\chi_4(s)\) in the returned dual square supply
automatic step-two cancellation?

## Exact calculation

Keep the full dual phase

\[
 F(s)=-{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}. \tag{106.C1}
\]

The \(u\)-stationary relation is

\[
 b_*={4d^2Xn\ell\over s^2}=a+2du_*.
\]

Therefore

\[
 F'(s)
 ={dXn\ell\over s^2}-{a\over4d}
 ={u_*\over2}. \tag{106.C2}
\]

Since the dual lattice is \(s\equiv d\pmod2\), its step is two and the
local step-two derivative is \(2F'(s)=u_*\). This is precisely the
integer primal variable at an exact discrete return. Hence the full phase
is stationary modulo one on the same modes which reconstruct the primal
\(u\)-sum.

If the linear term is extracted as

\[
 e(-as/(4d))=-i\chi_4(a/d)\chi_4(s),
\]

then the remaining reciprocal phase has step-two derivative

\[
 {2dXn\ell\over s^2}
 ={b_*\over2d}
 =u_*+{a/d\over2}. \tag{106.C3}
\]

Because \(a/d\) is odd, (106.C3) is half-integral when \(u_*\) is
integral. On the odd lattice, \(\chi_4(s)\) changes sign under
\(s\mapsto s+2\), contributing exactly the other half frequency.
The character therefore restores the integer stationary alias; it does
not remove it.

## Consequence

Abel summation using only bounded partial sums of \(\chi_4(s)\) is
invalid at the returned stationary modes. Pairing \(s,s+2\) before
retaining the reciprocal phase merely hides the same alias. This is the
dual analogue of the earlier quotient-parity carrier cancellation.

The result is a mechanism no-go only. It does not prove that the complete
actual-vector dual sum is large: its amplitudes, metric convolution,
owners and transitions may still cancel jointly.
