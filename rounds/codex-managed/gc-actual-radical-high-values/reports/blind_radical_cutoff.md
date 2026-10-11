# Round216: independent squarefree cutoff and finite-window audit

## 1. Result

Campaign: `gc-actual-radical-high-values`. Task: `blind_radical_cutoff`.
Role: statement-only independent rederivation. Status: blind report, not an
accepted state change. Generated: 2026-09-28. Supplied metadata-only graph
SHA256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
No graph file was read or verified.

The packet implies, uniformly in \(T\ge2\), \(Q\ge1\), and \(R\in\mathbb R\),

\[
 \sup_R|L_Q(R)|\ll_C Q^{1/4}(1+\log Q),                 \tag{1}
\]

and the sum of the absolute values of **all** exact-resonance terms in the
twelfth cosine expansion of \(Z_Q\) satisfies

\[
 E_{12}^{\rm abs}(T,Q)\ll_C Q^{-3}(1+\log(2Q))^{18}.   \tag{2}
\]

Consequently these quantities are respectively

\[
 O_{C,\eta}(Q^{1/4+\eta}),\qquad
 O_{C,\eta}(Q^{-3+\eta})\quad(\eta>0).                 \tag{3}
\]

The second estimate includes all \(2^{12}\) independently chosen cosine
signs, all ordered index tuples, repetitions, and exact relations that are
not pairings. Radical independence is proved below, not assumed as a
probabilistic model.

Put \(Q=\lfloor T^{2/5}\rfloor\), \(V=T^{13/125}\), and

\[
 \mathcal M_Z(U)=\int_{|Z_Q(R)|>U}w(R/T)|Z_Q(R)|^{12}\,dR.
\]

For all sufficiently large \(T\), with an explicit head-size condition
below,

\[
 \int_{|B_T|>V}w(R/T)|B_T|^{12}\,dR
 \le 2^{12}\mathcal M_Z(V/2).                         \tag{4}
\]

The exact-resonance contribution to the unrestricted finite-window moment
is bounded by

\[
 T\widehat w(0)E_{12}^{\rm abs}(T,Q)
 \ll_{C,w}T^{-1/5}(1+\log(2T))^{18}.                  \tag{5}
\]

Equation (5) does **not** bound either the unrestricted moment or the
high-value moment on the displaced window. The precise nonzero-frequency
remainder is displayed in Section 3. Under only the packet's coefficient
envelope, there exist even one fixed admissible coefficient sequence and a
fixed admissible \(\Psi\) for which, along unbounded \(T_j\), both relevant
high-value moments are \(\gg T_j^2\). Thus a finite-window high-tail estimate
at the scale (5) cannot follow from this envelope and the exact-resonance
estimate alone. No arithmetic interpretation of the coefficients is used.

## 2. Exact statements and hypotheses

Throughout, \(e(t)=\exp(2\pi i t)\), \(T\ge2\), \(Q\ge1\) is real unless
specified otherwise, and \(\Psi\) is the fixed real even Schwartz function
in the packet, with \( |\Psi|\le1\). The real coefficients are fixed and obey

\[
 |a_n|\le C\tau(n)n^{-3/4}.
\]

Write each positive integer uniquely as \(n=ds^2\), \(d\) squarefree and
\(s\ge1\), and set

\[
 b_{d,s}=a_{ds^2}\Psi(s\sqrt{d/T}),\qquad
 A_d=\sum_{s\ge1}|b_{d,s}|.
\]

All \(s\ge1\) remain present on both sides of the squarefree cutoff:

\[
 L_Q(R)=\sum_{\substack{d\le Q\\d\ {\rm squarefree}}}
       \sum_{s\ge1}b_{d,s}\cos(2\pi Rs\sqrt d-3\pi/4),
\]

\[
 Z_Q(R)=\sum_{\substack{d>Q\\d\ {\rm squarefree}}}
       \sum_{s\ge1}b_{d,s}\cos(2\pi Rs\sqrt d-3\pi/4).
\]

For an ordered twelve-tuple \(\boldsymbol\iota=((d_j,s_j))_{j=1}^{12}\)
with squarefree \(d_j>Q\), and independently chosen
\(\boldsymbol\epsilon\in\{+1,-1\}^{12}\), define

