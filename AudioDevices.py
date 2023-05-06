import pyaudio

def list_audio_devices():
    p = pyaudio.PyAudio()

    # Get the number of available audio devices
    device_count = p.get_device_count()

    print("Available audio devices:")
    print("------------------------")

    # Iterate over each device and print its index and name
    for i in range(device_count):
        device_info = p.get_device_info_by_index(i)
        device_index = device_info['index']
        device_name = device_info['name']
        print(f"Index: {device_index}, Name: {device_name}")

    p.terminate()

# Call the function to list audio devices
list_audio_devices()