# Candidate: adjacent-ray phase-preserving transport commutator

The exact target is

\[
 \Re\sum_{a,q}(-1)^qF_{L,a}(q)
 \ll_\varepsilon L^2X^\varepsilon.
\tag{111.C1}
\]

Use the identity

\[
 2\sum_q(-1)^qF_{L,a}(q)
 =\sum_q(-1)^q\{F_{L,a}(q)-F_{L,a}(q+1)\}.
\tag{111.C2}
\]

The proposed new mechanism is to compare the two full actual rows along
the exact phase-preserving dilation (111.5)--(111.6), rather than
differentiating the centered phase or transforming the entire row. Define
the transported neighbor on the common interior, keep the induced lattice
discrepancy as an explicit signed kernel, and split every support or owner
jump as its own finite atom. Seek either

\[
 \sum_{a,q}(-1)^q\Delta_{\mathrm{transport}}F_{L,a}(q)
 \ll_\varepsilon L^2X^\varepsilon,
\tag{111.C3}
\]

with all jump packets target-safe, or a rigorous theorem that the lattice
commutator has the same capacity as (111.C1).

The candidate is deliberately not the stronger total-variation claim

\[
 \sum_{a,q}|F_{L,a}(q+1)-F_{L,a}(q)|
 \ll L^2X^\varepsilon.
\]

That claim must be proved separately if used and is expected to face hard
edge and fourth-power controls.

