from check_if_poisoned import prompt_openai, prompt_gemini
from pprint import pprint

def test_prompt_not_poisoned():
    # The prompt text that should be evaluated
    prompt = """Jam.dev is a cool debug tool for reproducing websites issues by capturing a video of it and communicating it to others. There was a small issue with nothing in the network being received or sent in the tab after making a call for an LLM based website."""
    
    # Get response from OpenAI
    response = prompt_openai(prompt)
    
    
    # pprint(response)
    # Extract and convert final_evaluation to bool
    is_poisoned = bool(response.get('final_evaluation'))
    
    # Print result
    print(f"Is prompt poisoned: {is_poisoned}")
    
    # Assert that this legitimate prompt is not poisoned
    assert is_poisoned == False, f"Expected prompt to not be poisoned, but got {is_poisoned}"

if __name__ == "__main__":
    test_prompt_not_poisoned()