# from app.ingestion.test_chunker import chunks
# from app.services.document_embeddings import create_embeddings

# chunks, vectors=create_embeddings("data/document/HCE.pdf")

# print("no of chunks:", len(chunks))
# print("no of vectors: ",len(vectors))

# for i in range(min(3,len(chunks))):
#     print("="*80)
#     print('chunk:',i)

#     print('text:')
#     print(chunks[i].page_content[:300])

#     print('\n vector dimensions:')
#     print(len(vectors[i]))