\[
 \Omega(\boldsymbol\iota,\boldsymbol\epsilon)
       =\sum_{j=1}^{12}\epsilon_js_j\sqrt{d_j},\qquad
 p(\boldsymbol\epsilon)=e\!\left(-\frac38\sum_{j=1}^{12}\epsilon_j\right).
\]

The signed exact coefficient and its absolute upper certificate are

\[
 E_{12}^{0}=2^{-12}\sum_{\boldsymbol\epsilon}
       \sum_{\boldsymbol\iota:\Omega=0}
       p(\boldsymbol\epsilon)\prod_{j=1}^{12}b_{d_j,s_j},               \tag{6}
\]

\[
 E_{12}^{\rm abs}=2^{-12}\sum_{\boldsymbol\epsilon}
       \sum_{\boldsymbol\iota:\Omega=0}
       \prod_{j=1}^{12}|b_{d_j,s_j}|.                                \tag{7}
\]

The sums in (6)--(7) converge absolutely for fixed \(T\). In particular,
(2) also bounds \( |E_{12}^{0}|\). In fact \(E_{12}^{0}\ge0\), as proved
below, although its individual terms need not be nonnegative.

The weight is exactly the packet's fixed nonnegative smooth compactly
supported \(w\), supported in ([1/2,2]) and equal to one on
\([1/\sqrt2,\sqrt3]\). Its Fourier transform convention is

\[
 \widehat w(\xi)=\int_{\mathbb R}w(u)e(-u\xi)\,du.                   \tag{8}
\]

In particular \(\widehat w(0)=\int w>0\); no evenness of \(w\) is assumed.
All \(R\)-integrals below are over \(\mathbb R\), with their support imposed
by (w(R/T)).

## 3. Proof and derivation

### 3.1. Full class sums and the head

The elementary divisor inequalities

\[
 \tau(ds^2)\le\tau(d)\tau(s^2),\qquad
 \tau(s^2)\le\tau_3(s)
\]

give

\[
 A_d\le Kd^{-3/4}\tau(d),\qquad
 K=C\sum_{s\ge1}\tau(s^2)s^{-3/2}
   \le C\zeta(3/2)^3.                                               \tag{9}
\]

Here \(\tau_3(s)=\sum_{uvw=s}1\); the second inequality follows prime by
prime from \(2k+1\le(k+1)(k+2)/2\). The displayed zeta identity follows
by multiplying three absolutely convergent positive series. Thus (9)
retains the entire infinite \(s\)-tail and is independent of \(T\).

For \(Q\ge1\),

\[
 \begin{aligned}
 \sum_{d\le Q}\tau(d)d^{-3/4}
 &=\sum_{uv\le Q}(uv)^{-3/4}\\
 &\le4Q^{1/4}\sum_{u\le Q}u^{-1}
 \le4Q^{1/4}(1+\log Q).
 \end{aligned}                                                       \tag{10}
\]

Discarding the squarefree restriction in this positive upper bound proves
(1), with the explicit constant (4K). The cutoff is on \(d\), not on
\(n\) or \(s\); in particular (10) does not truncate \(n\) at \(T\).

### 3.2. Radical independence, including \(d=1\)

For distinct primes \(p_1,\ldots,p_r\), the \(2^r\) numbers

\[
 u_S=\sqrt{\prod_{i\in S}p_i}\qquad(S\subseteq\{1,\ldots,r\})
\]

form a rational basis of \(\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_r})\),
and each independent sign change of the prime square roots extends to a
field automorphism. Here is an induction proving both assertions.

The case \(r=0\) is \(\mathbb Q\). Suppose the assertions hold for (r-1)
and put \(K_{r-1}=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_{r-1}})\).
If some \(x\in K_{r-1}\) satisfied \(x^2=p_r\), every sign automorphism
\(\sigma\) would satisfy \(\sigma(x)=\pm x\). Expanding \(x\) in the
inductive basis, its simultaneous eigenvector property for the individual
sign flips forces at most one nonzero basis coefficient: two distinct
subsets have different signs under at least one flip. Hence
\(x=c u_S\) for rational \(c\). But \(c^2\prod_{i\in S}p_i=p_r\) is
impossible, since its two sides have respectively even and odd valuations
at \(p_r\). Thus \(X^2-p_r\) is irreducible over \(K_{r-1}\). Adjoining
its root doubles the degree and gives the stated basis. Each old
automorphism extends by fixing this new root (the polynomial has rational
coefficients), and the new-root sign flip is another automorphism. This
closes the induction.

