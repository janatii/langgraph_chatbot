from main import graph

def export_graph_image(filename="langgraph_chatbot.png"):
    graph.get_graph().draw_mermaid_png(output_file_path=filename)
    print(f"LangGraph diagram saved as {filename}")

if __name__ == "__main__":
    export_graph_image()
