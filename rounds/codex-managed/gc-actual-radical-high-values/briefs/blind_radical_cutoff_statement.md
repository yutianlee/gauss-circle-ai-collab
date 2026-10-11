# Round216 isolated squarefree-cutoff packet

Read only this packet and protocol.md. No graph, manifest, strategy,
earlier proof/report, sibling, web or source card. Write only
reports/blind_radical_cutoff.md in this campaign; seven numbered
protocol sections and stop. Metadata-only graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

Use e(t)=exp(2pi i t). Let T>=2 real and Psi be a fixed real even
Schwartz function with |Psi|<=1. Let real fixed coefficients a_n satisfy
|a_n|<=C tau(n)n^(-3/4), where tau is the divisor function. Define

    B_T(R)=sum_(n>=1) a_n Psi(sqrt(n/T))
                                  cos(2pi R sqrt(n)-3pi/4).

Every series is absolutely convergent for fixedT. Write n=d s^2
uniquely, with d squarefree. For real Q>=1 let L_Q be the complete
part withd<=Q, and Z_Q=B_T-L_Q the part withd>Q; both keep all s>=1.
Let w be fixed nonnegative smooth supported in[1/2,2], equal to1 on
[1/sqrt(2),sqrt(3)]. In eventual comparisons put Q=floor(T^(2/5))
and V0=T^(13/125).

Independently derive explicit power bounds for sup_R|L_Q(R)| and
for the absolute exact-resonance coefficient of the twelfth moment
ofZ_Q, uniformly inT. Include all twelve independently chosen cosine
signs and ordered indices, repeated classes and nonpairing relations.
Prove whatever radical independence is needed rather than treating
different classes as independent random variables. Restore the factor
T and Fourier convention when integrating againstw(R/T).

Derive a rigorous complete transfer from a bound on the high-value tail
ofZ_Q to integral_(|B_T|>V0)w(R/T)|B_T|^12. State the threshold
constants, actual event inclusion, head size requirement, integerQ,
boundedT treatment and all mixed-term costs. Test whether the exact
resonance estimate alone gives such a tail moment on the displaced
finite window. Write the full nonzero-frequency remainder explicitly,
including all signs and the full Fourier kernel, and explain the first
unproved estimate. A lower bound on an absolute upper certificate must
not be labeled a lower bound on the signed moment.

Analytical controls should include d=1, a nonpairing exact relation,
an admissible nonzero near-relation if useful, every cutoff/tail, and
the distinction between exact torus averaging and finite-radius
averaging. No numerical experiment or external source is needed.
Do not infer an actual arithmetic origin for a_n or a circle theorem.
