from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
import dijkstra
class createMeshTopo(Topo):
        def build(self,n):
                #Add Hosts
                switches = []
                hosts = []
                for x in range(n*n):
                        switches.append(self.addSwitch('s%s'%(x+1),cls=OVSKernelSwitch,dpid='%s'%(x+1)))
                        hosts.append(self.addHost('h%s'%(x+1),ip='10.0.0.%s'%(x+1),defaultRoute=None))
                        self.addLink(hosts[x],switches[x])
                for x in range(n*n - 1):
                        if(n*n - x - 1 < 3):
                                self.addLink(switches[x],switches[x + 1])
                        elif((x + 1) % n == 0):
                                self.addLink(switches[x],switches[x + 3])
                        else:
                                self.addLink(switches[x], switches[x + 1])
                                self.addLink(switches[x], switches[x + 3])

def MyController(net,n):
        """Controller Program """
        graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
                        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
                        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
                        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
                        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
                        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
                        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
        h1 = int(input())
        h2 = int(input())
        ans = dijkstra.dijkstra(graph,h1)
        print(ans)
        print("---------")
        for i in ans[h2-1]:
            s = 's' + str(i + 1)
            net.getNodeByName(s).dpctl('add-flow','priority=500,actions=normal')
        #net.getNodeByName('s2').dpctl('add-flow','priority=500,actions=normal')
        #net


def Test(a):
        topo = createMeshTopo(n=a)
        net = Mininet(topo)
        net.start()
        MyController(net,a)
        print("Dumping Node Connections")
        dumpNodeConnections(net.hosts)
        CLI(net)
        #net.pingAll()
        net.stop()

if __name__ == '__main__':
        a = int(input())
        setLogLevel('info')
        Test(a)