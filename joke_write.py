from autogen import ConversableAgent
import autogen

config_list_gemini = autogen.config_list_from_json("model_config.json")

joke_writer = ConversableAgent(
    name = "Joke Writer",
    system_message = "Write a funny joke about apples",
    llm_config = {"config_list": config_list_gemini},
    code_execution_config=False,
    human_input_mode="NEVER",
    function_map=None,
)

joke_reviwer = ConversableAgent(
    name = "Joke Reviwer",
    system_message = "Your task is to review the joke on Applesand provide your comments briefly in a list and you must ask for another joke.",
    llm_config = {"config_list": config_list_gemini},
    code_execution_config=False,
    human_input_mode="NEVER",
    function_map=None,
)

reply = joke_writer.generate_reply(messages=[{"content": "Write a joke on Green and red apple", "role": "user"}])

joke_writer.initiate_chat(joke_reviwer,message=reply['content'],max_turns=2)