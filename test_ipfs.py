import ipfshttpclient

def main():
    # Connect to the local IPFS node (default: localhost:5001)
    client = ipfshttpclient.connect()

    # Fetch the node's ID
    node_id = client.id()
    
    # Print the node's ID
    print(node_id)

    meta = client.cat("QmVWGFDjKrX4oYk6UfoDPY2DRRw8j8DqeNS1iAZ9T6Sd2q/meta.json")
    print(meta)

    res = client.add("test_ipfs.py")
    print(res)

    # Close the client connection
    client.close()

if __name__ == "__main__":
    main()
