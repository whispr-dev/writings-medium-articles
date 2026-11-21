# Did Gödel Solve a Famous Problem Twenty Years Early and Leave the Proof in Shorthand?

*An AI found a promising argument in Kurt Gödel’s private notebooks. A proof checker accepted a modern reconstruction. What, exactly, had Gödel left us?*

By Claudia G. Petersen

How would you know if you had proved something and then lost the proof? Would you remember the argument, or just the feeling of having reached the end of it? And if somebody found your working notes eighty years later, how much would they be allowed to fix before the proof became theirs?

Kurt Gödel left behind sixteen working notebooks from the early 1940s. They run to 1,009 densely written pages, much of them in Gabelsberger, a German shorthand already out of fashion when he used it. Gödel had made his reputation by finding limits to what mathematics could prove. His handwriting imposed a more immediate limit on what anybody could read.

Since 2017, the University of Helsinki logician Jan von Plato has led a project to make sense of the notebooks. Reading the shorthand was one job. Working out what Gödel meant once you had the words was another. A notebook is addressed to an audience of one, and that person can be relied upon to know why a definition has just changed or why a calculation stops halfway down the page. At least, that is what we all assume when we write things down for ourselves.

## The problem with a perfectly ordinary choice

Imagine a row of boxes, each containing at least one object. You want to take one object from every box. If there are twelve boxes, you can do this by hand. If there are infinitely many and each contains a set of positive integers, you can specify a rule: take the smallest number in each set. The rule settles every choice in one sentence.

Now suppose you have an arbitrary collection of nonempty sets, with no ordering or other common rule for picking an element from each. The **axiom of choice** says that a selection still exists. In mathematical terms, there is a *choice function* that assigns one element to every set in the collection. The axiom promises the existence of that assignment. You may still have no recipe for producing it.

The question that occupied Gödel and, later, the American mathematician Paul Cohen was whether that promise followed from the usual rules of set theory. Think of a mathematical model here as an interpretation in which the rules all come out true. If the same rules allow one model where choice holds and another where it fails, the rules alone cannot settle the question. Any conclusion you could actually deduce from them would have to hold in both.

Gödel had already published one half of the answer by 1940. He showed that if the usual rules of set theory are consistent, adding the axiom of choice keeps them consistent. In 1963, Cohen supplied the other half, showing that the rules also allow choice to fail. Together the two results establish what mathematicians call *independence*. When Cohen received the Fields Medal in 1966 for work that included this result, Gödel reportedly said he had proved it himself in the 1940s. The notebooks, when called upon, failed to produce a proof.

## What Claude was given

In September 2026, von Plato gave Claude his transcriptions of the notebooks, along with books he had written about Gödel and other scholarly material. The shorthand had already been read by people. Claude’s job began at the point where legible text can still leave you wondering what on earth the author was doing.

Within days, the model produced a digest of about 650 pages. This is a rather expansive interpretation of the word *digest*, though the useful thing was its ability to suggest connections across the notebooks. The definition that makes sense of an argument may sit hundreds of pages away, in a passage you had no reason to remember when you first read it. Von Plato said the digest still needed checking page by page.

Asked to identify results and ideas for proofs, Claude returned 663 candidates. Some came with arguments, some with sketches, and others with little more than a suggestion of how a proof might go. Von Plato told *The Guardian* that about 400 were verified as stated, about 200 needed repairs, and around 50 were judged false. Those are rounded figures. A repair could mean making a statement more precise or adding an assumption. Gödel himself occasionally returned to his notes and wrote *falsch* in the margin. There is some comfort in knowing he also had that sort of afternoon.

## What a proof checker can tell you

The checking was done with Coq, a proof assistant. To use it, you express the mathematical claim and its proof in a precise language. Coq checks that the proof establishes the claim you actually entered, using the definitions and assumptions available to it. If you claim that every whole number is positive, the fact that you were plainly thinking of the counting numbers buys you very little. Zero remains available for comment.

That distinction matters for the claim about Cohen. According to von Plato, the recovered argument used an incorrect definition, but Gödel had written down the definition needed for the reconstruction elsewhere, two years earlier. Von Plato says the reconstructed proof passed Coq. The code, its assumptions and the notebook passages would all need to be inspected together to judge what that result establishes and how much of the argument Gödel had assembled.

Joel David Hamkins, a logician at the University of Notre Dame, told *The Guardian* that he had yet to see the reconstruction. His caution goes to the heart of the story. Two passages can fit together beautifully when read by someone who already knows the answer. Did Gödel ever put them together himself? Coq can establish whether they fit once formalised. The date on which anyone first fitted them together is a question for the archive.

Even a short repair can change the historical answer. Suppose a composer leaves a manuscript with one awkward bar, and a tune in an earlier sketchbook makes the passage work. You can play the repaired version and hear that it works. To say the composer finished it that way, you would want some sign that they ever put that tune in that bar. The difference might occupy less than a second in performance and years in a biography.

## When does a discovery happen?

If Gödel once saw the complete argument and later forgot it, there was a moment when he knew something the rest of mathematics would have to wait twenty years to learn. If he had the necessary pieces but never joined them, there was a different sort of achievement in those notebooks. Both possibilities are worth taking seriously. A finished reconstruction makes the gap between them harder to see, especially once the argument seems obvious in its repaired form.

There is also a question of what it means for mathematics to know something. A private proof can be perfectly sound. It becomes available to other people when they can read it closely enough to find a mistake, carry a technique into another problem, or notice that a seemingly minor assumption is doing all the work. Cohen gave other mathematicians an argument they could use. The renewed work on Gödel’s notebooks may give them another, along with a chance to see how he thought when he was writing for himself.

The question I keep coming back to is what Gödel knew on the day he shut the notebook. Then I wonder whether he ever opened it again at the right page.

---

### Sources

- [Alex Bellos’s reporting and interviews with Jan von Plato and Joel David Hamkins in *The Guardian*, 13 November 2026](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)
- [The University of Helsinki’s Gödel Enigma research team](https://www.helsinki.fi/en/researchgroups/godel-enigma/people)
- [The axiom of choice and its history in the *Stanford Encyclopedia of Philosophy*](https://plato.stanford.edu/archives/sum2025/entries/axiom-choice/)
- [Coq’s documentation on how it verifies proofs](https://docs.rocq-prover.org/V8.19.1/refman/proofs/writing-proofs/proof-mode.html)
