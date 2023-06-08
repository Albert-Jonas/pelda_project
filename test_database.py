import os
import pytest
from authenticator import *

@pytest.fixture
def text_file(request):
    filename = "database.txt"
    backup_filename = "database_backup.txt"
    content = request.param  # String provided as a parameter to the fixture

    # Save the original file, if it exists
    if os.path.exists(filename):
        os.rename(filename, backup_filename)

    # Create a new file and fill it with the provided content
    with open(filename, 'w') as file:
        file.write(content)

    # Yield the file name so the test can access it
    yield filename

    # Remove the new file
    os.remove(filename)

    # Restore the original file if it exists
    if os.path.exists(backup_filename):
        os.rename(backup_filename, filename)


@pytest.mark.parametrize('text_file', ['Sanyi Jelszo'], indirect=True)
@pytest.mark.parametrize('username, password',[('Sanyi', 'Jelszo'), ('Béla', 'Macska')])
def test_example(text_file, username, password):
    databaseHandler = DatabaseHandler()
    result = databaseHandler.get_user_credentials(username)

    assert result == password