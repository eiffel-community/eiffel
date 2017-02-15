# Derived Confidence Level

As mentioned in EiffelConfidenceLevelModifiedEvent, the EiffelConfidenceLevelModifiedEvent declares that an entity has achieved (or failed to achieve) a certain level of confidence, or in a broader sense to annotate it as being applicable or relevant to a certain case (e.g. fit for release to a certain customer segment or having passed certain criteria.

This works well in scenarios where the confidence level can be directly associated with the entity in question. However, there is one scenario that goes beyond this: when you want to keep track of how well a specific entity has worked _in different contexts_.

The problem:

* Assume that you create an artifact A that is subjected to a number of tests and and as a result is given a set of confidence levels (using EiffelConfidenceLevelModifiedEvent).
* This artifact is included in number of other artifacts: C1, C2 and C3.
* How do you keep track on how well A has fared in C1, C2 and C3?

The Eiffel way is to view the confidence levels on the Cs as _derived confidence levels_ on A. In other words the condidence levels on the Cs also applies to A but as derived/computed information.

Example:

* Assume the same set of artifacts as above, i.e. A and the Cs.
* Versions of those are indicated with a v*N* suffx, i.e. A.v1.

1. We now test A.v1 in applicable ways and can set the confidence level CL1(A1.v1) = SUCCESS.
2. A1.v1 is now built into C1.v1, c2.v1 and C3.v1.
3. The Cs are tested and given confidence levels CL2(C1.v1) = SUCCESS, CL2(C2.v1) = FAILURE, CL2(C3.v1) = SUCCESS.
4. At this point the total set of confidence levels on A1.v1 is
  * Direct: CL1(A.v1) = SUCCESS
  * Derived: CL2(C1.v1) = SUCCESS, CL2(C2.v1) = FAILURE, CL2(C3.v1) = SUCCESS
  * ... where the derived confidence levels indicates the contexts A1.v1 has been used in.
5. As there was a problem with C2 a new version, C2.v2, is created, using the same A.v1.
6. V2.v2 passes the tests and get CL2(C2.v2) = SUCCESS
7. At this point the total set of confidence levels on A1.v1 is
  * Direct: CL1(A.v1) = SUCCESS
  * Derived: CL2(C1.v1) = SUCCESS, CL2(C2.v1) = FAILURE, Cl2(C2.V2) = SUCCESS, CL2(C3.v1) = SUCCESS
  * ... C2.v2 is a new context in which A1.v1 has been used.

This generalizes into arbitrary levels of contexts.