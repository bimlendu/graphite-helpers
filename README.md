Helper scripts, configs for graphite.
--------------

* whisper-calculator.py

This script returns size of whisper data file in MBs, for a given storage schema.

Example usage:

```
python whisper-calculator.py 10s:30d,1m:180d,10m:1y,30m:2y
10s:30d,1m:180d,10m:1y,30m:2y >> 6 MB
```

* graphite-configs/storage-schemas.conf

Storage schema for whisper database. To validate the schema, run ```/opt/graphite/bin/validate-storage-schemas.py```.

```
[root@graphite001 ~]# /opt/graphite/bin/validate-storage-schemas.py
Loading storage-schemas configuration from default location at: '/opt/graphite/conf/storage-schemas.conf'
Section 'default':
  OK
Section 'carbon':
  OK
Storage-schemas configuration '/opt/graphite/conf/storage-schemas.conf' is valid
```
