# Why Can Changing One Bit Send an AI Somewhere Else Entirely?

*Two neural networks can start almost identically and learn different things. The closer you look at where they part company, the stranger it gets.*

**By Claudia G. Petersen**

How little would you have to change to make an AI learn something different? A few thousand examples? The order you show them in? One number, perhaps, if you changed it enough?

Andrew Ly and Pulin Gong, researchers at the University of Sydney, took an image-recognition network and flipped the least significant bit of a single starting weight. Think of changing the last digit on a very long receipt. They then trained the network from that slightly altered starting point. Across the one-bit changes they examined, training arrived at a different internal destination 47.7 per cent of the time. An impressive amount of upheaval for a digit that had every reason to expect a quiet career. [The study in *Nature Machine Intelligence*](https://www.nature.com/articles/s42256-026-01336-3)

In that same vision model, shrinking the uncertainty in the starting settings by a factor of ten billion brought no measurable improvement in the ability to reproduce the internal destination. Ten billion is an extravagant number to spend on the same answer. [University of Sydney research summary](https://www.sydney.edu.au/news-opinion/news/2026/11/06/sydney-researchers-uncover-a-hidden-limit-to-ai-predictability.html)

What could make two starting points so close and their destinations so indifferent to the fact?

## Where does a network go when it learns?

Imagine a hillwalker in thick fog. She can feel which way the ground slopes beneath her boots, and she has instructions to take a step in the downhill direction. She knows very little about the valley she’ll eventually reach. At present, she knows rather a lot about her left boot.

Training a neural network involves a similar local calculation. Its *weights* are numbers that shape what it predicts. A measure called the *loss* tells us how poorly those predictions fit the training objective. Give every possible combination of weights a position and make its loss the height at that position, and you have a landscape. The training algorithm uses local information about the slope to decide how to adjust the weights. Every adjustment moves it to another point, where it can do the whole tedious business again.

Now forget the heights for a moment and draw a different map. Pick a starting point, run the training, and colour the starting point according to where training ends up. Do this again and again. All the starting points that lead to a particular destination make up its *basin of attraction*. A blue dot tells you where a journey ends. It tells you almost nothing about what the walker saw on the way.

On a well-behaved map, you could put two walkers down in the middle of blue territory and reasonably expect both to reach the blue destination. Near the edge you’d be more careful. Coastlines, after all, have been getting away with extravagant detail for some time. But deep inland, you might expect a little peace.

## A coastline all the way inland

The map Ly and Gong made for a small neural network resembles a butterfly. Look at one of its blue wings from a distance and you could be forgiven for thinking it’s blue. Zoom in and there’s orange. Pick an orange patch, zoom again, and there’s blue inside that. A coastline usually has the courtesy to leave you some inland. Here, the sea keeps turning up in the drawing room.

> **[INSERT FIGURE HERE — Ly & Gong, Figure 3a–c]**  
> *Caption:* Each dot marks a starting configuration, coloured by where training eventually takes it. Successive close-ups of the small network’s basin map reveal blue and orange starting points interwoven at finer scales.  
> *Alt text:* A blue-and-orange butterfly-shaped map with successive magnifications showing flecks of both colours within apparently uniform regions. [View the original figure](https://arxiv.org/html/2510.05606v2#:~:text=Riddling%20in%20the%20minimal%20model)

Mathematicians call a basin *riddled* when every neighbourhood around one of its points contains some genuine volume belonging to other outcomes. Imagine looking at a spot through a magnifying glass. As you move to stronger lenses and the circle you can see shrinks, there’s always some of the other colour inside it. How much there is can vary considerably. The peculiar thing is that you never reach a circle you can declare wholly yours.

The researchers could work through the mathematics in their small model. For larger networks, they looked for the same telltale patterns in experiments. They trained roughly half a million networks across configurations that included image classifiers and a model for classifying the sentiment of film reviews. They found evidence consistent with riddling across the architectures and training methods they tested. The extent of the phenomenon in frontier language models remains an open question. [Study and experimental methods](https://arxiv.org/html/2510.05606v2)

## The rules can be perfectly clear

Run a deterministic computation twice with precisely the same starting state and operations, and you get the same result. The Sydney experiment asks what happens when the starting states are *almost* the same. In the vision experiment, sensitivity to tiny differences persisted even when the researchers ran training deterministically on a CPU. The computation could be faithfully repeated. What it lacked was a reliable way to turn an approximately matching start into a matching destination.

And a different destination inside a network can mean several things. For example, swap two hidden neurons and swap their connections along with them, and you can change the arrangement of weights while preserving the same predictions. You’ve moved the furniture and left the room usable in precisely the same way.

So the researchers asked a second question. How often do two models trained from nearly identical starting points disagree about what they see? In one set of paired runs of the vision model, the average disagreement settled at about 2.9 per cent of inputs as the starting differences shrank. The 47.7 per cent result counted changes of internal destination after a one-bit perturbation. The 2.9 per cent result counted disagreements on individual predictions in a separate comparison. For anyone relying on a model, that second measure raises the more interesting question of *which* inputs it disagrees on. [Study, Figure 5 and discussion](https://arxiv.org/html/2510.05606v2#:~:text=Parameter%2D%20and%20function%2Dspace%20uncertainty%20exponents)

> **[OPTIONAL FIGURE INSERT — Ly & Gong, Figure 5c and 5e]**  
> *Caption:* In the deterministic CPU experiments, reducing the starting difference brought little improvement over the measured range. Panel c tracks changes in internal destination. Panel e tracks the share of inputs on which paired models disagreed.  
> *Alt text:* Two plots with nearly flat trends as the starting difference shrinks. One measures different internal destinations and the other measures prediction disagreement. [View the original figure](https://arxiv.org/html/2510.05606v2#:~:text=Parameter%2D%20and%20function%2Dspace%20uncertainty%20exponents)

## The price of treading carefully

You might reasonably ask whether the walker could just take smaller steps. In training, the *learning rate* controls the size of each adjustment. In most of the configurations the researchers tested, lowering it made outcomes more repeatable, while the settings that yielded the strongest training performance often came with greater sensitivity. In those experiments, the more dependable route could also be the less productive one. What a nuisance to discover that the dial you’ve been looking for is already attached to something else. [Study, performance and reproducibility](https://arxiv.org/html/2510.05606v2)

## Which model did we approve?

Suppose a hospital is evaluating two models that flag scans for review. Both get 95 per cent right on the same test set. They may agree on nearly every scan. They could also make their mistakes on quite different patients. If one model’s misses cluster around an uncommon presentation, the other model’s identical score tells the hospital very little about whether it will miss those same cases. The patients, for their part, have the inconvenient distinction of arriving one at a time.

The audit question changes depending on what you want to reproduce. If you want to know what actually ran last Tuesday, preserve the deployed model and record its version. If you want to know whether the training recipe reliably produces an acceptable replacement, train it again and compare the resulting models on cases that matter. And if you want to know how the model behaves in use, a single accuracy figure leaves you with an awkward amount of reading between the lines.

So what should we certify? The process that made the model, the behaviour of the particular model we put to work, or the outcomes we can measure once it’s there? Each is a different promise. A training recipe can be followed exactly. A score can be honestly reported. There is still a patient whose scan sits in the small patch where two apparently equivalent models part company.

There’s something rather chastening about a computer following every instruction it was given and leaving us with a question we thought the instructions had settled. We know the rules of the walk. To find out where we’ve arrived, we may still have to look down.

---

**Editor’s note for Medium:** The figure cues include captions, alt text and links to the authors’ figures. Check reuse terms before uploading the originals. If using links alone, remove the cue blocks and keep the links in the adjacent text.

**Suggested Medium tags:** Artificial Intelligence · Machine Learning · Mathematics · Science · Technology
