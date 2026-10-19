# Conductor nonauthor review of the isolated absorption proof

Round233,2026-10-12 Asia/Shanghai; campaign `gc-fixed-order-moment-absorption`. Claimant SHA256 `71e5827c677fb0975eb763f667cf1472ac4e28d71ded17293578cd0eb8b75f23`. Starting graph `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Initial statement-only isolation preceded any expanded review assignment.

## 1. Result

Pass. The isolated finite/summable relative inequality and its signed integral implications are correct. They neither require a bound uniform in order nor provide an estimate for the signed integral.

## 2. Hypotheses

Real finite or absolutely summable families; fixed integer m>=2, with even m for the nonnegative moment interpretation. For integration a fixed countable measurable family is required, pointwise absolutely summable almost everywhere, with J=int V^(m/2)<infinity. No family-size dependence is permitted in C_(m,delta).

## 3. Independent proof check

Expanding the signed permutation cycle sum, a tuple with equality blocks of sizes b has coefficient product_b sum_(sigma in S_b)sign(sigma). A transposition pairs signs for each b>=2, while singleton coefficients are1. The all-singleton term is Z^m. Every nonidentity permutation has at most m-2 fixed points. The l2 power inequality |P_h|<=V^(h/2), h>=2, therefore bounds its term by |Z|^s V^((m-s)/2). Counting permutations by fixed points gives binom(m,s)D_(m-s), whose total excluding the identity is m!-1. Normalizing t=|Z|/sqrt(V) and splitting at max(1,sqrt((m!-1)/delta)) proves the claimant's constant exactly. V=0 and m2 are treated correctly.

The tuple-tail estimate m S^(m-1)S_tail follows by a union bound on which position lies outside the truncation; it establishes pointwise convergence independently of integration. For the measurable theorem, delta1 bounds the negative part by an integrable multiple of V^(m/2). Thus the signed integral is well-defined before moment finiteness is known. Integrating the nonnegative quantity E_m+C V^(m/2)>=(1-delta)|Z|^m is legitimate in the extended sense. The resulting finite upper bound proves finiteness, without circularly invoking an already finite moment. The alternative domination conditions in Section3.5 are sufficient for direct convergence of truncation integrals and are correctly distinguished from mere pointwise summability.

## 4. First remaining gap

No finite or measure-theoretic gap found. An application still needs the variance-power integral J and an actual signed-integral upper estimate. The claim correctly works for adversarial positive sequences and hence cannot itself establish arithmetic cancellation.

## 5. Controls

E2=Z^2-V and E4=Z^4-6Z^2V+3V^2+8ZP3-6P4 agree with expansion. At m4 the absolute coefficients6,8,9 sum to23. Fewer than m equal indices force C>=(1-delta)(m-1)^(m/2), correctly excluding order-uniform constants. One negative entry among exactly m unit-magnitude entries gives E_m=-m!, while the moment can be positive. Equal positive families show the necessity of the relative term for m>2 and that I cannot be bounded by J alone. Every control has the stated limited scope.

## 6. Dependencies

Read `protocol.md`, `briefs/isolated_absorption.md`, and the frozen `reports/blind_partition_absorption.md` in this campaign. The conductor had independently derived the same permutation and threshold argument for the candidate kernel; the blind author's initial context excluded it. Wolfram/local finite checks agree but are not used as proof. Exact report hash is above and the input hashes are in the claimant. No external source import.

## 7. State recommendation

Approve this seam for the narrow fixed-order absorption lemma. Actual-family binding, sharp restoration and graph promotion require their separate reviews. No complete moment exponent or quarter estimate is justified by this isolated result.
