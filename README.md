

# Ansible Network Meta Collection.
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/builds?project=ansible-collections%2Fansible.network) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/ansible.network)](https://codecov.io/gh/ansible-collections/ansible.network)-->

The Ansible ``ansible.network`` collection is a meta collection that install all the following network supported content collections.
- ansible.netcommon
- ansible.utils
- arista.eos
- cisco.ios
- cisco.iosxr
- cisco.nxos
- frr.frr
- junipernetworks.junos
- openvswitch.openvswitch
- vyos.vyos


<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: *****.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

<!--start collection content-->
<!--end collection content-->

## Installing this collection

You can install the ``ansible.network`` collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install ansible.network

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ansible.network
```
## Using this collection

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.

**Using ``ansible.network`` meta collection to install supported network content collections.**
(python37) [root@fedora]$ ansible-galaxy collection install ansible.network
Process install dependency map
Starting collection install process
Installing 'ansible.network:1.0.0' to '/home/root/.ansible/collections/ansible_collections/ansible/network'
Installing 'frr.frr:1.0.3' to '/home/root/.ansible/collections/ansible_collections/frr/frr'
Installing 'cisco.ios:2.2.0' to '/home/root/.ansible/collections/ansible_collections/cisco/ios'
Installing 'vyos.vyos:2.3.0' to '/home/root/.ansible/collections/ansible_collections/vyos/vyos'
Installing 'arista.eos:2.1.2' to '/home/root/.ansible/collections/ansible_collections/arista/eos'
Installing 'cisco.nxos:2.3.0' to '/home/root/.ansible/collections/ansible_collections/cisco/nxos'
Installing 'cisco.iosxr:2.2.0' to '/home/root/.ansible/collections/ansible_collections/cisco/iosxr'
Installing 'ansible.utils:2.2.0' to '/home/root/.ansible/collections/ansible_collections/ansible/utils'
Installing 'ansible.netcommon:2.1.0' to '/home/root/.ansible/collections/ansible_collections/ansible/netcommon'
Installing 'junipernetworks.junos:2.2.0' to '/home/root/.ansible/collections/ansible_collections/junipernetworks/junos'
Installing 'openvswitch.openvswitch:2.0.0' to '/home/root/.ansible/collections/ansible_collections/openvswitch/openvswitch'

**List of installed network content collections.**
(python37) [root@fedora]$ ansible-galaxy collection list
# /home/root/.ansible/collections/ansible_collections
Collection              Version
----------------------- -------
ansible.netcommon       2.1.0
ansible.network         1.0.0
ansible.utils           2.2.0
arista.eos              2.1.2
cisco.ios               2.2.0
cisco.iosxr             2.2.0
cisco.nxos              2.3.0
frr.frr                 1.0.3
junipernetworks.junos   2.2.0
openvswitch.openvswitch 2.0.0
vyos.vyos               2.3.0

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [ansible.network collection repository](https://github.com/ansible-collections/ansible.network). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- Freenode IRC - ``#ansible-network`` Freenode channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Release notes
<!--Add a link to a changelog.md file or an external docsite to cover this information. -->

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Developing network resource modules](https://docs.ansible.com/ansible/latest/network/dev_guide/developing_resource_modules_network.html#developing-resource-modules)
- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
