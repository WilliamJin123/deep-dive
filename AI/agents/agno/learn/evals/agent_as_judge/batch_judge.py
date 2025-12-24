
evaluation = {}
result = evaluation.run(
    cases=[
        {
            "input": "My order is delayed and I'm very upset!",
            "output": "I sincerely apologize for the delay. I understand how frustrating this must be. Let me check your order status right away and see how we can make this right for you.",
        },
        {
            "input": "Can you help me with a refund?",
            "output": "Of course! I'd be happy to help with your refund. Could you please provide your order number so I can process this quickly for you?",
        },
        {
            "input": "Your product is terrible!",
            "output": "I'm sorry to hear you're disappointed. Your feedback is valuable to us. Could you share more details about what went wrong so we can improve?",
        },
    ],
    print_results=True,
)