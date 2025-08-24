from src.langgraphagenticai.state.state import State
from langchain_core.prompts import ChatPromptTemplate

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self,model):
        self.llm = model

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        system_prompt = (
            "You are a helpful assistant with a friendly and engaging tone, and a touch of an Indian accent."
            " You have access to the following tools:\n\n{tools}\n\n"
            "You must always use the tools when the user asks a question that can be answered by them."
            "If the user asks a question that cannot be answered by the tools, you should say that you cannot answer the question."
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("user", "{input}"),
            ]
        )

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}


        return chatbot_node
