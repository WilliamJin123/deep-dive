
import os
import shutil
from typing import List
from smolagents import Tool

# ----------------------------------------------------------------------
# Helper Functions (the original implementations)
# ----------------------------------------------------------------------
def create_directory(path: str) -> str:
    """Creates a directory at the given path. Creates parent directories if needed."""
    try:
        os.makedirs(path, exist_ok=True)
        return f"Directory created: {path}"
    except Exception as e:
        return f"Error creating directory {path}: {str(e)}"

def write_file(path: str, content: str, overwrite: bool = True) -> str:
    """
    Writes content to a file. Creates parent directories if needed.
    If overwrite is False, appends instead.
    """
    try:
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        mode = 'w' if overwrite else 'a'
        with open(path, mode, encoding='utf-8') as f:
            f.write(content)
        action = "Overwritten" if overwrite else "Appended to"
        return f"File {action}: {path}"
    except Exception as e:
        return f"Error writing to file {path}: {str(e)}"

def read_file(path: str) -> str:
    """Reads and returns the content of a file."""
    try:
        if not os.path.exists(path):
            return f"File not found: {path}"
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"Content of {path}:\n{content}"
    except Exception as e:
        return f"Error reading file {path}: {str(e)}"

def list_files(path: str = ".", recursive: bool = False) -> str:
    """Lists files in a directory. Optionally recursive."""
    try:
        if not os.path.exists(path):
            return f"Path not found: {path}"
        if not os.path.isdir(path):
            return f"Path is not a directory: {path}"

        files = []
        if recursive:
            for root, _, filenames in os.walk(path):
                for f in filenames:
                    files.append(os.path.join(root, f))
        else:
            files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        if not files:
            return f"No files found in {path}"
        return "Files:\n" + "\n".join(files)
    except Exception as e:
        return f"Error listing files in {path}: {str(e)}"

def delete_file_or_directory(path: str, confirm: bool = True) -> str:
    """Deletes a file or directory. If ``confirm`` is True, asks the user for
    confirmation before proceeding.

    Returns a status message.
    """
    # If confirmation is required, ask the user.
    if confirm:
        # Build a clear prompt (include the path so the user knows what will be deleted)
        response = input(f"Are you sure you want to delete '{path}'? (y/n): ").strip().lower()
        if response not in {"y", "yes"}:
            return "Deletion cancelled by user."

    # At this point we have either confirmation or the caller disabled it.
    try:
        if not os.path.exists(path):
            return f"Path not found: {path}"

        if os.path.isfile(path):
            os.remove(path)
            return f"File deleted: {path}"
        elif os.path.isdir(path):
            shutil.rmtree(path)
            return f"Directory deleted: {path}"
    except Exception as e:
        return f"Error deleting {path}: {str(e)}"


# ----------------------------------------------------------------------
# smolagents Tool Wrappers (Refactored)
# ----------------------------------------------------------------------
class CreateDirectoryTool(Tool):
    name = "create_directory"
    description = "Creates a directory at a specified path, including any necessary parent directories."
    inputs = {
        "path": {
            "type": "string",
            "description": "The full path of the directory to create.",
        }
    }
    output_type = "string"

    def forward(self, path: str) -> str:
        return create_directory(path)


class WriteFileTool(Tool):
    name = "write_file"
    description = "Writes text content to a specified file. Creates parent directories if they don't exist. Can either overwrite the file or append to it."
    inputs = {
        "path": {
            "type": "string",
            "description": "The full path of the file to write to.",
        },
        "content": {
            "type": "string",
            "description": "The text content to be written into the file.",
        },
        "overwrite": {
            "type": "boolean",
            "description": "If True (default), the file's content is overwritten. If False, the content is appended.",
            "nullable": True,
        }
    }
    output_type = "string"

    def forward(self, path: str, content: str, overwrite: bool = True) -> str:
        return write_file(path, content, overwrite)


class ReadFileTool(Tool):
    name = "read_file"
    description = "Reads and returns the entire content of a specified file."
    inputs = {
        "path": {
            "type": "string",
            "description": "The full path of the file to read.",
        }
    }
    output_type = "string"

    def forward(self, path: str) -> str:
        return read_file(path)


class ListFilesTool(Tool):
    name = "list_files"
    description = "Lists all files in a given directory. Can perform a recursive search to include files in all subdirectories."
    inputs = {
        "path": {
            "type": "string",
            "description": "The path to the directory to list files from. Defaults to the current directory '.'.",
            "nullable": True,
        },
        "recursive": {
            "type": "boolean",
            "description": "If True, lists files recursively from all subdirectories. Defaults to False.",
            "nullable": True,
        }
    }
    output_type = "string"

    def forward(self, path: str = ".", recursive: bool = False) -> str:
        return list_files(path, recursive)


class DeleteFileOrDirectoryTool(Tool):
    name = "delete_file_or_directory"
    description = "Deletes a specified file or an entire directory. For safety, it requires an explicit confirmation flag to be set to False."
    inputs = {
        "path": {
            "type": "string",
            "description": "The full path of the file or directory to delete.",
        },
        "confirm": {
            "type": "boolean",
            "description": "A safety flag. Must be set to False to proceed with the deletion. Defaults to True.",
            "nullable": True,
        }
    }
    output_type = "string"

    def forward(self, path: str, confirm: bool = True) -> str:
        return delete_file_or_directory(path, confirm)

# ----------------------------------------------------------------------
# Convenience list for easy loading into an agent
# ----------------------------------------------------------------------
TOOLS: List[Tool] = [
    CreateDirectoryTool(),
    WriteFileTool(),
    ReadFileTool(),
    ListFilesTool(),
    DeleteFileOrDirectoryTool(),
]