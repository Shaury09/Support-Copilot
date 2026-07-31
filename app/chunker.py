from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n## ",
        "\n# ",
        "\n\n",
        "\n",
        " ",
        ""
    ]
)

def create_chunks(text):
    return splitter.split_text(text)