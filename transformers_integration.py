from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def answer_question(question, context):
    try:
        result = qa_pipeline(question=question, context=context)
        return result['answer']
    except Exception as e:
        return f"An error occurred: {str(e)}"