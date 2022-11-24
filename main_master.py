import sys
import uvicorn

from master_node import app

def main(argv):
    if len(argv) > 1:
        if argv[1] == "-p":
            print(f"Running in port {argv[2]}")
            uvicorn.run(app=app, host="127.0.0.1", port=int(argv[2]), log_level="info")
        elif argv[1] == "-help":
            print("Use -p ## -> with ## being a port number to setup a server in the localhost and \n\t     the port mentioned.")
        
    else: 
        print("Use -help to get information about the accepted comands.")

if __name__ == "__main__":
    main(sys.argv)