Any finite collection of distinct positive squarefree \(d\)'s is a subset
of the \(u_S\) for the finite set of primes dividing those \(d\)'s.
Therefore their square roots are rationally linearly independent. The
empty subset supplies \(d=1\), so that case is included.

It follows, exactly, that

\[
 \Omega=0\quad\Longleftrightarrow\quad
 \sum_{j:d_j=d}\epsilon_js_j=0\quad\text{for every occurring }d.
                                                                        \tag{11}
\]

Since \(s_j\ge1\), no class can occur exactly once in an exact relation.
Equation (11) does not say that classes occur an even number of times or
that each within-class relation is a pairing.

### 3.3. The complete absolute exact-resonance estimate

Set

\[
 S_2=\sum_{\substack{d>Q\\d\ {\rm squarefree}}}A_d^2.
\]

The prime-power inequality \((k+1)^2\le\binom{k+3}{3}\) gives
\(\tau(d)^2\le\tau_4(d)\), and elementary divisor summation gives

\[
 \sum_{d\le x}\tau_4(d)\le x(1+\log x)^3\qquad(x\ge1).
\]

Splitting \(d>Q\) into (\(2^jQ,2^{j+1}Q]\) yields

\[
 S_2\le K^2 C_4 Q^{-1/2}(1+\log(2Q))^3,\qquad
 C_4=2\sum_{j\ge0}2^{-j/2}(j+1)^3<\infty.                            \tag{12}
\]

This handles the complete infinite \(d\)-tail with no \(T\)-dependent
termination. Also, for every real \(r\ge2\),

\[
 \sum_{d>Q}A_d^r\le S_2^{r/2}.                                      \tag{13}
\]

Indeed each \(A_d\le\sqrt{S_2}\), so multiply \(A_d^2\) by that bound
to the power (r-2) and sum.

Partition the twelve labeled positions by equality of their squarefree
classes. By (11) an exact tuple gives a set partition \(\pi\) having no
singleton block. For a given such partition, discard the within-block
integer equations, sum every \(s_j\ge1\), and then discard the condition
that distinct blocks carry distinct \(d\)'s. For each fixed sign vector
the resulting upper bound is

\[
 \prod_{B\in\pi}\left(\sum_{d>Q}A_d^{|B|}\right)
 \le S_2^{\sum_B|B|/2}=S_2^6.                                      \tag{14}
\]

There are at most \(12^{12}\) set partitions of twelve positions. Summing
all \(2^{12}\) sign vectors cancels the factor \(2^{-12}\) in (7).
Consequently

\[
 E_{12}^{\rm abs}\le12^{12}S_2^6
 \le12^{12}K^{12}C_4^6 Q^{-3}(1+\log(2Q))^{18}.                      \tag{15}
\]

Nothing in (14) distinguishes pairings from blocks of sizes 3, 4, ..., 12;
all are retained. The expansion uses labeled positions throughout, so no
unordered-tuple multiplicity is lost. Repeated \(s\)'s are permitted.

### 3.4. Exact torus averaging and the signed coefficient

For finitely many nonzero \(b_{d,s}\), introduce one torus variable
\(\theta_d\in\mathbb R/\mathbb Z\) for each occurring squarefree class and
put

\[
 F(\boldsymbol\theta)
 =\sum_{d,s}b_{d,s}\cos(2\pi s\theta_d-3\pi/4).
\]

Integration of \(F^{12}\) over this finite product torus retains precisely
the relations in (11). Thus it equals (6), is nonnegative, and is bounded
by (7). This is an exact deterministic Fourier identity, not a claim of
independence of the finite-radius variables \(R\sqrt d\pmod1\).

For fixed \(T\), absolute convergence permits finite truncations of all
coefficients and then passage to the limit in the coefficients of the
twelfth power. Hence

