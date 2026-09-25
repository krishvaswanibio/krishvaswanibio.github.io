import os
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

# 1. Define where the index files will live
INDEX_DIR = "my_search_index"

# 2. Define the Schema
# ID(stored=True) keeps the exact path/URL to display in results
# TEXT(stored=True) indexes the text for searching and saves it for previewing
schema = Schema(
    path=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    content=TEXT(stored=True)
)

# 3. Create or Open the Index
if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)
    ix = create_in(INDEX_DIR, schema)
    
    # 4. Populate with sample document data
    writer = ix.writer()
    writer.add_document(path="/home", title="Homepage", content="Welcome to our main terminal tool application.")
    writer.add_document(path="/docs", title="Documentation", content="Learn how to configure advanced search arguments and settings.")
    writer.add_document(path="/help", title="Help Center", content="Get immediate support for debugging script errors.")
    writer.commit()
    print("[System] Index created and populated with sample documents.")
else:
    ix = open_dir(INDEX_DIR)
    print("[System] Existing index loaded.")

# 5. Continuous Terminal Search Loop
print("\n--- Whoosh Terminal Search Engine Active ---")
print("Type your search query and press Enter. Type 'exit' to quit.\n")

while True:
    user_query = input("Search > ").strip()
    
    if user_query.lower() == 'exit':
        print("Goodbye!")
        break
        
    if not user_query:
        continue

    # Use a 'with' block so the searcher safely closes when done
    with ix.searcher() as searcher:
        # Construct the parser targeting the 'content' field
        parser = QueryParser("content", ix.schema)
        query = parser.parse(user_query)
        results = searcher.search(query)
        
        # Display Results
        print(f"\nFound {len(results)} matching document(s):")
        print("-" * 40)
        
        for i, hit in enumerate(results, 1):
            print(f"{i}. {hit['title']}")
            print(f"   Path:    {hit['path']}")
            print(f"   Snippet: {hit['content']}")
            print("-" * 40)
    print() # Formatting spacer
