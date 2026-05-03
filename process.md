# Game Preservation Index — Development Process

## 1. Project Purpose

The Game Preservation Index is a Python project that scores video games based on how important, vulnerable, and difficult they are to preserve.

The goal is to create a structured way to think about game preservation using data, scoring, and clear reasoning.

This project is being built as part of my learning journey in software development, game technology, and digital preservation.

---

## 2. Problem Statement

Many video games are at risk of becoming inaccessible because of issues such as:

- Digital storefront closures
- Online-only features
- Hardware dependency
- Licensing problems
- Lack of source code availability
- Poor documentation
- Emulation difficulty

The problem this project tries to solve is:

> How can we create a simple but meaningful way to assess how urgently a game needs preservation attention?

---

## 3. Computational Thinking

This project uses computational thinking to break the problem into smaller parts.

### Decomposition

The preservation problem is broken down into smaller scoring categories, such as:

- Historical importance
- Commercial/cultural importance
- Technical preservation difficulty
- Availability
- Legal/licensing risk
- Online dependency
- Hardware dependency

### Pattern Recognition

Many games share similar preservation risks. For example:

- Online-only games often become unplayable when servers shut down.
- Licensed games can disappear from storefronts.
- Games tied to unusual hardware are harder to preserve.
- Games with no physical release may be more vulnerable.

### Abstraction

The project simplifies a complex cultural and technical issue into measurable categories.

Instead of trying to capture every detail of a game, the project focuses on the most important preservation factors.

### Algorithm Design

Each game receives scores in different categories. These scores are combined to produce a final Game Preservation Index score.

The algorithm is designed to be understandable, adjustable, and explainable.

---

## 4. Current Scoring Model

Each game is represented using structured data.

Example fields:

- title
- year
- platform
- physical_release
- digital_only
- online_required
- server_status
- licensing_risk
- preservation_difficulty
- cultural_importance

The current goal is to calculate a `gpi_score` based on these factors.

This score is not intended to be perfect. It is a starting point that can be improved over time.

---

## 5. Development Steps

### Step 1 — Create basic project structure

Set up the project folder, Git repository, and GitHub repository.

### Step 2 — Create sample game data

Add a small number of example games using simple Python data structures.

### Step 3 — Create scoring logic

Write a function that calculates a preservation score for each game.

### Step 4 — Display the results

Print the games and their scores clearly in the terminal.

### Step 5 — Improve the algorithm

Refine the scoring system by adding better categories, weighting, and explanations.

### Step 6 — Add tests

Create simple tests to check that the scoring system works correctly.

### Step 7 — Add documentation

Use files like `README.md`, `PROCESS.md`, and comments in the code to explain the project.

---

## 6. Design Principles

This project follows these principles:

- Keep the code simple and readable
- Build in small steps
- Commit changes regularly
- Explain decisions clearly
- Make the scoring system transparent
- Improve the project through reflection

---

## 7. Future Improvements

Possible future improvements include:

- Store game data in CSV or JSON files
- Add more detailed preservation categories
- Create a command-line interface
- Build a simple web app
- Add charts or visualisations
- Add OpenAI-assisted analysis
- Create a public-facing version for Keep It Playable
- Allow users to submit games for assessment

---

## 8. Reflection Log

### Current Reflection

At this stage, the project is focused on learning the fundamentals of Python, Git, GitHub, and software design.

The most important goal is not to build a perfect system immediately. The goal is to build a working project step by step and understand why each part exists.

Future versions of the project can become more advanced as my programming skills improve.