\[
 0\le E_{12}^{0}\le E_{12}^{\rm abs}.                                \tag{16}
\]

Equally, for this one fixed (T,Q),

\[
 \lim_{Y\to\infty}\frac1Y\int_0^Y Z_Q(R)^{12}\,dR=E_{12}^{0}.        \tag{17}
\]

To prove (17), integrate each exponential: a nonzero fixed frequency has
mean tending to zero, and the absolutely summable coefficient products
dominate the passage to the limit. Equation (17) supplies no uniform rate
when both the coefficients and the averaging interval change with \(T\).

### 3.5. Finite displaced window: the full remainder

The exact cosine expansion is

\[
 Z_Q(R)^{12}=2^{-12}\sum_{\boldsymbol\epsilon\in\{\pm1\}^{12}}
 \sum_{\substack{d_1,\ldots,d_{12}>Q\ {\rm squarefree}\\
                  s_1,\ldots,s_{12}\ge1}}
 p(\boldsymbol\epsilon)\left(\prod_{j=1}^{12}b_{d_j,s_j}\right)
 e(R\Omega).
\]

Using \(R=Tu\) and (8),

\[
 \int w(R/T)e(R\Omega)\,dR=T\widehat w(-T\Omega).                    \tag{18}
\]

Since \(Z_Q\) is real, \(Z_Q^{12}=|Z_Q|^{12}\). Therefore

\[
 \int w(R/T)|Z_Q(R)|^{12}\,dR
   =T\widehat w(0)E_{12}^{0}+\mathcal R(T,Q),                        \tag{19}
\]

where the complete nonzero-frequency remainder is

\[
 \boxed{
 \begin{aligned}
 \mathcal R(T,Q)=\frac{T}{2^{12}}
 &\sum_{\boldsymbol\epsilon\in\{\pm1\}^{12}}
 \sum_{\substack{d_1,\ldots,d_{12}>Q\ {\rm squarefree}\\
                  s_1,\ldots,s_{12}\ge1\\
                  \sum_{j=1}^{12}\epsilon_js_j\sqrt{d_j}\ne0}}
 e\!\left(-\frac38\sum_{j=1}^{12}\epsilon_j\right)\\
 &\quad\times\prod_{j=1}^{12}
       \left[a_{d_js_j^2}\Psi(s_j\sqrt{d_j/T})\right]
 \widehat w\!\left(-T\sum_{j=1}^{12}\epsilon_js_j\sqrt{d_j}\right).
 \end{aligned}}                                                     \tag{20}
\]

All sums and integrals in this identity can be interchanged by absolute
convergence at fixed \(T\). Pairing a sign vector with its negative
conjugates both its phase and its Fourier factor, proving that
\(\mathcal R(T,Q)\) is real. Since \(w\) is displaced and not assumed
even, its Fourier kernel is generally complex. Replacing it by a positive
indicator, an exact-delta symbol, or an even kernel is not justified.

Smoothness gives \( |\widehat w(\xi)|\ll_{w,A}(1+|\xi|)^{-A}\), but no
decay follows when \(0<|T\Omega|\ll1\). An absolute upper certificate is

\[
 \mathcal A_{\rm off}(T,Q)=\frac{T}{2^{12}}
 \sum_{\boldsymbol\epsilon}\sum_{\boldsymbol\iota:\Omega\ne0}
 \prod_j|b_{d_j,s_j}|\,|\widehat w(-T\Omega)|,
 \qquad |\mathcal R|\le\mathcal A_{\rm off}.                          \tag{21}
\]

A lower bound for (21) is not a lower bound for (20), for (19), or for a
high-value moment. The actual-moment lower bound in Section 5 is instead
proved directly from a positive peak and continuity.

### 3.6. Integer cutoff and exact head threshold

For \(Q=\lfloor T^{2/5}\rfloor\) and \(T\ge2\),

\[
 \tfrac12T^{2/5}\le Q\le T^{2/5},\qquad Q\ge1.                       \tag{22}
\]

Thus (15) and (18) imply (5), with no loss from rounding. Write
\(H=\sup_R|L_Q(R)|\). One convenient completely explicit sufficient
threshold is obtained from

\[
 1+\log x\le(1+200/e)x^{1/200}\qquad(x\ge1).
\]

