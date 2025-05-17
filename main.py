"""
This script manages Docker images and containers.
It allows users to delete, build, and launch containers via command-line arguments.
"""
import subprocess
import sys

def run_command(command):
    """Executes a shell command and returns output & exit code."""
    result = subprocess.check_output(command, shell=True, text=True)
    return result.strip()

def delete_container(F_CONT_NAME):

   try:
    run_command(f"docker rm -f {F_CONT_NAME}")
    print("Docker container deleted")
   except subprocess.CalledProcessError as e:
     print(f"Error deleting {e} ")
   
def delete_image(F_IMG_NAME):
    """Deletes the existing Docker image if found."""
    print("Checking for existing Docker image...")
    output= run_command(f"docker images -q  {F_IMG_NAME}")

    if output:  # Image exists
        print("Image exists. Attempting to delete...")
        try:
            run_command(f"docker rmi {F_IMG_NAME}")
            print("Image deleted successfully.")
        except subprocess.CalledProcessError:
            print("Error: Failed to delete image.")
            sys.exit(1)
    else:
        print("No existing image found. Nothing to delete.")

def build_image(F_IMG_NAME):
    """Builds a new Docker image."""
    print("Building Docker image...")
    try :
        run_command(f"docker build -t {F_IMG_NAME} .")
        print("Docker image built successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to build the image.")
        sys.exit(1)

def launch_container(F_IMG_NAME,F_CONT_NAME):
    """Launches a Docker container using the built image."""
    print("Launching Docker container...")
    try :
        run_command(f"docker run -itd -p 8888:80 --name {F_CONT_NAME} {F_IMG_NAME}")
        print("Container started successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to launch container.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4 :
        print("Usage: python script.py <ACTION> <image-name>")
        print("ACTIONs: 0 = Delete image, 1 = Build image, 3 = Launch container")
        print("image-name: eg.Ubuntu , devknife , nginx")
        sys.exit(1)
    IMG_NAME = None
    CONT_NAME = None
    ACTION = None
    if len(sys.argv) == 3 :
        ACTION = sys.argv[1]
        IMG_NAME = sys.argv[2]
    elif len(sys.argv) == 4:
        ACTION = sys.argv[1]
        IMG_NAME = sys.argv[2]
        CONT_NAME = sys.argv[3]
    else :
        print("Error in argv")
    match ACTION:  # Python 3.10+ switch-case equivalent
        case "0":
            delete_image(IMG_NAME)
        case "4":
            delete_container(CONT_NAME)    
        case "1":
            build_image(IMG_NAME)
        case "3":
            launch_container(IMG_NAME,CONT_NAME)
        case _:
            print("Invalid option. Choose 0 (delete), 1 (build), or 3 (launch).")
            sys.exit(1)
