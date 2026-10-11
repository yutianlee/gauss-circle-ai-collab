# Round222 conductor review of the isolated finite correlation lemma

## 1. Result

GREEN for the complete and weighted-window identities, the stated
simple-frequency control and the fixed-row-twist distinction. They
do not prove an actual arithmetic vector estimate. Retain them as
reviewed finite evidence; no graph promotion is needed merely to
record standard finite Fourier algebra.

## 2. Exact hypotheses and final bindings

Report reports/blind_cross_modulus.md, SHA256
707a618e63169cc0251cdce6efc55dd2ed442e1751d9456649fea0df6be568d2.
Packet briefs/blind_cross_modulus_statement.md, SHA256
a91629290c8964e84e08bf7999dfd85fdb10baf189bd515ba509be8631983f8e.
Both paths are in rounds/codex-managed/m9-m2-complete-unbalanced-vector.
The moduli q,r are integers>=2, first arguments arbitrary integers,
and inverse representatives arbitrary. Windows are finite complex
weights; positivity is claimed only for the specified unweighted Gram.

## 3. Independent verification

Expanding both Kloosterman sums leaves the h-frequency x/q-y/r.
Over lcm(q,r) consecutive integers this is orthogonal unless the
frequency is integral. With unit representatives, both fractions
are reduced and lie strictly between0 and1, so equality forces
q=r,x=y. Inversion permutes the unit residues; the diagonal is
q c_q(A-B). Neither argument uses (A,q)=1 or (B,r)=1. Shifting
the complete window preserves the conclusion. Changing inverses
adds integral phases because A,B are integers.

For arbitrary weights the exact surviving factor is D_w(x/q-y/r).
Separate h-dependent row weights replace w by their full product.
The explicit q=3,r=5,A=B=0 one-column example is8 instead of zero,
so a complete unweighted identity cannot be applied to those weights.

The geometric interval sum has the printed phase and sine quotient.
The bound |sin(pi t)|>=2||t|| gives min(H,1/(2||t||)) with constant1;
integral t gives H and H=0 gives zero. No zero frequency is dropped.

For odd q and r=q+2, gcd(q,r)=1 and 2x-q=2y-r=1 verify both units.
Their frequency gap is exactly1/(qr). For1<=H<=qr/4, the inequalities
sin(pi H/(qr))>=2H/(qr) and sin(pi/(qr))<=pi/(qr) give the lower
magnitude2H/pi. The full qr-period sum is zero. These are two single
frequency rows, not complete Kloosterman rows; summing many complex
terms does not preserve that lower bound.

Their Gram eigenvalues are H+|C| and H-|C|. Constant unit row factors
conjugate this matrix unitarily, preserving its spectrum and all-vector
norm. They rotate a specified row coefficient vector. The H=1,m=0
example changes its squared norm from2 to0 while keeping the operator
norm sqrt(2). The report correctly distinguishes this from a fixed
column vector, whose output norm is invariant under left unitary
multiplication. Different h-dependent row factors have no such single
left-unitary representation; the example turning both rows into1
correctly changes the full-period Gram spectrum.

## 4. First unsupported step

The missing application estimate concerns the actual h-dependent
arithmetic weights and literal windows. Complete-period orthogonality
does not provide it, and the simple-row near-frequency control is not
an actual Kloosterman-vector lower bound. No gap remains in the
finite statements themselves.

## 5. Controls and outcomes

Equal/repeated moduli, arbitrary first-argument gcd, empty windows,
H=1, integral frequencies, shifted intervals and inverse choices are
all handled by the exact expansions. The row-weight counterexample
and two-row sign example have their correct limited scopes. Every
control is analytical; zero experiments and no source import.

## 6. Dependencies and provenance

Conductor, round222, graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Only the two bound artifacts and protocol are needed for this review.
The conductor independently derived the core finite frequency identities
before reading the report. The reused agent disclosed earlier-round
history; its current access was statement-only, not history-free.
Its subsequent review of the conductor's actual weighted-period control
is a separate application stage after the finite report froze.

## 7. Recommended state effect

Retain the finite report GREEN as evidence. Leave the complete UNBAL,
other M1/M2 parents, endpoints and full quarter target open. Do not
promote a source application, signed lower bound or exponent change
from this algebra.