With

\[
 K_* =4C\zeta(3/2)^3(1+200/e),\qquad
 T_* =\max\{2,(2K_*)^{500}\},
\]

we have

\[
 H\le K_*T^{51/500},\qquad
 V=T^{52/500},\qquad H/V\le K_*T^{-1/500}\le\tfrac12
 \quad(T\ge T_*).                                                    \tag{23}
\]

The sharper logarithmic version is \(H/V\ll_C T^{-1/250}(1+\log T)\).
Both verify the strict exponent gap; neither calls the head bounded
independently of \(Q\).

### 3.7. High-event inclusion and every mixed term

The general deterministic statement is as follows. If \(0\le H<V\), set
\(U=V-H>0\). Then the actual event inclusion is

\[
 \{|B_T|>V\}\subseteq\{|Z_Q|>V-H\}=\{|Z_Q|>U\}.                    \tag{24}
\]

This follows from \( |Z_Q|\ge|B_T|-|L_Q|>V-H\), with the strict
inequality preserved. Nonnegativity of \(w\), the triangle inequality,
and the binomial theorem give all thirteen costs:

\[
 \begin{aligned}
 \int_{|B_T|>V}w(R/T)|B_T|^{12}\,dR
 &\le\sum_{k=0}^{12}\binom{12}{k}H^{12-k}
       \int_{|Z_Q|>U}w(R/T)|Z_Q|^k\,dR\\
 &\le\sum_{k=0}^{12}\binom{12}{k}
       \left(\frac H U\right)^{12-k}\mathcal M_Z(U)\\
 &=\left(1+\frac H U\right)^{12}\mathcal M_Z(U)
 =\left(\frac V{V-H}\right)^{12}\mathcal M_Z(V-H).                  \tag{25}
 \end{aligned}
\]

For \(k=0\), the second line uses
\(\int_{|Z_Q|>U}w\le U^{-12}\mathcal M_Z(U)\); for every \(1\le k<12\)
it uses \(|Z_Q|^k\le U^{k-12}|Z_Q|^{12}\) on that event. Thus no mixed
term, constant term, or high-event measure has been silently discarded.

More generally if \(H\le\theta V\), \(0\le\theta<1\), then

\[
 \{|B_T|>V\}\subseteq\{|Z_Q|>(1-\theta)V\},\qquad
 \int_{|B_T|>V}w|B_T|^{12}
 \le(1-\theta)^{-12}\mathcal M_Z((1-\theta)V).                      \tag{26}
\]

Taking \(\theta=1/2\) and (23) proves (4). A tail bound only at the
unshifted threshold \(V\) does not suffice: it need not control the band
\(V-H<|Z_Q|\le V\). No event inclusion from (24) into \({|Z_Q|>V}\)
was proved or used.

If the input is a distributional high-value estimate rather than a tail
moment, put

\[
 D_Z(v)=\int_{|Z_Q|>v}w(R/T)\,dR.
\]

Then the exact layer-cake formula is

\[
 \mathcal M_Z(U)=U^{12}D_Z(U)+12\int_U^\infty v^{11}D_Z(v)\,dv.       \tag{27}
\]

Thus a bound for \(D_Z(v)\) must cover every \(v\ge U\), or supply an
upper cutoff and a bound on the remaining range. A single measure bound
at \(U\) alone does not bound the twelfth tail moment. For example a pure
\(D_Z(v)\le Av^{-12}\) estimate contributes a logarithm up to the upper
cutoff in (27); dropping that integral is invalid.

### 3.8. Schwartz tails, finite upper cutoff, and bounded \(T\)

For every fixed \(A>0\),

\[
 |\Psi(x)|\le C_{\Psi,A}(1+|x|)^{-A}.
\]

Using (10) for \(n\le T\), and the dyadic blocks
\(2^jT<n\le2^{j+1}T\) with \(A=2\) for the remainder, proves

\[
 \sum_{n\ge1}|a_n\Psi(\sqrt{n/T})|
 \le C_{C,\Psi}T^{1/4}(1+\log(2T))=:W_T.                            \tag{28}
\]

