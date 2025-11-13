#!/bin/bash

services=("mytest_crasher.service")

usage="Usage: $0 {status|monit <name>|start <name>|stop <name>|restart <name>}"

need_service() {
    if [ -z "$1" ]; then
        echo "$usage"
        exit 1
    fi
}

case "$1" in
  status)
    for svc in "${services[@]}"; do
        echo "$svc: $(systemctl is-active "$svc")"
    done
    ;;
  monit)
    need_service "$2"
    echo "=== Monitoring logs for $2.service ==="
    journalctl -u "$2.service" -f --since "now"
    ;;
  start|stop|restart)
    need_service "$2"
    systemctl "$1" "$2.service"
    echo "$2: $(systemctl is-active "$2.service")"
    ;;
  *)
    echo "$usage"
    exit 1
    ;;
esac
