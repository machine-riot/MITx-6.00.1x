"""
Problem 4: Decrypt a Story
5/5 Points

Now that you have all the pieces to the puzzle, please used them to decode the
file story.txt. The file ps6.py contains a helper function get_story_string()
that returns the encrypted version of the story as a string. Create a
CiphertextMessage object using the story string and use decrypt message to
return the appropriate shift value and unencrypted story string.
"""
def decrypt_story():
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()
