# Round 147 conductor adjudication

- Campaign: m9-m1-lower-cone-t1-squarefree-voronoi-gate
- Round: 147
- Starting graph SHA-256: 1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5
- Terminal label: squarefree_H_resonance_no_go

## 1. Decision

Round 147 accepts one exact fixed-parameter reduction and one scoped
method obstruction.

For the mandatory \(t=1\) face, write

\[
 C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi _4(e).
\]

If \(s=2^\nu n\), with \(\nu\in\{0,1\}\) and \(n\) odd and
squarefree, then

\[
 C(2^\nu n)=
 \sum_{\substack{e\mid n\\e>2^{1+\nu/2}\sqrt n}}\chi _4(e).
\]

Divisor pairing retains both the complete positive-total-character
sector and the mandatory antisymmetric negative-total-character tail.
No complete nonnegative divisor coefficient replaces this cone
coefficient.

After a target-safe \(\sqrt D\) cone collar and a local
\(d\asymp D\) Mellin partition, the exact orders satisfy

\[
 d^{-it}(e/d)^{i\tau}
 =(de)^{-it/2}(e/d)^{i(\tau+t/2)},\qquad
 z=i(\tau+t/2),
\]

with radial twist \(s^{-it/2}\) and external constants
\(D^{it}4^{-i\tau}\). The hard Perron alternative retains its
\(z=0\) residue. The smooth ratio bandwidth is
\(|\tau|\lesssim D^{1/2}X^\varepsilon\).

For

\[
 A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z,\qquad
 B_z(n)=\mu^2(n)A_z(n),
\]

the exact factorization is

\[
 \sum_n B_z(n)n^{-w}
 =H(w,z)\zeta(w+z)L(w-z,\chi _4),
 \qquad B_z=h_z*A_z.
\]

The two-adic and odd local factors, the powerful support of \(h_z\),
and the quadratic refactorization

\[
 H(w,z)=
 \frac{\mathscr K(w,z)}
 {\zeta(2w+2z)\zeta(2w-2z)L(2w,\chi _4)}
\]

are accepted. The corrected exact odd-prime identity is

\[
 \mathscr K_p
 =\frac{1+a+b}{(1+a)(1+b)(1-ab)}
 =1+\frac{a^2b+ab^2+a^2b^2}
 {(1+a)(1+b)(1-ab)}.
\]

It proves absolute convergence of \(\mathscr K\) for
\(\Re w>(1+|\Re z|)/3\), but it does not authorize a
residue-free contour shift through possible reciprocal-\(\zeta\) or
reciprocal-\(L\) poles.

For each fixed \(|\Re z|<1/4\) and compact-smooth test, the exact
conductor-four transform has scalar \(\pi4^z\), one polar term, the
reflected coefficient \(A_{-z}\), and the full \(J/Y/K\) package at
argument \(2\pi\sqrt{mx}\). For a physical test with
\(K_F=\lfloor\sup\operatorname{supp}F\rfloor=O(M)\), its exact
squarefree convolution is finite in \(k\le K_F\). Every
\(k>K_F\) polar-dual pair cancels for that same \(k\) and is not a
physical resonance.

The accepted fixed-order geometry is

\[
 m=kN+O\!\left(k\sqrt{N/M}\right),
\]

with raw one-term size \(M^{3/4}/(kR)\) and physical one-term size
\(1/(kR)\). A uniform use across all cone orders is not accepted.

On the unitary order line, even after granting the missing uniform
kernel theorem, termwise primal/dual optimization followed by modulus
over powerful \(k\) gives the physical upper capacity

\[
 X^\varepsilon
 \begin{cases}
 M^{1/4},&M\le R^{4/3},\\
 R^{1/2}M^{-1/8},&R^{4/3}\le M\le R^2.
 \end{cases}
\]

This loses \(R^{1/3}\) at \(M=R^{4/3}\) and \(R^{1/4}\) at the top.
These are upper-bound limitations of the specified absolute-value
placement, not lower bounds for the signed scalar.

The elementary bare reciprocal lemma

\[
 \sum_{q\asymp Q}\left|
 \sum_{d\asymp D}e(Nd/q)\right|
 \ll_\varepsilon (Q+D)(NQ)^\varepsilon,
 \qquad Q\le N/4,
\]

is accepted. Expanding \(\mu^2(d)\) and taking the same triangle gives
only \(QD^{1/2}+D\). This is the first literal squarefree loss for that
proof placement; it does not prove that a signed squarefree average
cannot do better.

No \(t=1\) target bound and no strict owner-complete top range are
proved.

## 2. Evidence adjudication

### Discovery report

The discovery report is accepted for the exact coefficient and Euler
algebra, compact-smooth completed-functional-equation identity,
conductor-four resonance, all-scale powerful-index ledger, bare
reciprocal lemma, and squarefree triangle loss. Its no-go language is
accepted only for the enumerated termwise menu.

### Statement-only report

