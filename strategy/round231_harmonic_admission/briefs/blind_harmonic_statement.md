# Isolated complete harmonic-pooling statement

Read only this statement, your own brief and protocol.md. No graph, history, sibling report or source search. These are supplied hypotheses, not claims you need retrieve elsewhere.

Let Psi be the restriction to the real axis of an entire function, real even Schwartz on R, with Psi(0)=1 and |Psi|<=1. Fix nonnegative smooth w supported[1/2,2] with integral>0. For squarefree positive integers d let c(d,s)=r2(ds^2), where r2(n)=4 sum_(k|n)chi4(k). You may assume c(d,s)>=0 and c(d,s)<=r2(d)tau(s^2), with c(d,1)=r2(d). Define
 f_d(R)=d^(-3/4) sum_(s>=1)c(d,s)s^(-3/2)Psi(s sqrt(d/T))cos(2pi R s sqrt(d)-3pi/4),
 C_harm(T)=sum_(ordered pairwise distinct squarefree d_j>floor(T^(2/5))) |integral w(R/T) product_(j=1)^12 f_(d_j)(R)dR|.
Assume the elementary bounds r2(n)<=C_eta n^eta, sum_(n<=x)r2(n)<=Cx, and for EVERY fixed 0<u<v, sum_(uT<=d<=vT,d squarefree) r2(d)>=c_(u,v)T for all sufficiently large realT. Constants may depend on fixed u,v. Also sum_s tau(s^2)s^(-3/2) is finite. All sums are absolutely convergent at fixedT.

Prove or refute the assertion C_harm(T)>=c_(Psi,w)T^(5/2) for all sufficiently large realT. Analyze the actual full harmonic sum; a lower bound before harmonic pooling cannot imply this. Retain the possibility that Psi changes sign, all common harmonic multiples, all mixed harmonic vectors, and the entire infinite tail. If the asserted lower bound is unprovable from the hypotheses, identify an exact counterexample or first missing step instead of assuming it. No numerical experiment. This is a statement-only proof challenge, with no claimant derivation supplied. It does not ask for a lower bound on the signed sum over squarefree-label tuples.
