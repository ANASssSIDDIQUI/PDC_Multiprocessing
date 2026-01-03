import Pyro4

@Pyro4.expose
class Chain(object):
    def __init__(self, name, next_server_name):
        self.name = name
        self.next_server_name = next_server_name
        self.next_server_proxy = None
    
    def process(self, message, val1=None, val2=None):
        # 1. Connect to the next server in the chain if not already connected
        if self.next_server_proxy is None:
            self.next_server_proxy = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.next_server_name)
        
        # 2. Integrate GCD logic from main_code.py
        if val1 and val2:
            # Each node can show it participated in the calculation
            temp_a, temp_b = val1, val2
            while temp_b != 0:
                temp_a, temp_b = temp_b, temp_a % temp_b
            current_gcd = temp_a
            print(f"Node {self.name}: Intermediate GCD check for ({val1}, {val2}) is {current_gcd}")

        # 3. Check if we've circled back to the start
        if self.name in message:
            print(f"Back at {self.name}; the chain is closed!")
            return [f"Final result handled at {self.name}"]
        else:
            print(f"{self.name} forwarding message to {self.next_server_name}")
            message.append(self.name)
            # Forward the call to the next server
            result = self.next_server_proxy.process(message, val1, val2)
            result.insert(0, f"passed on from {self.name}")
            return result