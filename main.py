#!/usr/bin/env python3
"""
Sovereign AI Infrastructure
Author: Pranay M.

Secure, independent AI systems for critical national infrastructure
that operate without external dependencies.
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
import json
import sys
from datetime import datetime

console = Console()

BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                 🛡️ SOVEREIGN AI INFRASTRUCTURE 🛡️                              ║
║                    Secure National AI Systems                                  ║
║                           Author: Pranay M.                                    ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

MODULES = {
    "1": ("Security Architecture", "security_arch", "Design secure AI architectures"),
    "2": ("Dependency Analyzer", "dependency", "Analyze and minimize dependencies"),
    "3": ("Threat Modeler", "threat_model", "Model AI system threats"),
    "4": ("Data Sovereignty Planner", "data_sov", "Plan data sovereignty compliance"),
    "5": ("Resilience Designer", "resilience", "Design resilient AI systems"),
    "6": ("Air-Gap Configurator", "air_gap", "Configure air-gapped deployments"),
    "7": ("Supply Chain Validator", "supply_chain", "Validate AI supply chain security"),
    "8": ("Compliance Checker", "compliance", "Check regulatory compliance"),
    "9": ("Incident Responder", "incident", "Plan incident response procedures"),
    "10": ("Sovereignty Assessor", "sovereignty", "Assess overall AI sovereignty")
}

SYSTEM_PROMPTS = {
    "security_arch": """You are an expert in secure AI system architecture.

For each security architecture design, provide:

1. **Security Layers**: Defense in depth, perimeter, application, data security
2. **Access Control**: Authentication, authorization, least privilege
3. **Encryption Strategy**: Data at rest, in transit, key management
4. **Network Security**: Segmentation, monitoring, intrusion detection
5. **Audit & Logging**: Comprehensive audit trails, tamper-proof logs
6. **Incident Response**: Detection, containment, recovery procedures

Design secure architectures for sovereign AI systems.""",

    "dependency": """You are an expert in software dependency analysis and risk.

For each dependency analysis, evaluate:

1. **Dependency Inventory**: All external dependencies, versions, sources
2. **Risk Assessment**: Each dependency's risk level, foreign control
3. **Critical Path**: Dependencies essential for operation
4. **Alternative Options**: Domestic or open-source alternatives
5. **Mitigation Strategies**: Reducing dependency risks
6. **Independence Roadmap**: Path to full independence

Analyze and minimize external dependencies.""",

    "threat_model": """You are an expert in AI security threat modeling.

For each threat model, develop:

1. **Asset Identification**: What needs protection
2. **Threat Actors**: Nation-states, criminals, insiders, activists
3. **Attack Vectors**: Data poisoning, model extraction, adversarial attacks
4. **Vulnerability Analysis**: System weaknesses, exposure points
5. **Risk Prioritization**: Likelihood and impact assessment
6. **Countermeasures**: Defenses for each threat

Model threats to AI infrastructure comprehensively.""",

    "data_sov": """You are an expert in data sovereignty and privacy law.

For each data sovereignty plan, address:

1. **Data Classification**: Types, sensitivity, sovereignty requirements
2. **Legal Framework**: Applicable laws, regulations, requirements
3. **Storage Strategy**: Where data must reside, backup locations
4. **Processing Controls**: Who can process, under what conditions
5. **Cross-Border Flows**: Controls on international data movement
6. **Compliance Verification**: How to prove compliance

Plan data sovereignty for AI systems.""",

    "resilience": """You are an expert in resilient system design.

For each resilience design, provide:

1. **Failure Modes**: What can fail, how, consequences
2. **Redundancy Strategy**: N+1, geographic, functional redundancy
3. **Failover Design**: Automatic failover, recovery time objectives
4. **Degraded Operations**: Graceful degradation plans
5. **Disaster Recovery**: Backup, restore, continuity procedures
6. **Testing Regime**: How to validate resilience

