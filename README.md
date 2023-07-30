# File Sharing App

## Description

File Sharing App is a simple Python application that allows users to share files securely and easily. It provides a user-friendly web interface to upload and download files with a focus on privacy and security.

## Working

1. The required modules, such as `os`, `socket`, `time`, `compressor`, `hashing`, `tkinter`, `tkinter.simpledialog`, and `tkinter.messagebox`, are imported.

2. The `formate` variable is assigned the value "utf-8", which specifies the encoding format for string operations.

3. The `client` class is defined with an `_init_` method that sets up the client. It initializes variables, calls the `receive` method, and creates a Tkinter window for displaying the received file details.

4. The `rec` method is defined within the `client` class. It handles the actual receiving of files. The method performs the following steps:
   - Receives the file details from the socket, such as filename, file size, and file hash, using `self.sock.recv()`. The received data is decoded using the specified encoding format.
   - Sends an acknowledgment back to the server using `self.sock.send()`.
   - Opens a file named "compressed.tar.gz" in write binary mode to receive the file data.
   - Enters a loop to receive data from the socket until the total received data size matches the file size.
   - Writes the received data to the file.
   - Calculates the time taken for the file transfer.
   - Calls the `decompress` function to decompress the received file.
   - Verifies the integrity of the received file by comparing its hash with the received file hash.
   - Sets the `error` flag to 1 if no error is detected during the hash comparison.

5. The `receive` method is defined within the `client` class. It prompts the user to enter the host name, creates a socket, and attempts to connect to the server at the specified host and port. If the connection is successful, it calls the `rec` method to receive the file. Finally, it closes the socket.

6. The `display` method is defined within the `client` class. It creates a Tkinter window and displays the received file details, including the filename, file size, total time taken for the transfer, and whether an error was detected during hash verification.

7. The `receiver` function is defined, which acts as the entry point for the client program. It creates a Tkinter window, hides it, and creates an instance of the `client` class.

8. The `mainloop` function is called to start the Tkinter event loop.

To use this client program, you would typically run the `receiver` function, which prompts for the host name, establishes a connection with the server, receives the file, and displays the relevant details in a Tkinter window.

## Technologies Used

- Python: The core programming language used to build the application.
- Python-GUI : used for graphical interface

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/file-sharing-app.git
