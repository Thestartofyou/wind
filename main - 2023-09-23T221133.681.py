import random
import time

def generate_wind_data():
    # Simulate wind speed in meters per second (mps) and wind direction in degrees
    wind_speed = random.uniform(0.1, 30.0)
    wind_direction = random.uniform(0, 360)
    return wind_speed, wind_direction

def record_wind_data(file_path):
    try:
        while True:
            wind_speed, wind_direction = generate_wind_data()
            
            # Simulated timestamp
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # Appending data to a CSV file
            with open(file_path, 'a') as file:
                file.write(f"{timestamp},{wind_speed},{wind_direction}\n")

            print(f"Recorded: {timestamp}, Wind Speed: {wind_speed} m/s, Wind Direction: {wind_direction}°")
            
            # Adjust the time interval as needed (e.g., every 5 minutes)
            time.sleep(300)

    except KeyboardInterrupt:
        print("Recording stopped.")

if __name__ == "__main__":
    file_path = "wind_data.csv"  # Specify the path to your data file
    print("Press Ctrl+C to stop recording.")
    record_wind_data(file_path)

