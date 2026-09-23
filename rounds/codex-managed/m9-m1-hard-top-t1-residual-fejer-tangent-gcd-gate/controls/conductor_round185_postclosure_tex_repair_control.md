# Round 185 postclosure TeX repair control

## Result

GREEN for the exact typographic repair surface. Three evidence artifacts
contained bare spacing-command text caused by lost TeX escape characters.
Only those command escapes, plus one redundant terminal blank line in the
adjudication, were repaired. No formula variable, relation, hypothesis,
bound, status, dependency, evidence path, graph byte, or mathematical
conclusion changed.

## Exact byte-delta controls

1. reports/literal_residual_fejer_tangent_gcd_attack.md

   - pre-repair SHA-256:
     2e429c02a1cac6dea3a9bde6731027bb074ba34468a9906f18ef83cf5989f172;
   - current SHA-256:
     1ba2eac8e052b33814b9f1be2a02d306b643095a4d156ff16f88f1ae9785093d;
   - exact change: insert 19 missing backslashes before 19 long-spacing
     TeX commands on lines 52, 113, 114, 196, 232, 236, 242, 248,
     255, 268, 274, and 421--423;
   - deleting exactly those 19 backslashes reproduces the recorded
     pre-repair hash byte-for-byte.

2. reviews/conductor_round185_adjudication.md

   - pre-repair SHA-256:
     f69030851b6c187e3428d27870367804b486541537387ea3b52a10a784a33914;
   - current SHA-256:
     9b490005e130acf5eacdefd6ad396b3f4c302cc3de6dc945b8fb408bd4e78f91;
   - exact change: insert four missing backslashes before short-spacing
     TeX commands on lines 116--118 and four missing backslashes before
     long-spacing TeX commands
     on lines 144, 149, 157, and 158; normalize two terminal line feeds to
     one;
   - deleting exactly those eight backslashes and restoring the one
     redundant terminal line feed reproduces the recorded pre-repair hash
     byte-for-byte.

3. reviews/joint_h_count_power_and_deletion_seam_review.md

   - pre-repair SHA-256:
     0481aa6ec289a40d09257a5cf5f77675fd1e233bcb53ed6c45c11d3697ff5866;
   - current SHA-256:
     17ef16259c8df356442924981f43f9c01a8201c170b6f7e812206acd0c98ea41;
   - exact change: insert two missing backslashes before the long-spacing
     TeX commands on lines 119 and 133;
   - deleting exactly those two backslashes reproduces the pre-repair
     bytes and hash.

## Scope and provenance

The historical preapplication and postapplication audits are left
immutable. Their recorded hashes correctly identify the bytes they
audited. This control connects those historical bytes to the repaired
current bytes by exact reversible edits. The authoritative graph remains
at f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575,
and the candidate and durable kernel retain their reviewed hashes.

The repair grants no proof-state promotion. The exact high-height signed
relation and every complete residual, parent, bridge, theorem, and
exponent remain open or unchanged.
