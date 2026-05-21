#My GenAI learning journey
Date: May 16, 2026
Topics covered: LLM basics, token prediction, training pipeline
  (Pre-training → SFT → RLHF)

Key concept (simple): LLMs predict next words using patterns 
  from massive text. Training has 3 stages to make them helpful.

Key concept (technical): Transformer-based models trained via 
  next-token prediction, then aligned via SFT + RLHF/CAI.

Questions I have: [write yours here]
Next session: Transformers & Attention mechanism (Week 1, Day 3)


Date: May 17, 2026
Topic: Transformer & Attention Mechanism

Simple version: Every word looks at every other word and 
  decides how relevant it is. That's attention.

Technical version: Multi-head self-attention using Q/K/V 
  vectors, repeated across N transformer blocks, with 
  positional encodings to preserve sequence order.

Key insight: The 2017 "Attention Is All You Need" paper 
  changed everything. All modern LLMs are Transformers.

Next session: Hallucination deep dive + LLM limitations


Date: May 18, 2026
Topics: Hallucination + LLM Limitations

Simple version: LLMs confidently make things up sometimes,
  and have real limits — no memory, no internet, no feelings.

Technical version: Hallucination stems from next-token 
  prediction optimizing for fluency over accuracy. 
  Limitations include knowledge cutoff, finite context 
  window, no persistent state, and weak novel reasoning.

Key insight: These limitations directly motivate WHY we 
  need RAG, Agents, and Tool Use — exactly what we build 
  in Phase 2.

Next session: Prompt Engineering — Week 2 begins 🎯


Day 5 — 19 May Week 1 Recap
Week 1 Topics Covered:
What is an LLM — next token predictor built on Transformer architecture
Training Pipeline — Pre-training → SFT → RLHF
Attention Mechanism — Q, K, V vectors + Multi-head attention
Hallucination — root cause is optimizing for fluency over accuracy
7 LLM Limitations — knowledge cutoff, no real-time awareness, no persistent memory, finite context window, no true reasoning, no real world awareness, prompt sensitivity

Week 2, Day 1 — Prompt Engineering
Topic 1 — System vs User Prompts
System prompt = owner's instructions to the chef (set by developer, strong, persistent)
User prompt = customer's order (set by user, weaker)
Real system prompts can only be set via API — not inside chat window
Every AI product you use has a hidden system prompt
Topic 2 — Zero Shot Prompting
Zero shot = asking directly with zero examples
Works because model learned tasks during pre-training
Formula: [Role] + [Task] + [Format] + [Constraint]
Always be specific — vague prompt = vague answer
Next Session:
Topic 3 — Few Shot Prompting

Day 6 may 20, 2026
Topic 3 — Few Shot Prompting
Core Idea:
Shot = example you give to the model
Few shot = give a few examples before asking
Works by showing the model exactly what you want — style, format, tone
Why it's powerful:
Zero shot = model guesses your intent
Few shot = you show your intent
Transfers specific style/format without retraining
What makes good examples:
Diverse — cover different cases
Representative — match real inputs
Consistent — same format every time
Sweet spot: 3-5 examples for most tasks. 10+ → consider fine-tuning instead.

May 20, 2026
Topic 4 — Chain of Thought (CoT) Prompting
Core Idea:
Forces model to think step by step before answering
Like a maths teacher saying "show your work"
Just adding "Think step by step" improves accuracy dramatically
Two types:
Zero Shot CoT → just add "Think step by step"
Few Shot CoT → show examples of step by step reasoning
Real use cases:
Math & logic problems
Code debugging
Decision making
Interview prep
Key insight:
CoT is the foundation of how AI Agents work — automated step by step reasoning
May 21, 2026
📓 Today's Session Notes — Week 2 Final + Core Engineering

Prompt Engineering — Topics Completed
Topic 5 — Structured JSON Output
Use JSON format for clean, parseable AI output
Always strip markdown backticks before parsing
Formula: specify exact keys + "Reply JSON only — no extra text"
Topic 6 — Prompt Injection & Security
Injection = user trying to override system prompt
Two types: Direct (user asks directly) + Indirect (hidden in documents)
Defence: Strong system prompt + Input validation in code + Least privilege access

Core Engineering — Git + GitHub
Commands learned:
bash
git clone     → copy repo to machine
git add .     → stage all files
git commit    → save with message
git push      → upload to GitHub
git remote set-url → change remote URL
Setup done:
GitHub account connected ✅
VS Code + gh CLI authenticated ✅
HTTPS push working ✅

Project 1 — Prompt System Designer ✅
What it does: Turns Claude into a study assistant — Simple → Medium → Deep explanation + JSON quiz
Files on GitHub:
project-1-prompt-system/
├── README.md
├── system_prompt.txt
└── test_output.md
GitHub: github.com/Sk-husamuddin/genai-learning-journey ✅

Current Status
Week 1 — LLM Foundations        ✅ COMPLETE
Week 2 — Prompt Engineering     ✅ COMPLETE
Project 1 — Prompt System       ✅ COMPLETE + GitHub
Git + GitHub Setup              ✅ COMPLETE

Next Session:
Week 3 — Your First API Calls
Topic 1: What is an API?
