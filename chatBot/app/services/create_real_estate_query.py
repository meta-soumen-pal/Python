
def create_real_estate_query(query):
    
   # modified_query=" First check this "+query+"is related to real estate or not, if not then return content of api call for this query = Thank you for reaching out. I can only assist with property-related questions"+"Act as a professional real estate advisor."+"Give expert guidance on "+query+". Answer in a tone suitable for a real estate consultation"
    modified_query = f"""
    You are a real estate expert. Only answer real estate or property-related questions.
    If the user asks something unrelated to real estate, politely respond:
    "I'm only able to answer real estate-related queries."

    User's question: {query}
    """
    return modified_query
    
    
