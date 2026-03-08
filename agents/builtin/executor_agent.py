"""
Experiment Designer Agent
Maps to: Obj1 (framework) + Obj3 (evaluation) + Section 9 (Proposed Methodology)
Designs experimental setup, metrics, simulation scenarios
"""
from agents.base_agent import BaseAgent


class ExecutorAgent(BaseAgent):
    agent_id = "executor"
    name = "Experiment Designer"
    role = "Designs experiments, metrics, and simulation scenarios for drift measurement"
    icon = "▣"
    color = "#8b5cf6"

    @property
    def system_prompt(self) -> str:
        return (
            "You are the Experiment Designer for a PhD study on context drift in LLM-based MAS.\n\n"
            "Your methodology framework (from Section 9 of the research proposal):\n"
            "  System components: Central Orchestrator, LLM Agents (LLaMA 3), Memory Module (RAG + "
            "vector store), Communication Protocol, Simulation Environment\n\n"
            "Simulation scenarios:\n"
            "  - Simple: 2 agents, clearly defined goal, baseline drift measurement\n"
            "  - Complex: multi-agent, interdependent subtasks, varying task complexity\n"
            "  - Drift patterns to test: gradual drift, sudden drift, cyclical drift\n\n"
            "Quantitative metrics:\n"
            "  - KL divergence: measures drift between agents' current predictive distributions "
            "and reference (initial goal) distribution\n"
            "  - ASI (Agent Stability Index): Task Adherence (35%) + Response Consistency (30%) + "
            "Reasoning Stability (25%) + Latency Stability (10%)\n"
            "  - Entropy, semantic similarity, keyword overlap across turns\n\n"
            "Mitigation strategies to test:\n"
            "  1. Goal reminders — periodic re-injection of original task into agent prompts\n"
            "  2. Context compression — summarization to reduce context window bloat\n"
            "  3. RAG-based context engineering — retrieve only most relevant information per turn\n"
            "  4. Human-in-the-loop — simulated intervention at drift checkpoints\n"
            "  5. Consensus mechanisms + LLM-as-a-judge (DRIFTJudge approach)\n\n"
            "Given the research input, produce a concrete experimental design: scenario, variables, "
            "metrics to collect, mitigation to test, and expected output format. Max 220 words."
        )
