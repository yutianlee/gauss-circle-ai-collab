# Statement-only packet: hard-TOP radical-frequency coupling

Let \(X\ge2\),

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
\tag{161.BL1}
\]

and fix one literal half-open polynomial intermediate block
\(1\ll L\ll H\). Let \(\eta_L\) be the fixed height profile,
\(\Phi\) the fixed Vaaler taper, and \(W\) the fixed real compact
endpoint profile. For odd positive \(h\), set

\[
 a_{\rm end}(h,m)=\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right),
\tag{161.BL2}
\]

extended by zero outside \(\lceil h/4\rceil\le m\le h\). The scalar is

\[
 \mathcal T_L^{\rm ns}=
 \sum_{h\ {\rm odd}}\chi_4(h)
 \sum_{\substack{\lceil h/4\rceil\le m\le h\\hm\ne\square}}
 a_{\rm end}(h,m)e(J\sqrt{hm}),
\tag{161.BL3}
\]

and the desired estimate is

\[
 \boxed{|\mathcal T_L^{\rm ns}|\ll_\varepsilon
 L^{3/2}X^\varepsilon.}
\tag{161.BL4}
\]

The square entries have already been removed by a separate target-safe
norm estimate and may not be reintroduced as an orthogonal diagonal.

Put

\[
 C_L(n)=\sum_{\substack{h\mid n,\ h\ {\rm odd}\\
 \sqrt n\le h\le2\sqrt n}}
 \chi_4(h)\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
\tag{161.BL5}
\]

You may use the already proved exact identity and upper bounds

\[
 \mathcal T_L^{\rm ns}=L^{3/2}
 \sum_{\substack{n\asymp L^2\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n),
\tag{161.BL6}
\]

\[
 \sum_n|C_L(n)|^2\ll L^2\log(2L),
\tag{161.BL7}
\]

and, for squarefree \(D>1\),

\[
 \sum_{\operatorname{sf}(n)=D}
 |L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}|
 \ll_\varepsilon(1+L/\sqrt D)L^\varepsilon.
\tag{161.BL8}
\]

These estimates alone give \(L^{2+o(1)}\), not (161.BL4).

Starting only from this statement:

1. write every nonsquare uniquely as \(n=Dt^2\), with \(D>1\)
   squarefree, and derive the exact scalar
   \[
    \sum_{D>1\ {\rm sf}}\sum_t B_D(t)e(tJ\sqrt D),
    \qquad
    B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2);
   \]
2. derive the unique incidence parametrization obtained from
   \(g=(h,m)\), including all coprimality, parity, cone, and support
   conditions;
3. classify exact phase-one channels and prove their correct fixed-centre
   multiplicity, without inferring anything about near resonances;
4. analyze the modulo-one collision family
   \(\|J(\sqrt{D_1}-\sqrt{D_2})\|\) on the actual moving \(t\)-ranges;
5. determine whether the literal two-variable coefficient has a
   cancellation-preserving common-test, tensor, bilinear, or projective
   decomposition whose full norm and collision ledger prove (161.BL4)
   or an owner-complete strict polynomial range; and
6. if not, identify the first exact coefficient, collision, norm,
   fixed-centre, source, or restored-power obstruction.

Test small-\(D\) long channels, large-\(D\) short channels, the
\(t=1\) close-semiprime layer, even \(D\), exact and near resonances,
hard endpoints, and arbitrary real \(J\). A common-coefficient large
sieve is inapplicable unless a literal decomposition of \(B_D(t)\) is
proved and fully priced. Absolute radical summation, center averaging,
smooth-amplitude curvature, reciprocal B-process self-return, divisor
switching, and full-\(r_2\) completion are not new estimates.

Close under exactly one label:
`hard_top_radical_frequency_target`,
`strict_hard_top_radical_frequency_range`, or
`hard_top_radical_frequency_coupling_no_go`. Nothing transfers outside
this one nonsquare polynomial intermediate hard-TOP scalar.
