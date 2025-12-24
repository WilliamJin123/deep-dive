import asyncio
from typing import List
from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.vectordb.lancedb import LanceDb, SearchType

from agno.knowledge.reader.pdf_reader import PDFReader, PDFImageReader
from agno.knowledge.reader.csv_reader import CSVReader
from agno.knowledge.reader.text_reader import TextReader
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.knowledge.types import ContentType
from agno.knowledge.chunking.strategy import ChunkingStrategyType, ChunkingStrategyFactory, ChunkingStrategy
from agno.knowledge.document.base import Document
from agno.knowledge.reader import ReaderFactory

# Every reader implements these core methods
class Reader:
    def read(self, obj, name=None) -> List[Document]:
        """Synchronously read and process content"""
        pass

    async def async_read(self, obj, name=None) -> List[Document]:
        """Asynchronously read and process content"""
        pass

    @classmethod
    def get_supported_content_types(cls) -> List[ContentType]:
        """Returns the content types this reader can handle"""
        return [ContentType.PDF]  # Example for PDFReader
    
    @classmethod
    def get_supported_chunking_strategies(cls) -> List[ChunkingStrategyType]:
        return [
            ChunkingStrategyType.DOCUMENT_CHUNKER,  # Respect document structure
            ChunkingStrategyType.FIXED_SIZE_CHUNKER, # Fixed character/token limits
            ChunkingStrategyType.SEMANTIC_CHUNKER,   # Semantic boundaries
            ChunkingStrategyType.AGENTIC_CHUNKER,    # AI-powered chunking
        ]

def MyStrategy():
    pass

reader = PDFReader(
    chunk=True,                    # Enable/disable chunking
    chunk_size=1000,              # Size of each chunk
    chunking_strategy=MyStrategy() # Custom chunking logic
)

reader = PDFReader(
    split_on_pages=True,          # Create separate documents per page
    password="secret123",         # Handle encrypted PDFs
    read_images=True             # Extract text from images via OCR
)

#ENCODINGS
reader = TextReader(
    encoding="utf-8"              # Override default encoding
)

reader = CSVReader(
    encoding="latin-1"            # Handle files with specific encodings
)

reader = MarkdownReader(
    encoding="cp1252"             # Windows-specific encoding
)

documents = reader.read(
    "filepath",
    name="custom_document_name",  # Override default naming
    password="file_password"      # Runtime password override
)
# Readers convert raw content into Document objects with this structure:
Document(
    content="The extracted text content...",
    id="unique_document_identifier",
    name="document_name",
    meta_data={
        "page": 1,                # Page number for PDFs
        "url": "https://...",     # Source URL for web content
        "author": "...",          # Document metadata
    },
    size=len("content")             # Content size in characters
)

# Large PDF gets broken into multiple documents
pdf_reader = PDFReader(chunk=True, chunk_size=1000)
documents = pdf_reader.read("large_document.pdf")
# Returns: [Document(chunk1), Document(chunk2), Document(chunk3), ...]

#Automatic Factories (very useful for not having to manage imports)

# Automatic reader selection based on file extension
reader = ReaderFactory.get_reader_for_extension(".pdf")  # Returns PDFReader
reader = ReaderFactory.get_reader_for_extension(".csv")  # Returns CSVReader

# URL-based reader selection
reader = ReaderFactory.get_reader_for_url("https://youtube.com/watch?v=...")  # YouTubeReader
reader = ReaderFactory.get_reader_for_url("https://example.com/doc.pdf")     # PDFReader

#ASYNC OPS
async def func(file_list):
    documents = await reader.async_read("file.pdf")

    # Batch processing with async
    tasks = [reader.async_read(file) for file in file_list]
    all_documents = await asyncio.gather(*tasks)
    return documents, all_documents


from agno.knowledge.reader.pdf_reader import PDFReader

# Custom reader configuration
reader = PDFReader(
    chunk_size=1000,
    chunking_strategy=ChunkingStrategyFactory.create_strategy(ChunkingStrategyType.SEMANTIC_CHUNKER, chunk_size=500, overlap=250),
)

knowledge_base = Knowledge(
    vector_db=vector_db,
    contents_db=contents_db
)

# Use custom reader
knowledge_base.add_content(
    path="data/documents",
    reader=reader  # Override default reader
)

# Custom Chunker
class CustomChunking(ChunkingStrategy):
    def __init__(self, separator: str = "---", **kwargs):
        self.separator = separator

    def chunk(self, document: Document) -> List[Document]:
        # Split by custom separator
        chunks = document.content.split(self.separator)

        result = []
        for i, chunk_content in enumerate(chunks):
            chunk_content = self.clean_text(chunk_content)  # Use inherited method
            if chunk_content:
                meta_data = document.meta_data.copy()
                meta_data["chunk"] = i + 1
                result.append(Document(
                    id=f"{document.id}_{i+1}" if document.id else None,
                    name=document.name,
                    meta_data=meta_data,
                    content=chunk_content
                ))
        return result

from agno.knowledge.chunking.semantic import SemanticChunking   
from agno.knowledge.chunking.fixed import FixedSizeChunking
#  Fast processing for simple content
fast_chunking = FixedSizeChunking(
    chunk_size=800,
    overlap=80
)

# Better quality for complex content (but slower)
quality_chunking = SemanticChunking(
    chunk_size=1200,
    similarity_threshold=0.5
)