# Quantum Computers May Need a 1950s Invention Made from Diamond

*The maser arrived before the laser, then spent decades being rather less famous. Quantum engineering may finally have found a use for its difficult temperament.*

**By Claudia G. Petersen**

What does the future look like?

Presumably something sleek. Something recently patented. Something whose promotional photographs suggest it has never encountered dust.

Probably not an invention from 1954, tucked inside a refrigerator, relying on imperfections in a small piece of diamond.

Yet that is a reasonable description of a new contender for one of quantum computing’s less glamorous jobs: making an extraordinarily faint signal loud enough to read.

In research published on 16 November 2026, a team led from the Okinawa Institute of Science and Technology demonstrated a diamond-based microwave amplifier working at temperatures close to absolute zero. Its ancestry belongs to the maser, the older relative of the laser. Its attraction is that the cold, once an obstacle to wider use, is already part of the working environment for many quantum devices. [1, 2]

The accommodation, in other words, has finally caught up with the guest.

The maser came first. Charles Townes and his colleagues made the first one work in 1954; the first working laser followed in 1960. Both exploit stimulated emission, a process through which matter can be persuaded to contribute energy to an electromagnetic wave. The names preserve the family resemblance: maser stands for *microwave amplification by stimulated emission of radiation*. Replace “microwave” with “light” and you have its more successful sibling. [3]

The laser acquired the visibility. This was helped, admittedly, by being visible.

But obscurity is not failure. Masers became valuable instruments in radio astronomy and communication with spacecraft, where a weak signal needs unusually considerate treatment. Their cooling requirements were an inconvenience worth accepting for particular jobs. They were considerably harder to sell as an everyday arrangement. [3]

Now consider a quantum laboratory that has already gone to enormous trouble to make things cold.

An extra demand for refrigeration begins to look less like an unreasonable personality trait and more like compatibility.

To see why this matters, forget the computer for a moment and imagine an amplifier.

Its job sounds almost insultingly straightforward: receive a small signal and produce a larger version. Unfortunately, a larger signal is useful only if you can still distinguish it from the accompanying noise. An amplifier that adds too much of its own random fluctuation can make the output more powerful while making the original message harder to identify.

At the quantum scale, this is more than poor component selection. There is a fundamental restriction. A high-gain amplifier that preserves a wave’s phase — its position within the repeating cycle — while amplifying both independent components must add noise. Expressed as equivalent noise at the input, the minimum approaches half a quantum at the operating frequency. [4]

A quantum here is a unit of energy: the energy of one microwave photon. Saying “half a quantum of noise” describes a measured noise level in those units; it does not require anyone to cut a photon in half.

Physics is quite demanding enough without introducing microscopic kitchen equipment.

That qualification about the kind of amplifier matters. The rule is not that every conceivable measurement must pay exactly the same noise penalty. It applies to amplification that treats both components of the wave equally. [4]

For quantum readout, practical noise adds another difficulty. The microwave signal carrying information about a qubit — a quantum computer’s unit of information — may be extremely weak. Extra fluctuations can blur the distinction between the possible measurement results. Turning up the gain afterwards does not undo the ambiguity introduced at the beginning. [2]

This is why an amplifier can be a serious scientific achievement without doing anything that looks especially dramatic through a laboratory window.

The diamond supplies the active material, but its usefulness begins with a small departure from perfection.

Diamond is an orderly structure of carbon atoms. Occasionally, a nitrogen atom occupies a position normally belonging to carbon. This substitutional nitrogen defect is called a P1 centre. Associated with it is an unpaired electron whose spin gives it magnetic behaviour. [5]

“Spin” is the name of an intrinsic quantum property. It is tempting to picture a tiny rotating ball, but the electron is not literally a miniature planet. For present purposes, the useful picture is a microscopic magnetic compass with only certain allowed states.

An applied magnetic field gives those states different energies. Microwaves of the appropriate frequency can drive transitions between them. A crystal containing many such defects therefore offers a collection of controllable magnetic systems. [5]

The jeweller’s language of purity is not particularly helpful here. What counts as a flaw depends very much on what you intended the stone to do.

To amplify a signal, those systems need an energy supply. Under ordinary conditions, more occupy the lower-energy state than the higher one. Reverse that balance and you create *population inversion*: an excess of systems ready to release energy rather than absorb it. An incoming wave can then stimulate transitions downward, collecting the released energy as additional radiation coordinated with the signal. [3]

