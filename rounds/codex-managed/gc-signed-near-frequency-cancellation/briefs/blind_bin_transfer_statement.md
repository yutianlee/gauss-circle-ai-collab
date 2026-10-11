# Round210 isolated frequency-bin transfer packet

Read only protocol.md and this packet. No graph, active state, other
reports, generated general brief, historical proofs or web. Write only
rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/blind_bin_transfer.md
with seven numbered protocol sections, then stop. No numerical experiments.

Let X>=2, I=[aX,bX] with fixed a<b, and a finite set of real frequencies
mu with absolutely continuous complex amplitudes C_mu on a fixed slightly
larger interval I*. Put F(x)=sum_mu C_mu(x)e(mu x), e(t)=exp(2pi i t).
Partition frequencies into bins [j/X,(j+1)/X), j integer, and set

B_j(x)=sum_(mu in bin j) C_mu(x)e((mu-j/X)x).

Thus F(x)=sum_j e(jx/X)B_j(x) exactly. Investigate these assertions;
prove, refute or repair them without assuming they are true.

1. With a fixed smooth cutoff eta(x/X) supported in I* and equal to1 on I,
one has integral_I |F|^2 dx <= C sum_j integral_I*
(|B_j|^2+X^2|B_j'|^2) dx. Constants depend only on the fixed interval and
cutoff. Give all scale factors and a self-contained proof. Is replacing
this right side by sum_j integral|B_j|^2 valid for arbitrary amplitudes?
Give an explicit analytic control if it fails. Also determine whether
bin-zero sums sum C_mu can replace B_j without any internal-phase cost.
2. Let coefficients include a moving prefix: C_mu(x)=sum_(ell<=f(x))
C_(mu,ell)(x) with ordered labels1..L and arbitrary integer-valued f.
Each C_(mu,ell) is smooth, but the prefix may jump. Derive a legitimate
logarithmic-cost sufficient bound by decomposing prefixes into canonical
dyadic label intervals Q, applying part1 to the FULL fixed Q-amplitudes
over I*, and retaining the resulting total energy summed over Q. Do not
assume that this total Q-energy is no larger than the full unmasked energy;
test that claim with a cancellation example. Show exactly which logarithms
are paid and why merely differentiating the prefix is invalid.
3. For physical interpretation only, suppose the required norm is
G=T^(473/65)N^-1/2 with X=T^2 and T^(166/325)<N<T^(242/325).
An already available exact single-frequency energy is XHQ^4, with
H=T/sqrt(N), Q comparable toT, but distinct fifth frequency sums can be
as close as a guaranteed separation of orderQ^-10. Does the exact energy
alone prove the required binned derivative energy? Distinguish a generic
transfer counterexample from an actual arithmetic counterexample. No
specific arithmetic coefficient claim is permitted without supplied data.

The result must identify the first unproved input and correct state scope.
