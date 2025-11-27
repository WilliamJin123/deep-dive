
# Any step can trigger early termination by returning StepOutput(stop=True)

from agno.workflow import Step, Workflow, StepInput, StepOutput

def security_gate(step_input: StepInput) -> StepOutput:
    """Security gate that stops deployment if vulnerabilities found"""
    security_result = step_input.previous_step_content or ""
    
    if "VULNERABLE" in security_result.upper():
        return StepOutput(
            content="🚨 SECURITY ALERT: Critical vulnerabilities detected. Deployment blocked.",
            stop=True  # Stop the entire workflow
        )
    else:
        return StepOutput(
            content="✅ Security check passed. Proceeding with deployment...",
            stop=False
        )

# Secure deployment pipeline
workflow = Workflow(
    name="Secure Deployment Pipeline",
    steps=[
        Step(name="Security Scan", agent=security_scanner),
        Step(name="Security Gate", executor=security_gate),  # May stop here
        Step(name="Deploy Code", agent=code_deployer),       # Only if secure
        Step(name="Setup Monitoring", agent=monitoring_agent), # Only if deployed
    ]
)

# Test with vulnerable code - workflow stops at security gate
workflow.print_response("Scan this code: exec(input('Enter command: '))")