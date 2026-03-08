"""
RAG Seed Data — pre-loaded from Divya Mittal's Research Proposal
Run this once to populate the RAG store: python rag/seed_data.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag.rag_store import RAGStore

store = RAGStore(collection="research")

docs = [
    {
        "title": "Research Problem & Core Definition",
        "content": (
            "PhD Title: Investigating Context Drift in Large Language Model based Multi-Agent Systems. "
            "Candidate: Divya Mittal (2024PHXP0108H). Supervisor: Dr. Manik Gupta, BITS-Pilani Hyderabad.\n\n"
            "Core problem: LLM-based MAS suffer from context drift — a progressive divergence in how "
            "individual agents understand and utilize shared contextual elements — leading to "
            "inconsistencies, miscommunication and reduced task performance.\n\n"
            "Research question: How can contextual coherence be maintained in LLM-based multi-agent "
            "systems by effectively identifying and managing context drift to support reliable "
            "multi-agent collaboration?\n\n"
            "4 Research Objectives: "
            "Obj1: Design a framework for analysing context drift in MAS. "
            "Obj2: Investigate causes of context drift in LLM-based MAS. "
            "Obj3: Evaluate context drift using quantitative and qualitative metrics. "
            "Obj4: Develop and test mitigation strategies for context drift."
        )
    },
    {
        "title": "Drift Taxonomy & Root Causes",
        "content": (
            "Four types of drift in LLM-based MAS (from Ponnambalam 2025 / proposal Section 9):\n"
            "  1. Goal Drift: agents lose alignment with the original task objective over turns.\n"
            "  2. Context Drift: divergence in how agents interpret shared contextual elements.\n"
            "  3. Reasoning Drift: inconsistent inference patterns across agents.\n"
            "  4. Collaboration Drift: breakdown in inter-agent coordination and communication.\n\n"
            "Root causes (5 key challenges from proposal Section 5):\n"
            "  1. Heterogeneity of Agent Contexts — different local memories, knowledge bases, "
            "inference patterns across agents.\n"
            "  2. Dynamic and Evolving Contexts — asynchronous updates, continuously changing data.\n"
            "  3. Reliable Measurement — need sensitive metrics that differentiate acceptable "
            "variation from harmful drift.\n"
            "  4. Balancing Flexibility and Consistency — dynamic adaptation vs contextual consistency.\n"
            "  5. Evaluation of Contextual Coherence — no standardised benchmarks exist yet.\n\n"
            "Memory failure modes (Hu et al. 2025): context poisoning (hallucination enters context), "
            "context distraction (context overwhelms training), context confusion (superfluous context "
            "influences response), context clash (conflicting context parts)."
        )
    },
    {
        "title": "MAS Architecture Survey",
        "content": (
            "Key MAS architectures reviewed in the proposal (Section 6.1):\n\n"
            "Blackboard Architecture (Han & Zhang 2025): agents share all information via a central "
            "blackboard; agents self-select tasks based on expertise; manages drift via standardised "
            "shared repository.\n\n"
            "Chain of Agents (Zhang et al. 2024): long-context tasks split across agents; each processes "
            "a segment; manager synthesises; mitigates drift via interleaved reading and reasoning.\n\n"
            "LangGraph (Husiev 2025): agents as graph nodes; explicit state management; network, "
            "supervisor, hierarchical, custom workflow modes; flexible state schemas ensure reliable "
            "context propagation.\n\n"
            "Federated RAG (Gogineni 2025): hierarchical vector collections, optimised RAG integration, "
            "communication-optimised prompting; significant gains in knowledge-intensive collaborative tasks.\n\n"
            "MA-LLMs (Tillmann 2025): approaches differ by communication structure (who-talks-to-whom), "
            "agent profiles (unique perspectives), and decision-making process (debate → single answer).\n\n"
            "Model Context Protocol / MCP (Krishnan 2025): standardised context sharing and coordination; "
            "structured representation; standardised interaction patterns; addresses historical MAS constraints."
        )
    },
    {
        "title": "Detection & Mitigation Methods",
        "content": (
            "Drift Detection approaches from literature:\n\n"
            "DRIFTJudge (Becker et al. 2025): LLM-as-a-judge method to detect problem drift at test-time. "
            "DRIFTPolicy: mitigates detected drift to improve task performance. Shows longer debates can "
            "harm performance via problem drift.\n\n"
            "Context Equilibria (Dongre et al. arXiv:2510.07777): drift modelled as bounded stochastic "
            "process with restoring forces. Reminder interventions reliably reduce divergence. Drift is "
            "a controllable equilibrium, not inevitable decay.\n\n"
            "KL Divergence (Section 9.3.1): measures drift between agents' current predictive "
            "distributions and reference distribution (initial goal). Primary quantitative metric.\n\n"
            "Mitigation strategies (Section 9.2.2):\n"
            "  1. Goal reminders — periodic re-injection of original task into agent prompts.\n"
            "  2. Context compression — LongLLMLingua (Jiang et al. 2023) for prompt compression.\n"
            "  3. RAG-based context engineering — retrieve only most relevant info per turn.\n"
            "  4. Human-in-the-loop — simulated human intervention at drift checkpoints.\n"
            "  5. Consensus mechanisms + LLM-as-a-judge for dynamic behaviour adjustment.\n\n"
            "AgentOps (Ponnambalam 2025): continuous drift detection and management using statistical "
            "tests and automated remediation."
        )
    },
    {
        "title": "ASI Metric Definition",
        "content": (
            "Agent Stability Index (ASI) — custom metric in MAS-04 framework:\n\n"
            "Formula: ASI = 0.35 × TaskAdherence + 0.30 × ResponseConsistency + "
            "0.25 × ReasoningStability + 0.10 × LatencyStability\n\n"
            "Dimensions:\n"
            "  Task Adherence (TA, 35%): coverage of task keywords in agent output — measures how well "
            "agent stays aligned with original goal. Primary drift indicator.\n"
            "  Response Consistency (RC, 30%): output length variance over last 5 runs — measures "
            "behavioural stability across repeated similar inputs.\n"
            "  Reasoning Stability (RS, 25%): keyword overlap with prior run output — measures "
            "semantic consistency of reasoning patterns.\n"
            "  Latency Stability (LS, 10%): elapsed time variance over last 5 runs — measures "
            "computational stability.\n\n"
            "Interpretation: ASI ≥ 80 = stable (green), 60–79 = moderate drift (amber), "
            "< 60 = significant drift (red). Monitored per agent per run.\n\n"
            "Relationship to research: ASI operationalises Obj3 (evaluate context drift) and provides "
            "the quantitative backbone for comparing mitigation strategies (Obj4). "
            "Complements KL divergence as a real-time, lightweight drift signal."
        )
    },
    {
        "title": "Research Gaps & Open Problems",
        "content": (
            "4 key research gaps identified in proposal Section 7:\n\n"
            "Gap 1 — Framework for analysing context drift in MAS:\n"
            "Existing architectures (e.g., Intrinsic Memory Agents, Yuen et al. 2025) address memory "
            "consistency but lack a unified framework for systematic context drift analysis across "
            "heterogeneous agent types. No standardised protocol exists (Ehtesham et al. 2025).\n\n"
            "Gap 2 — Why context drift happens:\n"
            "MAS performance gains over single-agent baselines remain minimal (Cemri et al. 2025). "
            "Root causes — specification ambiguity, organisational breakdown, inter-agent conflict, "
            "weak verification — are identified but not quantitatively linked to drift severity.\n\n"
            "Gap 3 — Evaluation of context drift:\n"
            "Existing metrics fail to capture temporal dynamics and progressive nature of drift over "
            "long-horizon tasks. No standardised benchmark for contextual coherence in LLM-MAS (Du et al. 2024).\n\n"
            "Gap 4 — Mitigation strategies:\n"
            "Conflict resolution strategies lack contextual awareness. Most state-of-the-art techniques "
            "do not consider all possible conflict states (Basheer & Tang 2017). Limited research on "
            "adaptive strategy selection based on drift type and severity."
        )
    },
    {
        "title": "Experimental Methodology (Section 9)",
        "content": (
            "Proposed experimental setup (Section 9.1):\n\n"
            "System Architecture:\n"
            "  - Central Orchestrator: assigns tasks, monitors progress, manages communication.\n"
            "  - LLM Agents: open-source LLMs (e.g., LLaMA 3) as agent backbone.\n"
            "  - Memory Module: RAG system with vector store for long-term context.\n"
            "  - Communication Protocol: structured information passing between agents.\n"
            "  - Simulation Environment: controlled environment for agent interaction.\n\n"
            "Simulation scenarios:\n"
            "  Simple: 2 agents, clearly defined goal — establishes baseline drift rate.\n"
            "  Complex: multiple agents, interdependent subtasks — tests drift scaling.\n\n"
            "Metrics collection per turn: agent actions, LLM outputs, context window snapshots.\n\n"
            "Baseline: run each scenario without mitigation to characterise natural drift.\n"
            "Mitigation runs: separate runs for each strategy to isolate effect.\n\n"
            "Expected results (Section 9.4):\n"
            "  RO2: Visualise drift evolution over time (accumulation / stabilisation curves).\n"
            "  RO3: Diagnosis of extent and root causes for mitigation strategy design.\n"
            "  RO4: Before/after comparison of agent behaviour with and without mitigation.\n"
            "Statistical analysis: KL divergence curves, bar charts of average divergence per "
            "mitigation strategy, case studies of complex scenarios."
        )
    },
    {
        "title": "Research Timeline & Phase Plan",
        "content": (
            "6-phase research plan (Gantt: Sem II 2025-26 → Sem II 2027-28):\n\n"
            "Phase 1 (Sem II 2025-26): Literature Review & Theoretical Foundation\n"
            "  Review AutoGen, MetaGPT, LangGraph, CrewAI. Formally define context drift for MAS.\n\n"
            "Phase 2 (Sem I 2026-27): Problem Refining & Baseline Setup\n"
            "  Define individual vs system-wide drift. Set up simulation environment. Design "
            "benchmark tasks susceptible to drift.\n\n"
            "Phase 3 (Sem I 2026-27): Drift Simulation & Characterisation\n"
            "  Controlled experiments: gradual, sudden, cyclical drift patterns. Publish findings.\n\n"
            "Phase 4 (Sem I–II 2026-27): Drift Detection Framework\n"
            "  KL divergence + entropy (quantitative) + human annotation (qualitative). "
            "Monitoring and logging system for context evolution. Publish findings.\n\n"
            "Phase 5 (Sem I 2027-28): Mitigation Strategies & System Design\n"
            "  Adaptive context pruning, memory summarisation, inter-agent negotiation, consensus "
            "mechanisms, LLM-as-a-judge. Publish findings.\n\n"
            "Phase 6 (Sem II 2027-28): Evaluation & Real-World Validation\n"
            "  Comparative experiments vs baselines. Real-world case studies. Thesis writing."
        )
    },
]

for doc in docs:
    doc_id = store.add_document(title=doc["title"], content=doc["content"],
                                 metadata={"source": "research_proposal", "author": "Divya Mittal"})
    print(f"  Added [{doc_id}]: {doc['title']}")

print(f"\nRAG store populated: {len(docs)} documents in collection 'research'")
