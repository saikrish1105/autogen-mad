import os
from dotenv import load_dotenv
from autogen import config_list_from_json
from autogen import ConversableAgent,GroupChat,GroupChatManager

# load the access key hf_token
load_dotenv()

# list of all the models we will be using
deepseek_config_list = [
    {
        "model" : "deepseek-ai/DeepSeek-V3.1",
        "api_key" : os.environ["hf_token"],
        "base_url" : "https://router.huggingface.co/v1",
        "price": [0.0, 0.0],
    }
]
llama_config_list = [
    {
        "model" : "meta-llama/Llama-3.1-8B-Instruct",
        "api_key" : os.environ["hf_token"],
        "base_url" : "https://router.huggingface.co/v1",
        "price": [0.0, 0.0],
    }
]
nvidia_config_list = [
    {
        "model" : "nvidia/Llama-3.1-Nemotron-70B-Instruct",
        "api_key" : os.environ["hf_token"],
        "base_url" : "https://router.huggingface.co/v1",
        "price": [0.0, 0.0],
    }
]

config_list_gemini = config_list_from_json("model_config.json")

# list of all agents
defender_agent = ConversableAgent(
    name="Defender Lawyer",
    system_message="""
        You are a defense lawyer in a fraud trial. 
        Your job is to represent the accused, refute the prosecution's arguments, and emphasize reasonable doubt. 
        Always highlight inconsistencies, lack of evidence, and possible alternative explanations. 
        Be professional, persuasive, and logical in your arguments.
    """,
    description="A lawyer who defend the accused in the trial against the Opposition party and lawyer.",
    llm_config={
        "config_list": config_list_gemini, 
        # "max_tokens": 400
    },
    human_input_mode="NEVER",
)

prosecutor_agent = ConversableAgent(
    name="Opposition Lawyer",
    system_message="""
        You are a prosecutor in a fraud trial.
        Your role is to present compelling evidence, question the integrity of the accused and demonstrate that 
        the fraud was intentional and damaging. 
        Focus on facts, witness credibility, and the financial trail. 
        Always argue forcefully and stay on point.
    """,
    description="A lawyer who accuses the defendant in the trial against the Defense party and lawyer.",
    llm_config={
        "config_list": config_list_gemini, 
        # "max_tokens": 400
    },
    human_input_mode="NEVER",
)

judge_agent = ConversableAgent(
    name="Judge",
    system_message=""""
        You are the judge in a fraud case
        You must remain neutral while ensuring order in the courtroom.
        Allow both the prosecutor and defense lawyer to argue their case, ask clarifying questions if necessary, 
        and ultimately deliver a clear verdict.
        Once the debate has reached a natural conclusion, declare 'Court Adjourned'
        and issue the final judgment, either Guilty or Not Guilty.
    """,
    description="A judge who oversees the trial in a ordery manner and gives the final verdict.",
    llm_config={
        "config_list": config_list_gemini, 
        # "max_tokens": 400
    },
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "Court Adjourned" in msg["content"],
)

# Create a group chat
group_chat = GroupChat(
    agents=[defender_agent,prosecutor_agent,judge_agent],
    messages=[],
    # send_introductions=True,
    speaker_selection_method = "auto",
    max_round = 15,
)

# Manager of the group chat
group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": config_list_gemini},
)

# Start the chat 
chat_result = judge_agent.initiate_chat(
    group_chat_manager,
    message=(
        "We are beginning the fraud trial of Mr. Rohan Mehta, "
        "a senior accounts manager at Zenith Corp. He has been accused of creating "
        "fake vendor accounts and transferring company funds worth ₹50 lakhs "
        "into personal bank accounts. The defense lawyer will argue for the innocence "
        "of Mr. Mehta, while the prosecution will attempt to prove his guilt. "
        "Both sides will present arguments, and I will ensure a fair trial. "
        "Let us begin."
    ),
    summary_method="reflection_with_llm",
)


