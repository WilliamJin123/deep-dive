from agno.workflow import Step, Workflow

# Named steps for better tracking
workflow = Workflow(
    name="Content Creation Pipeline",
    steps=[
        Step(name="Research Phase", team=researcher),
        Step(name="Analysis Phase", executor=custom_function), 
        Step(name="Writing Phase", agent=writer),
    ]
    #Use Step objects for better support, probably norm for me
)

workflow.print_response(
    "AI trends in 2024",
    markdown=True,
)