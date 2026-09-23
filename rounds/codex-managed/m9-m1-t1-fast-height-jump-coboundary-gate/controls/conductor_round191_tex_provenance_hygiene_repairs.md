# Round 191 TeX and provenance hygiene repairs

## Purpose

This control records formatting-only repairs made after mathematical
review.  No formula, quantifier, estimate, dependency, state effect, or
scope boundary was changed by these operations.

## Report-level escape repairs

Several agent-authored Markdown files contained display-only escape
damage from transport through a JavaScript string:

- a carriage-return byte in place of the r in a TeX roman-font command;
- missing backslashes before TeX spacing, inequality, set-difference, or
  indicator commands; and
- a missing thin-space backslash in a superscript.

The conductor mechanically restored the intended TeX spelling in:

- review_packets/signed_inverse_transport_sector_statement_only.md;
- reports/blind_fast_jump_rederivation.md;
- reports/literal_height_jump_coboundary_attack.md;
- reviews/blind_signed_inverse_transport_sector_review.md;
- reviews/blind_post_unmask_signed_inverse_sector_postrepair_verification.md;
- reviews/literal_jump_parity_projector_owner_scope_postrepair_verification.md.

These repairs changed only rendering.  The mathematical prose and
verdicts are unchanged.

## Candidate and kernel hygiene repair

The first final-formalization review found one unmatched Markdown
delimiter in the prose phrase describing the transported superscript
and two surplus terminal newlines in the kernel.  The conductor replaced
the prose spelling by the valid TeX phrase \({\rm tr}\), normalized both
files to one terminal line feed, and refreshed the candidate provenance
hash in the kernel header.

Current frozen artifacts:

- candidate SHA-256:
  76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978;
- durable kernel SHA-256:
  7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2;
- raw post-header body SHA-256:
  f29eb55c0620bfdfbafb3974fa23bc6cd01594de04668b857d96f2c61d9834d4.

The candidate and kernel post-header bodies are byte-identical and each
file has exactly one terminal line feed.

## Independent replay

Three focused post-hygiene reviews return PASS:

- final kernel/candidate consistency:
  SHA-256
  5ebaa7901d876b2f3872f5a0e34f1660d2add43e2d94457fb4ee0ee2e42ac098;
- final power/literal/owner scope:
  SHA-256
  8193106f54a970fb50713a6e9e5f8e792ac7c261f22afb3ae5086ca9e31aeb5e;
- final formalization/provenance/hygiene:
  SHA-256
  563ec0c5da8433af4d20034346083eadb328c3400ed7820ec156c0dc8dc2604b.

They verify identical mathematical bodies, paired Markdown and TeX
delimiters, unique equation tags, refreshed provenance, strict UTF-8,
one terminal line feed, unchanged dependencies and ledger, and the
continued open status of (191.C12).

## Outcome

PASS.  The repaired candidate and kernel are the only frozen
formalization artifacts used by the State Patch.  Earlier hashes remain
historical review references only.
