"""
Understanding Hash Tables from Scratch
"""

def simple_hash_function(text, table_size):
    """
    Our simple hash function: count letters and take remainder
    """
    letter_count = len(text)
    hash_value = letter_count % table_size
    print(f"Hash('{text}') = {letter_count} % {table_size} = {hash_value}")
    return hash_value

def demonstrate_hash_basics():
    print("=== STEP 1: Understanding Hash Function ===")
    table_size = 5  # We have 5 buckets
    
    # Test our hash function
    books = ["Cat", "Dog", "Elephant", "Ant", "Butterfly"]
    
    for book in books:
        hash_value = simple_hash_function(book, table_size)
        print(f"'{book}' goes to bucket {hash_value}")
    
    print("\n" + "="*50)
    print("=== STEP 2: Creating the Hash Table ===")
    
    # Create empty hash table (array of buckets)
    hash_table = [None] * table_size
    print(f"Empty hash table: {hash_table}")
    
    # Add items to hash table
    for book in books:
        bucket_index = simple_hash_function(book, table_size)
        hash_table[bucket_index] = book
        print(f"Added '{book}' to bucket {bucket_index}")
        print(f"Hash table now: {hash_table}")
        print()

def demonstrate_hash_collision():
    print("=== STEP 3: The Collision Problem ===")
    table_size = 3
    hash_table = [None] * table_size
    
    books = ["Cat", "Dog", "Ant"]  # All have 3 letters!
    
    print("What happens when multiple items hash to the same bucket?")
    
    for book in books:
        hash_value = simple_hash_function(book, table_size)
        if hash_table[hash_value] is None:
            hash_table[hash_value] = book
            print(f"✓ Added '{book}' to bucket {hash_value}")
        else:
            print(f"❌ COLLISION! Bucket {hash_value} already has '{hash_table[hash_value]}'")
            print(f"❌ Cannot add '{book}' - bucket is full!")
        
        print(f"Hash table: {hash_table}")
        print()

def demonstrate_chaining_solution():
    print("=== STEP 4: Solving Collisions with Chaining ===")
    table_size = 3
    
    # Each bucket now holds a list instead of single item
    hash_table = [[] for _ in range(table_size)]
    print(f"Hash table with lists: {hash_table}")
    
    books = ["Cat", "Dog", "Ant", "Elephant", "I"]
    
    for book in books:
        hash_value = simple_hash_function(book, table_size)
        hash_table[hash_value].append(book)
        print(f"Added '{book}' to bucket {hash_value}")
        print(f"Hash table: {hash_table}")
        print()

def demonstrate_lookup():
    print("=== STEP 5: Looking Up Items ===")
    table_size = 3
    hash_table = [[] for _ in range(table_size)]
    
    # Build our hash table
    books = ["Cat", "Dog", "Ant", "Elephant"]
    for book in books:
        hash_value = len(book) % table_size
        hash_table[hash_value].append(book)
    
    print(f"Final hash table: {hash_table}")
    print()
    
    # Now search for items
    search_items = ["Dog", "Bird", "Ant"]
    
    for item in search_items:
        print(f"Searching for '{item}'...")
        
        # Step 1: Hash the item to find which bucket
        bucket_index = len(item) % table_size
        print(f"  Hash value: {bucket_index}")
        
        # Step 2: Look in that bucket
        bucket = hash_table[bucket_index]
        print(f"  Checking bucket {bucket_index}: {bucket}")
        
        # Step 3: Search the bucket
        if item in bucket:
            print(f"  ✓ Found '{item}' in bucket {bucket_index}!")
        else:
            print(f"  ❌ '{item}' not found")
        print()

def demonstrate_better_hash_function():
    print("=== STEP 6: Better Hash Functions ===")
    
    def better_hash(text, table_size):
        """Sum of ASCII values of all characters"""
        total = sum(ord(char) for char in text)
        return total % table_size
    
    table_size = 5
    words = ["Cat", "Dog", "Act", "God"]  # Some anagrams
    
    print("Using simple letter count hash:")
    for word in words:
        simple = len(word) % table_size
        print(f"  {word} → bucket {simple}")
    
    print("\nUsing ASCII sum hash:")
    for word in words:
        better = better_hash(word, table_size)
        print(f"  {word} → bucket {better}")
    
    print("\nNotice: Better distribution with ASCII sum!")

if __name__ == "__main__":
    demonstrate_hash_basics()
    print("\n" + "="*50)
    
    demonstrate_hash_collision()
    print("\n" + "="*50)
    
    demonstrate_chaining_solution()
    print("\n" + "="*50)
    
    demonstrate_lookup()
    print("\n" + "="*50)
    
    demonstrate_better_hash_function()