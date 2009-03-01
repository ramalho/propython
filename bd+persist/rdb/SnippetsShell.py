#!/usr/bin/env python2.5
'''
An Interactive Shell for the SQLite3 RDBMS (http://www.sqlite.org/)

adapted to sqlite by Florent Xicluna -- 2007-07-29
  inspired from similar tool 'gfplus.py' for Gadfly,
    by Jeff Berliner -- 1998-11-24

sqliteplus is a simple interactive shell for SQLite3.
sqliteplus allows you to type SQL directly.

Documentation:

 * http://www.sqlite.org/lang.html
 * http://www.sqlite.org/faq.html
 * http://www.sqlite.org/datatype3.html

Some administrative commands:

sql> PRAGMA database_list;
sql> PRAGMA table_info(sqlite_master);
sql> SELECT * FROM sqlite_master;
sql> SELECT * FROM sqlite_temp_master;
sql> ATTACH '' AS tmp;
sql> ATTACH 'foobar.db' AS foobar;
sql>


Thanks to:
     Jeff Berliner
     Aaron Watters
     Richard Jones
     Lars M. Garshol
     Marc Risney
'''
__version__ = '1.0 (2007-07-29)'

import traceback, cmd, re
import sqlite3

# location = 'example.db' or '' for a temp file
location = ':memory:'

## pp() function by Aaron Watters, posted to gadfly-rdbms@egroups.com 1999-01-18
## modified version
def pp(cursor):
    rows = cursor.fetchall()
    desc = cursor.description
    if not desc:
        return rows
    names = [d[0] for d in desc]
    rcols = range(len(desc))
    rrows = range(len(rows))
    maxen = [max(0,len(names[j]),*(len(str(rows[i][j]))
             for i in rrows)) for j in rcols]
    names = ' '+' | '.join(
            [names[j].ljust(maxen[j]) for j in rcols])
    sep = '='*(reduce(lambda x,y:x+y, maxen) + 3*len(desc) - 1)
    rows = [names, sep] + [' '+' | '.join(
            [str(rows[i][j]).ljust(maxen[j])
            for j in rcols] ) for i in rrows]
    return '\n'.join(rows)+(
           len(rows)==2 and '\n no row selected\n' or '\n')

