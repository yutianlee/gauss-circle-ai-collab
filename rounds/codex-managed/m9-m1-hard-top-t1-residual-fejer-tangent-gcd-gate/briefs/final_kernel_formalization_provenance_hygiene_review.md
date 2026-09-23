# Round 185 final-kernel formalization, provenance, and hygiene review brief

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Role: independent formalization, provenance, and artifact-hygiene reviewer
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Source candidate SHA-256:
  74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65
- Durable kernel SHA-256:
  4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160
- Output:
  reviews/final_kernel_formalization_provenance_hygiene_review.md

Read completely: `protocol.md`, `state/active_campaign.yml`, the repaired
candidate, durable kernel, reconciliation, exact control, normalized
blind report and its post-repair verification.  Verify all recorded hashes
before review.

Audit whether the durable kernel is self-contained and formally literal:
all variables before use; total domains; the `U=1` convention; positivity
before square roots; canonical representatives; unique orientation and
index; consistent equation references; exactly one outer real part;
exactly one terminal label; candidate-to-kernel provenance; blind
normalization attribution; diagnostic-only computation scope; dependency
classification; and downstream quarantine.  Run strict UTF-8,
control-byte, replacement-character, line-ending, trailing-whitespace,
EOF-newline, TeX-delimiter/environment, duplicate-tag, and unresolved
cross-reference checks.

Write one seven-section report only to the assigned output.  Return GREEN
only if every formal, provenance, and hygiene seam passes.  Otherwise
return REPAIR with the first failing item.  Make no other edit and no
graph or shared-state mutation.
