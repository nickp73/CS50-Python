import mimetypes
import os

def get_file_mime_type(filename):

    # Use mimetypes.guess_type to get the MIME type
    mime_type, _ = mimetypes.guess_type(filename)

    # If guess_type returns None, default to "application/octet-stream"
    if mime_type is None:
        return "application/octet-stream"
    return mime_type


user_file = input("Enter your file name (e.g., cat.jpeg): ").strip()
mime_type = get_file_mime_type(user_file)
print(mime_type)