Design resilient AI infrastructure.""",

    "air_gap": """You are an expert in air-gapped system deployment.

For each air-gap configuration, design:

1. **Isolation Architecture**: Physical and logical separation
2. **Data Transfer Protocols**: Secure data diode, one-way transfers
3. **Update Mechanisms**: Secure offline update procedures
4. **Monitoring Strategy**: Isolated monitoring systems
5. **Access Controls**: Physical and logical access restrictions
6. **Operational Procedures**: Day-to-day secure operations

Configure air-gapped AI deployments.""",

    "supply_chain": """You are an expert in AI supply chain security.

For each supply chain validation, assess:

1. **Hardware Provenance**: Chip origins, manufacturing chain
2. **Software Supply Chain**: Code origins, build processes
3. **Model Provenance**: Training data, model origins, integrity
4. **Vendor Assessment**: Supplier security, trustworthiness
5. **Tamper Detection**: How to detect supply chain compromises
6. **Secure Procurement**: Trusted acquisition processes

Validate AI supply chain security.""",

    "compliance": """You are an expert in AI regulatory compliance.

For each compliance check, evaluate:

1. **Regulatory Landscape**: Applicable laws, standards, frameworks
2. **Compliance Requirements**: Specific obligations
3. **Gap Analysis**: Current state vs required state
4. **Remediation Plan**: How to close compliance gaps
5. **Documentation**: Required records and evidence
6. **Ongoing Monitoring**: Continuous compliance verification

Check regulatory compliance for AI systems.""",

    "incident": """You are an expert in AI security incident response.

For each incident response plan, develop:

1. **Detection Capabilities**: How incidents are discovered
2. **Classification Framework**: Incident severity levels
3. **Response Procedures**: Step-by-step response actions
4. **Containment Strategies**: Limiting incident damage
5. **Recovery Procedures**: Restoring normal operations
6. **Post-Incident**: Lessons learned, improvements

Plan incident response for AI infrastructure.""",

    "sovereignty": """You are an expert in AI sovereignty assessment.

For each sovereignty assessment, evaluate:

1. **Independence Score**: Overall sovereignty level
2. **Critical Dependencies**: Key foreign dependencies
3. **Control Assessment**: What you control vs external control
4. **Risk Exposure**: Sovereignty-related risks
5. **Improvement Roadmap**: Path to greater sovereignty
6. **Strategic Recommendations**: Priority actions

Assess and improve AI sovereignty posture."""
}

def get_multiline_input(prompt_text):
    console.print(f"\n[cyan]{prompt_text}[/cyan]")
    console.print("[dim](Type 'END' on a new line when finished)[/dim]\n")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def query_llama(system_prompt, user_input):
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure Ollama is running."

def display_menu():
    console.print(BANNER, style="bold blue")
    table = Table(title="🛡️ Sovereignty Modules", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=8)
    table.add_column("Module", style="green", width=28)
    table.add_column("Description", style="white", width=42)
    for key, (name, _, desc) in MODULES.items():
        table.add_row(key, name, desc)
    table.add_row("0", "Exit", "Exit the application")
    console.print(table)

def run_module(module_key):
    name, key, desc = MODULES[module_key]
    console.print(Panel(f"🛡️ {name}", style="bold green"))
    user_input = get_multiline_input(f"Describe your {name.lower()} request:")
    with console.status(f"[bold green]Processing {name}..."):
        response = query_llama(SYSTEM_PROMPTS[key], user_input)
    console.print(Panel(Markdown(response), title=f"🛡️ {name} Results", border_style="green"))

def main():
    while True:
        display_menu()
        choice = Prompt.ask("\nSelect a module", choices=["0","1","2","3","4","5","6","7","8","9","10"])
        if choice == "0":
            console.print("\n[yellow]Thank you for using Sovereign AI Infrastructure![/yellow]")
            console.print("[dim]Author: Pranay M.[/dim]\n")
            break
        try:
            run_module(choice)
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled.[/yellow]")
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
