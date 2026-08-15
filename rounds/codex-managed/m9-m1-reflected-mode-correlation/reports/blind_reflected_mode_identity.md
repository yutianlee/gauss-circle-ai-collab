# 1. Result

At finite Mellin height the functional equation gives an exact reflected
radial integral, but not an M1/M2 complementary sector.  The arithmetic
coefficient is reflected from \(a_z\) to \(a_{-z}\), while the outside
scale/profile symbol remains the original \((u,v)\)-symbol.  Turning that
into the naively reflected symbol requires moving both Mellin contours
through \(u=0\) and \(v=0\); the hard-top and height residues are nonzero.
Thus functional-equation reflection alone supplies no signed cancellation
of the top Perron mode.

# 2. Exact statement and hypotheses

Let \(z=u+v\),
\[
 A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 (D_j/(2\sqrt X))^u(H_j+1)^v,
\quad g_v(x)=x^{-3/4-v/2}e(\sqrt{Xx})\mathbf1_{1\le x\le N_X}^{*}.
\]
Here \(\widehat W_0=\widehat W_+\), the star is symmetric half weight,
and \(\widehat W_+(u)=1/u+\widehat W_{+,r}(u)\).  For \(a,b>0\), finite
\(T\), and initially \(c>1+|\Re z|/2\), put
\[
 I_{j,T}=\frac1{(2\pi i)^2}\int_{a-iT}^{a+iT}
 \int_{b-iT}^{b+iT}A_j(u,v)\sum_na_z(n)g_v(n)\,dv\,du.
\]
If \(G_v(s)=\int_0^\infty g_v(x)x^{s-1}dx\), then, after a finite
radial truncation avoiding poles,
\[
 \sum_na_z(n)g_v(n)=\frac1{2\pi i}\int_{(c)}G_v(s)F_z(s)\,ds.
\]
Writing \(\Lambda_z=C_zF_z\) with the accepted completion and
\(K_z(s)=C_{-z}(1-s)/C_z(s)\), contour displacement gives
\[
 \frac1{2\pi i}\int_{(c)}G_v(s)F_z(s)ds
 =\mathop{\rm Res}_{s=1-z/2}G_v(s)F_z(s)
 +\frac1{2\pi i}\int_{(c)}G_v(1-s)K_z(1-s)F_{-z}(s)ds,
\]
with additional cutoff-boundary half residues when a boundary lies on a
contour.  This identity is understood first on finite rectangles.

# 3. Proof or derivation

Mellin inversion of \(g_v\) and absolute convergence on \(\Re s=c\)
give the first radial integral.  Substitute
\(F_z(s)=K_z(s)F_{-z}(1-s)\), move the \(s\)-line to \(1-c\), and then
set \(s\mapsto1-s\).  The crossed arithmetic pole is
\(s=1-z/2\), from \(\zeta(s+z/2)\), with residue
\(G_v(1-z/2)L(1-z,\chi_4)\).  Gamma poles visible after splitting
\(K_z\) occur at the nonpositive-integer arguments of its two numerator
gamma factors; in the intact completed identity they pair with the
corresponding trivial zeros.  They must not be counted twice.

The reflected outside symbol is still \(A_j(u,v)\).  A divisor-angle
reflection would instead demand
\[
 A_j(-u,-v)=\widehat W_j(-u)\widehat\phi(-v)
 (D_j/(2\sqrt X))^{-u}(H_j+1)^{-v}.
\]
Reaching it crosses \(v=0\), where \(\widehat\phi(v)\) has its constant-term
Mellin residue, and, at the top scale, \(u=0\), where \(1/u\) has residue
one.  The resulting symbol is therefore neither the actual M1 symbol nor
the accepted M2/complementary symbol.

# 4. First doubtful or unproved step

No uniform limit \(T\to\infty\) is proved.  In particular, controlling the
horizontal sides jointly in \(u,v,s\) and the principal-value \(1/u\)
piece is exactly the open maximal-correlation problem.

# 5. Required control test and outcome

Control: retain only the top \(1/u\) term and reflect \(u\mapsto-u\).
Symmetric Perron inversion assigns half weight at equality, but shifting
between the two vertical lines crosses residue \(1\).  Hence the two
pieces do not cancel merely because \(1/(-u)=-1/u\).  Outcome: the proposed
automatic top cancellation fails algebraically.

# 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, Round-15 `synthesis.md`, and Round-14
`synthesis.md`, at graph SHA-256
`7619a6b552347ce9b522018a104aeaa048304e2913ea1e072e583c0a2ace2c86`.

# 7. Recommended state effect

Promote the finite-height reflected-integral identity and retain the
top-Perron correlation as open.  Reject any claim that coefficient
reflection alone creates an actual complementary M1/M2 sector or cancels
the \(1/u\) mode.  Recommended effect: **retain/no-go**, not proof of GAR.
