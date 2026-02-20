# Setup Guide

This document explains how to use this LeetCode journey repository effectively.

## Quick Start

1. **Clone or fork this repository**
   ```bash
   git clone <your-repo-url>
   cd leetcode-journey
   ```

2. **Choose a pattern to start with**
   - Begin with Arrays or Strings (fundamentals)
   - Read the pattern README to understand key concepts

3. **Create a new problem file**
   ```bash
   ./scripts/new-problem.sh arrays easy two-sum
   ```

4. **Solve the problem**
   - Open the generated markdown file
   - Fill in the problem statement from LeetCode
   - Work through multiple approaches
   - Document your solution and insights

5. **Update progress**
   - Mark the problem as solved by filling in the "Date Solved" field
   - Run the progress generator:
   ```bash
   python scripts/generate-progress.py
   ```

## Workflow

### Daily Practice Routine

1. **Select a problem** from your current pattern focus
2. **Set a timer** (20-30 minutes for easy, 45+ for medium/hard)
3. **Attempt without looking at solution**
4. **Document your approach** even if you don't solve it
5. **Review optimal solution** and understand why it works
6. **Implement and test** the optimal solution
7. **Write key takeaways** for future reference

### Weekly Review

- Review all problems solved this week
- Identify patterns you struggled with
- Redo 2-3 challenging problems from memory
- Update your learning goals in README.md

### Monthly Assessment

- Run progress generator to see statistics
- Celebrate milestones achieved
- Adjust learning strategy based on weak areas
- Plan next month's focus patterns

## Using the Scripts

### Creating New Problems

```bash
# General syntax
./scripts/new-problem.sh <pattern> <difficulty> <problem-name>

# Examples
./scripts/new-problem.sh arrays easy two-sum
./scripts/new-problem.sh dynamic-programming medium coin-change
./scripts/new-problem.sh graphs hard word-ladder
```

The script will:
- Create a new file from the template
- Place it in the correct pattern/difficulty folder
- Prompt you to fill in the details

### Generating Progress Statistics

```bash
python scripts/generate-progress.py
```

This will:
- Scan all problem files
- Count solved vs unsolved problems
- Calculate mastery percentages
- Update PROGRESS.md with current stats
- Show recent activity

**Note**: A problem is considered "solved" when the `Date Solved` field contains a valid date (YYYY-MM-DD format).

## Documentation Standards

### Problem Documentation

Each problem should include:
1. **Problem Statement** - Copy from LeetCode
2. **Initial Thoughts** - Your first approach
3. **Multiple Approaches** - Brute force → optimized
4. **Complexity Analysis** - Time and space for each approach
5. **Code Implementation** - Well-commented code
6. **Edge Cases** - What to watch out for
7. **Key Takeaways** - Pattern recognition and insights
8. **Backend Context** - Real-world applications

### Code Comments

Write comments that explain:
- **Why**, not what (the code shows what)
- Key insights or non-obvious optimizations
- Edge cases being handled
- Complexity trade-offs

Example:
```python
# Use hash map to achieve O(1) lookup instead of O(n) nested loop
seen = {}

# Store value->index to find complement later
seen[num] = i
```

## Tracking Your Progress

### Marking Problems as Solved

In each problem file, update the header:
```markdown
**Date Solved**: 2026-02-16
```

The progress generator looks for this field to count solved problems.

### Revision Tracking

Use the "Revision Notes" section to track your improvement:
```markdown
**First Attempt**: 2026-02-16 - Struggled with optimal approach, took 45 min
**Second Attempt**: 2026-02-23 - Recognized pattern immediately, solved in 20 min
**Third Attempt**: 2026-03-02 - Can implement in under 5 minutes, fully mastered
```

## Best Practices

### For Backend Engineers

Focus on patterns relevant to backend systems:
- **Arrays & Hash Tables**: Caching, rate limiting
- **Trees**: Database indexes, routing
- **Graphs**: Service dependencies, distributed tracing
- **Dynamic Programming**: Resource optimization
- **Heaps**: Job scheduling, task prioritization

Document how each problem relates to real backend scenarios.

### Deliberate Practice

- Focus on **understanding** over memorization
- Solve problems **multiple times** with increasing complexity
- **Explain your solution** out loud or in writing
- **Time yourself** to build interview readiness
- **Review mistakes** and document pitfalls

### Portfolio Showcase

This repository is designed to impress potential employers:
- Shows systematic learning approach
- Demonstrates depth over breadth
- Connects algorithms to real-world systems
- Proves technical communication skills
- Tracks continuous improvement

Make sure your documentation is:
- Professional and well-formatted
- Free of typos and grammatical errors
- Detailed but concise
- Focused on insights, not just code

## Customization

Feel free to adapt this structure to your needs:

- Add more patterns as you discover them
- Create custom scripts for your workflow
- Modify templates to match your style
- Add language-specific folders if practicing multiple languages
- Include visual diagrams for complex problems

## Tips for Success

1. **Consistency over intensity** - 1-2 problems daily beats 10 problems once
2. **Pattern recognition** - Focus on identifying patterns, not memorizing solutions
3. **Spaced repetition** - Revisit problems after 1 day, 1 week, 1 month
4. **Active learning** - Write explanations in your own words
5. **Connect to experience** - Relate problems to your backend work

## Getting Help

If you get stuck:
1. Read the pattern README for techniques
2. Draw examples and walk through manually
3. Start with brute force, then optimize
4. Check LeetCode discussion after attempting
5. Document what you learned, even if you didn't solve it

## Maintenance

### Weekly
- Run progress generator
- Commit solved problems to git
- Review and update learning goals

### Monthly
- Update README with new insights
- Add new patterns if needed
- Review overall progress and adjust strategy

---

Happy coding! Remember: **The goal is deep understanding, not just green checkmarks.** 🚀
