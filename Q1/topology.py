from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)

    print("Adding controller...")
    net.addController('c0')

    print("Adding hosts...")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')
    h7 = net.addHost('h7')

    print("Adding switches...")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    print("Creating links with bandwidth constraints...")
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s3)
    net.addLink(h5, s3)
    net.addLink(h6, s4)
    net.addLink(h7, s4)

    net.addLink(s1, s2, bw=100)
    net.addLink(s2, s3, bw=50)
    net.addLink(s3, s4, bw=100)

    print("Starting the network...")
    net.start()

    print("Launching Mininet CLI...")
    CLI(net)

    print("Stopping the network...")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
