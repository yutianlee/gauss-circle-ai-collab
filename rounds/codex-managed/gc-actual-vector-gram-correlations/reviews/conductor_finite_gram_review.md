# Round221 conductor review of the isolated finite Gram report

## 1. Result

GREEN for the finite statements and their stated limitations. No actual
arithmetic estimate or full moment improvement follows. Retain this as
reviewed round evidence; a new graph node for routine finite linear
algebra is unnecessary for this round's complete-target decision.

## 2. Exact statement and review bindings

Reviewed report: reports/blind_anchored_gram.md, SHA256
c79eb543c4dd1229e8e6b9c6550f9b6df0fb10bed0ed76f386bf08c79d7d2ebd.
Statement packet: briefs/blind_anchored_gram_statement.md, SHA256
5e15f8516a2a9c00f278588f59e8f2c0644fbf296bdab383fdfe01e0976389d9.
Both are in rounds/codex-managed/gc-actual-vector-gram-correlations.
For finite U, prescribed b, f=Ub, B=b*b, M=U*U and G=UU*, the
report proves a_k=b*M^k b=f*G^(k-1)f and a_1^k<=B^(k-1)a_k.
For candidate data f,B, the bordered PSD criterion is exactly
f in range(G), f*G-dagger*f<=B, equivalent to a preimage of norm
at most sqrt(B). It is not identification of a prescribed vector.

## 3. Independent verification

Associativity gives U*G^(k-1)U=M^k, including k=1. Expanding M entry
by entry gives the report's column chain, with conjugates on the first
endpoint and first factor of each adjacent column pair. Expansion of
f*G^(k-1)f gives the row chain. Neither expansion makes its summands
positive. Only the completed PSD quadratic form is nonnegative.

In an eigenbasis of M, a_k is the sum of lambda^k times the squared
spectral coefficients of b. Dividing these weights by B proves the
inequality by convexity. For k>1, strict convexity gives equality
exactly when every occupied eigenvalue is the same, including zero.
The B=0 and k=1 conventions in the report avoid division by zero and
the expression 0^0. The high-value consequence also retains the
separate equality condition |f_j|=v on every nonempty row.

For the border, testing kernel vectors of G first forces the range
condition. With g=G-dagger*f, completing the quadratic form as
(x+zg)*G(x+zg)+(B-f*G-dagger*f)|z|^2 proves sufficiency and necessity.
The minimum preimage U*G-dagger*f is orthogonal to ker(U); every
other preimage adds a kernel vector. Its norm squared is precisely
f*G-dagger*f. Thus all singular cases and the distinction between
an at-most and an exact norm budget are treated correctly.

Under time translation U becomes U D, with D diagonal unitary.
Then G is unchanged, M becomes D*M D, and the prescribed-vector
value becomes U D b. Replacing a_k by B||G||^k in the sharp
interpolation yields exactly a_1<=B||G||, independent of k.
Adding b* as a row gives the stated border, but its new entries
are the unknown values themselves. Positivity supplies ordinary
Cauchy bounds only.

## 4. First unproved step

There is no gap in the reviewed finite lemma. Its use toward the
campaign target requires an additional actual-vector estimate for
the chain. No such estimate is contained in this report. A range or
PSD certificate cannot be substituted for coefficient identification.

## 5. Controls and outcomes

The two-frequency example has U initially all ones, G all twos,
B=2, and f=(2,2). Translation by 1/2 changes the second column's
sign, preserving G and B but giving f=0. The initial eigenvalue is
4 on b, so a_k=2*4^k; afterwards all moments vanish. The prescribed
b remains nonnegative. This is an exact finite control, without an
arithmetic-frequency assertion.

For G=diag(1,0) and f=(0,1), the pseudoinverse quadratic form is
zero, but the missing range condition gives a principal determinant
-1 in the border. For U=(1,0), the candidate f=0 has an exact-norm
preimage (0,1) distinct from the prescribed b=(1,0). Zero matrices,
empty dimensions, nullspace slack, repeated eigenvalues and rank
identities follow from the same decompositions. No numerical test
or external source was used.

## 6. Dependencies and provenance

Conductor review, round221; graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Only the two bound artifacts and protocol are needed for this finite
review. The conductor independently derived the chain and its scalar
ceiling limitation before reading the isolated report. The report
discloses reuse of an agent with earlier-round history; it is not a
fresh history-free derivation. Its current packet excluded current
claimant derivations and arithmetic application. Subsequent application
review by that agent is a separately assigned stage after this freeze.

## 7. Recommended state effect

Retain the finite report as validated evidence, with all arithmetic
and complete-target obligations open. No promotion, rejection of the
actual signed target, proof-draft edit or exponent change is warranted.
