from langgraph.graph import StateGraph, END

from state import GraphState

from agents_langgraph import (
    schema_agent,
    planner_agent,
    sql_agent,
    execute_agent,
    fixer_agent,
    answer_agent
)


workflow = StateGraph(GraphState)


# Nodes
workflow.add_node("planner", planner_agent)
workflow.add_node("schema", schema_agent)
workflow.add_node("sql", sql_agent)
workflow.add_node("execute", execute_agent)
workflow.add_node("fix", fixer_agent)
workflow.add_node("answer", answer_agent)


# Flow
workflow.set_entry_point("planner")

workflow.add_edge("planner", "schema")

workflow.add_edge("schema", "sql")

workflow.add_edge("sql", "execute")


# Conditional routing
def route(state):

    if state.get("error"):

        return "fix"

    return "answer"


workflow.add_conditional_edges(

    "execute",

    route,

    {

        "fix": "fix",

        "answer": "answer"

    }

)


workflow.add_edge("fix", "sql")

workflow.add_edge("answer", END)


app = workflow.compile()


def ask(question):

    return app.invoke({

        "question": question

    })