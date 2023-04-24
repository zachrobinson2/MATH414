from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def binary_file_to_array(file_path):
    """
    Reads a binary file and creates a two-dimensional array with (timestamp, polarity) tuples.

    Args:
        file_path (str): The path to the binary file.

    Returns:
        np.ndarray: A two-dimensional numpy array with (timestamp, polarity) tuples.
    """
    # Open the binary file in binary mode
    with open(file_path, 'rb') as file:
        # Read the binary file as bytes
        binary_data = file.read()

        # Calculate the number of events based on the size of the binary data
        num_events = len(binary_data) // 5

        # Create an empty two-dimensional numpy array to store the events
        array = np.empty((256, 256), dtype=np.dtype([('timestamp', '<i4'), ('polarity', 'u1')]))

        # Iterate over the binary data, reading and decoding each event
        for i in range(num_events):
            # Extract the event data from the binary data
            x_address = binary_data[i * 5]  # Xaddress is the first byte
            y_address = binary_data[i * 5 + 1]  # Yaddress is the second byte
            polarity = binary_data[i * 5 + 2] & 0x01  # Polarity is the least significant bit of the third byte
            timestamp = int.from_bytes(binary_data[i * 5 + 3:i * 5 + 6], byteorder='little')  # Timestamp is the last three bytes

            # Store the event data as a tuple in the corresponding index of the array
            array[x_address][y_address] = (timestamp, polarity)

    return array

def array_to_image(array):
    """
    Converts a two-dimensional array into an image.

    Args:
        array (np.ndarray): A two-dimensional numpy array with (timestamp, polarity) tuples.

    Returns:
        None
    """
    # Extract the timestamps and polarities from the array
    timestamps = array['timestamp']
    polarities = array['polarity']

    # Create a binary image based on the polarities (0 for OFF, 255 for ON)
    image = np.where(polarities == 1, 255, 0)

    # Display the image using matplotlib
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


array = binary_file_to_array("Test/0/00011.bin")
#print(array)
array_to_image(array)
