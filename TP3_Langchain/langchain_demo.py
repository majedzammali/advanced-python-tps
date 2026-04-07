from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Note: You need to set OPENAI_API_KEY in your environment
# For demo without API key, we'll create a mock example

class MockLLM:
    """Mock LLM for demonstration without API key"""
    def predict(self, text):
        return f"[AI Response] Here's a helpful answer about: {text[:50]}..."

def demo_langchain():
    """Demonstrate Langchain concepts"""
    
    # Create a prompt template
    template = """
    Question: {question}
    
    Let me explain this advanced Python concept step by step:
    1. First, understand the basics...
    2. Then, here's how it works...
    3. Finally, here's an example...
    
    Answer:
    """
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Use mock LLM (replace with OpenAI('gpt-3.5-turbo') if you have API key)
    llm = MockLLM()
    chain = LLMChain(llm=llm, prompt=prompt)
    
    questions = [
        "What is a decorator in Python?",
        "How do generators work?",
        "Explain context managers"
    ]
    
    for q in questions:
        print(f"\n❓ {q}")
        response = chain.run(question=q)
        print(f"💡 {response}")
        print("-" * 50)

if __name__ == "__main__":
    print("🤖 Langchain Demo")
    print("=" * 50)
    demo_langchain()
    print("\n✅ To use real OpenAI, set OPENAI_API_KEY and use OpenAI()")