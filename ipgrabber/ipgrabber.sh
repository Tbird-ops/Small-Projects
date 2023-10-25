#!/bin/bash
ip4=$(/sbin/ip -o -4 addr list wlan0 | awk '{print $4}' | cut -d/ -f1)
WEBHOOK={WEBHOOK HERE!!!!}
curl \
        -s \
        -X POST \
        -H "Content-Type: application/json" \
        -d "{\"username\": \"cafe-pi\", \"content\": \"$ip4\"}" \
        "$WEBHOOK"
