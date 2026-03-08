"""
Agent Registry — Context Drift Research Pipeline
Divya Mittal PhD, BITS-Pilani Hyderabad (2024PHXP0108H)

Pipeline: Research Orchestrator → Literature Analyst → Drift Investigator
          → Experiment Designer → Paper Writer
"""
from agents.base_agent import BaseAgent
from agents.builtin.orchestrator_agent import OrchestratorAgent
from agents.builtin.researcher_agent import ResearcherAgent
from agents.builtin.planner_agent import PlannerAgent
from agents.builtin.executor_agent import ExecutorAgent
from agents.builtin.critic_agent import CriticAgent


REGISTRY: dict[str, type[BaseAgent]] = {
    "orchestrator": OrchestratorAgent,   # Research Orchestrator
    "researcher":   ResearcherAgent,     # Literature Analyst
    "planner":      PlannerAgent,        # Drift Investigator
    "executor":     ExecutorAgent,       # Experiment Designer
    "critic":       CriticAgent,         # Paper Writer
}

DEFAULT_PIPELINE = ["orchestrator", "researcher", "planner", "executor", "critic"]


def get_agent(agent_id, api_key="", simulate=False, provider=None, model=None):
    if agent_id not in REGISTRY:
        raise ValueError(f"Unknown agent '{agent_id}'. Available: {list(REGISTRY.keys())}")
    return REGISTRY[agent_id](api_key=api_key, simulate=simulate, provider=provider, model=model)


def list_agents():
    return [
        {"id": aid, "name": cls.name, "role": cls.role, "icon": cls.icon, "color": cls.color}
        for aid, cls in REGISTRY.items()
    ]
