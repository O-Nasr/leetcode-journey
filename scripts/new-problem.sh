#!/bin/bash

# Script to create a new LeetCode problem file from template
# Usage: ./new-problem.sh <pattern> <difficulty> <problem-name>
# Example: ./new-problem.sh arrays easy two-sum

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check arguments
if [ "$#" -ne 3 ]; then
    echo -e "${RED}Error: Incorrect number of arguments${NC}"
    echo "Usage: $0 <pattern> <difficulty> <problem-name>"
    echo ""
    echo "Examples:"
    echo "  $0 arrays easy two-sum"
    echo "  $0 dynamic-programming medium coin-change"
    echo "  $0 graphs hard word-ladder"
    echo ""
    echo "Available patterns:"
    echo "  - arrays"
    echo "  - strings"
    echo "  - linked-lists"
    echo "  - trees"
    echo "  - graphs"
    echo "  - dynamic-programming"
    echo "  - backtracking"
    echo "  - binary-search"
    echo "  - heaps"
    echo "  - sliding-window"
    echo "  - stack-queue"
    echo "  - two-pointers"
    echo "  - hash-tables"
    exit 1
fi

PATTERN=$1
DIFFICULTY=$2
PROBLEM_NAME=$3

# Validate difficulty
if [[ ! "$DIFFICULTY" =~ ^(easy|medium|hard)$ ]]; then
    echo -e "${RED}Error: Difficulty must be 'easy', 'medium', or 'hard'${NC}"
    exit 1
fi

# Define paths
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_FILE="$REPO_ROOT/templates/problem-template.md"
TARGET_DIR="$REPO_ROOT/$PATTERN/$DIFFICULTY"
TARGET_FILE="$TARGET_DIR/$PROBLEM_NAME.md"

# Check if pattern directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Error: Pattern directory not found: $TARGET_DIR${NC}"
    echo "Make sure the pattern name is correct."
    exit 1
fi

# Check if template exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo -e "${RED}Error: Template file not found: $TEMPLATE_FILE${NC}"
    exit 1
fi

# Check if problem file already exists
if [ -f "$TARGET_FILE" ]; then
    echo -e "${YELLOW}Warning: Problem file already exists: $TARGET_FILE${NC}"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 0
    fi
fi

# Copy template to target location
cp "$TEMPLATE_FILE" "$TARGET_FILE"

echo -e "${GREEN}✓ Created problem file: $TARGET_FILE${NC}"
echo ""
echo "Next steps:"
echo "  1. Open the file: $TARGET_FILE"
echo "  2. Fill in the problem details from LeetCode"
echo "  3. Solve the problem and document your approach"
echo "  4. Run tests and update PROGRESS.md"
echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"
