#!/usr/bin/env python3
"""
Generate progress statistics for LeetCode journey.

This script scans all problem files and generates/updates PROGRESS.md
with current statistics, completion rates, and recent activity.

Usage:
    python generate-progress.py
"""

import os
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Define patterns and their directories
PATTERNS = [
    "arrays",
    "strings",
    "linked-lists",
    "trees",
    "graphs",
    "dynamic-programming",
    "backtracking",
    "binary-search",
    "heaps",
    "sliding-window",
    "stack-queue",
    "two-pointers",
    "hash-tables"
]

DIFFICULTIES = ["easy", "medium", "hard"]

def get_repo_root():
    """Get repository root directory."""
    script_dir = Path(__file__).parent
    return script_dir.parent

def is_problem_solved(file_path):
    """
    Check if a problem is solved by looking for 'Date Solved' field.
    Returns (is_solved, date_solved).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for "Date Solved: YYYY-MM-DD" pattern
            match = re.search(r'\*\*Date Solved\*\*:\s*(\d{4}-\d{2}-\d{2})', content)
            if match:
                return True, match.group(1)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return False, None

def scan_problems():
    """
    Scan all pattern directories and collect problem statistics.
    Returns dict with pattern -> difficulty -> list of (problem_name, solved, date).
    """
    repo_root = get_repo_root()
    stats = defaultdict(lambda: defaultdict(list))

    for pattern in PATTERNS:
        pattern_dir = repo_root / pattern
        if not pattern_dir.exists():
            continue

        for difficulty in DIFFICULTIES:
            diff_dir = pattern_dir / difficulty
            if not diff_dir.exists():
                continue

            # Find all markdown files (problems)
            for md_file in diff_dir.glob("*.md"):
                problem_name = md_file.stem
                is_solved, date_solved = is_problem_solved(md_file)
                stats[pattern][difficulty].append({
                    'name': problem_name,
                    'solved': is_solved,
                    'date': date_solved,
                    'path': str(md_file.relative_to(repo_root))
                })

    return stats

def calculate_overall_stats(stats):
    """Calculate overall statistics across all patterns."""
    total_problems = 0
    solved_problems = 0
    by_difficulty = defaultdict(lambda: {'total': 0, 'solved': 0})

    for pattern in stats:
        for difficulty in stats[pattern]:
            problems = stats[pattern][difficulty]
            total_problems += len(problems)
            solved = sum(1 for p in problems if p['solved'])
            solved_problems += solved

            by_difficulty[difficulty]['total'] += len(problems)
            by_difficulty[difficulty]['solved'] += solved

    return {
        'total': total_problems,
        'solved': solved_problems,
        'by_difficulty': by_difficulty
    }

def get_recent_activity(stats, limit=10):
    """Get most recently solved problems."""
    all_solved = []

    for pattern in stats:
        for difficulty in stats[pattern]:
            for problem in stats[pattern][difficulty]:
                if problem['solved'] and problem['date']:
                    all_solved.append({
                        'pattern': pattern,
                        'difficulty': difficulty,
                        'name': problem['name'],
                        'date': problem['date'],
                        'path': problem['path']
                    })

    # Sort by date (most recent first)
    all_solved.sort(key=lambda x: x['date'], reverse=True)
    return all_solved[:limit]

def format_pattern_name(pattern):
    """Format pattern name for display."""
    name_map = {
        'arrays': 'Arrays & Hash Tables',
        'strings': 'Strings',
        'linked-lists': 'Linked Lists',
        'trees': 'Trees & Binary Trees',
        'graphs': 'Graphs',
        'dynamic-programming': 'Dynamic Programming',
        'backtracking': 'Backtracking',
        'binary-search': 'Binary Search',
        'heaps': 'Heaps / Priority Queues',
        'sliding-window': 'Sliding Window',
        'stack-queue': 'Stack & Queue',
        'two-pointers': 'Two Pointers',
        'hash-tables': 'Hash Tables'
    }
    return name_map.get(pattern, pattern.title())

def generate_progress_md(stats, overall_stats, recent_activity):
    """Generate the PROGRESS.md content."""
    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "# Progress Dashboard 📊",
        "",
        f"Last Updated: {today}",
        "",
        "## Overall Statistics",
        "",
        "| Metric | Count | Target | Progress |",
        "|--------|-------|--------|----------|"
    ]

    # Overall stats table
    total = overall_stats['total']
    solved = overall_stats['solved']
    pct = (solved / total * 100) if total > 0 else 0

    lines.append(f"| Total Problems Solved | {solved} | {total} | {pct:.0f}% |")

    for diff in DIFFICULTIES:
        d_total = overall_stats['by_difficulty'][diff]['total']
        d_solved = overall_stats['by_difficulty'][diff]['solved']
        d_pct = (d_solved / d_total * 100) if d_total > 0 else 0
        lines.append(f"| {diff.capitalize()} Problems | {d_solved} | {d_total} | {d_pct:.0f}% |")

    patterns_mastered = sum(
        1 for pattern in stats
        if sum(
            len([p for p in stats[pattern][d] if p['solved']])
            for d in stats[pattern]
        ) / max(1, sum(len(stats[pattern][d]) for d in stats[pattern])) >= 0.8
    )

    lines.append(f"| Patterns Mastered | {patterns_mastered} | {len(PATTERNS)} | {patterns_mastered/len(PATTERNS)*100:.0f}% |")
    lines.append("")
    lines.append("## Progress by Pattern")
    lines.append("")

    # Pattern-specific stats
    for pattern in PATTERNS:
        if pattern not in stats or not any(stats[pattern].values()):
            continue

        pattern_name = format_pattern_name(pattern)
        pattern_total = sum(len(stats[pattern][d]) for d in stats[pattern])
        pattern_solved = sum(
            len([p for p in stats[pattern][d] if p['solved']])
            for d in stats[pattern]
        )
        mastery = (pattern_solved / pattern_total * 100) if pattern_total > 0 else 0
        status = "Mastered" if mastery >= 80 else "In Progress" if pattern_solved > 0 else "Not Started"

        lines.append(f"### {pattern_name}")
        lines.append(f"**Status**: {status} | **Solved**: {pattern_solved}/{pattern_total} | **Mastery**: {mastery:.0f}%")
        lines.append("")
        lines.append("| Difficulty | Solved | Problems |")
        lines.append("|-----------|--------|----------|")

        for diff in DIFFICULTIES:
            if diff not in stats[pattern]:
                continue

            problems = stats[pattern][diff]
            if not problems:
                continue

            solved_count = sum(1 for p in problems if p['solved'])
            problem_names = ', '.join([
                f"[{p['name'].replace('-', ' ').title()}]({p['path']})"
                for p in problems[:5]  # Show first 5
            ])
            if len(problems) > 5:
                problem_names += f", ... (+{len(problems) - 5} more)"

            lines.append(f"| {diff.capitalize()} | {solved_count}/{len(problems)} | {problem_names} |")

        lines.append("")
        lines.append("---")
        lines.append("")

    # Recent activity
    lines.append("## Recent Activity")
    lines.append("")

    if recent_activity:
        for activity in recent_activity:
            name_display = activity['name'].replace('-', ' ').title()
            lines.append(
                f"- **{activity['date']}** - Solved [{name_display}]({activity['path']}) "
                f"({activity['difficulty'].capitalize()}, {format_pattern_name(activity['pattern'])})"
            )
    else:
        lines.append("No problems solved yet. Start your journey today!")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Milestones
    lines.extend([
        "## Milestones",
        "",
        f"- [{'x' if solved >= 1 else ' '}] First problem solved",
        f"- [{'x' if solved >= 10 else ' '}] 10 problems solved",
        f"- [{'x' if solved >= 25 else ' '}] 25 problems solved",
        f"- [{'x' if solved >= 50 else ' '}] 50 problems solved",
        f"- [{'x' if patterns_mastered >= 1 else ' '}] First pattern mastered (80%+ completion)",
        f"- [{'x' if solved >= 100 else ' '}] 100 problems solved",
        f"- [{'x' if patterns_mastered >= 5 else ' '}] 5 patterns mastered",
        f"- [{'x' if solved >= 150 else ' '}] 150 problems solved",
        f"- [{'x' if overall_stats['by_difficulty']['hard']['solved'] >= 1 else ' '}] First hard problem solved",
        f"- [{'x' if solved >= 200 else ' '}] 200 problems solved",
        f"- [{'x' if patterns_mastered == len(PATTERNS) else ' '}] All patterns mastered",
        "",
        "---",
        "",
        "**Note**: Pattern mastery is achieved when 80% of problems in that category are solved with optimized solutions.",
        ""
    ])

    return '\n'.join(lines)

def main():
    """Main function."""
    print("🔍 Scanning problem files...")
    stats = scan_problems()

    print("📊 Calculating statistics...")
    overall_stats = calculate_overall_stats(stats)

    print("⏰ Getting recent activity...")
    recent_activity = get_recent_activity(stats)

    print("📝 Generating PROGRESS.md...")
    progress_content = generate_progress_md(stats, overall_stats, recent_activity)

    # Write to PROGRESS.md
    repo_root = get_repo_root()
    progress_file = repo_root / "PROGRESS.md"

    with open(progress_file, 'w', encoding='utf-8') as f:
        f.write(progress_content)

    print(f"✅ Successfully updated {progress_file}")
    print("")
    print("Summary:")
    print(f"  Total problems: {overall_stats['total']}")
    print(f"  Solved: {overall_stats['solved']}")
    print(f"  Progress: {(overall_stats['solved']/max(1, overall_stats['total'])*100):.1f}%")

if __name__ == "__main__":
    main()
