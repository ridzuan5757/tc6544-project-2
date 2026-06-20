# Presentation Script

10 minutes total, 3 speakers, ~3.3 minutes each.

---

## Speaker 1: Nur Ira Natasha Jafarizal

### Slide 1 — Title (~15s)

Good morning, Prof. Salwani. Our project is on metaheuristic optimisation of the Traveling Salesman Problem using a genetic algorithm with repair mechanisms. I will cover the problem and the genetic algorithm design, then Mutiara will walk through the crossover operators and constraint handling, and Ridzuan will present the evaluation and results.

### Slide 2 — Outline (~10s)

We have four parts: the problem, the genetic algorithm, constraint handling, and evaluation. Let me start with the problem.

### Slide 3 — kroA100 Benchmark (~1 min 15s)

We use kroA100 from TSPLIB as our benchmark. It has 100 cities in a two-dimensional Euclidean plane, and you can see the city layout on the right. The known optimal tour length is 21,282. The search space is enormous — roughly 4.7 times 10 to the power of 155 distinct tours — so exact enumeration is out of the question and we need a metaheuristic.

The objective is straightforward: find the permutation pi that minimises the total closed tour length. The distance between consecutive cities is summed around the full cycle, and the modular index closes the tour back to the starting city.

### Slide 4 — Permutation Encoding (~1 min)

Each candidate solution is encoded as a permutation of city indices. For example, this eight-city chromosome tells the salesman to visit city 3, then 0, then 7, and so on, returning to city 3 at the end. The fitness is simply the total distance of this closed tour — lower is better.

The key constraint is highlighted in red: every city must appear exactly once. If a chromosome has duplicates or missing cities, it is not a valid tour. The tricky part is that the fitness function still returns a number for an invalid chromosome — it just sums whatever edges are there. That number tends to look artificially good. This is the core problem that the rest of the presentation addresses.

### Slide 5 — Evolutionary Operators (~50s)

Now the building blocks. For selection, the primary operator is tournament with size 3 — pick three candidates at random, keep the best. Roulette wheel is implemented as a comparison.

For crossover, the primary is naive single-point. We will see in a moment why this is deliberate. PMX is the feasibility-preserving alternative we compare against.

Mutation uses swap only — pick two positions and exchange their values. Swap preserves the permutation by construction, so it never introduces infeasibility on its own.

On the right: elitism carries the top 2 forward, each run goes 500 generations with 30 seeds, and the best configuration uses population 200, crossover rate 0.95, mutation rate 0.10.

*[Hand over to Mutiara]*

---

## Speaker 2: Mutiara Jassy Atikah

### Slide 6 — Main Loop (~1 min)

Thank you, Ira. This pseudocode shows how those operators fit together in the main loop. At each generation, we copy the elites, then repeatedly select two parents, apply crossover with probability r_c, mutate, and optionally repair. The offspring fills the new population until we reach the target size.

The two lines to pay attention to are line 8 — the crossover step — and line 14 — the repair step. What goes wrong at line 8, and how line 14 fixes it, is the focus of this presentation. Let me show you both.

### Slide 7 — Naive Crossover Breaks the Permutation (~1 min)

Here is what happens at line 8 when we use naive single-point crossover. We take positions 0 through 3 from Parent A and positions 4 through 7 from Parent B, and just concatenate them. The result has cities 2 and 3 appearing twice, shown in red, while cities 0 and 5 disappear entirely.

This child is not a valid tour. But the fitness function still computes a distance for it, and because it skips two cities, that distance looks deceptively short. Selection then favours this invalid chromosome, and over a few generations the whole population drifts toward pseudo-tours rather than real tours.

### Slide 8 — PMX Prevents It by Construction (~45s)

One solution is to use a smarter crossover operator. PMX copies a segment from Parent A into the child, then for each displaced value, it follows a mapping chain until it finds an unoccupied position. The remaining slots are filled directly from Parent B.

The result is always a valid permutation — every city appears exactly once, no repair needed. But if we use PMX, we never get to study what happens when infeasible offspring appear and how to fix them. That is why we deliberately keep naive crossover and use repair instead.

### Slide 9 — Our Approach: Repair After the Fact (~1 min 15s)

So instead of switching to PMX, we keep naive crossover and repair every offspring after the fact. This way, repair has to do real work on every generation, which is the point of this project.

The repair works in two phases. Phase 1 is diagnosis: scan the chromosome left to right, track which cities we have seen, flag duplicates, compute the missing set.

Phase 2 is correction using random insertion — shuffle the missing cities and place them at the duplicate positions. We chose random insertion because it introduces no geometric bias and it preserves diversity, since two identical infeasible chromosomes can repair into different valid tours.

The example at the bottom shows this concretely. The input has city 1 duplicated at position 3 and city 3 duplicated at position 7. Cities 0 and 7 are missing. After repair, we get a valid permutation. Now Ridzuan will show whether this actually works.

*[Hand over to Ridzuan]*

---

## Speaker 3: Muhamad Ridzuan Mohd Yazid Goi

### Slide 10 — Experiment Setup (~50s)

Thank you, Mutiara. So does repair work well compared to the alternatives? To answer this, we set up a three-arm experiment on kroA100. All three arms share the same GA settings — population 100, crossover rate 0.8, mutation rate 0.2, tournament selection, 500 generations — and each arm runs 30 independent seeds. The only thing that changes is how we handle the permutation constraint.

The repair arm uses naive crossover and fixes offspring with random insertion. The penalty arm also uses naive crossover but adds a penalty of 50,000 times the violation count to the fitness instead of repairing. And the PMX arm uses feasibility-preserving crossover, so no repair or penalty is needed.

### Slide 11 — Results (~1 min 15s)

Here are the results. On the left, the boxplot shows the distribution of final tour lengths across 30 seeds for each strategy. On the right, the convergence curves show how the best fitness improves over 500 generations.

Looking at the table: repair achieves a mean best tour length of 49,778 with a gap of about 134% from the known optimal. PMX is at 50,655, gap of 138%. These two are practically tied — the difference is only about 2%. Penalty, on the other hand, sits at 57,948, trailing both by roughly 16%.

The convergence plot on the right confirms this is not just a matter of convergence speed. The penalty arm plateaus higher and never catches up. Repair and PMX overlap closely throughout, with repair converging slightly faster in the first 50 to 100 generations.

### Slide 12 — Takeaways (~45s)

To wrap up. First, naive crossover with repair performs almost as well as PMX on kroA100 — the difference is only about 2%. Second, random insertion keeps more population diversity than deterministic repair. Third, penalty is about 16% worse than both feasibility-based approaches. And fourth, the main lesson is that fixing or preventing infeasibility works much better than just penalising it.

Thank you. We are happy to take questions.
