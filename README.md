Installation under devstack
---------------------------
Start with git cloning and installing the package on your system
```
sudo su - stack
git clone https://github.com/eandersson/nova-filter-example.git
cd nova-filter-example
pip install -e .
```

Next modify `/etc/nova/nova.conf` to include your new filter. You need to add the new filter to both available_filters and to enabled_filters.

```
[filter_scheduler]
available_filters = nova.scheduler.filters.all_filters
available_filters = nova_filter_example.RandomFilter
track_instance_changes = False
enabled_filters = ComputeFilter,RandomFilter
```

Finally, restart Nova.
```
sudo systemctl restart devstack@n-*
```

You can confirm that your new random filter works by creating a VM and looking for the log lines we added. These lines will show up inside the nova-scheduler. You can access these logs using this command.
```
sudo journalctl -u devstack@n-sch -f -n 200
```
The logs will then look like this.
```
nova-scheduler DEBUG nova_filter_example [None req-uuid alt_demo admin] Allowing VM on host: ubuntu due to result: 1
nova-scheduler DEBUG nova_filter_example [None req-uuid alt_demo admin] Not Allowing VM on host: ubuntu due to result: 0
```
