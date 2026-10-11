# Round218 conductor packet-coherence review and actual binding

## 1. Result

GREEN for the isolated coherence lemma and its application to the named
positive dual-tuple certificates, conditional on the exact final-hash
bindings below. Conductor NONBLIND application review, 2026-09-28;
campaign gc-complete-signed-radical-kernel; starting graph
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
The estimate is for a sum of moduli after complete radius integration.
It is not a lower bound for a signed moment.

Isolated report:reviews/isolated_packet_coherence_rederivation.md,
SHA256 bec8ef06ba0a0105bf0cf07feb2ed2bacb301d7958a7b41e42276d02ffd73f1e.
Actual report:reports/joint_lattice_kernel.md, SHA256
c3193b053d594b3a1599cdf707161b438f3387703f9e0f2010cf1d3b0101d41c.

## 2. Exact hypotheses

The abstract packet has even fixed p, M comparable to T^2 labeled
centers rho_a in a compact positive-width subinterval T J' of the
plateau of w(R/T), L>=1, positive amplitudes comparable to T^(-1/2),
real profiles H_T converging in Lp to nonzero H, and uniform global
Lp errors o(T^(-1/2)L^(-1/p)). Centers may repeat, with their complete
label multiplicities. No amplitude sign or profile smoothness beyond
the stated assumptions is silently added to the abstract lemma.

## 3. Independent derivation and actual application

Translation continuity of H in Lp chooses a fixed delta such that
all shifts of size at most delta are sufficiently close to H. Convergence
of H_T makes this uniform for large T. A telescoping product expansion
and Holder bound the full L1 difference of a product of p nearby
translates from H^p. Since p is even and H is nonzero, integral H^p
is strictly positive. After R=rho_0+u/L, the plateau margin grows like
TL, so the weighted integral differs from that full integral only by
uniformly small L1 tails. Global Lp errors give a uniformly smaller
product-integral error by the same Holder expansion. Thus every tuple
of centers in one delta/L bin has integral modulus at least
c T^(-p/2)L^(-1).

There are at most C T L such bins, including any endpoint bins.
If b_j counts labeled centers in bin j, convexity gives
sum b_j^p >= M^p/(C T L)^(p-1). Multiplying by the preceding tuple
bound yields T^(1+p/2)L^(-p). No division by p! occurs because all
tuples are ordered. Repeated centers only increase some b_j.
Uniformity holds even if L grows arbitrarily fast; the product loss
and the number of bins retain the exact same L powers. For odd p a
compact odd profile with all centers equal can have zero integral,
so the parity premise cannot be dropped.

For the COMPLETE actual lattice certificate take p=12,L=1,
centers rho_k=|k| in[T,3T/2], and c_k=|k|^(-1/2). The elementary
disk count gives M comparable to T^2 with exact Gaussian-integer
multiplicity. The actual H_T converges in L12 to the nonzero odd
H_infinity stated in the lattice report. The exact transform has a
localized error O(T^(-3/2)(1+|R-rho_k|)^(-A)) plus an arbitrarily
small uniform remainder on the physical window, hence L12 error
O(T^(-3/2)), smaller by T^(-1) than the leading L12 scale.

One application detail matters: the abstract error is global in R,
whereas the actual report needs its expansion only on the physical
positive window. Define the abstract F_k to be the actual F_T on
[T/2,2T] and zero elsewhere. This leaves every integral against w
unchanged. Outside that window the leading translated H_T is a
uniform Schwartz tail, since rho_k has a fixed T-sized margin from
its endpoints. Thus the resulting global error has the same small
Lp norm. No global expansion of the uncut transform, which could
have another packet at negative R, is assumed. The abstract functions
need not be smooth at these artificial edges.

This proves the complete lower certificate T^7. The lattice report's
divisor-bound shell census and rapidly decaying far frequencies give
the matching T^(7+epsilon) upper certificate.

For an annular block use L as in the actual report and profiles
H_eta(s)=integral_1^2 v(t)Psi(eta t)sin(2pi st)dt/t,
eta=L/sqrt(T) in[0,c]. This is a compact continuous family in L12
with uniform Schwartz seminorms, uniform translation continuity and
norm bounded below, since Psi>=1/2 and its derivative-at-zero
integral is positive. These uniform properties are exactly what the
preceding proof uses; alternatively any contrary sequence has a
subsequence eta tending to a limit and then meets the isolated packet's
literal L12 convergence hypothesis. The error is smaller by (TL)^(-1)
in L12 after scaling. The same count gives T^7 L^(-12), including
T^3 at L=T^(1/3). This argument keeps each full R integral before
modulus and is stronger than the separate inside-integral controls.

## 4. First doubtful or unproved step

The signed sum over all dual tuples remains unestimated. Other tuples
can cancel the positive close-tuple coefficients used in this certificate.
No lower bound on M12(B_T), I12, or a high-value set follows. Likewise,
the smooth extension chi is part of this particular certificate; changing
the extension or subtracting the paid head before a different transform
requires a separate analysis and is not ruled out here.

## 5. Controls and outcomes

GREEN for full versus weighted integral, global Lp error via zero
extension, odd profiles with even p, exact multiplicities, all endpoint
bins, growing L, uniform compact annular families, and complete radius
integration before modulus. Pointwise smallness of the error would not
alone justify integration over a growing window; the localized Lp bound
is used explicitly. No numerical experiment or new source theorem.

## 6. Dependencies and provenance

Read the isolated statement and frozen independent derivation, the exact
lattice report at the above hash, protocol, actual216 reduction, and the
existing coefficient/disk/divisor facts. The isolated reviewer received
no actual application or claimant proof for the coherence task and
disclosed its prior context. This conductor binding is explicitly nonblind.
All cited report bytes remain frozen; no shared graph inference is made
solely from a candidate report.

## 7. Recommended state effect

Retain the fully reviewed certificate no-go and close the bounded method
attempt with an identity State Patch. Do not promote a new open signed
aggregate merely because it is an exact reformulation. The original
complete moment target, every parent and the full quarter goal remain
open; no accepted bound or proof-draft claim changes.
