#!/usr/bin/env python2.4

import time
import socket
import sys

sys.path.append('eagle-gtk')
from eagle import *

good_time = 1.0 # in seconds

default_test_ip = (
    ( "Intranet (Local Router)", "192.168.0.1", 80 ),
    ( "Same ISP", "200.210.52.20", 80 ),
    ( "UNICAMP/Brazil", "143.106.10.30", 80 ),
    ( "Slashdot", "66.35.250.150", 80 ),
    ( "Error", "192.168.1.123", 1234 ),
    )

default_test_name = (
    ( "www.google.com", ),
    ( "www.slashdot.org", ),
    )


def test_name( name ):
    try:
        t = time.time()
        socket.gethostbyname( name )
        t = time.time() - t
        return True, t
    except socket.gaierror, e:
        print "test_name( %r ): %s" % ( name, e )
        return False, None
# test_name()

def test_ip( ip, port ):
    try:
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        s.settimeout( 5.0 )
        t = time.time()
        s.connect( ( ip, port ) )
        t = time.time() - t
        s.close()
        return True, t
    except ( socket.error, socket.herror, socket.timeout ), e:
        print "test_ip( %r, %r ): %s" % ( ip, port, e )
        return False, None
# test_ip()


def clear_results( app, button ):
    table = app[ "table-ip" ]
    for row in table:
        row[ 3 ] = 0.0
        row[ 4 ] = ""

    table = app[ "table-name" ]
    for row in table:
        row[ 1 ] = 0.0
        row[ 2 ] = ""
# clear_results()

def cell_format( idx ):
    def f( app, table, row, col, value ):
        if col == idx:
            if value == "Slow":
                return Table.CellFormat( fgcolor="orange" )
            elif value == "Failed":
                return Table.CellFormat( fgcolor="red" )
            elif value == "Ok":
                return Table.CellFormat( fgcolor="#009900", bold=True )
    # f()
    return f
# cell_format()

def run_tests( app, button ):
    app[ "progress" ] = 0.0

    clear_results( app, button )

    table1 = app[ "table-ip" ]
    table2 = app[ "table-name" ]

    total = float( len( table1 ) + len( table2 ) )

    for i, row in enumerate( table1 ):
        ok, time = test_ip( row[ 1 ], row[ 2 ] )
        app[ "progress" ] = ( i + 1.0 ) / total

        if ok:
            row[ 3 ] = time
            if time > good_time:
                row[ 4 ] = "Slow"
            else:
                row[ 4 ] = "Ok"
        else:
            row[ 3 ] = 0.0
            row[ 4 ] = "Failed"
    # end for

    offset = i
    for i, row in enumerate( table2 ):
        i += offset
        ok, time = test_name( row[ 0 ] )
        app[ "progress" ] = ( i + 1.0 ) / total

        if ok:
            row[ 1 ] = time
            if time > good_time:
                row[ 2 ] = "Slow"
            else:
                row[ 2 ] = "Ok"
        else:
            row[ 1 ] = 0.0
            row[ 2 ] = "Failed"
    # end for

    app[ "progress" ] = 0
# run_tests()



app = App( title="Network Tester",
           help="""
<h3>Direct IP Connection Tests</h3>
<p>
These tests will attempt to connect to IP address at given port.
</p>
<p>
If they fail, you cannot reach the other peer and you may check
your cables, router, modem and the other peer to ensure it's ok.
</p>
<p>
If they succeeds but you cannot resolve names (see Name Resolution
Tests), then you have a problem with your DNS (Domain Name
Service), it may be invalid/incorrect IP address or it's not
reachable.
</p>
<p>
If they are marked as "slow", then connections are taking too long,
so web surfing may be slow even if download rates are high.
</p>

<h3>Name Resolution Tests</h3>
<p>
These tests will try to resolve (convert) given DNS (Domain Name
Service), a easy to remember name like www.google.com to the
number computers use to identify themselves, like 64.233.179.99.
</p>
<p>
This process occurs every time you try to access another peer given
its name, like browsing http://www.google.com.
</p>
<p>
If Direct IP Connection Tests fails, this will probably fail too.
</p>
<p>
If Direct IP Connection Tests succeeds and these fails, then you need
to check your DNS servers.
</p>

<h3>General Usage</h3>
<p>
You may run pre-defined tests just click "Run Tests" button.
</p>
<p>
To clear previous results, just hit "Clear Results".
</p>
<p>
To add new tests or edit existing, use buttons below tables.
</p>
""",
           left=( Button( "run",
                          label="Run Tests",
                          callback=run_tests,
                          ),
                  Button( "clear",
                          label="Clear Results",
                          callback=clear_results,
                          ),
                  HelpButton(),
                  Progress( "progress", "Progress" ),
                  ),
           center=( Table( "table-ip", "Direct IP Connection Tests",
                           types=( str, str, int, float, str ),
                           headers=( "Test", "IP Address", "Port",
                                     "Time (seg)", "Status" ),
                           expand_columns_indexes=0,
                           cell_format_func=cell_format( 4 ),
                           editable=True,
                           ),
                    Table( "table-name", "Name Resolution Tests",
                           types=( str, float, str ),
                           headers=( "Name", "Time (seg)", "Status" ),
                           expand_columns_indexes=0,
                           cell_format_func=cell_format( 2 ),
                           editable=True,
                           ),
                    )
           )

t = app[ "table-ip" ]
t[ : ] = default_test_ip

t = app[ "table-name" ]
t[ : ] = default_test_name

run()
