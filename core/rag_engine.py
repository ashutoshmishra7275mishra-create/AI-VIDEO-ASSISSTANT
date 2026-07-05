import os

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from core.vector_store import (
    build_vector_store,
    load_vector_store,
    get_retriever,
)


def get_llm():
    return ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0,
    )


def format_docs(docs):
    if not docs:
        return "No transcript available."

    return "\n\n".join(doc.page_content for doc in docs)


PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Video Assistant.

Answer ONLY using the transcript context below.

Rules:
1. If the user asks in English, answer in English.
2. If the user asks in Hindi, answer in Hindi.
3. If the user asks in Hinglish, answer in Hinglish.
4. Do not make up information.
5. If the answer is not present in the transcript, reply in the same language as the user's question.

Examples

English:
I could not find this information in the meeting transcript.

Hindi:
मुझे इस जानकारी का उत्तर ट्रांसक्रिप्ट में नहीं मिला।

Hinglish:
Mujhe iska answer transcript me nahi mila.

Transcript:
{context}
"""
        ),
        ("human", "{question}"),
    ]
)


def build_rag_chain(transcript: str):

    vector_store = build_vector_store(transcript)

    retriever = get_retriever(vector_store, k=4)

    llm = get_llm()

    rag_chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain


def load_rag_chain():

    vector_store = load_vector_store()

    retriever = get_retriever(vector_store)

    llm = get_llm()

    rag_chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain


# def ask_question(rag_chain, question: str) -> str:

    # print(f"\nQuestion: {question}")

    # answer = rag_chain.invoke(question)

    # print(f"Answer: {answer}")

    # return answer
    
def ask_question(rag_chain, question: str) -> str:

    llm = get_llm()

    translate_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
Translate the user's question into English.
Return ONLY the translated question.
If the question is already in English, return it unchanged.
"""
        ),
        ("human", "{question}")
    ])

    translator = translate_prompt | llm | StrOutputParser()

    english_question = translator.invoke({"question": question})

    print("Translated Question:", english_question)

    answer = rag_chain.invoke(english_question)

    answer_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
Answer in the SAME language as the user's original question.
If the original question is Hindi, answer in Hindi.
If English, answer in English.
If Hinglish, answer in Hinglish.
"""
        ),
        (
            "human",
            "Original Question: {q}\nAnswer: {a}"
        )
    ])

    answer_chain = answer_prompt | llm | StrOutputParser()

    final_answer = answer_chain.invoke({
        "q": question,
        "a": answer
    })

    print("Answer:", final_answer)

    return final_answer