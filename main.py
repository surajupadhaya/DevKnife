"""
This script manages Docker images and containers.
It allows users to delete, build, and launch containers via command-line arguments.
"""
import subprocess
import sys
import logging

# Configure logging to write to a log file
logging.basicConfig(filename="docker_script.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_command(command):
    """Executes a shell command and returns output & exit code."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout.strip(), result.returncode

def container_exists(container_name):
    """Checks if the Docker container exists."""
    output, _ = run_command(f"docker ps -a --filter name={container_name} -q")
    return bool(output)

def image_exists(image_name):
    """Checks if the Docker image exists."""
    output, _ = run_command(f"docker images -q {image_name}")
    return bool(output)

def delete_container(container_name):
    """Deletes a Docker container if found."""
    if container_exists(container_name):
        logging.info("Container exists. Attempting to delete...")
        output,_ = run_command(f"docker rm -f {container_name}")
        if bool(output) == True:
            logging.info("Container deleted successfully.")
        else:
            logging.info(f"Error deleting container '{container_name}'.")
            sys.exit(1)
    else:
        logging.info("No existing container found. Proceeding...")

def delete_image(image_name):
    """Deletes a Docker image if found."""
    if image_exists(image_name):
        logging.info("Image exists. Attempting to delete...")
        output,_ = run_command(f"docker rmi {image_name}")
        if bool(output) == True:
            logging.info("Image deleted successfully.")
        else:
            logging.info(f"Error deleting image '{image_name}'.")
            sys.exit(1)
    else:
        logging.info("No existing image found. Proceeding...")

def build_image(image_name):
    """Builds a new Docker image."""
    logging.info("Building Docker image...")
    _, ret_code = run_command(f"docker build -t {image_name} .")
    if ret_code == 0:
        logging.info("Docker image built successfully.")
    else:
        logging.info("Error: Failed to build the image.")
        sys.exit(1)

def launch_container(image_name, container_name):
    """Launches a Docker container using the built image."""
    logging.info("Launching Docker container...")
    _, ret_code = run_command(f"docker run -itd -p 8888:80 --name {container_name} {image_name}")
    if ret_code == 0:
        logging.info("Container started successfully.")
    else:
        logging.info("Error: Failed to launch container.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        logging.info("Usage: python script.py <ACTION> <image-name> [container-name]")
        logging.info("Actions: 0 = Delete, Build & Launch | 1 = Build | 3 = Launch")
        sys.exit(1)

    ACTION = sys.argv[1]
    IMAGE_NAME = sys.argv[2]
    CONTAINER_NAME = sys.argv[3] if len(sys.argv) == 4 else f"{IMAGE_NAME}_container"

    match ACTION:
        case "0":  # Delete if exists and then build & launch
            delete_container(CONTAINER_NAME)            
        case "1":
            delete_image(IMAGE_NAME)
        case "2":  # Build only
            build_image(IMAGE_NAME)
        case "3":  # Launch only
            launch_container(IMAGE_NAME, CONTAINER_NAME)
        case _:
            logging.info("Invalid option. Choose 0 (delete & rebuild), 1 (build), or 3 (launch).")
            sys.exit(1)