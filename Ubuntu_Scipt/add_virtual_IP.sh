#!/bin/bash
addIP (){
ip addr add 192.188.11.22 dev lo
ip addr add 192.188.22.22 dev lo
ip addr add 192.188.33.22 dev lo
ip addr add 192.188.44.22 dev lo
ip addr add 192.188.55.22 dev lo
ip addr add 192.188.66.22 dev lo
ip addr add 192.188.77.22 dev lo
ip addr add 192.188.88.22 dev lo
ip addr add 192.188.99.22 dev lo
ip addr add 192.188.100.22 dev lo
ip addr add 192.188.101.22 dev lo
ip addr add 192.188.102.22 dev lo
}

delIP (){
ip addr del 192.188.11.22 dev lo
ip addr del 192.188.22.22 dev lo
ip addr del 192.188.33.22 dev lo
ip addr del 192.188.44.22 dev lo
ip addr del 192.188.55.22 dev lo
ip addr del 192.188.66.22 dev lo
ip addr del 192.188.77.22 dev lo
ip addr del 192.188.88.22 dev lo
ip addr del 192.188.99.22 dev lo
ip addr del 192.188.100.22 dev lo
ip addr del 192.188.101.22 dev lo
ip addr del 192.188.102.22 dev lo
}

addsingleIP (){
ip addr add 192.188.44.22 dev lo
#ip addr add 192.188.11.22 dev lo
}


addIP
#delIP
#addsingleIP