For clarity, each tail block is bounded by a constant times
\(T^{1/4}2^{-3j/4}(1+\log(2T)+j)\), whose sum converges. This verifies
the full \(n\)-tail, the uniformity used on compact \(T\)-ranges, and a
legitimate upper endpoint \(D_Z(v)=0\) for \(v\ge W_T\). The inequalities
\(|B_T|,|Z_Q|,|L_Q|\le W_T\) all follow by taking subsets of the same
absolute coefficient sum.

For \(2\le T<T_*\), (23) need not hold. Directly,

\[
 \int_{|B_T|>V}w(R/T)|B_T|^{12}\,dR
 \le T\|w\|_1W_T^{12}<\infty.                                     \tag{29}
\]

Consequently an asymptotic conclusion \(O(T^\beta)\) deduced from a
high-tail input for \(T\ge T_*\) extends to all \(T\ge2\) by enlarging
its constant on the compact remaining range, for any fixed real
\(\beta\). A literal bound solely by \(2^{12}\mathcal M_Z(V/2)\) for
every \(T\ge2\) is not asserted when the head condition fails. One may
instead write (4) for \(T\ge T_*\) and (29) for \(2\le T<T_*\), or add
the compact-range term (29) with its indicator.

## 4. First doubtful or unproved step

There is no unproved step in (1)--(29). The first missing input in a
proposed application of (4) is a bound on

\[
 \mathcal M_Z(V/2)=
 \int_{|Z_Q|>V/2}w(R/T)|Z_Q|^{12}\,dR.                              \tag{30}
\]

The exact coefficient supplies only the first term of (19). For example,
to obtain a tail bound of the diagonal scale from the unrestricted
moment, one would additionally need an upper bound of the type

\[
 \mathcal R(T,\lfloor T^{2/5}\rfloor)
 \ll T^{-1/5}(1+\log(2T))^{18},                                    \tag{31}
\]

or another estimate sufficient for the desired larger target. A bound on
\(|\mathcal R|\) would be stronger than the one-sided bound required.
Alternatively one could prove (30) directly without bounding the entire
moment. None of these inputs follows merely from \(\Omega\ne0\),
Schwartz decay of \(\widehat w\), or exact torus averaging.

The analytical peak control below refutes (31) under the packet's
envelope alone, even for one fixed coefficient sequence. The conclusion
is limited to this envelope-only inference; it does not refute a tail
estimate that exploits additional, explicitly proved structure in some
other specified sequence.

## 5. Required analytical controls and outcomes

### 5.1. The class \(d=1\)

Its complete contribution is

\[
 \sum_{s\ge1}a_{s^2}\Psi(s/\sqrt T)
       \cos(2\pi Rs-3\pi/4),
\]

and its absolute value is at most \(C\zeta(3/2)^3\) by (9).
It belongs to \(L_Q\) for every allowed \(Q\ge1\). It is a full harmonic
series with many within-class exact relations. It is neither omitted nor
mistaken for several independent squarefree classes. **Outcome: passes.**

### 5.2. Nonpairing exact relations and signed phases

In any one class, \(1+1-2=0\) is an allowed three-entry exact relation.
Choose four distinct squarefree classes \(d>Q\) and use this relation in
each. The resulting twelve-entry exact relation has four blocks of size
three and has no pairing inside any block. Its total sign sum is (4),
so its cosine phase is \(e(-3\cdot4/8)=-1\). With positive nonzero
coefficients for these indices it is an actual negative term in (6).
Equation (15) includes it through the four size-three blocks; (16) does
not rely on positivity of individual exact terms. **Outcome: passes.**

### 5.3. A nonzero near-relation inside the natural \(n\asymp T\) range

Let \(T=M\) be a sufficiently large integer and \(Q=\lfloor M^{2/5}\rfloor\).
The number of integers \(n\le2M\) whose squarefree part is at most \(Q\)
is at most

\[
 \sum_{d\le Q}\left\lfloor\sqrt{2M/d}\right\rfloor
 \le2\sqrt{2MQ}=O(M^{7/10}).                                       \tag{32}
\]

Each such integer spoils at most three possible starts \(N\). Therefore
some \(N\in[M,2M-2]\cap\mathbb Z\) has all of (N,N+1,N+2) with
squarefree parts greater than \(Q\). For these retained tail indices,