class SQLiteShell(cmd.Cmd):
    prompt, prompt2 = 'sql> ', '...  '
    intro = """
 sqliteplus %s -- Interactive sqlite shell
    SQLite %s, pysqlite %s

 Now using database '%s'

Enter your SQL commands to execute in SQLite3.
Enter 'q' to exit.
"""

    SQLCOMMANDS = [ 'ALTER ', 'ANALYZE', 'ATTACH ', 'BEGIN ', 'CREATE ',
            'DELETE ', 'DETACH ', 'DROP ', 'END', 'EXPLAIN ', 'INSERT ',
            'PRAGMA ', 'REINDEX ', 'REPLACE ', 'SELECT ', 'UPDATE ',
            'VACUUM ' ]
    SQLWORDS = [ 'ABORT ', 'ADD ', 'ALL ', 'AS ', 'ASC ', 'AUTOINCREMENT ',
            'BY ', 'CHECK ', 'COLUMN ', 'COLLATE ', 'CONFLICT ',
            'CONSTRAINT ', 'CROSS ', 'DATABASE ', 'DEFERRED', 'DEFAULT ',
            'DESC ', 'DISTINCT ', 'EXCEPT ', 'EXCLUSIVE', 'EXISTS ', 'FAIL ',
            'FULL ', 'FROM ', 'GROUP ', 'HAVING ', 'IF ', 'IGNORE ',
            'IMMEDIATE', 'INNER ', 'INTERSECT ', 'INTO ', 'INDEX ', 'JOIN ',
            'KEY ', 'LEFT ', 'LIMIT ', 'NATURAL ', 'NOT ', 'NULL ', 'OFFSET ',
            'ON ', 'OR ', 'ORDER ', 'OUTER ', 'PRIMARY ', 'RENAME ', 'RIGHT ',
            'ROLLBACK ', 'SET ', 'TABLE ', 'TEMP ', 'TEMPORARY ', 'TO ',
            'TRIGGER ', 'UNION ', 'UNIQUE ', 'USING ', 'VALUES ', 'VIEW ',
            'VIRTUAL ', 'WHERE ' ]
    PRAGMA = [ 'database_list;', 'foreign_key_list(', 'freelist_count;',
            'index_info(', 'index_list(', 'table_info(',
            'schema_version;', 'user_version;' ]

    def __init__(self, location = ':memory:'):
        cmd.Cmd.__init__(self)

        self.intro = self.intro % (__version__,
                sqlite3.sqlite_version, sqlite3.version, location)

        self.db = sqlite3.connect(location)
        self.db.isolation_level = None

        # create a DB cursor to execute our SQL in.
        self.cur = self.db.cursor()

        # for "do something to the last command" commands
        self.last_command = ''

    def do_exit(self, arg):
        ''' commit changes and exit
        '''
        print 'Commit...',
        self.db.commit()
        self.db.close()
        print 'exit'
        return 1
    do_quit = do_q = do_exit

    def do_EOF(self, arg):
        print
        return self.do_exit(arg)

    def do_commit(self, arg):
        ''' commit database
        '''
        self.db.commit()

    def do_rollback(self, arg):
        ''' rollback to last commit
        '''
        self.db.rollback()

    def precmd(self, line):
        if line.strip() in ('/', '!!'):
            line = self.lastcmd
        if line.startswith('s/') or line.startswith('c/'):
            line = 'change '+line[2:]
        return line

    def emptyline(self):
        pass

    def postcmd(self, stop, line):
        ''' I need to have the last command altered _after_ the current
            command is run
        '''
        self.last_command = self.lastcmd
        return stop

    def do_desc(self, table):
        ''' list columns for table
        '''
        prefix, table = '', table.rstrip(';')
        if '.' in table:
            prefix, table = table.split('.',1)
            prefix += '.'
        self.onecmd('PRAGMA %stable_info(%s);' % (prefix, table))

    def do_change(self, arg):
        ''' repeat the last command, but change it according to the re arg:

    s/pattern/replace
    c/pattern/replace
        '''
        if not self.last_command:
            print ' No last command to change'
            return
        # TODO: allow \-escaped / to appear in the arg
        pattern, repl = arg.split('/')
        try:
            line = re.sub(pattern, repl, self.last_command)
            print line
            return self.onecmd(line)
        except:
            print ' Wrong substitution request'

    def do_use(self, dbase):
        ''' switch active database:

    use 'example.db'

        'example.db' becomes the new 'main' database.
        '''
        dbase = dbase.strip('\'"; ')
        self.db.commit()
        self.db.close()
        self.db = sqlite3.connect(dbase)
        self.db.isolation_level = None
        self.cur = self.db.cursor()
        print '\n Now using database \'%s\'\n' % dbase
        return

    def do_help(self, arg):
        ''' display help screen
        '''
        if arg:
            if arg.lower().startswith(('command', 'cmd')):
                arg = ''
            if arg.lower().startswith('sql'):
                self.print_topics('\nSQL Commands:', self.SQLCOMMANDS, 15, 80)
                return
            return cmd.Cmd.do_help(self, arg)
        print ''' sqliteplus -- Interactive SQLite3 Shell

    Commands:

        <any sql statement>;        Execute SQL commands
        help                        This screen
        help commands               Standard list of commands
        help sql                    Print some SQL commands (not exhaustive)
        commit                      Commit changes to database
        rollback                    Rollback changes to last committed state
        desc <relation>             Display all columns in a table or view
        use <database-file>         Switch main database to <database-file>
        exit                        Exit sqliteplus
        '''

    def default(self, arg):
        ''' Run the command to SQLite
        '''
        # make sure we have a whole query
        query = arg.strip()

        if sqlite3.complete_statement(query):
            try:
                self.cur.execute(query)
                # display results
                results = pp(self.cur)
                if results:
                    print results
            except sqlite3.Error, e:
                # SQLite returned an error
                print 'An error occurred:', e.args[0]
            except:
                # Other error
                # use traceback to print it.
                traceback.print_exc()

        else:
            while not sqlite3.complete_statement(query):
                query += ' ' + raw_input(self.prompt2).strip()
            self.onecmd(query)

    def completenames(self, text, *ignored):
        return ( cmd.Cmd.completenames(self, text, *ignored)+
                 [c for c in self.SQLCOMMANDS if c.startswith(text.upper())] )

    def completedefault(self, text, line, begidx, *ignored):
        """Method called to complete an input line when no command-specific
        complete_*() method is available.
        """
        stdline = line[:begidx].rstrip().upper()
        if stdline.endswith(('ANALYZE', 'DESC', 'FROM', 'INTO ', 'REINDEX',
                             'REPLACE', 'TABLE', 'UPDATE', 'VACUUM')):
            return self.get_tables(text)
        if stdline.endswith(('PRAGMA')):
            return [i for i in self.PRAGMA if i.startswith(text.lower())]
        return [i for i in (self.SQLWORDS + self.SQLCOMMANDS)
                        if i.startswith(text.upper())]

    def complete_desc(self, *args):
        return self.completedefault(*args)

    def get_tables(self, text):
        self.cur.execute('pragma database_list;')
        dblist = [row[1] for row in self.cur]
        tables = []
        for db in dblist:
            prefix = (not db == 'main') and ('\''+db+'.\'||') or ''
            master = (db == 'temp') and 'sqlite_temp_master' or 'sqlite_master'
            self.cur.execute('select %sname from %s.%s;' % (prefix, db, master))
            tables += [row[0] for row in self.cur]
            if db in ( 'main', 'temp' ):
                tables += [master]
            else:
                tables += [db+'.'+master]
        return [t for t in tables if t.startswith(text)]


def main():
    shell = SQLiteShell(location)
    shell.cmdloop()

if __name__ == '__main__':
    main()
