# Round 53 derivation packet: complete adjacent-dyadic alpha difference

This packet freezes the first lawful scale-difference object after the
Round-52 type correction.  It does not assert that scale differencing saves
the alpha trace.

## 1. Exact physical scale data

Let (y=\lfloor\sqrt X\rfloor), (D_j=2^{-j}y), and
(H_j=\lfloor D_jX^{-1/4}\rfloor).  Let

\[
 \eta(t)=1-s(3(t-1)),\qquad W(t)=\eta(t)-\eta(2t),
\]

where (\eta=1) on (t\le1), (\eta=0) on (t\ge4/3).  For the interior
scales (j\ge1),

\[
 w_j(d)=W(d/D_j).
\]

The top profile is (w_0(d)=\mathbf1_{d\le y}W(d/y)), and the bottom
inactive profile is separately target-safe.  The exact telescoping identity
is

\[
 W(t)=\eta(t)-\eta(2t).
\]

The Vaaler height profile is

\[
 a_{H_j}(h)=\mathbf1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right).
\]

On the finite Mellin antecedent, one scale carries

\[
 \mathcal A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v.
\]

After physical alpha return, its lattice profile is

\[
 \mathscr B_j(n,q)=
 V_j^*\!\left(\frac{2\sqrt{Xn/q}}{D_j}\right)
 \phi\!\left(\frac n{H_j+1}\right),
\]

with the inherited product star at (nq=N_X), the top-profile star, the
common phase and arithmetic factors, and the single external
(X^{1/4}) normalization.

## 2. Frozen objective

Construct the exact coupled adjacent-scale difference between (j) and
(j+1) on one common ambient support, both:

1. on the finite positive-line alpha antecedent, retaining the difference
   of (D_j^u(H_j+1)^v\widehat W_j(u)\widehat\phi(v)), and
2. after the licensed physical return, retaining the difference
   (\mathscr B_{j+1}-\mathscr B_j), all support boundaries and stars.

Determine whether the telescoping profile identity and the exact relation

\[
 H_{j+1}=\left\lfloor\frac{H_j}{2}\right\rfloor
\]

produce a signed scale-partial-sum estimate strong enough to reduce the
normalized (X^{1/8}) lattice capacity.  If not, isolate the first exact
survivor or give a sharp actual-profile countercapacity.

## 3. Mandatory distinctions

- A difference of two separately bounded blocks is not a telescoping
  theorem.
- Do not apply the physical (H\mapsto H+1) variation uniformly on the
  finite (v)-rectangle; the factor ((H+1)^v) can have full bulk size.
- The identity (W(t)=\eta(t)-\eta(2t)) telescopes only after the exact
  scale indexing, top, and bottom owners are aligned.
- A profile support boundary and its equality star are distinct from the
  Vaaler cutoff (h\le H_j) and the product star (nq=N_X).
- Any Abel summation in (j) must state and prove the signed partial-sum
  bound for its actual arithmetic/phase antecedent and retain both boundary
  terms.
- Physical return, finite mask connectors, and outside-height limits may not
  be interchanged without an accepted aggregate identity.

## 4. Completion rule

A successful result supplies an exact common-support owner table and either
a target-relevant signed scale-partial-sum lemma or a rigorous no-go/capacity
theorem.  It must state separately what is true on the finite Mellin
antecedent and what is true only after the physical profile limit.  No
numerical experiment or external theorem is needed.