\[
 \begin{aligned}
 \Omega_*&=\sqrt N+\sqrt{N+2}-2\sqrt{N+1}\\
 &=-\frac14\int_0^1\int_0^1(N+u+v)^{-3/2}\,du\,dv\ne0,
 \end{aligned}
\]

and

\[
 \tfrac14(N+2)^{-3/2}\le|\Omega_*|\le\tfrac14N^{-3/2},
 \qquad |M\Omega_*|\le\tfrac14M^{-1/2}.                            \tag{33}
\]

Add four canceling pairs of retained indices to make twelve entries.
All twelve signs remain legitimate independent choices in (20), and the
sign sum of this example is zero. Hence its phase is (1), while
\(\widehat w(-M\Omega_*)\to\widehat w(0)>0\).
This establishes that nonzero frequencies need not lie in the decaying
part of the Fourier kernel, even without using \(n\gg T\).
An example such as \(\Psi(x)=e^{-x^2}\) permits nonzero weights at every
one of these indices. This observation alone is only a frequency and
certificate control, not a lower bound on the signed moment.
**Outcome: exact-to-finite-window substitution fails.**

### 5.4. Direct coherent-peak control: actual high-tail moments can be large

This control uses \(\Psi(x)=e^{-x^2}\), which meets every packet
hypothesis, and coefficients with \(C=1\). First fix an arbitrarily large
integer \(M\), and let

\[
 I_M=\{n\in[M,2M]\cap\mathbb Z:
             \text{squarefree part of }n>\lfloor M^{2/5}\rfloor\}.
\]

By (32), \(m=|I_M|\ge M/2\) for sufficiently large \(M\). For each \(n\),
integration of a squared cosine on \(J=[M,3M/2]\) gives

\[
 \int_J\cos^2(2\pi R\sqrt n-3\pi/4)\,dR
 =|J|/2+O(n^{-1/2}).
\]

Thus there is \(R_0\in J\) with

\[
 \sum_{n\in I_M}\cos^2(2\pi R_0\sqrt n-3\pi/4)\ge m/3.
\]

Choose the fixed, finitely supported real coefficients

\[
 a_n=n^{-3/4}\cos(2\pi R_0\sqrt n-3\pi/4)\quad(n\in I_M),
 \qquad a_n=0\quad(n\notin I_M).
\]

They satisfy \( |a_n|\le n^{-3/4}\le\tau(n)n^{-3/4}\). At \(T=M\),
\(L_Q=0\), and

\[
 Z_Q(R_0)=B_M(R_0)
 =\sum_{n\in I_M}n^{-3/4}e^{-n/M}
         \cos^2(2\pi R_0\sqrt n-3\pi/4)
 \ge c_0M^{1/4},\qquad c_0=e^{-2}2^{-3/4}/6.                       \tag{34}
\]

The derivative of this block obeys

\[
 |Z_Q'(R)|\le2\pi\sum_{n\in I_M}n^{-1/4}e^{-n/M}
 \le4\pi M^{3/4}.                                                  \tag{35}
\]

Therefore on an interval centered at \(R_0\) of radius
\(c_0M^{-1/2}/(8\pi)\),

\[
 Z_Q(R)\ge(c_0/2)M^{1/4}.
\]

That interval lies inside the region \(w(R/M)=1\) for sufficiently large
\(M\), because \(J\subset(M/\sqrt2,\sqrt3M)\) with margins proportional
to \(M\). Since \(1/4>13/125\), all of the interval is above both thresholds
\(V=M^{13/125}\) and (V/2) for large \(M\). Consequently

\[
 \int_{|B_M|>V}w(R/M)|B_M|^{12}\,dR\gg M^2,
 \qquad \mathcal M_Z(V/2)\gg M^2.                                  \tag{36}
\]

These are genuine lower bounds on the actual moments, obtained from
(34)--(35), not from an absolute Fourier certificate.

For completeness the obstruction can be realized by **one fixed
infinite coefficient sequence**, so it does not depend on allowing the
sequence to vary with the asymptotic parameter. Choose sufficiently
rapidly growing integers \(M_1<M_2<\cdots\), with

