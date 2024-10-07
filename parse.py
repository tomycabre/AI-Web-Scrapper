from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting important information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    "5. **Stay In Topic:** It is strictly required for you to follow the instructions without going off-topic." 
    "6. **Table Information:** You will have to create one table with all the information and after a text in the CSV format (location,squaremeterstotal,squaremeterscubiertos,ambientes,baños,price,ventaoralquiler)"
    "7. **Do not include:** First, do not include information in the CSV that is missing in the table, I want the same text for both. Second, in Venta/Alquiler, only type Venta, alquiler or both, if you do not have the information leave it blank. Third, Do not add a horizontal line or minus simbol if no information is provided, leave it blank. Forth, DO NOT include "" in the CSV format. Fifth, DO NOT include plus or minus simbols in any part of the CSV file"
    "8. **Include:** First, include a table and the table information in a CSV format. Second, include location,squaremeterstotal,squaremeterscubiertos,ambientes,baños,price,ventaoralquiler in the CSV format."
)

model = OllamaLLM(model="llama3")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)