The diamond experiment establishes that imbalance through microwave pumping and a four-spin process called cross-relaxation. Two pumped spins exchange energy with two others; unequal relaxation rates then help build the population needed for amplification. The pump uses roughly 100 nanowatts or less. [1]

That is a tiny power delivered to the device, not the electricity bill for the entire refrigerator. The distinction is worth making before anyone orders one for reasons of household economy.

At 6.595 gigahertz, the amplifier achieved more than 30 decibels of power gain: over a thousandfold increase. Its reported added noise was approximately **2.55 quanta above the standard quantum limit**. [1]

The word “above” deserves its place in the sentence.

“Near quantum limited” is the researchers’ description. It does not mean quantum limited, and it certainly does not mean noiseless. A result can be encouraging without being promoted to perfection on the journey from a paper to a headline.

Why pursue it, then, when superconducting amplifiers already perform exceptionally well?

Because a laboratory is a place where several requirements have to be met at once, often while actively inconveniencing one another.

Conventional Josephson amplifiers use superconducting circuitry to amplify weak microwave signals. Strong magnetic fields can present problems for these devices. Semiconductor spin qubits, meanwhile, use magnetic fields as part of their operation. Putting the readout equipment beside the thing being read therefore involves an awkward negotiation. [2]

The diamond maser offers a different route: amplification through magnetic spins rather than superconducting circuitry. The authors identify strong-field compatibility as a potential advantage, with possible uses in spin-qubit readout, magnetic-resonance measurements and searches for hypothetical dark-matter particles called axions. [1]

The appeal is situational. An amplifier need not win every comparison to become the useful choice in a particular machine.

Nor is the comparison simply diamond versus superconductors. Researchers are also developing superconducting alternatives that tolerate magnetic fields. The engineering landscape has more than two inhabitants. [1]

For now, the diamond device’s noise performance, useful frequency range and tunability lag behind the best superconducting amplifiers. Bandwidth means the range of frequencies it can amplify effectively; tunability means how readily that operating range can be moved. Practical integration also requires lower losses and further reductions in pumping demands. [1]

A promising demonstration is a beginning. The cables, connections and inconvenient losses will expect their own meetings.

Still, the most interesting thing here may be the reversal of context.

We tend to discuss technology as though inventions stand in a queue, each waiting to replace the one ahead. Newer becomes better; older becomes historical; eventually somebody opens a museum.

But usefulness is a relationship between an idea and its surroundings. Change the surroundings and the verdict can change with them.

A demand that once made a device cumbersome can become routine infrastructure. A capability that once seemed rather specialised can become the feature another machine urgently needs. The invention has not become younger. The problem has become more suitable.

None of this means every abandoned technology deserves resurrection. Some ideas were abandoned for excellent reasons, and nostalgia remains a poor substitute for a measurement.

It does suggest a better question than whether something is old.

Which of its disadvantages still matter? Which of its peculiar strengths have acquired a customer?

How many apparently failed technologies were simply waiting for a problem with the right constraints?

Progress is not always the arrival of an invention nobody has seen before.

Sometimes it is the moment an old idea finally meets the world it needed.

---

**Sources**

1. Ohta and colleagues, [A near-quantum-limited diamond maser amplifier operating at millikelvin temperatures](https://www.nature.com/articles/s41467-026-79021-7), *Nature Communications*, 16 November 2026.
2. OIST, [Ultracold diamond microwave laser amplifies quantum signals 1,000-fold](https://www.oist.jp/news-center/news/2026/11/16/ultracold-diamond-microwave-laser-amplifies-quantum-signals-1000-fold). Technical noise wording follows the paper rather than the simplified wording in this account.
3. Charles H. Townes, [Nobel Lecture: Production of Coherent Radiation—Masers and Lasers](https://www.nobelprize.org/uploads/2018/06/townes-lecture.pdf).
4. Caves and colleagues, [Quantum limits on phase-preserving linear amplifiers](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.86.063802), *Physical Review A* (2012).
5. [Detection of nanoscale electron spin resonance spectra demonstrated using nitrogen-vacancy centre probes in diamond](https://www.nature.com/articles/ncomms10211), *Nature Communications* (2016).

**Suggested Medium tags:** Quantum Computing · Physics · Technology · Science · Innovation
