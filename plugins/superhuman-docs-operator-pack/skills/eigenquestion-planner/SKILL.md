---
name: eigenquestion-planner
description: Plan any build, decision, or strategy doc by aiming at the real problem instead of polishing the surface. Frame the Eigenquestion (the one question whose answer collapses the rest), run Root Cause Reasoning (Problem, Root Cause, Solution, from the Zoom discipline), use Five Whys as the supplementary drill, and show the alternatives you considered and why you chose the direction. Trigger on "how should I frame this", "what is the real problem", "plan this build", "structure this decision", "root cause", "five whys", "eigenquestion", "why did we choose this", "make the case for this build", or any planning task where the reasoning matters as much as the output.
---

# Eigenquestion planner

Most plans polish the surface. This one aims at the root, because effort spent on the wrong problem is wasted no matter how good the execution. Two tools do the work: the Eigenquestion (frame the problem so the right answer is obvious) and Root Cause Reasoning (attack the cause, not the symptom). You are measured on the HOW as much as the WHAT, so make the reasoning visible.

## The Eigenquestion
The Eigenquestion is the single question that, once answered, determines the most downstream decisions. Find it by asking: which unknown, if resolved, collapses the rest of the choices? Write it as one plain line. A good Eigenquestion reframes a messy problem into a sharp one, and the answer then points straight at the solution. (Frame from Shishir Mehrotra.)

## Root Cause Reasoning
Three beats, in order, each earning the next:
- **Problem.** State it plainly, with evidence. Not "engagement is low" but "only about 1 in 4 launches hit target, and the cause is rarely the product." Cite the source.
- **Root cause.** Why it really happens, one level under the symptom. The symptom is what you see; the root cause is what produces it. Name the single connected cause, not a list.
- **Solution.** The move that attacks the root cause, not the symptom. Test every candidate against one question: does this reduce the failure, or just report it? Only a solution that reduces the failure earns the build.

(Discipline from Zoom, via Oded Gal and Ross Mayfield.)

## Five Whys (supplementary)
The drill that gets from symptom to root: ask why five times, each answer feeding the next. Keep it supplementary to the Eigenquestion, not the headline, and render it as a causal chain (A leads to B leads to C), not a bulleted interrogation. It is how you show your work on the root cause, not the main event.

## Alternatives considered (how the solution evolved)
Show 2 to 3 versions you worked through and why you chose the direction, testing each against the root cause. "v1 tracked, v2 generated, v3 orchestrates; only v3 attacks the coordination failure, so v3 is what we built." Showing the iterations is what proves the choice was reasoned, not lucky.

## Output structure (for a plan or doc)
1. **Eigenquestion** (one line, up top).
2. **Problem, Root cause, Solution** (the spine).
3. **Five Whys** (supplementary, collapsed or compact).
4. **How the solution evolved** (the alternatives and the test each faced).
5. **The build** (what you are actually doing, now that it aims at the root).

## Grounding
Every external claim gets a real, verifiable source; if you cannot verify it, flag it or soften the claim. A plan built on a fabricated number is worse than no plan. Prefer "not found" over a confident guess.

## Make it yours
Fork it. Swap in your domain's evidence, your framing questions, your test for a real solution. The point is to aim every build at the root problem and to make the reasoning legible to whoever reads it. Built by an operator. Customize it, break it, make it better.
