import random

from oslo_log import log as logging
from nova.scheduler import filters

LOG = logging.getLogger(__name__)


class RandomFilter(filters.BaseHostFilter):
    """A simple filter that gives each hypervisor a 50% chance to pass on the VM."""

    def host_passes(self, host_state, spec_obj):
        allow_vm_on_host = random.randint(0, 1)
        if allow_vm_on_host:
            LOG.debug(f'Allowing VM on host: {host_state.host} due to result: {allow_vm_on_host}')
            return True
        LOG.debug(f'Not allowing VM on host: {host_state.host} due to result: {allow_vm_on_host}')
        return False
