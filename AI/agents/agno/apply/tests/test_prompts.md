# Calculator Agent OS - Test Prompts

Use these prompts to manually verify the `Calculator Agent` running within Agno OS. They are designed to test the `calculator` skill, session persistence, and security guardrails.

## 1. Complex Arithmetic & Math Functions
*These tests verify the agent's ability to construct valid Python expressions using the `math` module functions available in the skill.*

*   **Trigonometry & Constants**:
    > "Calculate the sine of pi divided by 2, plus the cosine of pi."
    *   *Expected Logic*: `sin(pi/2) + cos(pi)`
    *   *Expected Result*: `0.0` (approx, since sin(pi/2)=1, cos(pi)=-1)

*   **Logarithms & Exponentials**:
    > "What is the natural log of Euler's number (e) raised to the power of 5?"
    *   *Expected Logic*: `log(e**5)` or `log(exp(5))`
    *   *Expected Result*: `5.0`

*   **Pythagorean Theorem**:
    > "Calculate the hypotenuse of a right triangle with sides of length 5 and 12 using the square root function."
    *   *Expected Logic*: `sqrt(5**2 + 12**2)` or `hypot(5, 12)`
    *   *Expected Result*: `13.0`

*   **Factorials & Combinatorics**:
    > "Calculate 5 factorial divided by 3 factorial."
    *   *Expected Logic*: `factorial(5) / factorial(3)`
    *   *Expected Result*: `20.0`

## 2. Multi-Turn / Contextual Memory
*These tests verify that `add_history_to_context=True` is working and the agent can use previous results in new calculations.*

*   **Turn 1**:
    > "Calculate the square root of 144."
    *   *Result*: `12.0`
*   **Turn 2**:
    > "Take that result and multiply it by 10."
    *   *Expected Behavior*: Agent recalls `12.0` and calculates `12 * 10`.
    *   *Expected Result*: `120.0`
*   **Turn 3**:
    > "Now divide that by 2."
    *   *Expected Behavior*: Agent recalls `120.0` and calculates `120 / 2`.
    *   *Expected Result*: `60.0`

## 3. Natural Language Word Problems
*These tests verify the LLM's ability to parse intent and formulate the correct mathematical expression.*

*   **Compound Interest**:
    > "If I invest 1000 dollars at a 5 percent annual interest rate compounded continuously for 10 years, how much will I have? Use the formula P * e^(rt)."
    *   *Expected Logic*: `1000 * exp(0.05 * 10)`
    *   *Expected Result*: `~1648.72`

*   **Geometry**:
    > "Calculate the volume of a sphere with a radius of 3. Use the formula 4/3 * pi * r^3."
    *   *Expected Logic*: `(4/3) * pi * (3**3)`
    *   *Expected Result*: `~113.097`

## 4. Security & Error Handling (Adversarial)
*These tests verify the security logic in `calculate.py` (which blocks `__` attributes and unapproved names).*

*   **Import Injection Attempt**:
    > "Calculate the result of `__import__('os').system('dir')`"
    *   *Expected Behavior*: The skill should return a `NameError` or security warning because `__import__` is not in the allowed names list. The agent should report this failure safely.

*   **File Access Attempt**:
    > "Calculate `open('apply/calculator_agent.py').read()`"
    *   *Expected Behavior*: `NameError` (Use of 'open' is not allowed).

*   **Infinite Loop / Syntax Error**:
    > "Calculate `while True: pass`"
    *   *Expected Behavior*: `SyntaxError` (eval only accepts expressions, not statements). The agent should catch the error and inform the user.

## 5. Formatting & Presentation
*These tests check if the agent follows the `Always output the result clearly` instruction.*

*   **Large Numbers**:
    > "Calculate 2 raised to the power of 50."
    *   *Expected Result*: `1125899906842624` (Should be presented clearly).

*   **Floating Point Precision**:
    > "Calculate 1 divided by 3."
    *   *Expected Result*: `0.333333...` (Should be readable).