\[
 \lfloor M_j^{2/5}\rfloor>2M_{j-1}\quad(j\ge2),                     \tag{37}
\]

and on each disjoint \(I_{M_j}\) choose its coefficients by the preceding
construction with its own \(R_j\in[M_j,3M_j/2]\); set all other
coefficients to zero. In selecting \(M_k\), impose for every \(j<k\)

\[
 \sum_{n=M_k}^{2M_k}n^{-3/4}e^{-n/M_j}
 \le 2^{-k}(c_0/4)M_j^{1/4}.                                      \tag{38}
\]

Only finitely many conditions occur at each stage, and each is possible
because its left side is at most \(2M_k^{1/4}e^{-M_k/M_j}\to0\).
At \(T=M_j\), all preceding blocks lie in the head by (37), while all
future blocks together perturb \(Z_Q(R)\), uniformly in \(R\), by at most
\((c_0/4)M_j^{1/4}\), by (38). The current block is at least
\((c_0/2)M_j^{1/4}\) on the interval supplied by (35). Hence the full
tail is at least \((c_0/4)M_j^{1/4}\) there. The full head is
\(O(M_j^{1/10}\log M_j)=o(M_j^{1/4})\) by (1), so \(B_{M_j}\) is at
least \((c_0/8)M_j^{1/4}\) on that same interval for large \(j\).
Equation (36) therefore holds along this unbounded sequence for one
fixed admissible real coefficient sequence.

On the other hand (5) is \(O(M_j^{-1/5}(1+\log(2M_j))^{18})\). Combining
the actual unrestricted-moment lower bound with the exact identity (19)
even gives

\[
 \mathcal R(M_j,\lfloor M_j^{2/5}\rfloor)\gg M_j^2
\]

for all sufficiently large \(j\). Thus (31) is false under the stated
envelope. **Outcome: exact resonance alone cannot supply the displaced
high-tail moment, including when the coefficient sequence is fixed.**

### 5.5. Cutoff, threshold, and averaging controls

* All \(s\)-tails are retained in (9); all \(d>Q\) tails in (12); all
  \(n\)-tails in (28). No sharp \(n\le T\) cutoff is introduced.
* Integer rounding is handled by (22), including the possible value
  \(Q=1\). Small \(T\) uses (29), not an unjustified head-small claim.
* The event transfer uses (V-H), or its lower bound (V/2), with strict
  events and all mixed terms explicitly included in (25).
* Exact torus averaging and fixed-\(T\) infinite-radius averaging are
  (16)--(17). The moving displaced window is (19)--(20); it retains every
  nonzero frequency with its actual Fourier factor.
* Signed phases and signed coefficients remain in (6), (19), and (20).
  The quantities in (7), (15), and (21) are explicitly absolute upper
  certificates. They are never substituted for signed lower bounds.

All controls are analytical. No numerical or symbolic experiment, web
lookup, or external theorem was used. **Outcome: the proved cutoff and
transfer lemmas pass; the envelope-only finite-window inference fails.**

## 6. Dependencies and exact artifacts used

The only files read were:

1. `protocol.md`.
2. `rounds/codex-managed/gc-actual-radical-high-values/briefs/blind_radical_cutoff_statement.md`.

The supplied graph hash is metadata only. No graph, manifest, strategy,
general brief, earlier report, current sibling report, source card,
legacy evidence, or web source was read. The mathematical dependencies
are the packet's hypotheses, elementary divisor identities, the proved
multiquadratic-basis lemma, absolute convergence, Fourier expansion,
and elementary integration and continuity. No arithmetic origin for
\(a_n\), and no circle-problem conclusion, has been inferred.

## 7. Recommended state effect

**Retain** (1)--(3) and the precisely conditional transfer (24)--(29) as
independently derived evidence, subject to the conductor's required seam
reviews and graph validation. **Reject** the inference that the exact
twelfth-resonance coefficient alone gives the finite-window twelfth
high-tail bound under the packet's coefficient envelope. The direct
fixed-sequence control supplies a rigorous no-go result for that
inference. **No state edit and no theorem promotion are performed here.**
The missing application-specific input is an independently proved bound
on (30), or sufficient control of (20), using whatever additional
hypotheses a future explicitly stated application may actually possess.
