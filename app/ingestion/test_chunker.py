# from app.ingestion.chunker import split_documents
# from app.ingestion.loader import load_pdf

# documents=load_pdf("data/document/HCE.pdf")

# chunks =split_documents(documents)

# print(f"Pages: {len(documents)}")
# print(f"chunks: {len(chunks)}")

# for index, chunk in enumerate(chunks[:5]):
#     print("="*80)
#     print(f"chunk: {index}")
#     print(f"source: {chunk.metadata.get('source')}")
#     print(f"Page: {chunk.metadata.get('page')}")
#     print(chunk.page_content)