The blind report independently confirms the odd/even coefficient,
character sectors, \(p=2\) factor, powerful support, level-four
normalization at \(z=0\), resonance centre, width, amplitude, and
all-scale loss. Its terminal audit forced the exact local
cone-to-Mellin normalization, the unitary power line, finite physical
\(k\)-support, route-specific sufficiency wording, and radical
controls. All repairs are present, and its terminal verdict is GREEN.

### Source report

The source report verifies the Banerjee--Khurana specialization with
scalar \(\pi4^z\), one pole, and the exact \(J/Y/K\) combination. It
also distinguishes the fixed-parameter identity from the missing
growing-order estimate. The first source review exposed the coarse
fourth-order remainder in the proof of the \(\mathscr K\) domain; the
candidate now uses the exact mixed-monomial identity. The terminal
source verdict is GREEN.

### Hostile power review

The hostile review independently recomputed the raw and physical
prices, the \(k_0=M^{3/4}/R\) split, both endpoint losses, the
\(Q\le N/4\) reciprocal lemma, and the \(QD^{1/2}+D\) squarefree
triangle loss. It required fixed-order qualifications, unitary
orders, the true \(K_F\) cutoff, per-\(k\) tail cancellation, and the
correct reciprocal/primal crossover wording. After the final
\(k\le K_F\) repair in the power sum, its v2 terminal verdict is GREEN.

## 3. Accepted statements

The graph may record:

1. the exact \(t=1\) coefficient and character-sector identities;
2. the target-safe cone collar, hard-versus-smooth bandwidth
   distinction, exact local Mellin normalization, radial twist, and
   retained zero mode;
3. the exact \(p=2\) and odd Euler factors, powerful support, and
   corrected quadratic refactorization;
4. the fixed-parameter compact-smooth conductor-four transform,
   finite physical \(H\)-convolution, one pole, all Bessel branches,
   and per-\(k\) nonphysical-tail cancellation;
5. the fixed-order centre, width, and amplitude;
6. the unitary-line absolute aggregation ledger and its
   \(R^{1/3}\) and \(R^{1/4}\) losses;
7. the bare reciprocal lemma and the precise loss caused by the
   literal Möbius-square expansion under triangle inequality.

The accepted obstruction is method-specific. None of the last two
items is a signed lower bound.

## 4. Rejected inferences

Reject the following inferences:

1. the fixed-order Banerjee--Khurana identity is already uniform for
   the growing cone orders and moving prefixes;
2. absolute convergence or powerful support of \(H\) supplies a
   physical unweighted \(\ell^1\) saving;
3. convergence of \(\mathscr K\) below \(1/2\) permits a
   residue-free contour shift through the reciprocal factors;
4. the bare top reciprocal transform proves the literal squarefree
   \(t=1\) face;
5. the bare \(Q+D\) lemma survives a literal \(\mu^2\) expansion by
   triangle inequality;
6. disjoint moving \(k\)-bands imply orthogonality of the resulting
   scalar contributions;
7. an adverse upper-capacity ledger is a signed lower bound or a
   disproof of the target estimate;
8. a separate \(t=1\) estimate is necessary for every possible proof
   rather than merely sufficient for a layerwise route;
9. this round proves lower GAR, M9-M1, M9-M2, M9, the quarter target,
   or a better exponent.

## 5. First open owner

For this separate-\(t=1\) route, the first open analytic seam is a
uniform complex-order, moving-prefix estimate for every \(J/Y/K\)
regime through the exact unitary orders above.

Granting that theorem, the first missing arithmetic estimate is the
signed, physically truncated correlation

\[
 \sum_{\substack{k\le K_F\\k\ {\rm powerful}}}\frac{h_z(k)}k
 \sum_{|j|\lesssim k\sqrt{N/M}}
 A_{-z}(kN+j)\mathcal W_{k,z,U}(j)
 \ll_\varepsilon X^\varepsilon,
\]

after physical normalization and integration over the actual
\((\tau,t)\) orders. An equivalent survivor is a squarefree/coprime
strengthening of the bare reciprocal lemma which avoids the
\(QD^{1/2}\) triangle loss.

The separate \(t=1\) target is sufficient for a layerwise proof but is
not necessary for a proof which uses cancellation across \(t\)-layers.
The independent Round-138 cross owner and every \(t\ge2\) layer remain
separate.

## 6. State decision

Create:

- M9-M1-lower-cone-t1-squarefree-voronoi-reduction;
- M9-M1-lower-cone-t1-squarefree-H-resonance-obstruction.

Update the small-\(t\) reduction, Banerjee--Khurana source audit,
selected prior obstructions, and global lower-radial owner with the
new fixed-order interface and scoped obstruction. Reject the false
inferences listed above.

Record no change for M9-M1, M9-M2, endpoint uniformity, M9, the
conditional bridge, the internally proved \(1/3\) exponent, the
separately audited external Li--Yang exponent, or the quarter target.
