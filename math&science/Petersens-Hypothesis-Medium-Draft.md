# Does Nature Use Wilson Primes? An Open Challenge

*Petersen’s hypothesis asks whether an obscure number-theoretic property has an intrinsic role in a natural mechanism. Here is what would count as a counterexample.*

By Claudia G. Petersen

5. 13. 563.

Three small numbers, one unusually demanding membership rule, and a question I would like someone to help answer: does nature ever depend on their being Wilson primes?

I have published a short research note, **Wilson primes in nature**, setting out what I call **Petersen’s hypothesis**. It proposes that no naturally occurring physical or biological process has an intrinsic generating mechanism in which the Wilson-prime condition plays an essential role in determining observable behaviour.

That is a broad claim. The useful part is making the challenge precise enough for someone to bring evidence against it.

If you know a natural mechanism that meets the criteria below—or earlier work establishing one—I would like to see it.

## The mathematical starting point

A prime number p is a Wilson prime when:

**p² divides ((p − 1)! + 1).**

The exclamation mark means factorial: multiply all the positive integers up to p − 1. Add one. For a Wilson prime, the result is divisible by the square of the prime.

For 5, this is pleasantly manageable:

**4! + 1 = 24 + 1 = 25 = 5².**

The three known examples are **5, 13 and 563**, recorded in [OEIS A007540](https://oeis.org/A007540). Costa, Gerbicz and Harvey’s [exhaustive search below 20 trillion](https://arxiv.org/abs/1209.3436) found no further examples.

Their scarcity makes them interesting. It does not imply that they encode the universe, or that mathematics must have a physical purpose. A number can satisfy a definition without being required to operate a butterfly, a star or anything else.

Still, whether this particular property has a natural role is a question worth asking carefully.

## Finding the numbers is not enough

Imagine observing something with five parts, thirteen repetitions and 563 measurable states. Intriguing? Certainly. A demonstrated Wilson-prime mechanism? Not yet.

Those numbers can appear for unrelated reasons. We can also change units, choose labels, select observations or adjust formulas until a numerical resemblance appears. With enough freedom, finding a resemblance becomes easy.

The challenge concerns the **defining property**. What in the mechanism makes Wilson primality matter? Why would the system behave differently if the relevant mathematical condition were absent?

A derivation using a provably equivalent condition would count. Nature does not have to write “Wilson prime” on the apparatus.

## What would count as a counterexample?

The paper asks for five connected pieces of evidence:

1. **An independently identified phenomenon.** Reproducible observations, or independent confirmation where repetition is impossible. The system must not have been deliberately constructed to calculate, display or encode Wilson primes.
2. **A derived connection to the property.** Explain how the actual mechanism leads to the Wilson-prime condition, or an equivalent. A mechanism involving primes generally does not automatically qualify.
3. **A measurement interpretation fixed independently.** Explain what the numbers represent. Counts and dimensionless quantities need a justified connection to observations; arbitrary units or relabelled states must not manufacture the result.
4. **An independently validated prediction.** Derive a testable consequence that was not used to select or fit the mechanism, and obtain independent validation. Address uncertainties, alternatives and the effects of searching many possible formulas.
5. **Wilson specificity.** Show what this property contributes. Where meaningful, compare other primes or nearby values with the same modelling freedoms, while retaining the physical constraints that make the mechanism plausible.

A spontaneous laboratory process could qualify. So could an evolved natural computation. A machine deliberately programmed to print Wilson primes would not answer the question.

You would not have to observe the next Wilson prime. A sound mechanism with accessible, independently validated consequences could establish the connection. Conversely, three matching observations do not establish a generating law.

## What the numerical exploration actually found

Before setting out the challenge, I explored a more modest question: could simple products, ratios and powers involving 5, 13 and 563 approximate selected mathematical and physical constants unusually well?

The accompanying software, **Wilson Ratio Scout**, searches a bounded family of expressions and repeats the same searches with replacement primes for comparison. Physical lengths are compared through dimensionless ratios rather than unit-dependent numerical values.

Across the reported runs, including comparison searches and related targets, the program represents **54,677,747,904 expression–target combinations**. It locates candidate neighbourhoods efficiently and reevaluates shortlisted expressions at high precision. That headline count does not mean 54 billion independent hypotheses, or 54 billion individually evaluated products.

No Wilson-specific physical relationship was established.

Some approximations to Planck-length ratios fell within their estimated uncertainties. But most comparison triples fitted those targets at least as closely. The interesting-looking matches did not make the Wilson triple stand out.

That is why the comparison searches matter. Finding a close formula tells us little until we ask how easily the same procedure finds close formulas with other inputs.

The search is reproducible background work, with source, tests, settings and results in the [research repository](https://github.com/whisprer/petersens-hypothesis/). It is not a survey of every natural phenomenon or the full literature, and it cannot establish a universal absence of connections.

## Why call it a hypothesis?

Because it is unproved, and because evidence should be able to change the answer.

“No connection is currently known” describes knowledge at a particular time. “No such natural mechanism exists” makes a claim about the world. The second is what this hypothesis proposes; failure to find a counterexample does not prove it.

There is also an honest boundary here: “intrinsic” and “essential” retain an interpretive element. The criteria make submissions assessable, but they do not turn physical relevance into a completely formal mathematical definition. Objections to that formulation are welcome too. Disagreement should be recorded rather than answered by redefining the claim after a result arrives.

The name identifies my formulation for discussion. It does not establish originality, peer review, community adoption or the status of a recognised major open problem.

## Bring the mechanism

The [challenge page on whispr.dev](https://whispr.dev/writing/petersens-hypothesis/) collects the criteria, paper and software links.

If you have a candidate, [open an issue in the public research repository](https://github.com/whisprer/petersens-hypothesis/issues/new). Include the observations or sources, derivation, measurement mapping, independent prediction, uncertainties and relevant comparisons. Reproducible calculations are welcome. GitHub submissions are public and require an account.

If someone has already done the work, point me towards it. A well-supported connection would answer the curiosity that started this, whether it is newly discovered or sitting in a paper I have not read.

I would be delighted to have a reason to reject the hypothesis.

---

**Paper:** Petersen, C. G. (2026). *Wilson primes in nature* (Version 1.0.0). Zenodo. [https://doi.org/10.5281/zenodo.23489260](https://doi.org/10.5281/zenodo.23489260).

**Software and results:** [Petersen’s Hypothesis on GitHub](https://github.com/whisprer/petersens-hypothesis/).

**Disclosure:** The proposal arose in discussion with ChatGPT, which assisted with drafting, code, calculations, reference checking and typesetting. The research note is not peer reviewed.
