# Round222 actual weighted rows and common-period orthogonality

## 1. Result

Complete-period orthogonality of unweighted Kloosterman rows does not
persist after multiplication by the actual inverse-selector Fourier
coefficient. For coprime distinct moduli, the complete correlation of
the weighted rows is exactly the product of their original reciprocal
row totals. Deleting the value at h=0 replaces those totals by the
corresponding centered totals; it does not remove their constant
Fourier coefficient.

This is an exact application control, not a lower bound on the actual
UNBAL sum or a no-go for a new signed joint estimate. It identifies
which coefficient information a proposed orthogonality argument must
estimate rather than discard.

## 2. Exact hypotheses and definitions

Fix an integer A, an integer n>=2 and any complex coefficients b_n(j)
on a finite collection of distinct unit residues j modulo n. Literal
zero extension implements the actual moving support. Define

    gamma_n(h)=1/n sum_j b_n(j)e(-h inverse(j)/n),
    S(A,h;n)=sum_(x unit mod n)e((A inverse(x)+h x)/n),
    F_n(h)=gamma_n(h)S(A,h;n),
    U_n=sum_j b_n(j)e(Aj/n),
    z_n=F_n(0), V_n=U_n-z_n,
    F_n^circ(h)=F_n(h)-z_n 1_(h=0 modulo n).

Every function in h is n-periodic. A may have any gcd with n; inverse
representatives are arbitrary. If several physical j values share a
unit residue, first add their coefficients in that residue; all finite
identities remain valid. In the accepted flat strict-UNBAL application,
j occupies its prescribed short residue range and no such folding
is required.

At fixed odd g, bind A=N0=floor(X) and
b_n(j)=q_L(4Xj/(g n^2))/(gj)e((X-N0)j/n), with the exact support.
Then U_n is the original reciprocal row. Its outer weight is
chi4(g)chi4(n)W(X/(gnD)). The accepted h=0 Ramanujan contribution
is z_n and is removed once. This binding has the flat-component scope
of the accepted143/160 artifacts; it supplies no endpoint transfer.

## 3. Exact derivation

Expansion in h gives

    F_n(h)=sum_(t modulo n)c_n(t)e(ht/n),
    c_n(t)=1/n sum_j b_n(j)
          1_(t+inverse(j) is a unit mod n)
          e(A inverse(t+inverse(j))/n).

At t=0, the inner inverse is j modulo n, so c_n(0)=U_n/n. In
particular sum_(h modulo n)F_n(h)=U_n, which is the complete
orthogonality self-return with its normalization retained. Since
1_(h=0 mod n)=n^-1 sum_t e(ht/n), centering the single h-value gives

    F_n^circ(h)=sum_t d_n(t)e(ht/n),
    d_n(t)=c_n(t)-z_n/n,
    d_n(0)=V_n/n.

Thus the column h=0 and the Fourier frequency t=0 are different
objects. The accepted safe-column removal does not make the resulting
sequence have mean zero.

For a second modulus m>=2 put d=gcd(n,m), P=lcm(n,m). Exact
orthogonality over a common period gives

    sum_(h=0)^(P-1) F_n^circ(h)conjugate(F_m^circ(h))
      =P sum_(ell=0)^(d-1)
          d_n(n ell/d)conjugate(d_m(m ell/d)).          (1)

Indeed two frequencies t/n and u/m, both in[0,1), are equal precisely
when they are ell/d with the displayed indices. This is a proof by
finite expansion, without a primality or primitive-first-argument
assumption. All shared denominators dividing d remain in (1).

For coprime n,m, P=nm and only ell=0 remains. Therefore exactly

    sum_(h=0)^(nm-1)F_n^circ(h)conjugate(F_m^circ(h))
           =V_n conjugate(V_m).                       (2)

Without the h=0 centering, the same statement has U_n in place of
V_n. In contrast, bare S(A,h;n) has only primitive frequencies x/n;
these are disjoint for different moduli. Multiplication by gamma_n
forms frequency differences x/n-inverse(j)/n, which need not be
primitive and include zero. That is the exact source of the change.

There is also a direct aggregate control. For any finite modulus set,
arbitrary weights alpha_n, and a common period P of every modulus, put

    G(h)=sum_n alpha_n n F_n^circ(h).

Its average over P is exactly sum_n alpha_n V_n. Parseval, or
Cauchy on the finite mean, gives

    |sum_n alpha_n V_n|^2
            <=1/P sum_(h=0)^(P-1)|G(h)|^2.             (3)

The constant Fourier coefficient on the right is already the desired
weighted row total. A bound on the right would be a substantive new
estimate; it cannot be obtained by declaring the weighted different-
modulus rows orthogonal. Formula (3) neither asserts that such a
bound is impossible nor claims that the original total is large.

For the actual flat component alpha_n=chi4(g)chi4(n)W(X/(gnD)),
the left side retains both character directions. Summing the analogous
finite construction over all g also retains their exact coefficients.
The common-period statement is algebraic: the potentially enormous
lcm is not granted as a cheap physical frequency completion, and the
literal row h-ranges still require their original windows.

## 4. First unsupported application step

One may not combine the bare-S common-period cancellation with the
actual h-dependent gamma_n as if it were a constant row coefficient.
Nor may one remove the safe column h=0 and infer removal of the
constant Fourier coefficient of F_n. Equations (1)--(3) show exactly
what remains. A short-window estimate additionally needs the complete
window transform, since no common-period averaging has occurred there.

No bound at the physical quarter scale or dual three-quarter scale
is proved by these identities. They leave the full signed vector
problem open and do not replace it by an unestimated smaller success.

## 5. Exact controls and outcomes

Take distinct coprime odd primes p,q, A=0, and in each modulus take
the single coefficient b(1)=1. Then U_n=1, z_n=phi(n)/n=1-1/n,
and V_n=1/n. Equation (2) gives a strictly positive complete centered
cross-correlation 1/(pq), although the bare Kloosterman cross-correlation
is zero. This finite example has a deliberately different coefficient
vector; it is not a counterexample for the actual physical symbol.

Empty coefficient collections make every quantity zero. For n=m,
(1) is the usual Parseval identity P sum_t |d_n(t)|^2. Noncoprime
moduli retain all d shared frequencies rather than only the constant.
The h=0 subtraction is exactly one residue per row; no positive h
that is zero modulo a different denominator is accidentally deleted.
All inverse representative changes introduce integral phases. No
numerical experiment or external theorem was used.

## 6. Dependencies and provenance

Conductor, round222; graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Dependencies: the exact row definitions and self-return in accepted
proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md,
and Sections2,3.4--3.6 of the143 level-four embedding report. The finite
proof above was derived independently before reading the current
statement-only report or either attack report. Its main control was
sent to the joint-cross-modulus role for an independent application
check. No claim is promoted until final-hash review and State Patch.

## 7. Recommended state effect

Retain as an exact weighted-orthogonality scope control after review.
No accepted graph or exponent change follows. It rejects a free
orthogonality inference for the actual weighted rows, not the complete
signed vector theorem, the UNBAL target or the full quarter goal.
