uwsgi -s webapp.sock -w webcode --chmod-socket=664 >>webapp.log &
#uwsgi -s 127.0.0.1:8000 -w webcode --chmod-socket=664
