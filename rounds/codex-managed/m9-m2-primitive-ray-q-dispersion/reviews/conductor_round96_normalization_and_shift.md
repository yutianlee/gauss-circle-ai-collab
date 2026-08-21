# Round 96 conductor review: normalization, lattice, and shifts

Starting graph SHA-256:
242a5f0c6cb22d2e9a400bca110a91c08aea3b3cc8c537bc17fd73418df88fd1

Reviewed independently:

- reports/blind_primitive_ray_q_rederivation.md;
- reports/primitive_ray_q_dispersion_attack.md;
- reports/primitive_ray_q_hostile_source_audit.md;
- candidates/conductor_q_curvature_audit.md.

## Primitive lattice

For

\[
 m=(a+b)/2,\qquad q=(b-a)/2,
\]

odd primitive \(a<b<4a\) are in bijection with

\[
 0<q<3m/5,\qquad m\not\equiv q\pmod 2,\qquad (m,q)=1.
\]

Indeed

\[
 (a,b)=(m-q,m+q)=(m-q,2q)=(m-q,q)=(m,q),
\]

where the factor \(2\) is removable because \(m-q\) is odd. Also

\[
 \chi_4(a)\chi_4(b)=(-1)^{m-1}=(-1)^q.
\]

All three reports agree on these identities.

## Shift taxonomy

At fixed \(m\), every admissible \(q\) belongs to one residue class
modulo \(2\). The first legal shift is \(q\mapsto q+2h\), and

\[
 (-1)^{q+2h}(-1)^q=1.
\]

Odd shifts have empty support; they do not contribute a negative
character correlation.

At fixed \(a=m-q\), the legal cross-ray move is

\[
 (m,q)\mapsto(m+h,q+h),\qquad b\mapsto b+2h,
\]

and its character correlation is \((-1)^h\). This is a genuinely
different direction and must retain two independently moving reciprocal
intervals, lift sets, primitive masks, and entry/exit samples. A general
\(q\)-slice shift transfers the sign to
\((-1)^h=(-1)^{m'-m}\); it does not create an additional character.

## Endpoints and complete coefficient

The exact half-angle and metric quantities are

\[
 u=\frac{q}{m+\sqrt{m^2-q^2}},\qquad
 \Lambda=X\bigl(m-\sqrt{m^2-q^2}\bigr),
\]

and the reciprocal interval is

\[
 \frac J2\left(\sqrt{\frac ba}-1\right)
 <k<
 J\left(1-\sqrt{\frac ab}\right).
\]

The reports lawfully use zero extension rather than identifying shifted
integer intervals. The complete coefficient retains \(W_R\), its
density and discrepancy modes, the physical integral, profiles, floors,
stars, lift endpoints, owner masks, and saddle entry/exit.

Completing the physical square gives

\[
 W_R(\Lambda/k)\mathfrak C^\circ
 =\sum_{r\in\mathbb Z}\widehat W_R(r)
 e\!\left((r-g/2)\Lambda/k\right)\widetilde{\mathfrak C},
\]

so \(r-g/2\in\mathbb Z+1/2\) for odd \(g\). The density mode \(r=0\)
is part of the same nonzero half-integral family; it cannot be deleted.
On the exact fixed-\(m\) parity coset, Poisson has dual lattice
\(\frac12\mathbb Z\), including zero. The two descriptions are
unitarily equivalent.

## Review verdict

The normalization, parity, gcd, character, endpoint, and complete-symbol
seams pass. Promote the exact legal-shift character cancellation and
parity-aware adjoint-return identities as a scoped route obstruction.
They do not estimate the remaining complete shifted Gram form.
