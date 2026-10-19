# Round233 localized review repair

Date2026-10-12 Asia/Shanghai. Two nonauthor arithmetic reviewers independently identified the same optional-head range seam. The p2 layer-cake step has a log(2+Q) factor; the displayed Q ceiling alone permits absorbing it into T^epsilon when Q is polynomially bounded in T, including both intended cutoffs. The original paragraph did not state that restriction explicitly.

The sole repair inserts: “For the optional head refinement only, restrict to1<=Q<=T, which includes both proposed cutoffs.” It changes no main all-real-Q absorption or variance/head estimate, no finite constant, no signed budget equivalence, and no claimed cutoff corollary. The optional theorem is only used at Q=1 or floor(T^(1/p)). A stronger arbitrary-Q saturation argument is unnecessary and was not added.

- Original conductor candidate, preserved as `conductor_fixed_order_kernel_v1.md`: SHA256 `6e2be69a41d2bee8b8391e154a01e2f7468291314668c4363a93cc4b126b2caf`.
- Repaired candidate `conductor_fixed_order_kernel.md`: SHA256 `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0`.

All three initial reports are unchanged. Final arithmetic reviews bind the repaired hash. The initial finite review binds the original hash; its separate final-hash supplement checks the single change and carries forward only the unchanged finite/integral verdict. No arithmetic result is accepted from an unreviewed repair.

The final save also converts LF line endings to CRLF. Reviewers verified exact full-text equality after newline normalization and removal of the single inserted sentence. No claim of byte identity outside the insertion is made; the original version's complete bytes are preserved separately.
