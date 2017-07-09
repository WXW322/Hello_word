from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # initilaize topology   
        Topo.__init__( self )

        # add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )

        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' ) 
	switch6 = self.addSwitch( 's6' )
        switch7 = self.addSwitch( 's7' )
        switch8 = self.addSwitch( 's8' )
        switch9 = self.addSwitch( 's9' )
        switch10 = self.addSwitch( 's10' ) 


        # link1
        self.addLink(host1,switch10,1,1)

	# link2
	self.addLink(switch10,switch9,2,1)

	# link3
	self.addLink(switch9,switch1,2,2)

	# link4
	self.addLink(switch10,switch8,3,1)
	
	# link5
	self.addLink(switch8,switch7,2,1)
		
	# link6
	self.addLink(switch7,switch6,2,1)

	# link7
	self.addLink(switch6,switch5,2,1)

	# link8
	self.addLink(switch5,switch1,2,3)

	# link9
	self.addLink(switch10,switch4,4,1)

	# link10
	self.addLink(switch4,switch3,2,1)

	# link11
	self.addLink(switch3,switch2,2,1)	

	# link12
	self.addLink(switch2,switch1,2,4)

	# link13
	self.addLink(switch1,host2,1,1)


topos = { 'mytopo': ( lambda: MyTopo() ) }


