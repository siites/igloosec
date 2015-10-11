import datetime
import os
import socket
import sys
import psutil
  
  
def print_(a, b):
    fmt = '%-15s %s' % (a, b)
    sys.stdout.write(fmt + '\n')

  
def run(pid):
    ACCESS_DENIED = ''
    try:
        p = psutil.Process(pid)
        pinfo = p.as_dict(ad_value=ACCESS_DENIED)
    except psutil.NoSuchProcess:
        sys.exit(str(sys.exc_info()[1]))
  
    try:
        parent = p.parent()
        if parent:
            parent = '(%s)' % parent.name()
        else:
            parent = ''
    except psutil.Error:
        parent = ''
    started = datetime.datetime.fromtimestamp(
        pinfo['create_time']).strftime('%Y-%M-%d %H:%M')
    io = pinfo.get('io_counters', ACCESS_DENIED)
    children = p.children()
  
    print_('pid', pinfo['pid'])
    print_('name', pinfo['name'])
    print_('exe', pinfo['exe'])
    print_('parent', '%s %s' % (pinfo['ppid'], parent))
    print_('cmdline', ' '.join(pinfo['cmdline']))
    print_('started', started)
    print_('user', pinfo['username'])

    if hasattr(p, 'getcwd'):
        print_('cwd', pinfo['cwd'])
    print_('cpu', '%s%% (user=%s, system=%s)' % (
        pinfo['cpu_percent'],
        getattr(pinfo['cpu_times'], 'user', '?'),
        getattr(pinfo['cpu_times'], 'system', '?')))
    print_('status', pinfo['status'])
    print_('niceness', pinfo['nice'])
    print_('num threads', pinfo['num_threads'])
    if children:
        print_('children', '')
        for child in children:
            print_('', 'pid=%s name=%s' % (child.pid, child.name()))
  
    if pinfo['open_files'] != ACCESS_DENIED:
        print_('open files', '')
        for file in pinfo['open_files']:
            print_('', 'fd=%s %s ' % (file.fd, file.path))
  
    if pinfo['threads']:
        print_('running threads', '')
        for thread in pinfo['threads']:
            print_('', 'id=%s, user-time=%s, sys-time=%s' % (
                thread.id, thread.user_time, thread.system_time))
    if pinfo['connections'] not in (ACCESS_DENIED, []):
        print_('open connections', '')
        for conn in pinfo['connections']:
            if conn.type == socket.SOCK_STREAM:
                type = 'TCP'
            elif conn.type == socket.SOCK_DGRAM:
                type = 'UDP'
            else:
                type = 'UNIX'
            lip, lport = conn.laddr
            if not conn.raddr:
                rip, rport = '*', '*'
            else:
                rip, rport = conn.raddr
            print_('', '%s:%s -> %s:%s type=%s status=%s' % (
                lip, lport, rip, rport, type, conn.status))
  
def main():
    print "=======================START======================="
    for proc in psutil.get_pid_list():
        try:
            run(proc)
            print "*"*50
        except:
            pass
  
if __name__ == '__main__':
    sys.exit(main())
